#!/usr/bin/env python3
"""Deterministic, area-accurate conceptual Venn video; independent of ML inference.

Requirements: Python 3.11+, Pillow, FFmpeg and ffprobe.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFont, __version__ as pillow_version

DESIGN_WIDTH, DESIGN_HEIGHT = 1600, 900
FONT_BOLD = [
    '/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf',
    '/usr/share/fonts/opentype/inter/Inter-Bold.otf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
]
FONT_NORMAL = [
    '/usr/share/fonts/opentype/inter/Inter-Regular.otf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def overlap_area(a: float, b: float, separation: float) -> float:
    """Exact Euclidean area shared by two disks of radii a, b."""
    if separation >= a + b:
        return 0.0
    if separation <= abs(a - b):
        return math.pi * min(a, b) ** 2
    cosine_a = (separation**2 + a**2 - b**2) / (2 * separation * a)
    cosine_b = (separation**2 + b**2 - a**2) / (2 * separation * b)
    return (
        a*a * math.acos(max(-1.0, min(1.0, cosine_a)))
        + b*b * math.acos(max(-1.0, min(1.0, cosine_b)))
        - 0.5 * math.sqrt(max(0, (-separation+a+b)*(separation+a-b)
                                   *(separation-a+b)*(separation+a+b)))
    )


def solve_college_circle(good_radius: float, constant_overlap: float, bad_good_ratio: float) -> tuple[float, float]:
    """Return college radius and center separation for the requested area ratio.

    College area = (1+ratio)×intersection. Bisection keeps the intersection
    itself fixed. Therefore college-only area / overlap = ratio exactly.
    """
    college_radius = math.sqrt((bad_good_ratio + 1.0)*constant_overlap/math.pi)
    lower = abs(good_radius-college_radius)
    upper = good_radius+college_radius
    if constant_overlap >= math.pi*min(good_radius,college_radius)**2:
        raise ValueError('overlap too large for college and good job disks')
    for _ in range(68):
        middle = (lower+upper)/2
        if overlap_area(good_radius, college_radius, middle) > constant_overlap:
            lower = middle
        else:
            upper = middle
    separation = (lower + upper)/2
    actual = overlap_area(good_radius, college_radius, separation)
    calculated_ratio = (math.pi*college_radius**2-actual)/actual
    if abs(calculated_ratio-bad_good_ratio) > 1e-8:
        raise AssertionError(f'area solver error: {calculated_ratio} vs {bad_good_ratio}')
    return college_radius, separation


def smooth(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t*t*(3-2*t)


def schedule(config: dict) -> tuple[list[tuple[float, float, float]], float]:
    """Return (start_seconds,end_seconds,ratio) for holds and transitions.

    Negative ratios are rejected, and durations are explicit inputs.
    """
    start = float(config['start_ratio'])
    marks = [float(x) for x in config['milestones']]
    if start < 0 or any(b <= a for a,b in zip([start]+marks,marks)):
        raise ValueError('ratios must grow strictly and be nonnegative')
    hold0 = float(config['start_hold_seconds'])
    transition = float(config['transition_seconds'])
    hold = float(config['milestone_hold_seconds'])
    last_hold = float(config['end_hold_seconds'])
    if min(hold0, transition, hold, last_hold) <= 0:
        raise ValueError('all timing durations must be positive')
    out = [(0.0, hold0, start, start)]
    now = hold0
    previous = start
    for i, next_ratio in enumerate(marks):
        out.append((now, now+transition, previous, next_ratio))
        now += transition
        h = last_hold if i == len(marks)-1 else hold
        out.append((now, now+h, next_ratio, next_ratio))
        now += h
        previous = next_ratio
    return out, now


def ratio_at(time_s: float, segments: list) -> float:
    for start,end,r0,r1 in segments:
        if time_s <= end + 1e-10:
            return r0 + (r1-r0)*smooth((time_s-start)/(end-start))
    return segments[-1][3]


def rgba(color: str) -> tuple[int,int,int,int]:
    h=color.lstrip('#')
    if len(h)!=6:
        raise ValueError('palette colors must be six-digit hex')
    return tuple(int(h[i:i+2],16) for i in (0,2,4))+(255,)


def choose_font(paths: list[str]) -> str:
    for path in paths:
        if Path(path).is_file():
            return path
    raise RuntimeError('no compatible system font (Inter or DejaVu Sans)')


def circle_bbox(cx: float, cy: float, radius: float, scale: float) -> tuple[int,int,int,int]:
    return tuple(round(v*scale) for v in (cx-radius,cy-radius,cx+radius,cy+radius))


def label_center(draw: ImageDraw.ImageDraw, xy: tuple[float,float], content: str,
                 font: ImageFont.FreeTypeFont, fill: str, scale: float, spacing: float = 1.08):
    lines=content.split('\n')
    line_height=font.size*spacing
    start_y=xy[1]*scale - len(lines)*line_height/2
    for i,line in enumerate(lines):
        box=draw.textbbox((0,0),line,font=font)
        text_width=box[2]-box[0]
        draw.text((xy[0]*scale-text_width/2, start_y+i*line_height),line,font=font,fill=fill)


def render(config: dict, output_dir: Path, retain_frames: bool) -> dict:
    width, height, fps = [int(config[k]) for k in ('width','height','fps')]
    if width < 640 or height*16 != width*9 or fps < 10 or fps > 60:
        raise ValueError('expected 16:9 output, width >= 640, fps 10–60')
    scale = width / DESIGN_WIDTH
    c = config['palette']
    for field in ('background','good','good_outline','college','college_outline','intersection','main_text','secondary_text'):
        rgba(c[field])
    good = config['good_circle']
    good_x,good_y,good_r = (float(good[k]) for k in ('x','y','radius'))
    area=float(config['constant_overlap_area'])
    if area <= 0 or good_r<=0 or area>=math.pi*good_r**2:
        raise ValueError('invalid fixed overlap / good job circle')
    segments,duration=schedule(config)
    count=round(duration*fps)
    if count<1:
        raise ValueError('empty animation')
    output_dir.mkdir(parents=True,exist_ok=True)
    frames=output_dir/'frames'
    frames.mkdir(exist_ok=True)
    bold=choose_font(FONT_BOLD)
    normal=choose_font(FONT_NORMAL)
    font=lambda path,pts: ImageFont.truetype(path,max(9,round(pts*scale)))
    fonts={
        'title':font(bold,57), 'subtitle':font(normal,20),
        'disc':font(bold,18), 'big':font(bold,36),
        'medium':font(bold,30), 'overlap':font(bold,19),
        'footer_label':font(normal,24), 'footer_sub':font(normal,18),
        'percentage':font(bold,78), 'tiny':font(normal,14),
        'callout':font(bold,38), 'callout_sub':font(normal,20)
    }
    title=str(config['title'])
    subtitle=str(config['subtitle'])
    if '\n' in title or '\n' in subtitle:
        raise ValueError('single-line title and subtitle required')
    # Fit the title across supported fonts (DejaVu is wider than Inter).
    while fonts['title'].getlength(title)>1450*scale and fonts['title'].size>round(32*scale):
        fonts['title']=ImageFont.truetype(bold,fonts['title'].size-1)
    if fonts['title'].getlength(title)>1450*scale:
        raise ValueError('title is too long even at minimum display size')
    bg=Image.new('RGBA',(width,height),rgba(c['background']))
    grid=ImageDraw.Draw(bg)
    # Background grid and divider, generated once.
    for x in range(75,1580,72):
        sx=round(x*scale)
        grid.line((sx,round(195*scale),sx,round(760*scale)),fill='#18283E',width=max(1,round(scale)))
    for y in range(198,760,72):
        sy=round(y*scale)
        grid.line((round(70*scale),sy,round(1540*scale),sy),fill='#18283E',width=max(1,round(scale)))
    for x in range(110,1500,180):
        for y in range(218,760,180):
            r=max(1,round(1.5*scale))
            grid.ellipse((x*scale-r,y*scale-r,x*scale+r,y*scale+r),fill='#40506A')
    grid.rectangle((0,round(775*scale),width,height),fill='#070E1D')
    grid.line((round(85*scale),round(174*scale),round(1515*scale),round(174*scale)),fill='#2B3E55',width=2)
    grid.line((0,round(774*scale),width,round(774*scale)),fill='#37506B',width=2)
    grid.rectangle((round(86*scale),round(51*scale),round(94*scale),round(123*scale)),fill=c['college_outline'])
    grid.text((114*scale,51*scale),title,font=fonts['title'],fill=c['main_text'])
    grid.text((114*scale,132*scale),subtitle,font=fonts['subtitle'],fill=c['secondary_text'])
    grid.text((1430*scale,142*scale),'SCHEMATIC',font=fonts['disc'],fill=c['secondary_text'])
    # Static good job area.
    good_box=circle_bbox(good_x,good_y,good_r,scale)
    good_mask=Image.new('L',(width,height),0)
    ImageDraw.Draw(good_mask).ellipse(good_box,fill=255)
    good_layer=Image.new('RGBA',(width,height),rgba(c['good']))
    good_layer.putalpha(good_mask.point([int(i*.78) for i in range(256)]))
    bg.alpha_composite(good_layer)
    bad_layer_color=rgba(c['college'])
    overlap_color=rgba(c['intersection'])
    milestone_frames={}
    frame_statistics=[]
    footer_labels={
        'college_graduates_with_good_job_pct': '% of college graduates\nwith a good job',
        'good_job_holders_with_college_degree_pct': '% of people with a good job\nwho have a college degree',
    }
    for i in range(count):
        elapsed=i/fps
        q=ratio_at(elapsed,segments)
        r,d=solve_college_circle(good_r,area,q)
        cx=good_x+d
        actual_overlap=overlap_area(good_r,r,d)
        # Same numerator, different populations in the denominators.
        percentages={
            'college_graduates_with_good_job_pct': 100*actual_overlap/(math.pi*r*r),
            'good_job_holders_with_college_degree_pct': 100*actual_overlap/(math.pi*good_r*good_r),
        }
        percentage_texts={key:f'{value:.1f}%' for key,value in percentages.items()}
        statistics={
            'frame':i,'ratio':q,'circle_radius':r,'center_separation':d,
            'actual_overlap_area':actual_overlap,**percentages,
            'footer_display':percentage_texts,
        }
        frame_statistics.append(statistics)
        if cx+r>1150 or good_y+r>772 or good_y-r<180:
            raise ValueError('geometry exceeds diagram viewport; adjust design inputs')
        box=circle_bbox(cx,good_y,r,scale)
        college_mask=Image.new('L',(width,height),0)
        ImageDraw.Draw(college_mask).ellipse(box,fill=255)
        college_layer=Image.new('RGBA',(width,height),bad_layer_color)
        college_layer.putalpha(college_mask.point([int(i*.75) for i in range(256)]))
        frame=bg.copy()
        frame.alpha_composite(college_layer)
        intersection_mask=ImageChops.multiply(good_mask,college_mask)
        inter_layer=Image.new('RGBA',(width,height),overlap_color)
        inter_layer.putalpha(intersection_mask.point([int(i*.97) for i in range(256)]))
        frame.alpha_composite(inter_layer)
        draw=ImageDraw.Draw(frame)
        # The two outlines remain visible through their overlap.
        draw.ellipse(good_box,outline=c['good_outline'],width=max(2,round(4*scale)))
        draw.ellipse(box,outline=c['college_outline'],width=max(2,round(4*scale)))
        label_center(draw,(355,430),'GOOD\nJOB',fonts['big'],c['main_text'],scale)
        label_center(draw,(cx+r*.43,435),'WENT TO\nCOLLEGE',fonts['medium'],'#FFE4D9',scale)
        # Intersection stays fixed in area, though its boundary adjusts slightly.
        draw.rounded_rectangle((round(516*scale),round(570*scale),round(658*scale),round(605*scale)),
                               radius=16*scale,fill='#0A4651',outline='#83CECF',width=max(1,round(scale)))
        label_center(draw,(587,581),'OVERLAP',fonts['overlap'],'#E8FCF8',scale)
        # The coral region to the right of blue is the bad-job part of college.
        arrow_start=round(1162*scale)
        arrow_end=round((cx+r+18)*scale)
        arrow_y=round(470*scale)
        draw.line((arrow_start,arrow_y,arrow_end,arrow_y),fill=c['college_outline'],width=max(2,round(3*scale)))
        draw.polygon([(arrow_end,arrow_y),(arrow_end+round(14*scale),arrow_y-round(8*scale)),
                      (arrow_end+round(14*scale),arrow_y+round(8*scale))],fill=c['college_outline'])
        draw.text((1180*scale,402*scale),'BAD JOBS',font=fonts['callout'],fill=c['college_outline'])
        draw.text((1180*scale,451*scale),'College graduates',font=fonts['callout_sub'],fill=c['main_text'])
        draw.text((1180*scale,480*scale),'outside the blue circle',font=fonts['callout_sub'],fill=c['secondary_text'])
        # Two conditional percentages, each bound to its whole-circle population.
        # The right counter stays constant because good jobs and overlap are fixed.
        draw.line((800*scale,794*scale,800*scale,860*scale),fill='#37506B',width=max(1,round(scale)))
        for key,left,right,color in (
            ('college_graduates_with_good_job_pct',85,755,c['college_outline']),
            ('good_job_holders_with_college_degree_pct',840,1515,c['good_outline']),
        ):
            draw.multiline_text((left*scale,794*scale),footer_labels[key],
                                font=fonts['footer_label'],fill=c['main_text'],spacing=7*scale)
            value_text=percentage_texts[key]
            value_width=draw.textlength(value_text,font=fonts['percentage'])
            draw.text((right*scale-value_width,784*scale),value_text,
                      font=fonts['percentage'],fill=color)
        draw.text((85*scale,878*scale),'ILLUSTRATIVE AREAS — NOT LABOR-MARKET DATA',
                  font=fonts['tiny'],fill=c['secondary_text'])
        path=frames/f'frame-{i:04}.png'
        frame.convert('RGB').save(path,optimize=False,compress_level=3)
        for target in [float(config['start_ratio'])]+[float(k) for k in config['milestones']]:
            if target not in milestone_frames and abs(q-target)<.0000001:
                milestone_frames[target]=statistics.copy()
        if i==count-1:
            final_frame=path
    stem=config['filename']
    mp4=output_dir/f'{stem}.mp4'
    gif=output_dir/f'{stem}.gif'
    preview=output_dir/f'{stem}-preview.png'
    shutil.copyfile(final_frame,preview)
    # Use exactly enumerated frames and reject any failed encoder.
    framerate=str(fps)
    pattern=str(frames/'frame-%04d.png')
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-framerate',framerate,
                    '-i',pattern,'-c:v','libx264','-preset','fast','-crf','22',
                    '-pix_fmt','yuv420p','-movflags','+faststart',str(mp4)],check=True)
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(mp4),
                    '-filter_complex',('fps=10,scale=720:-2:flags=lanczos,split[s0][s1];'
                        '[s0]palettegen=max_colors=64:stats_mode=diff[p];'
                        '[s1][p]paletteuse=dither=bayer:bayer_scale=4'),
                    '-loop','0',str(gif)],check=True)
    probe=json.loads(subprocess.run(['ffprobe','-v','error','-count_frames','-select_streams','v:0',
                                     '-show_entries','stream=width,height,nb_read_frames,r_frame_rate',
                                     '-of','json',str(mp4)],capture_output=True,text=True,check=True).stdout)
    stream=probe['streams'][0]
    if int(stream['width'])!=width or int(stream['height'])!=height or int(stream['nb_read_frames'])!=count:
        raise AssertionError(f'encoded video mismatch: {stream}')
    if stream['r_frame_rate'] != f'{fps}/1':
        raise AssertionError(f'video fps mismatch: {stream}')
    manifest={
        'schema_version':2,
        'generator':'scripts/render-college-job-venn.py',
        'generator_sha256':sha256(Path(__file__)),
        'title':title,
        'semantic_definition':{
            'college_graduates_with_good_job_pct':'100 * area(college intersect good jobs) / area(college)',
            'good_job_holders_with_college_degree_pct':'100 * area(college intersect good jobs) / area(good jobs)',
        },
        'geometry_ratio_definition':'area(college minus good jobs) / area(college intersect good jobs); not a footer statistic',
        'footer_labels':{key:value.replace('\n',' ') for key,value in footer_labels.items()},
        'frame_statistics':frame_statistics,
        'data_status':'schematic; no empirical counts asserted',
        'constant_good_job_radius':good_r,
        'constant_good_job_overlap_area':area,
        'milestone_frames':{str(k):v for k,v in sorted(milestone_frames.items())},
        'config_sha256':sha256(Path(config['_config_path'])),
        'font_sha256':{'bold':sha256(Path(bold)),'normal':sha256(Path(normal))},
        'font_paths':{'bold':bold,'normal':normal},
        'runtime':{'python':platform.python_version(),'pillow':pillow_version,
                   'ffmpeg':subprocess.run(['ffmpeg','-version'],capture_output=True,text=True,check=True).stdout.splitlines()[0]},
        'frames':count,'fps':fps,'width':width,'height':height,'duration_seconds':count/fps,
        'files':{p.name:{'sha256':sha256(p),'bytes':p.stat().st_size} for p in (mp4,gif,preview)},
    }
    receipt_path=output_dir/f'{stem}-receipt.json'
    receipt_path.write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
    if not retain_frames:
        shutil.rmtree(frames)
    return manifest


def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument('--config',required=True,type=Path)
    parser.add_argument('--output-dir',type=Path,default=Path('.flexible-pipes/artifacts/college-job-venn'))
    parser.add_argument('--retain-frames',action='store_true')
    args=parser.parse_args()
    config=json.loads(args.config.read_text(encoding='utf-8'))
    if config.get('schema_version')!=1:
        raise ValueError('unsupported config schema_version')
    config['_config_path']=str(args.config.resolve())
    manifest=render(config,args.output_dir,args.retain_frames)
    print(json.dumps({'result':'rendered-and-probed','video':str(args.output_dir/(config['filename']+'.mp4')),
                      'frames':manifest['frames'],'milestones':manifest['milestone_frames']},sort_keys=True))
    return 0


if __name__=='__main__':
    sys.exit(main())
