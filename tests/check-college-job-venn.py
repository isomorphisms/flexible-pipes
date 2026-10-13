#!/usr/bin/env python3
"""Existing acceptance adapter: invoke real Idriç, then check actual model/media.

The model's dependent proofs are checked by Idriç, not by this Python file.
This inherited checker remains migration debt; no new Python runtime is hidden.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageStat

ROOT = Path(__file__).resolve().parents[1]
PIN = '2734ac5a86610eddfab73b1644d72b4ac85a65ee'
SOURCE = ROOT/'models/CollegeVenn.idric'

NEGATIVES = {
 'SwappedQueries': '''bad : Percentage symmetric good_job college → Percentage symmetric college good_job
bad answer = answer
''',
 'MixedFrames': '''other : PopulationFrame "oracle people" "unit weight"
other = Population 1009 2 3 3 7
bad : Percentage symmetric good_job college → Percentage other good_job college
bad answer = answer
''',
 'MixedUniverses': '''other : PopulationFrame "different people" "unit weight"
other = Population 1001 2 3 3 7
bad : Percentage symmetric good_job college → Percentage other good_job college
bad answer = answer
''',
 'MixedUnits': '''other : PopulationFrame "oracle people" "different weight"
other = Population 1001 2 3 3 7
bad : Percentage symmetric good_job college → Percentage other good_job college
bad answer = answer
''',
 'ForgedNumerator': '''bad : Percentage symmetric good_job college
bad = PercentageOf (NonemptyPopulation 3 5 ItIsSucc (LTESucc (LTESucc (LTESucc LTEZero))))
''',
 'WrongDenominator': '''bad : Percentage asymmetric good_job college
bad = PercentageOf (NonemptyPopulation 2 7 ItIsSucc (LTESucc (LTESucc LTEZero)))
''',
 'ZeroDenominator': '''bad : BoundedFraction 0 0
bad = NonemptyPopulation 0 0 ItIsSucc LTEZero
''',
 'AboveOneHundred': '''bad : BoundedFraction 2 1
bad = NonemptyPopulation 2 1 ItIsSucc (LTESucc (LTESucc LTEZero))
''',
 'WrongComplement': '''bad : complement (the (Region "people") good_job) = intersection college (complement good_job)
bad = Refl
''',
}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def run_logged(argv, path, cwd=ROOT, timeout=900, env=None):
    result = subprocess.run([str(x) for x in argv],cwd=cwd,stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,timeout=timeout,env=env)
    path.write_bytes(result.stdout)
    return result


def require_compiler_success(result, phase):
    diagnostic=result.stdout.decode(errors='replace')
    # The pinned compiler can return zero for a source-less loading error.
    # Such a diagnostic is never evidence that a positive control passed.
    require(result.returncode==0 and not re.search(r'(?m)^Error:|^Uncaught error:',diagnostic),
            phase+' failed (compiler exit '+str(result.returncode)+'):\n'+diagnostic)


def expected_percent(numerator,denominator):
    if denominator == 0:
        require(numerator == 0,'nonempty intersection of empty population')
        return 'undefined'
    tenths = (1000*numerator+denominator//2)//denominator
    return f'{tenths//10}.{tenths%10}%'


def expected_label(event,among):
    people = {'1100':'college graduates','1010':'people with a good job',
              '0101':'people with a bad job or no job'}
    condition = {'1100':'who have a college degree','1010':'with a good job',
                 '0101':'with a bad job or no job'}
    return '% of '+people.get(among,'people in region '+among)+' '+condition.get(event,'who are in region '+event)


def check_model_text(text):
    rows = [line.split('\t') for line in text.splitlines()]
    require(rows[0] == ['model','college-venn-dependent-v1','196','24','8600'],'wrong model identity or profile')
    frames, region_rows, answers, oracle = {}, {}, {}, []
    for row in rows[1:]:
        if row[0] == 'frame':
            time,*weights=map(int,row[1:])
            require(time not in frames and len(weights)==4 and min(weights)>=0,'invalid frame')
            frames[time]=weights
        elif row[0] == 'region':
            require(len(row)==4 and row[1] not in region_rows,'invalid region declaration')
            region_rows[row[1]]=row[2:]
        elif row[0] == 'answer':
            answers.setdefault(int(row[1]),[]).append(row)
        elif row[0] == 'oracle':
            oracle.append(row)
        else:
            raise ValueError('unrecognized model record: '+repr(row))
    require(region_rows == {'college':['1100','WENT TO COLLEGE'],'good':['1010','GOOD JOB'],
                            'complement':['0101','BAD JOB OR NO JOB']},'wrong region/complement meaning')
    expected_frames={**{time:None for time in range(196)},1000:[2,3,5,7],1001:[2,3,3,7],1002:[0,0,0,0]}
    require(set(frames)==set(expected_frames),'missing or additional population frames')
    for time in (1000,1001,1002):
        require(frames[time]==expected_frames[time],'wrong independent oracle fixture')
    all_codes={f'{i:04b}' for i in range(16)}
    seen=set()
    for row in oracle+[row for group in answers.values() for row in group]:
        require(len(row)==8,'wrong query record shape')
        kind,time,event,among,numerator,denominator,displayed,label=row
        time=int(time)
        require(event in all_codes and among in all_codes,'invalid event bits')
        key=(kind,time,event,among)
        require(key not in seen,'duplicate query')
        seen.add(key)
        population=[cell for cell,weight in enumerate(frames[time]) for _ in range(weight)]
        conditioning=[cell for cell in population if among[cell]=='1']
        intersection=[cell for cell in conditioning if event[cell]=='1']
        n,d=len(intersection),len(conditioning)
        require((int(numerator),int(denominator))==(n,d),'wrong intersection or denominator')
        require(displayed==expected_percent(n,d),'wrong displayed value')
        require(label==expected_label(event,among),'query label does not describe its fraction')
    required={('oracle',t,e,b) for t in (1000,1001,1002) for e in all_codes for b in all_codes}
    require({key for key in seen if key[0]=='oracle'}==required,'not all 256 conditionals were executed')
    previous=None
    for time in range(196):
        weights=frames[time]
        require(sum(weights)==8600,'population was created or lost')
        require(weights[0]==500 and weights[2]==820,'good jobs or overlap changed')
        if previous:
            require(weights[1]>=previous[1] and weights[3]<=previous[3],'non-monotone college expansion')
            require(weights[1]-previous[1]==previous[3]-weights[3],'unbalanced membership transfer')
        previous=weights
        require([(row[2],row[3]) for row in answers.get(time,[])]==[('1010','1100'),('1100','1010')],
                'wrong query order or meaning')
    require(frames[0]==[500,500,820,6780] and frames[195]==[500,2000,820,5280],'wrong movie endpoints')
    return frames,answers,len(required)


def check_type_model(compiler,output):
    output.mkdir(parents=True,exist_ok=True)
    # Invalidate previous success before attempting any new compiler work.
    for name in ('model-check.json','render-receipt.json','acceptance.json','model.tsv',
                 'college-good-jobs-venn.mp4','initial.png','college-good-jobs-venn-preview.png'):
        (output/name).unlink(missing_ok=True)
    for path in (output/'frames').glob('[0-9][0-9][0-9][0-9].png'):
        path.unlink()
    if (output/'frames').is_dir():
        (output/'frames').rmdir()
    logdir=output/'type-checks'
    logdir.mkdir(exist_ok=True)
    compiler=compiler.resolve()
    runtime=ROOT/'runtime/idric'
    observed=subprocess.check_output(['git','-C',str(runtime),'rev-parse','HEAD'],text=True).strip()
    require(observed==PIN,'wrong compiler source revision')
    require(not subprocess.check_output(['git','-C',str(runtime),'status','--porcelain','--untracked-files=no']),
            'modified compiler sources')
    # Bootstrap installs its libraries under this prefix; the final compiler's
    # default prefix is the builder's home, which is not a consumer runtime.
    environment={key:value for key,value in os.environ.items() if not key.startswith('IDRIS2_')}
    environment['IDRIS2_PREFIX']=str((runtime/'bootstrap-build').resolve())
    require((runtime/'bootstrap-build').is_dir(),'missing bootstrapped library prefix')
    executable=ROOT/'build/exec/college-venn-model'
    executable.unlink(missing_ok=True)
    compile_argv=[compiler,'--source-dir','models','--cg','node','-o','college-venn-model','models/CollegeVenn.idric']
    result=run_logged(compile_argv,logdir/'model-compile.log',env=environment)
    require_compiler_success(result,'model compilation')
    require(executable.is_file() and executable.stat().st_size>0,'compiler emitted no fresh model executable')
    source_text=SOURCE.read_text()
    for forbidden in ('believe_me','assert_total','assert_smaller','%unsafe','%foreign'):
        require(forbidden not in source_text,'untrusted escape in semantic source')
    outcomes=[]
    with tempfile.TemporaryDirectory(prefix='venn-type-cases-') as directory:
        work=Path(directory)
        shutil.copyfile(SOURCE,work/'CollegeVenn.idric')
        positive='module Positive\nimport CollegeVenn\nimport Data.Nat\n'+'''same : Percentage symmetric good_job college → Percentage symmetric good_job college
same answer = answer
empty_ok : BoundedFraction 0 0
empty_ok = EmptyPopulation
bound_ok : BoundedFraction 2 5
bound_ok = NonemptyPopulation 2 5 ItIsSucc (LTESucc (LTESucc LTEZero))
complement_ok : complement (the (Region "people") good_job) = Cells False True False True
complement_ok = Refl
'''
        (work/'Positive.idric').write_text(positive)
        (logdir/'Positive.idric').write_text(positive)
        control=run_logged([compiler,'--check','Positive.idric'],logdir/'positive-control.log',cwd=work,env=environment)
        require_compiler_success(control,'positive control for rejection tests')
        for name,body in NEGATIVES.items():
            code=f'module {name}\nimport CollegeVenn\nimport Data.Nat\n'+body
            source=work/(name+'.idric')
            source.write_text(code)
            (logdir/(name+'.idric')).write_text(code)
            result=run_logged([compiler,'--check',source.name],logdir/(name+'.log'),cwd=work,env=environment)
            diagnostic=result.stdout.decode(errors='replace')
            require(not re.search(r'(Parse error|parse error|Module .*not found|Unsolved holes|Undefined name)',diagnostic),
                    'unrelated compiler failure in '+name+' (exit '+str(result.returncode)+'):\n'+diagnostic)
            require(result.returncode!=0,'invalid program accepted: '+name)
            require(re.search(r'(Mismatch|mismatch|unify|constraint|Type mismatch)',diagnostic),
                    'rejection was not a type/index mismatch: '+name+'\n'+diagnostic)
            require(not re.search(r'(Parse error|parse error|Module .*not found|Unsolved holes)',diagnostic),
                    'unrelated compiler failure in '+name)
            require('bad' in diagnostic,'wrong declaration failed in '+name)
            outcomes.append({'case':name,'exit_code':result.returncode,'source_sha256':digest(source),
                             'log_sha256':digest(logdir/(name+'.log'))})
    result=run_logged(['node',executable],output/'model.tsv')
    require(result.returncode==0,'compiled model execution failed')
    text=(output/'model.tsv').read_text()
    frames,answers,oracle_count=check_model_text(text)
    wrongs=[text.replace('50.0%','1 : 1',1),
            text.replace('region\tcomplement\t0101','region\tcomplement\t0100',1),
            text.replace('answer\t0\t1010\t1100','answer\t0\t1100\t1010',1),
            text.replace('\t500\t1000\t50.0%','\t500\t1320\t50.0%',1),
            text.replace('undefined','0.0%',1)]
    for wrong in wrongs:
        require(wrong!=text,'mutation did not alter observed output')
        try:
            check_model_text(wrong)
        except ValueError:
            pass
        else:
            raise ValueError('incorrect model serialization accepted')
    receipt={'status':'PASS','compiler_revision':observed,'compiler_sha256':digest(compiler),
        'model_source_sha256':digest(SOURCE),'model_output_sha256':digest(output/'model.tsv'),
        'executable_sha256':digest(executable),'compile_argv':list(map(str,compile_argv)),
        'backend':'Idriç-generated Node host evaluator; not native/device acceptance',
        'negative_type_cases':outcomes,'positive_control':'Positive.idric',
        'oracle_conditionals':oracle_count,'movie_conditionals':392,'mutated_outputs_rejected':len(wrongs)}
    (output/'model-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':'PASS','phase':'dependent-model','type_rejections':len(outcomes),
                      'oracle_conditionals':oracle_count,'movie_conditionals':392}))


def require_number_pixels(frame, answers, font, palette, scale):
    expected=Image.new('RGB',frame.size,'#070E1D')
    draw=ImageDraw.Draw(expected)
    for index,(right,color) in enumerate(((755,palette['college_outline']),(1515,palette['good_outline']))):
        text=answers[index][6]
        draw.text((right*scale-font.getlength(text),784*scale),text,font=font,fill=color)
        left=right*scale-font.getlength(text)-2*scale
        box=(int(left),int(784*scale),int((right+3)*scale),int(870*scale))
        require(ImageChops.difference(frame.crop(box),expected.crop(box)).getbbox() is None,
                'visible percentage differs from the checked query')


def check_movie(config_path,output):
    config=json.loads(config_path.read_text())
    receipt=json.loads((output/'render-receipt.json').read_text())
    require(receipt['schema_version']==4,'wrong renderer schema')
    require(receipt['renderer_sha256']==digest(ROOT/'scripts/render-college-job-venn.py'),'changed renderer')
    require(receipt['config_sha256']==digest(config_path),'changed visual config')
    require(receipt['model_output_sha256']==digest(output/'model.tsv'),'changed model output')
    require(receipt['model_check_sha256']==digest(output/'model-check.json'),'changed compiler acceptance')
    frames,answers,oracle_count=check_model_text((output/'model.tsv').read_text())
    width,height=receipt['width'],receipt['height']
    scale=width/1600
    font_path=Path(receipt['bold_font'])
    require(digest(font_path)==receipt['bold_font_sha256'],'changed font bytes')
    font=ImageFont.truetype(str(font_path),max(9,round(72*scale)))
    image_paths=sorted((output/'frames').glob('*.png'))
    require(len(image_paths)==196,'wrong source frame count')
    for time,path in enumerate(image_paths):
        with Image.open(path) as frame:
            require(frame.size==(width,height),'wrong frame size')
            require_number_pixels(frame,answers[time],font,config['palette'],scale)
    with Image.open(image_paths[0]) as frame:
        mutant=frame.copy()
    ImageDraw.Draw(mutant).rectangle((470*scale,784*scale,760*scale,870*scale),fill='#070E1D')
    try:
        require_number_pixels(mutant,answers[0],font,config['palette'],scale)
    except ValueError:
        pass
    else:
        raise ValueError('erased visible counter accepted')
    previous=None
    for time in (0,195):
        masks=[]
        for cell in range(4):
            with Image.open(output/f'cell-{time}-{cell}.png') as image:
                mask=image.copy()
            require(mask.mode=='L' and mask.size==(width,height),'invalid atom mask')
            actual=sum(mask.histogram()[1:])
            expected=frames[time][cell]*receipt['area_per_weight']*scale*scale
            require(abs(actual-expected)<max(500*scale,expected*.015),'atom area does not represent its measured weight')
            masks.append(mask)
        union=Image.new('L',(width,height),0)
        for mask in masks:
            require(ImageChops.multiply(union,mask).getbbox() is None,'atomic regions overlap')
            union=ImageChops.lighter(union,mask)
        universe=Image.new('L',(width,height),0)
        ImageDraw.Draw(universe).rectangle(tuple(round(x*scale) for x in receipt['universe']),fill=255)
        require(ImageChops.difference(union,universe).getbbox() is None,'atomic regions do not partition U')
        with Image.open(output/f'complement-{time}.png') as image:
            complement=image.copy()
        expected_complement=ImageChops.lighter(masks[1],masks[3])
        require(ImageChops.difference(complement,expected_complement).getbbox() is None,'bad/no job is not all of the complement')
        college=ImageChops.lighter(masks[0],masks[1])
        if previous:
            require(ImageChops.subtract(previous,college).getbbox() is None,'visible college membership shrank')
        previous=college
    video=output/'college-good-jobs-venn.mp4'
    require(digest(video)==receipt['mp4_sha256'],'changed movie bytes')
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v:0',
        '-show_entries','stream=width,height,nb_read_frames,r_frame_rate','-of','json',str(video)]))['streams'][0]
    require((int(probe['width']),int(probe['height']),int(probe['nb_read_frames']),probe['r_frame_rate'])
            ==(width,height,196,'24/1'),'wrong encoded movie')
    decoder=subprocess.Popen(['ffmpeg','-v','error','-i',str(video),'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    worst=0
    try:
        for time,path in enumerate(image_paths):
            data=decoder.stdout.read(width*height*3)
            require(len(data)==width*height*3,'truncated decoded movie')
            decoded=Image.frombytes('RGB',(width,height),data)
            with Image.open(path) as original:
                delta=ImageChops.difference(decoded,original.convert('RGB'))
                error=max(ImageStat.Stat(delta).rms)
                worst=max(worst,error)
                require(error<12,'encoded frame differs excessively from verified rendering')
        require(decoder.stdout.read(1)==b'','unexpected extra encoded frame')
        require(decoder.wait(timeout=30)==0,'video decoder failed')
    finally:
        if decoder.poll() is None:
            decoder.kill()
    result={'status':'PASS','phase':'movie','frames':196,'oracle_conditionals':oracle_count,
        'visible_counter_checks':392,'erased_counter_rejected':True,'video_sha256':digest(video),
        'maximum_decoded_channel_rms':worst,'initial_counters':[a[6] for a in answers[0]],
        'final_counters':[a[6] for a in answers[195]],'model_check_sha256':digest(output/'model-check.json')}
    (output/'acceptance.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--config',type=Path,default=ROOT/'examples/college-job-venn.json')
    parser.add_argument('--output-dir',type=Path,default=ROOT/'.flexible-pipes/artifacts/college-job-venn')
    parser.add_argument('--typecheck',action='store_true')
    parser.add_argument('--compiler',type=Path,default=ROOT/'runtime/idric/build/exec/idris2')
    args=parser.parse_args()
    if args.typecheck:
        check_type_model(args.compiler,args.output_dir.resolve())
    else:
        check_movie(args.config,args.output_dir.resolve())


if __name__=='__main__':
    main()
