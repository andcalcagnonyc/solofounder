#!/usr/bin/env python3
"""Lexical routing baseline: TF-IDF cosine between each synthetic request and each skill's
name + description. No language model involved. Measures how well descriptions separate
skills on words alone; a model routing on meaning is expected to do better."""
import json, math, re, sys, pathlib
from collections import Counter

REPO = pathlib.Path(__file__).resolve().parent.parent
ROOT = REPO / "solofounder-os"
STOP = set("a an the and or to of for my i me is in on with this that be should used when user asks needs it do what how are from at by as we our you your".split())

def toks(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1]

docs = {}
for d in sorted((ROOT / "skills").iterdir()):
    fm = (d / "SKILL.md").read_text().split("---")[1]
    desc = re.search(r'^description: "(.*)"$', fm, re.M).group(1)
    docs[d.name] = toks(d.name.replace("-", " ") + " " + desc)

df = Counter(w for t in docs.values() for w in set(t))
N = len(docs)
idf = lambda w: math.log((N + 1) / (df.get(w, 0) + 1)) + 1

def vec(t):
    c = Counter(t)
    v = {w: n * idf(w) for w, n in c.items()}
    norm = math.sqrt(sum(x * x for x in v.values())) or 1
    return {w: x / norm for w, x in v.items()}

dv = {k: vec(t) for k, t in docs.items()}
cases = [l.split("\t", 1) for l in (REPO / "tests/routing_cases.tsv").read_text().splitlines() if l.strip()]
top1 = top3 = area = 0
misses = []
for exp, prompt in cases:
    q = vec(toks(prompt))
    rank = sorted(dv, key=lambda k: -sum(q.get(w, 0) * x for w, x in dv[k].items()))
    top1 += rank[0] == exp
    top3 += exp in rank[:3]
    area += rank[0].split("-")[0] == exp.split("-")[0]
    if rank[0] != exp:
        misses.append({"expected": exp, "got": rank[0], "prompt": prompt})
n = len(cases)
res = {"cases": n, "top1_pct": round(100 * top1 / n, 1), "top3_pct": round(100 * top3 / n, 1),
       "same_area_top1_pct": round(100 * area / n, 1), "misses": misses}
print(json.dumps({k: v for k, v in res.items() if k != "misses"}, indent=2))
if "--json" in sys.argv:
    pathlib.Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(res, indent=2))
