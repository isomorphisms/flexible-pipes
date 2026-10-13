#!/usr/bin/env python3
"""Independent geometry and conditional-percentage checks for the Venn movie."""
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import subprocess
from PIL import Image, ImageChops, ImageDraw


LABELS = {
    'college_graduates_with_good_job_pct': '% of college graduates with a good job',
    'good_job_holders_with_college_degree_pct': '% of people with a good job who have a college degree',
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_percentages(row, good_area, college_area, overlap):
    """Do not import the producer or confuse the two denominator populations."""
    expected = {
        'college_graduates_with_good_job_pct': 100 * overlap / college_area,
        'good_job_holders_with_college_degree_pct': 100 * overlap / good_area,
    }
    if set(row['footer_display']) != set(expected):
        raise ValueError('footer must display exactly the two conditional percentages')
    for key, value in expected.items():
        observed = row[key]
        if not math.isfinite(observed) or not math.isclose(observed, value, abs_tol=1e-7):
            raise ValueError('wrong denominator or percentage scale: ' + key)
        if row['footer_display'][key] != f'{value:.1f}%':
            raise ValueError('wrong displayed percentage: ' + key)


def integrated_overlap(good_radius, college_radius, distance):
    """Independent midpoint integration, rather than the producer's lens formula."""
    left = max(-good_radius, distance - college_radius)
    right = min(good_radius, distance + college_radius)
    if right <= left:
        return 0.0
    step = (right - left) / 8192
    total = 0.0
    for i in range(8192):
        x = left + (i + .5) * step
        total += 2 * min(math.sqrt(max(0, good_radius**2 - x**2)),
                         math.sqrt(max(0, college_radius**2 - (x-distance)**2)))
    return total * step


def check_rejected_footer_regressions(first, last, good_area, overlap):
    """The previous count ratio and either wrong denominator must fail."""
    cases = []
    for key in LABELS:
        mutant = copy.deepcopy(first)
        other = next(k for k in LABELS if k != key)
        mutant[key] = first[other]
        mutant['footer_display'][key] = first['footer_display'][other]
        cases.append(mutant)
    mutant = copy.deepcopy(first)
    mutant['footer_display']['college_graduates_with_good_job_pct'] = '1 : 1'
    cases.append(mutant)
    mutant = copy.deepcopy(first)
    mutant['college_graduates_with_good_job_pct'] /= 100
    cases.append(mutant)
    mutant = copy.deepcopy(last)
    mutant['college_graduates_with_good_job_pct'] = first['college_graduates_with_good_job_pct']
    mutant['footer_display']['college_graduates_with_good_job_pct'] = first['footer_display']['college_graduates_with_good_job_pct']
    cases.append(mutant)
    for row in cases:
        try:
            check_percentages(row, good_area, math.pi * row['circle_radius']**2, overlap)
        except ValueError:
            continue
        raise AssertionError('incorrect footer unexpectedly accepted')
    return len(cases)


def require_complement(candidate, universe, good):
    """G and its complement partition U, regardless of college membership."""
    if candidate.size != universe.size or candidate.mode != 'L':
        raise ValueError('complement mask has the wrong shape or mode')
    if ImageChops.multiply(candidate, good).getbbox() is not None:
        raise ValueError('good-job holders cannot be in the complement')
    if ImageChops.difference(ImageChops.lighter(candidate, good), universe).getbbox() is not None:
        raise ValueError('complement omits people outside good jobs or exceeds the universe')


def check_complement(receipt, conf, root):
    assert receipt['complement_label'] == 'BAD JOB OR NO JOB'
    assert receipt['complement_definition'] == 'universe minus good jobs; independent of college membership'
    assert receipt['universe_design_bbox'] == [70, 180, 1540, 766]
    size = (conf['width'], conf['height'])
    scale = conf['width'] / 1600
    universe = Image.new('L', size, 0)
    ImageDraw.Draw(universe).rectangle(tuple(round(x*scale) for x in (70,180,1540,766)), fill=255)
    x, y, r = (float(conf['good_circle'][k]) for k in ('x','y','radius'))
    good = Image.new('L', size, 0)
    ImageDraw.Draw(good).ellipse(tuple(round(v*scale) for v in (x-r,y-r,x+r,y+r)), fill=255)
    with Image.open(root / receipt['complement_mask']) as image:
        observed = image.copy()
    require_complement(observed, universe, good)
    # Reject the previous mistake at every growth milestone, not just one frame.
    rejected = 0
    for row in receipt['milestone_frames'].values():
        cx, cr = x + row['center_separation'], row['circle_radius']
        college = Image.new('L', size, 0)
        ImageDraw.Draw(college).ellipse(tuple(round(v*scale) for v in (cx-cr,y-cr,cx+cr,y+cr)), fill=255)
        for wrong in (ImageChops.multiply(observed,college),
                      ImageChops.subtract(observed,college), universe):
            try:
                require_complement(wrong,universe,good)
            except ValueError:
                rejected += 1
            else:
                raise AssertionError('incorrect complement accepted')
    return rejected


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--config',required=True,type=Path)
    p.add_argument('--output-dir',required=True,type=Path)
    args=p.parse_args()
    conf=json.loads(args.config.read_text())
    root=args.output_dir
    receipt=json.loads((root/(conf['filename']+'-receipt.json')).read_text())
    assert receipt['schema_version']==3
    assert receipt['config_sha256']==sha(args.config)
    assert receipt['generator_sha256']==sha(Path(__file__).resolve().parents[1]/receipt['generator'])
    assert receipt['title']=="You can't get a good job without a college degree"
    assert receipt['data_status'].startswith('schematic')
    assert receipt['footer_labels']==LABELS
    area=float(conf['constant_overlap_area'])
    good_r=float(conf['good_circle']['radius'])
    good_area=math.pi*good_r**2
    assert 0<area<good_area
    marks=conf['milestones']
    frames=receipt['milestone_frames']
    for expected in [conf['start_ratio']]+marks:
        match=frames[str(float(expected))]
        r=match['circle_radius']
        intersection=match['actual_overlap_area']
        ratio=(math.pi*r*r-intersection)/intersection
        assert abs(intersection-area)<1e-6,(expected,intersection,area)
        assert abs(integrated_overlap(good_r,r,match['center_separation'])-area)<area*1e-5
        assert abs(ratio-expected)<1e-8,(expected,ratio)
        check_percentages(match,good_area,math.pi*r*r,area)
    rows=receipt['frame_statistics']
    assert len(rows)==receipt['frames']
    previous=math.inf
    for i,row in enumerate(rows):
        assert row['frame']==i
        assert abs(row['actual_overlap_area']-area)<1e-6
        college_area=math.pi*row['circle_radius']**2
        assert abs(college_area/area-1-row['ratio'])<1e-8
        check_percentages(row,good_area,college_area,area)
        current=row['college_graduates_with_good_job_pct']
        assert current<=previous+1e-8
        previous=current
    rejected=check_rejected_footer_regressions(rows[0],rows[-1],good_area,area)
    for name,meta in receipt['files'].items():
        file=root/name
        assert file.is_file() and file.stat().st_size==meta['bytes']
        assert sha(file)==meta['sha256']
    complement_rejected=check_complement(receipt,conf,root)
    video=root/(conf['filename']+'.mp4')
    stream=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v:0',
        '-show_entries','stream=width,height,nb_read_frames,r_frame_rate','-of','json',str(video)],text=True))['streams'][0]
    assert int(stream['nb_read_frames'])==receipt['frames']
    assert int(stream['width'])==int(conf['width'])
    assert int(stream['height'])==int(conf['height'])
    assert stream['r_frame_rate']==str(conf['fps'])+'/1'
    preview=root/(conf['filename']+'-preview.png')
    with Image.open(preview) as frame:
        assert frame.size==(conf['width'],conf['height'])
    print(json.dumps({'status':'PASS','video_sha256':sha(video),'frames':receipt['frames'],
        'footer_labels':LABELS,'final_percentages':rows[-1]['footer_display'],
        'incorrect_footer_regressions_rejected':rejected,
        'incorrect_complement_regressions_rejected':complement_rejected},sort_keys=True))


if __name__=='__main__':
    main()
