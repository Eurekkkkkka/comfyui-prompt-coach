#!/usr/bin/env python3
"""Render a stable course entry card and check its presentation contract, offline."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def select(lesson, step):
    data = json.loads((ROOT / 'assets/course-20260909/manifest.json').read_text(encoding='utf-8'))
    lesson_id = str(lesson).zfill(2)
    item = next((x for x in data['lessons'] if x['id'] == lesson_id), None)
    if item is None or not 1 <= step <= len(item['steps']):
        raise ValueError('课次或步骤不存在，请先查看当前课卡。')
    return data, item, item['steps'][step-1]


def render(lesson, step):
    data, item, current = select(lesson, step)
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    sections = [
        f"课程{data['course_version']}｜Skill {version}｜第{item['id']}课｜{current['id']}｜教案提取模板｜待输入",
        current['title'],
        f"待补充：{current['input']}\n\n本步交付目标：{current['deliverable']}。尚未生成或验收。",
        '先在当前对话提供本步输入；需要操作节点时，提供实际工作流JSON或截图后定位。',
        f"状态：待输入。\n\n{current['gate']}",
        f"只提供本步输入。\n\n可以直接回复：继续 {current['id']}，这是本步需要的材料。",
    ]
    return '\n\n'.join(f'## {h}\n\n{s}' for h,s in zip(data['headings'],sections))+'\n'


def check(text, lesson, step):
    data, item, current = select(lesson, step)
    # Ignore headings inside fenced prompt/JSON blocks.
    clean = re.sub(r'```[^\n]*\n.*?```', '', text, flags=re.S)
    headings = re.findall(r'^## (.+?)\s*$', clean, flags=re.M)
    errors=[]
    if headings != data['headings']:
        errors.append('六个二级标题缺失、重复、顺序或名称不符。')
    progress = clean.split('## 本步目标')[0]
    if current['id'] not in progress or f"第{item['id']}课" not in progress:
        errors.append('课程进度与请求课次/步骤不一致。')
    if data['course_version'] not in progress:
        errors.append('课程快照版本缺失。')
    for heading in data['headings']:
        match=re.search(r'^## '+re.escape(heading)+r'\s*\n(.*?)(?=^## |\Z)',clean,re.M|re.S)
        if match and not match.group(1).strip():
            # Prompt-only results still have content in the original text.
            original=re.search(r'^## '+re.escape(heading)+r'\s*\n(.*?)(?=^## |\Z)',text,re.M|re.S)
            if not original or not original.group(1).strip(): errors.append(heading+'为空。')
    return {'ok':not errors,'errors':errors,'scope':'仅检查输出外壳，不验证事实、媒体、推进条件或模型兼容性。'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['render','check'])
    parser.add_argument('--lesson',required=True)
    parser.add_argument('--step',type=int,required=True)
    parser.add_argument('--file',type=Path)
    args=parser.parse_args()
    try:
        if args.command=='render': print(render(args.lesson,args.step),end='')
        else:
            if not args.file: parser.error('check需要--file')
            result=check(args.file.read_text(encoding='utf-8-sig'),args.lesson,args.step)
            print(json.dumps(result,ensure_ascii=False))
            if not result['ok']: sys.exit(1)
    except (ValueError,OSError) as error:
        print(str(error),file=sys.stderr); sys.exit(2)


if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
    main()
