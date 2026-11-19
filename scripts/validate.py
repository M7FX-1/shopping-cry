#!/usr/bin/env python3
"""validate.py — family-wide integrity checks for the shopping-cry skills.

Errors (E) fail the run; warnings (W) print but do not fail.
Python 3 standard library only — no PyYAML dependency.
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
LEGEND_SENTINEL = "> **Verification tags.**"
TAG_RE = re.compile(r"\[([SPA])(?:[0-9][0-9, ]*)?(?:[ :][^\[\]]{1,120})?\]")
FORBIDDEN_PHRASES = [
    "pending build", "interim rule", "once built", "critique-G",
    "apply round", "group log", "G1/G2 precedent", "G2 precedent",
    "G1 skills", "this build", "(G6, pending",
]
MIGRATION_START = "<!-- migration:start -->"
MIGRATION_END = "<!-- migration:end -->"
CORE_CAP = 24576
SPECIALTY_WARN = 24576
SPECIALTY_FAIL = 32768
REF_WARN = 40960
HARD_DESC = 1024
WARN_DESC = 650

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def strip_migration(text):
    """Return text outside migration markers (for path/phrase scans)."""
    return re.sub(
        re.escape(MIGRATION_START) + r".*?" + re.escape(MIGRATION_END),
        "", text, flags=re.S,
    )


def migration_blocks(text):
    return re.findall(
        re.escape(MIGRATION_START) + r"(.*?)" + re.escape(MIGRATION_END),
        text, flags=re.S,
    )


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    return text[4:end] if end != -1 else None


skill_files = sorted(glob.glob(os.path.join(SKILLS, "*", "SKILL.md")))
if len(skill_files) != 17:
    err(f"expected 17 SKILL.md files under skills/, found {len(skill_files)}")

bundle_expected = os.path.join(ROOT, "shopping-cry.md")

# ---- per-file checks ----
for path in skill_files:
    name = os.path.basename(os.path.dirname(path))
    text = open(path, encoding="utf-8").read()
    fm = frontmatter(text)
    if fm is None:
        err(f"E1 {name}: no YAML frontmatter")
        continue
    m = re.search(r'^name:\s*(\S+)', fm, re.M)
    if not m or m.group(1) != name:
        err(f"E1 {name}: frontmatter name missing or != folder name")
    dm = re.search(r'^description:\s*"(.*)"\s*$', fm, re.M)
    if not dm:
        dm = re.search(r"^description:\s*(\S.*)$", fm, re.M)
        if dm and not dm.group(1).lstrip().startswith('"'):
            warn(f"W1 {name}: description is not a quoted single-line YAML string")
        if not dm:
            err(f"E1 {name}: description missing")
            continue
    desc_len = len(dm.group(1).strip().strip('"'))
    if desc_len > HARD_DESC:
        err(f"E1 {name}: description {desc_len} chars > {HARD_DESC} (discovery limit)")
    elif desc_len > WARN_DESC:
        warn(f"W1 {name}: description {desc_len} chars > {WARN_DESC} — consider trimming")
    if "calibrated:" not in fm:
        err(f"E2 {name}: metadata.calibrated missing from frontmatter")
    else:
        cm = re.search(r'calibrated:\s*"?(\d{4}-\d{2})"?', fm)
        if not cm:
            err(f"E2 {name}: calibrated not in YYYY-MM form")
        elif cm.group(1) < "2026-05":
            warn(f"W2 {name}: calibrated {cm.group(1)} is older than 12 months — re-verify figures")
    # legend presence for files using tags
    if TAG_RE.search(strip_migration(text)) and LEGEND_SENTINEL not in text:
        err(f"E3 {name}: uses [S]/[P]/[A] tags but no canonical legend")
    # size caps
    size = len(text.encode())
    if name == "product-scout" and size > CORE_CAP:
        err(f"E4 core: {size} bytes > {CORE_CAP} hard cap")
    elif name != "product-scout":
        if size > SPECIALTY_FAIL:
            err(f"E4 {name}: {size} bytes > {SPECIALTY_FAIL} hard cap")
        elif size > SPECIALTY_WARN:
            warn(f"W4 {name}: {size} bytes >= {SPECIALTY_WARN} — trim before it hits the fail line")
    # forbidden remnants (outside migration block)
    body = strip_migration(text)
    for phrase in FORBIDDEN_PHRASES:
        if phrase in body:
            err(f"E5 {name}: forbidden remnant {phrase!r}")
    # local-path hygiene (outside migration block)
    if "/home/" in body or "m7fx" in body:
        err(f"E6 {name}: local machine path outside the migration block")
    # references cross-check (both directions)
    mentioned = set(re.findall(r"references/([a-z0-9-]+\.md)", text))
    refdir = os.path.join(SKILLS, name, "references")
    on_disk = {f for f in os.listdir(refdir) if f.endswith(".md")} if os.path.isdir(refdir) else set()
    for miss in mentioned - on_disk:
        err(f"E7 {name}: references {miss} mentioned but missing on disk")
    for orphan in on_disk - mentioned:
        warn(f"W7 {name}: references {orphan} exists but is never mentioned")

# ---- migration-block content allowlist (core only carries the block) ----
core_path = os.path.join(SKILLS, "product-scout", "SKILL.md")
core_text = open(core_path, encoding="utf-8").read()
blocks = migration_blocks(core_text)
if len(blocks) != 1:
    err(f"E8 core: expected exactly 1 migration block, found {len(blocks)}")
else:
    block = blocks[0]
    if len(re.findall(re.escape(MIGRATION_START), core_text)) != 1 or \
       len(re.findall(re.escape(MIGRATION_END), core_text)) != 1:
        err("E8 core: unclosed or duplicated migration markers")
    allowed = [
        "Path migration (one-time, automatic)", "~/.product-scout/profiles/<name>.md",
        "~/.zcode/product-scout/profiles/<name>.md", "mkdir -p", "cp", "chmod 600",
        "consent.enabled", "updated:", "install.sh --check",
    ]
    lines = block.split("\n")
    for i, line in enumerate(lines):
        s = line.strip().lstrip("-").strip()
        if not s:
            continue
        if not any(a in line for a in allowed) and not re.match(r"^[a-z(]", s):
            warn(f"W8 core migration block line {i+1}: unrecognized content {line.strip()[:60]!r}")
        if re.search(r"(\d{1,3}\.){1,3}\d{1,3}", line) or "http" in line:
            err(f"E8 core migration block line {i+1}: URL/IP-like content not allowed in block")

# ---- dated [A] tags present on rail files ----
for path in skill_files:
    name = os.path.basename(os.path.dirname(path))
    text = open(path, encoding="utf-8").read()
    # exclude the legend block (blockquote after the sentinel) before scanning
    lines = text.split("\n")
    idx = next((i for i, l in enumerate(lines) if l.startswith(LEGEND_SENTINEL)), None)
    if idx is not None:
        j = idx + 1
        while j < len(lines) and lines[j].startswith("> "):
            j += 1
        body = "\n".join(lines[:idx] + lines[j:])
    else:
        body = text
    bare_a = re.findall(r"\[A\](?![ \d])", body)
    if bare_a:
        err(f"E9 {name}: bare [A] tag without YYYY-MM date")

# ---- dispatch-phrase residue on non-channel lines (semantic, paragraph-joined) ----
for path in skill_files:
    name = os.path.basename(os.path.dirname(path))
    text = open(path, encoding="utf-8").read()
    for para in re.split(r"\n\s*\n", text):
        if "re-verify at dispatch" in para or "re-check at dispatch" in para or "re-anchor at dispatch" in para:
            if re.search(r"\$|€|£|price band|street anchor|walk-away|ceiling", para, re.I) and \
               not re.search(r"channel|store|sites|chains|dealers|marketplaces|tariff|regulator|utility|exchange", para, re.I):
                warn(f"W9 {name}: possible dispatch promise on a figure line: {para.strip()[:80]!r}")

# ---- reference sizes ----
for p in glob.glob(os.path.join(SKILLS, "*", "references", "*.md")):
    size = len(open(p, "rb").read())
    if size > REF_WARN:
        warn(f"W10 references/{os.path.basename(p)}: {size} bytes — keep it data, not rules")

# ---- core description registry count ----
core_fm = frontmatter(core_text)
dm = re.search(r'^description:\s*"(.*)"\s*$', core_fm, re.M)
if dm and re.search(r"(\d+) specialty skills", dm.group(1)):
    claimed = int(re.search(r"(\d+) specialty skills", dm.group(1)).group(1))
    actual = len(skill_files) - 1
    if claimed != actual:
        err(f"E11 core description claims {claimed} specialty skills; repo has {actual}")

# ---- bundle equality ----
if not os.path.exists(bundle_expected):
    err("E12 shopping-cry.md missing — run scripts/build-bundle.sh")
else:
    committed = open(bundle_expected, encoding="utf-8").read()
    r = subprocess.run(["bash", "-c",
        f"cd '{ROOT}' && ORDER=$(grep -o 'product-scout-[a-z0-9-]*/SKILL\\.md' "
        f"skills/product-scout/SKILL.md | cut -d/ -f1 | awk '!seen[$0]++'); "
        f"N=$(ls -d skills/product-scout*/ | wc -l); "
        "{ echo 'For human reading only. Agents: never load this file — read "
        "skills/product-scout/SKILL.md and dispatch per its registry.'; echo; echo "
        "'# shopping-cry — the product-scout skill family'; echo; echo "
        "\"Generated: $(date +%F). This file bundles all ${N} SKILL.md files of the family "
        "verbatim, in registry order. Reference files (domain knowledge bases) are NOT "
        "included — they live next to each skill in its own folder.\"; echo; echo; echo; "
        "i=0; for name in product-scout $ORDER; do i=$((i+1)); if [ \"$i\" -gt 1 ]; then "
        "echo; echo; fi; printf -- '---\\n\\n# ═══════════ Skill %s of %s ═══════════\\n\\n' "
        "\"$i\" \"$N\"; cat \"skills/$name/SKILL.md\"; done; }"], capture_output=True, text=True)
    if r.returncode != 0:
        err(f"E12 bundle rebuild failed: {r.stderr[:200]}")
    else:
        def norm(t):
            return re.sub(r"^Generated: \d{4}-\d{2}-\d{2}\.", "Generated: DATE.", t, flags=re.M)
        if norm(committed) != norm(r.stdout):
            err("E12 shopping-cry.md is stale — run scripts/build-bundle.sh")

# ---- report ----
for w in warnings:
    print(f"WARN  {w}")
for e in errors:
    print(f"ERROR {e}")
print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
