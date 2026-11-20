#!/usr/bin/env python3
"""Structural validation of the solofounder plugin. Usage: python3 tests/validate_structure.py [--json out.json]"""
import json, re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
ROOT = REPO / "solofounder-os"
REQUIRED_SECTIONS = ["## Workflow", "## Deliverables", "## Founder approval gates", "## Guardrails"]
AREAS = {"core", "legal", "finance", "marketing", "sales", "product", "eng", "ops", "support"}

checks, failures = 0, []

def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        failures.append(msg)

manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
check(re.fullmatch(r"[a-z0-9-]+", manifest.get("name", "")) is not None, "plugin name not kebab-case")
check(re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")) is not None, "version not semver")
market = json.loads((REPO / ".claude-plugin/marketplace.json").read_text())
check(any(p["name"] == manifest["name"] for p in market["plugins"]), "plugin missing from marketplace.json")

connectors = (ROOT / "CONNECTORS.md").read_text()
documented = set(re.findall(r"`~~([A-Za-z -]+)`", connectors))

skills, words, by_area = {}, {}, {}
for d in sorted((ROOT / "skills").iterdir()):
    f = d / "SKILL.md"
    check(f.exists(), f"{d.name}: SKILL.md missing")
    if not f.exists():
        continue
    text = f.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    check(m is not None, f"{d.name}: frontmatter missing")
    if not m:
        continue
    fm, body = m.group(1), m.group(2)
    name = re.search(r"^name: (.+)$", fm, re.M)
    desc = re.search(r'^description: "(.*)"$', fm, re.M)
    area = re.search(r"^  area: (.+)$", fm, re.M)
    check(name and name.group(1) == d.name, f"{d.name}: name does not match directory")
    check(desc is not None, f"{d.name}: description missing")
    if desc:
        dl = len(desc.group(1))
        check(80 <= dl <= 1024, f"{d.name}: description length {dl}")
        check(desc.group(1).startswith("This skill should be used when"), f"{d.name}: description not third-person trigger form")
        check(desc.group(1).count('\\"') >= 6, f"{d.name}: fewer than 3 quoted trigger phrases")
    check(area and area.group(1) in AREAS, f"{d.name}: bad area")
    for s in REQUIRED_SECTIONS:
        check(s in body, f"{d.name}: missing section {s}")
    if area and area.group(1) in ("legal", "finance"):
        check("## Jurisdiction protocol" in body, f"{d.name}: missing jurisdiction protocol")
    if d.name not in ("start",):
        check("company-profile.md" in body, f"{d.name}: does not read company profile")
    wc = len(body.split())
    check(wc <= 3000, f"{d.name}: body {wc} words")
    check(wc >= 150, f"{d.name}: body too thin ({wc} words)")
    for ref in re.findall(r"`(references/[^`]+)`", body):
        check((d / ref).exists(), f"{d.name}: missing {ref}")
    for ph in re.findall(r"~~([A-Za-z-]+(?: [a-z]+){0,2})", body):
        parts = ph.split()
        ok = any(" ".join(parts[:n]) in documented for n in range(len(parts), 0, -1))
        check(ok, f"{d.name}: undocumented connector ~~{ph}")
    skills[d.name] = body
    words[d.name] = wc
    if area:
        by_area.setdefault(area.group(1), []).append(d.name)

# hand-off graph: every backticked skill-like reference must resolve
edges, incoming = 0, {s: 0 for s in skills}
prefixes = ("legal-", "finance-", "marketing-", "sales-", "product-", "eng-", "ops-", "support-")
for s, body in skills.items():
    for ref in set(re.findall(r"`([a-z][a-z0-9-]+)`", body)):
        if ref.startswith(prefixes) or ref in ("start", "launch-sprint", "founder-weekly-review", "stack-and-automation-setup"):
            check(ref in skills, f"{s}: hand-off to unknown skill {ref}")
            if ref in skills and ref != s:
                edges += 1
                incoming[ref] += 1
orphans = [s for s, n in incoming.items() if n == 0 and s != "start"]
check(not orphans, f"skills never referenced by another skill: {orphans}")

plan = (ROOT / "skills/launch-sprint/references/14-day-plan.md").read_text()
in_plan = {s for s in skills if f"`{s}`" in plan}
check(in_plan == set(skills), f"skills not scheduled in the sprint plan: {sorted(set(skills) - in_plan)}")

result = {
    "skills": len(skills),
    "skills_by_area": {a: len(v) for a, v in sorted(by_area.items())},
    "checks_run": checks,
    "checks_failed": len(failures),
    "pass_rate": round(100 * (checks - len(failures)) / checks, 1),
    "handoff_edges": edges,
    "orphan_skills": len(orphans),
    "sprint_plan_coverage_pct": round(100 * len(in_plan) / len(skills), 1),
    "median_body_words": sorted(words.values())[len(words) // 2],
    "max_body_words": max(words.values()),
    "failures": failures,
}
print(json.dumps(result, indent=2))
if "--json" in sys.argv:
    pathlib.Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(result, indent=2))
sys.exit(1 if failures else 0)
