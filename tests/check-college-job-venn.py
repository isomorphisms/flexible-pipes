#!/usr/bin/env python3
"""Independent output checks for the college/job Venn animation."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
from PIL import Image


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--config',required=True,type=Path)
    p.add_argument('--output-dir',required=True,type=Path)
    args=p.parse_args()
    conf=json.loads(args.config.read_text())
    root=args.output_dir
    receipt=json.loads((root/(conf['filename']+'-receipt.json')).read_text())
    assert receipt['config_sha256']==sha(args.config)
    assert receipt['title']=="You can't get a good job without a college degree"
    assert receipt['data_status'].startswith('schematic')
    area=float(conf['constant_overlap_area'])
    good_r=float(conf['good_circle']['radius'])
    assert 0<area<math.pi*good_r**2
    marks=conf['milestones']
    frames=receipt['milestone_frames']
    for expected in [conf['start_ratio']]+marks:
        match=frames[str(float(expected))]
        r=match['circle_radius']
        intersection=match['actual_overlap_area']
        ratio=(math.pi*r*r-intersection)/intersection
        assert abs(intersection-area)<1e-6,(expected,intersection,area)
        assert abs(ratio-expected)<1e-8,(expected,ratio)
    for name,meta in receipt['files'].items():
        file=root/name
        assert file.is_file() and file.stat().st_size==meta['bytes']
        assert sha(file)==meta['sha256']
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
        'ratios':[conf['start_ratio']]+marks},sort_keys=True))


if __name__=='__main__':
    main()
