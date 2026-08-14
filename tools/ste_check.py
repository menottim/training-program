import json, re, sys

FIELDS = ('notes','desc','longDesc','reason','details','subtitle','title','label','findings','changes')

def walk(o, path, out):
    if isinstance(o, dict):
        for k, v in o.items():
            p = f'{path}.{k}'
            if isinstance(v, str) and k in FIELDS:
                out.append((p, k, v))
            else:
                walk(v, p, out)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, f'{path}[{i}]', out)

def violations(k, v):
    bad = []
    body = v.replace('\n\n', ' \x00 ')
    sents = [s for s in re.split(r'(?<=[.!?])\s+', body) if s.strip() and s.strip() != '\x00']
    limit = 20 if k in ('notes',) else 25
    for s in sents:
        s = s.replace('\x00', '').strip()
        n = len(s.split())
        if n > limit:
            bad.append(f'len{n}: {s[:90]}')
    for c in re.findall(r"(?:\b[A-Z][A-Z'-]{2,}\b[ ,]+){2,}\b[A-Z][A-Z'-]{2,}\b", v):
        toks = [t for t in re.split(r'[ ,]+', c) if t]
        if any(len(t) > 4 and t.isalpha() for t in toks):
            bad.append(f'caps: {c.strip()[:60]}')
    paras = v.split('\n\n') if k != 'notes' else []
    for i, p in enumerate(paras):
        ns = len([s for s in re.split(r'(?<=[.!?])\s+', p) if s.strip()])
        if ns > 6:
            bad.append(f'para{i} has {ns} sentences')
    if k == 'desc' and len(v.split()) > 9:
        bad.append(f'desc too long ({len(v.split())} words)')
    CAP = {'longDesc': 150, 'reason': 200, 'notes': 60, 'findings': 250, 'changes': 200}
    n = len(v.split())
    if k in CAP and n > CAP[k]:
        bad.append(f'{k} bloat: {n} words (cap {CAP[k]})')
    SCAFFOLD = [
        'ORIGINAL PLAN FOLLOWS', 'ORIGINAL RATIONALE FOLLOWS', 'ORIGINAL PRESCRIPTION FOLLOWS',
        'The original plan follows', 'The original rationale follows', 'The original prescription follows',
        'The plan below was written', 'This session is complete',
        'The first was the', 'The second was the',
        'Two items went wrong', 'Two findings support', 'One problem does need',
        'for one reason', 'It also turns', 'worth naming',
    ]
    for phrase in SCAFFOLD:
        if phrase in v:
            bad.append(f'scaffolding: {phrase}')
    return bad

d = json.load(open(sys.argv[1] if len(sys.argv) > 1 else 'data.json'))
scope = sys.argv[2] if len(sys.argv) > 2 else ''
out = []
walk(d, '', out)
tot = 0
files = {}
for path, k, v in out:
    if scope and not path.startswith(scope):
        continue
    bad = violations(k, v)
    if bad:
        tot += len(bad)
        files.setdefault(path.split('[')[0] if 'schedule' not in path else path, []).extend(bad)
print(f'fields scanned: {len([1 for p,k,v in out if not scope or p.startswith(scope)])}  violations: {tot}')
for p, b in sorted(files.items(), key=lambda x: -len(x[1]))[:int(sys.argv[3]) if len(sys.argv) > 3 else 12]:
    print(f'\n{p}  ({len(b)})')
    for x in b[:4]:
        print('   ', x)
