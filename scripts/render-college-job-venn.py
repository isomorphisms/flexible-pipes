#!/usr/bin/env python3
"""Existing raster adapter; all event names and percentages come from Idriç.

Python/Pillow remains inherited rendering debt. This is not the type checker.
The checked model owns the population, membership, query meaning and numbers.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
from PIL import Image, ImageChops, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PIN = '2734ac5a86610eddfab73b1644d72b4ac85a65ee'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_checked_model(root):
    proof = json.loads((root/'model-check.json').read_text())
    checks = {
        'model_source_sha256': ROOT/'models/CollegeVenn.idric',
        'model_output_sha256': root/'model.tsv',
        'executable_sha256': ROOT/'build/exec/college-venn-model',
    }
    if proof['status'] != 'PASS' or proof['compiler_revision'] != PIN:
        raise ValueError('missing successful pinned model check')
    for key, path in checks.items():
        if proof[key] != digest(path):
            raise ValueError('changed checked input: '+key)
    frames, regions, answers = {}, {}, {}
    header = None
    for raw in (root/'model.tsv').read_text().splitlines():
        fields = raw.split('\t')
        if fields[0] == 'model':
            if header is not None or fields[1] != 'college-venn-dependent-v1':
                raise ValueError('duplicate or unsupported model header')
            header = tuple(map(int, fields[2:]))
        elif fields[0] == 'region':
            _, name, code, label = fields
            if name in regions or len(code) != 4 or set(code)-{'0','1'}:
                raise ValueError('invalid region')
            regions[name] = {'code':code, 'label':label}
        elif fields[0] == 'frame':
            time, *weights = map(int, fields[1:])
            if time in frames or len(weights) != 4 or min(weights) < 0:
                raise ValueError('invalid population frame')
            frames[time] = weights
        elif fields[0] == 'answer':
            _, time, event, among, numerator, denominator, displayed, label = fields
            answers.setdefault(int(time), []).append({
                'event':event, 'among':among, 'numerator':int(numerator),
                'denominator':int(denominator), 'displayed':displayed, 'label':label})
        elif fields[0] != 'oracle':
            raise ValueError('unexpected model output: '+raw)
    if header is None:
        raise ValueError('model did not emit a header')
    count, fps, total = header
    if set(regions) != {'college','good','complement'}:
        raise ValueError('missing declared region')
    if regions['college']['code'] != '1100' or regions['good']['code'] != '1010':
        raise ValueError('this layout requires the declared two-predicate cell order')
    if regions['complement']['code'] != ''.join('1' if b == '0' else '0' for b in regions['good']['code']):
        raise ValueError('incorrect complement in model output')
    for time in range(count):
        if sum(frames[time]) != total or len(answers.get(time, [])) != 2:
            raise ValueError('incomplete movie frame')
    return proof, regions, frames, answers, count, fps, total


def font_path(bold):
    candidates = ([ '/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf',
                    '/usr/share/fonts/opentype/inter/Inter-Bold.otf',
                    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'] if bold else
                  ['/usr/share/fonts/opentype/inter/Inter-Regular.otf',
                   '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'])
    for candidate in candidates:
        if Path(candidate).is_file():
            return candidate
    raise RuntimeError('Inter or DejaVu Sans is required')


def wrap_words(text, font, width):
    lines = ['']
    for word in text.split():
        trial = (lines[-1]+' '+word).strip()
        if lines[-1] and font.getlength(trial) > width:
            lines.append(word)
        else:
            lines[-1] = trial
    return '\n'.join(lines)


def selected_area(weights, code):
    return sum(weight for weight, bit in zip(weights, code) if bit == '1')


def right_cap_cut(radius, target_area):
    low, high = -radius, radius
    for _ in range(70):
        cut = (low+high)/2
        area = radius*radius*math.acos(cut/radius)-cut*math.sqrt(max(0,radius*radius-cut*cut))
        if area > target_area:
            low = cut
        else:
            high = cut
    return (low+high)/2


def union_cells(code, cells):
    result = Image.new('L', cells[0].size, 0)
    for bit, cell in zip(code, cells):
        if bit == '1':
            result = ImageChops.lighter(result, cell)
    return result


def render(config, output):
    proof, regions, frames, answers, count, fps, total = load_checked_model(output)
    width, height = int(config['width']), int(config['height'])
    if width < 640 or width % 2 or height % 2 or height*16 != width*9 or config['fps'] != fps:
        raise ValueError('layout must be even-sized 16:9; frame rate comes from the model')
    scale = width/1600
    palette = config['palette']
    bold, regular = font_path(True), font_path(False)
    font = lambda path, size: ImageFont.truetype(path, max(9, round(size*scale)))
    fonts = {name:font(path,size) for name,path,size in (
        ('title',bold,57),('subtitle',regular,20),('large',bold,36),
        ('small',bold,18),('callout',bold,38),('detail',regular,20),
        ('label',regular,24),('percentage',bold,72),('tiny',regular,14))}
    while fonts['title'].getlength(config['title']) > 1400*scale:
        if fonts['title'].size <= 20*scale:
            raise ValueError('title does not fit')
        fonts['title'] = ImageFont.truetype(bold,fonts['title'].size-1)
    good = config['good_circle']
    gx, gy, radius = (float(good[k]) for k in ('x','y','radius'))
    initial = frames[0]
    good_weight = selected_area(initial,regions['good']['code'])
    intersection_code = ''.join('1' if a == b == '1' else '0' for a,b in
                                zip(regions['good']['code'], regions['college']['code']))
    overlap_weight = selected_area(initial,intersection_code)
    area_per_weight = math.pi*radius*radius/good_weight
    cut = gx+right_cap_cut(radius,area_per_weight*overlap_weight)
    universe = (70,180,1540,180+total*area_per_weight/1470)
    if universe[3] > 766:
        raise ValueError('the population does not fit the fixed viewport')
    xy = lambda values: tuple(round(v*scale) for v in values)
    good_box = xy((gx-radius,gy-radius,gx+radius,gy+radius))
    universe_mask = Image.new('L',(width,height),0)
    ImageDraw.Draw(universe_mask).rectangle(xy(universe),fill=255)
    good_mask = Image.new('L',(width,height),0)
    ImageDraw.Draw(good_mask).ellipse(good_box,fill=255)
    if ImageChops.subtract(good_mask,universe_mask).getbbox():
        raise ValueError('good-job region escapes the universe')
    frames_dir = output/'frames'
    frames_dir.mkdir(exist_ok=False)
    layouts = []
    previous_college = Image.new('L',(width,height),0)
    for time in range(count):
        weights = frames[time]
        if selected_area(weights,regions['good']['code']) != good_weight or selected_area(weights,intersection_code) != overlap_weight:
            raise ValueError('this layout requires fixed good jobs and fixed intersection')
        college_weight = selected_area(weights,regions['college']['code'])
        right = cut+college_weight*area_per_weight/(2*radius)
        if right < gx+radius or right > 1150:
            raise ValueError('requested measures do not fit this monotone rectangle/circle layout')
        college_mask = Image.new('L',(width,height),0)
        ImageDraw.Draw(college_mask).rectangle(xy((cut,gy-radius,right,gy+radius)),fill=255)
        if ImageChops.subtract(previous_college,college_mask).getbbox():
            raise ValueError('college membership shrank')
        previous_college = college_mask.copy()
        both = ImageChops.multiply(college_mask,good_mask)
        cells = [both,ImageChops.subtract(college_mask,good_mask),
                 ImageChops.subtract(good_mask,college_mask),
                 ImageChops.subtract(universe_mask,ImageChops.lighter(good_mask,college_mask))]
        complement = union_cells(regions['complement']['code'],cells)
        frame = Image.new('RGB',(width,height),palette['background'])
        frame.paste(palette['good'],(0,0),union_cells(regions['good']['code'],cells))
        frame.paste(palette['college'],(0,0),union_cells(regions['college']['code'],cells))
        frame.paste(palette['intersection'],(0,0),both)
        hatching = Image.new('RGBA',(width,height),(0,0,0,0))
        hd = ImageDraw.Draw(hatching)
        for x in range(-900,2500,36):
            hd.line(xy((x,0,x-900,900)),fill=(255,189,159,45),width=max(1,round(scale)))
        hatching.putalpha(ImageChops.multiply(hatching.getchannel('A'),complement))
        frame = Image.alpha_composite(frame.convert('RGBA'),hatching).convert('RGB')
        draw = ImageDraw.Draw(frame)
        draw.rectangle(xy(universe),outline=palette['secondary_text'],width=max(1,round(scale)))
        draw.ellipse(good_box,outline=palette['good_outline'],width=max(2,round(4*scale)))
        draw.rectangle(xy((cut,gy-radius,right,gy+radius)),outline=palette['college_outline'],width=max(2,round(4*scale)))
        draw.rectangle(xy((0,775,1600,900)),fill='#070E1D')
        draw.line(xy((0,774,1600,774)),fill='#37506B',width=2)
        draw.rectangle(xy((86,51,94,123)),fill=palette['college_outline'])
        draw.text((114*scale,51*scale),config['title'],font=fonts['title'],fill=palette['main_text'])
        draw.text((114*scale,132*scale),config['subtitle'],font=fonts['subtitle'],fill=palette['secondary_text'])
        draw.text((1410*scale,142*scale),'SCHEMATIC',font=fonts['small'],fill=palette['secondary_text'])
        draw.rectangle(xy((88,194,238,230)),fill=palette['background'])
        draw.text((98*scale,201*scale),'ALL PEOPLE',font=fonts['small'],fill=palette['main_text'])
        draw.multiline_text((302*scale,410*scale),regions['good']['label'].replace(' ','\n'),font=fonts['large'],fill=palette['main_text'],spacing=4*scale)
        college_title = regions['college']['label']
        title_width = fonts['small'].getlength(college_title)
        draw.text(((cut+right)*scale/2-title_width/2,232*scale),college_title,font=fonts['small'],fill=palette['college_outline'])
        complement_title = wrap_words(regions['complement']['label'],fonts['callout'],335*scale)
        draw.multiline_text((1180*scale,352*scale),complement_title,font=fonts['callout'],fill=palette['college_outline'],spacing=5*scale)
        draw.text((1180*scale,466*scale),'Everything outside',font=fonts['detail'],fill=palette['main_text'])
        draw.text((1180*scale,495*scale),'the good-job region.',font=fonts['detail'],fill=palette['main_text'])
        draw.text((1180*scale,543*scale),'With or without a degree.',font=fonts['detail'],fill=palette['secondary_text'])
        draw.line(xy((800,794,800,860)),fill='#37506B',width=max(1,round(scale)))
        for index,(left,right_edge,color) in enumerate(((85,755,palette['college_outline']),(840,1515,palette['good_outline']))):
            answer = answers[time][index]
            label = wrap_words(answer['label'],fonts['label'],410*scale)
            if len(label.splitlines()) > 2:
                raise ValueError('conditional population label does not fit')
            draw.multiline_text((left*scale,794*scale),label,font=fonts['label'],fill=palette['main_text'],spacing=7*scale)
            text = answer['displayed']
            draw.text((right_edge*scale-fonts['percentage'].getlength(text),784*scale),text,
                      font=fonts['percentage'],fill=color)
        draw.text((85*scale,878*scale),'ILLUSTRATIVE WEIGHTS — NOT LABOR-MARKET DATA',font=fonts['tiny'],fill=palette['secondary_text'])
        frame.save(frames_dir/f'{time:04}.png',compress_level=3)
        layouts.append({'frame':time,'college_right':right,'weights':weights,'answers':answers[time]})
        if time in (0,count-1):
            frame.save(output/('initial.png' if time==0 else 'college-good-jobs-venn-preview.png'))
            for index,mask in enumerate(cells):
                mask.save(output/f'cell-{time}-{index}.png')
            complement.save(output/f'complement-{time}.png')
    mp4 = output/'college-good-jobs-venn.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(fps),'-i',str(frames_dir/'%04d.png'),
                    '-frames:v',str(count),'-c:v','libx264','-preset','fast','-crf','20',
                    '-pix_fmt','yuv420p','-movflags','+faststart',str(mp4)],check=True)
    manifest = {'schema_version':4,'status':'rendered-not-yet-verified','frames':count,'fps':fps,
        'width':width,'height':height,'model_output_sha256':digest(output/'model.tsv'),
        'model_check_sha256':digest(output/'model-check.json'),'renderer_sha256':digest(__file__),
        'config_sha256':digest(config['_path']),'bold_font':bold,'regular_font':regular,
        'bold_font_sha256':digest(bold),'regular_font_sha256':digest(regular),
        'universe':universe,'good_circle':good,'college_cut':cut,'area_per_weight':area_per_weight,
        'layout':'fixed good-job disk; monotonically expanding college rectangle',
        'regions':regions,'frame_layouts':layouts,'mp4_sha256':digest(mp4)}
    (output/'render-receipt.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'status':'rendered','video':str(mp4),'frames':count,'model':proof['compiler_revision']}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config',required=True,type=Path)
    parser.add_argument('--output-dir',type=Path,default=ROOT/'.flexible-pipes/artifacts/college-job-venn')
    args = parser.parse_args()
    config = json.loads(args.config.read_text())
    config['_path'] = str(args.config.resolve())
    render(config,args.output_dir.resolve())


if __name__ == '__main__':
    main()
