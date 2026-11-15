#!/usr/bin/env bash
# build-bundle.sh — regenerate shopping-cry.md from the 17 SKILL.md files.
# Skill order is read from the core's specialty registry (never hardcoded).
# Run after editing any SKILL.md. shopping-cry.md is generated output:
# never edit it by hand.
set -euo pipefail
cd "$(dirname "$0")/.."

ORDER=$(grep -o 'product-scout-[a-z0-9-]*/SKILL\.md' skills/product-scout/SKILL.md | cut -d/ -f1 | awk '!seen[$0]++')
N_SKILLS=$(ls -d skills/product-scout*/ | wc -l)

{
  echo "For human reading only. Agents: never load this file — read skills/product-scout/SKILL.md and dispatch per its registry."
  echo
  echo "# shopping-cry — the product-scout skill family"
  echo
  echo "Generated: $(date +%F). This file bundles all ${N_SKILLS} SKILL.md files of the family verbatim, in registry order. Reference files (domain knowledge bases) are NOT included — they live next to each skill in its own folder."
  echo; echo; echo
  i=0
  for name in product-scout $ORDER; do
    i=$((i+1))
    if [ "$i" -gt 1 ]; then echo; echo; fi
    printf -- '---\n\n# ═══════════ Skill %s of %s ═══════════\n\n' "$i" "$N_SKILLS"
    cat "skills/$name/SKILL.md"
  done
} > shopping-cry.md

echo "bundle rebuilt: shopping-cry.md ($i skills)"
