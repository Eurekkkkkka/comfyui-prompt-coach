#!/usr/bin/env python3
"""Read workflow sockets and links; export learner-facing facts without saved media or prompts.

Usage: python inspect_workflow_inputs.py WORKFLOWS --object-info object_info.json --output facts.json
No network requests, execution of nodes, or alteration of source workflows.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

TEXT_FIELDS = {'text', 'prompt', 'positive_prompt', 'negative_prompt', 'global_prompt',
               'custom_prompt', 'target_text', 'instruct', 'brief', 'lyrics', 'constraints',
               'reference_map', 'instruction', 'string', 'prompt_1', 'prompt_2', 'prompt_3',
               'multi_line_prompt', 'high_level_description', 'background', 'aesthetics', 'lighting', 'medium'}
PARAMS = {'width', 'height', 'custom_width', 'custom_height', 'duration_s', 'duration_seconds',
          'frame_rate', 'fps', 'length', 'total_frames', 'frame_load_cap', 'skip_first_frames',
          'select_every_nth', 'force_rate', 'target_lufs', 'multiplier', 'scale_by',
          'top', 'bottom', 'left', 'right', 'denoise', 'horizontal_angle', 'vertical_angle',
          'zoom', 'azimuth', 'elevation'}
DIRECTORS = {'MiniMaxH3Creator', 'MiniMaxH3Director', 'ComfyBerniniDirector', 'LTXDirector'}
EXCLUDED = {'Note', 'MarkdownNote', 'SetNode', 'GetNode', 'PreviewAny', 'ShowText|pysssss',
            'easy showAnything', 'StringFunction|pysssss', 'Krea2EditGroundedEncode'}

def socket_role(node, field, byid, links):
    """Use explicit socket names and conditioning routes, never words in prompt prose."""
    if 'negative' in field.lower(): return '负向'
    if field in {'lyrics', 'target_text'}: return '歌词' if field == 'lyrics' else '台词'
    if field == 'instruct': return '音色/表演说明'
    if field == 'reference_map': return '素材编号对应'
    if field == 'constraints': return '约束'
    if 'negative' in node.get('title', '').lower() or '负向' in node.get('title', ''): return '负向'
    seen=set();todo=[node['id']];found=set()
    for _ in range(len(byid)+1):
        nxt=[]
        for nid in todo:
            if nid in seen: continue
            seen.add(nid)
            for link in links:
                if link[1] != nid: continue
                dest=byid.get(link[3],{}); ins=dest.get('inputs',[])
                name=ins[link[4]].get('name','').lower() if link[4]<len(ins) else ''
                if name in {'negative','negative_prompt'}: found.add('负向')
                elif name in {'positive','positive_prompt'}: found.add('正向/编辑指令')
                elif dest.get('type') not in {'ConditioningZeroOut','KSampler','KSamplerAdvanced'}:
                    nxt.append(link[3])
        todo=nxt
        if not todo:break
    if len(found)==1:return found.pop()
    return '文本（用途见专用说明）'

def inspect(path, root, schemas):
    raw=path.read_bytes();d=json.loads(raw);nodes=d.get('nodes',[]);byid={n['id']:n for n in nodes}
    links=[l for l in d.get('links',[]) if isinstance(l,list) and len(l)>=6]
    bylink={l[0]:l for l in links};rel=path.relative_to(root).as_posix()
    setters={}
    for n in nodes:
        if n['type']=='SetNode' and n.get('widgets_values'):
            setters[n['widgets_values'][0]]=n
    # Get/Set are virtual links in the editor, and must be followed for true input locations.
    for n in nodes:
        if n['type']=='GetNode' and n.get('widgets_values'):
            setter=setters.get(n['widgets_values'][0])
            if setter:links.append([f"virtual-{n['id']}",setter['id'],0,n['id'],0,'*'])
    def resolve_source(nid):
        seen=set()
        while nid not in seen:
            seen.add(nid);n=byid.get(nid,{})
            if n.get('type')=='GetNode':
                vals=n.get('widgets_values',[]);setter=setters.get(vals[0]) if vals else None
                if not setter:break
                nid=setter['id']
            elif n.get('type') in ('SetNode','Reroute'):
                ins=n.get('inputs',[]);l=bylink.get(ins[0].get('link')) if ins else None
                if not l:break
                nid=l[1]
            else:break
        return nid
    r={'file':rel,'sha256':hashlib.sha256(raw).hexdigest(),'name':path.stem,
       'category':rel.split('/')[0] if '/' in rel else '根目录',
       'id':'wf-'+hashlib.sha256(rel.encode()).hexdigest()[:10],
       'text_inputs':[],'linked_text':[],'media':[],'controls':[],'outputs':[], 'mask_nodes':[],
       'node_types':sorted({n['type'] for n in nodes}), 'nodes':[]}
    for n in nodes:
        typ=n['type'];title=n.get('title','');nid=n['id'];mode=n.get('mode',0)
        inputs=n.get('inputs',[])
        r['nodes'].append({'id':nid,'type':typ,'mode':mode,'inputs':[{k:i[k] for k in ('name','type','link') if k in i} for i in inputs]})
        marketing_image=typ=='LoadImage' and re.search('二维码|速成班|免费速成|扫码',str(n.get('widgets_values',[])))
        if mode in (2,4) or marketing_image or re.search('扫码|二维码|入群|免费速成|联系方式|作者',title):continue
        schema=schemas.get(typ,{});fields={}
        for group in ('required','optional'):fields.update(schema.get('input',{}).get(group,{}))
        saved={i['name']:i for i in inputs}
        # Workflows with legacy sockets use the runtime schema; new ones expose widgets in inputs.
        candidates={k:v for k,v in fields.items() if v and v[0]=='STRING'}
        for i in inputs:
            if i.get('type')=='STRING' and i.get('widget'):candidates.setdefault(i['name'],['STRING',{}])
        if typ=='PrimitiveNode' and any(l[1]==nid and l[5]=='STRING' for l in links):candidates['value']=['STRING',{}]
        if typ not in EXCLUDED and not any(x in typ.lower() for x in ('loader','showtext','preview')):
            for field,spec in candidates.items():
                if field not in TEXT_FIELDS and not (field=='value' and 'primitive' in typ.lower()) and not re.fullmatch(r'(prompt|text)_?\d+',field):continue
                if field=='instruction' and 'TextEncodeQwen' in typ:continue # internal model template
                if typ=='LTXDirector' and field!='global_prompt':continue
                if typ=='MiniMaxH3Creator':continue
                item={'id':nid,'type':typ,'title':title,'field':field,'role':socket_role(n,field,byid,links)}
                link=bylink.get(saved.get(field,{}).get('link'))
                if link:
                    sid=resolve_source(link[1]);src=byid.get(sid,{});item['source_id']=sid;item['source_type']=src.get('type','')
                    item['source_title']=src.get('title','');r['linked_text'].append(item)
                else:
                    force=len(spec)>1 and isinstance(spec[1],dict) and spec[1].get('forceInput')
                    if not force:r['text_inputs'].append(item)
        if typ in DIRECTORS:
            r['media'].append({'id':nid,'type':typ,'title':title,'field':'节点内素材/时间线','kind':'按模式上传'})
            if typ=='MiniMaxH3Creator':r['text_inputs'].append({'id':nid,'type':typ,'title':title,'field':'镜头卡 prompt（单段）/ 全局 prompt（多段共有约束）','role':'H3 提示词'})
            if typ=='LTXDirector':r['text_inputs'].append({'id':nid,'type':typ,'title':title,'field':'时间线文本片段','role':'分段描述'})
        elif re.search(r'^(LoadImage|LoadAudio|LoadVideo|VHS_LoadVideo)',typ):
            if any(l[1]==nid for l in links):
                kind='图片' if 'image' in typ.lower() else '音频' if 'audio' in typ.lower() else '视频'
                key='image' if kind=='图片' else 'audio' if kind=='音频' else 'video'
                labels=[]
                for l in links:
                    dest=byid.get(l[3],{})
                    if l[1]==nid and dest.get('type')=='SetNode':
                        vals=dest.get('widgets_values',[])
                        if vals and isinstance(vals[0],str):labels.append(vals[0])
                r['media'].append({'id':nid,'type':typ,'title':title,'field':key,'kind':kind,'roles':labels})
        if any(x in typ.lower() for x in ('mask','sam2','pointseditor')) and typ not in ('MaskPreview','PreviewMask'):
            r['mask_nodes'].append({'id':nid,'type':typ,'title':title})
        for field in sorted(set(fields)|set(saved)):
            if field in PARAMS:
                s=saved.get(field,{});link=bylink.get(s.get('link'))
                r['controls'].append({'id':nid,'type':typ,'field':field,'source_id':link[1] if link else None})
        if schema.get('output_node') and not re.search(r'preview|show|display',typ,re.I) or re.search(r'^(SaveImage|SaveVideo|SaveAudio|VHS_VideoCombine|MiniMaxH3Creator)',typ):
            r['outputs'].append({'id':nid,'type':typ,'title':title})
    return r

def main():
    p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('--object-info',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    schemas=json.loads(a.object_info.read_text('utf-8'))
    rows=[inspect(f,a.root,schemas) for f in sorted(a.root.rglob('*.json'))]
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps({'snapshot':'2026-09-20','count':len(rows),'workflows':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Inspected {len(rows)} workflow files; output contains no saved prompts or media filenames.')

if __name__=='__main__':main()
