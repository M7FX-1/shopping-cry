#!/usr/bin/env bash
# shopping-cry installer — installs the core engine + 16 specialty skills
# (17 folders under ./skills/) into an agent's skills root.
#
# Usage:
#   ./install.sh --zcode          # ZCode harness root (~/.zcode/skills)
#   ./install.sh --claude         # Claude Code root (~/.claude/skills)
#   ./install.sh --agents         # generic root (~/.agents/skills)
#   ./install.sh --dir <path>     # any custom skills root
#   ./install.sh --list           # show the installable skills
#   ./install.sh --check          # compare installed copies with this repo
#   ./install.sh --uninstall [--yes]  # remove (dry-run unless --yes)
#   ./install.sh --only a,b       # install a subset (core always included)
#   FORCE=1 ./install.sh ...      # overwrite already-installed skills
#
# No dependencies beyond bash + coreutils. Safe by default: an existing
# skill folder with the same name is skipped unless FORCE=1 (and is only
# overwritten when it actually contains a SKILL.md). Uninstalling never
# touches your personal profiles in ~/.product-scout/profiles/.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$SCRIPT_DIR/skills"
TARGET=""
ONLY=""

usage() {
  echo "usage: $0 [--zcode|--claude|--agents|--dir <path>|--list|--check|--uninstall [--yes]|--only <names>]" >&2
  echo "       FORCE=1 to overwrite already-installed skills" >&2
  exit 1
}

while [ $# -gt 0 ]; do
  case "$1" in
    --zcode) TARGET="${HOME}/.zcode/skills" ;;
    --claude) TARGET="${HOME}/.claude/skills" ;;
    --agents) TARGET="${HOME}/.agents/skills" ;;
    --dir) shift; TARGET="${1:?--dir requires a path}" ;;
    --list) LIST=1 ;;
    --check) CHECK=1 ;;
    --uninstall) UNINSTALL=1 ;;
    --yes) YES=1 ;;
    --only) shift; ONLY="${1:?--only requires a comma-separated list}" ;;
    *) usage ;;
  esac
  shift
done

# ---- --list ----
if [ "${LIST:-0}" = "1" ]; then
  echo "shopping-cry — installable skills:"
  echo
  echo "  core"
  for f in "$SRC"/product-scout/SKILL.md; do
    d=$(awk 'c==1 && /^---$/{exit} c==1 && /^description:/{sub(/^description:[[:space:]]*/,""); gsub(/^"|"$/,""); print; exit} /^---$/{c++}' "$f")
    printf '    %-32s %.90s\n' "$(basename "$(dirname "$f")")" "$d"
  done
  echo "  specialties"
  for f in "$SRC"/product-scout-*/SKILL.md; do
    d=$(awk 'c==1 && /^---$/{exit} c==1 && /^description:/{sub(/^description:[[:space:]]*/,""); gsub(/^"|"$/,""); print; exit} /^---$/{c++}' "$f")
    printf '    %-32s %.90s\n' "$(basename "$(dirname "$f")")" "$d"
  done
  echo
  echo "Usage: $0 --zcode|--claude|--agents|--dir <path>   (FORCE=1 overwrites)"
  echo "       $0 --check | $0 --uninstall [--yes] | $0 --only <names>"
  exit 0
fi

# ---- resolve TARGET for install/check/uninstall ----
if [ -z "$TARGET" ] && { [ "${CHECK:-0}" = "1" ] || [ "${UNINSTALL:-0}" = "1" ]; }; then
  TARGET="${HOME}/.zcode/skills"   # default root for --check / --uninstall
fi
if [ -z "$TARGET" ]; then
  usage
fi

# ---- --check ----
if [ "${CHECK:-0}" = "1" ]; then
  total=0; same=0
  for d in "$SRC"/product-scout*/; do
    name="$(basename "$d")"; total=$((total + 1))
    inst="$TARGET/$name"
    if [ ! -e "$inst" ]; then
      echo "  missing in install: $name"
    elif diff -rq "$d" "$inst" >/dev/null 2>&1; then
      same=$((same + 1))
    else
      echo "  differs from repo: $name"
    fi
  done
  echo
  if [ "$same" -eq "$total" ]; then
    echo "All $total skills in $TARGET match this repository."
  else
    echo "To update everything to this repo's versions: FORCE=1 $0 --dir \"$TARGET\""
  fi
  # legacy profile migration status
  legacy=0
  for n in beauty clothing health; do
    [ -f "${HOME}/.zcode/product-scout/profiles/$n.md" ] && legacy=$((legacy + 1))
  done
  [ "$legacy" -gt 0 ] && echo "Note: $legacy legacy profile file(s) at ~/.zcode/product-scout/profiles/ will migrate automatically on first use."
  exit 0
fi

# ---- --uninstall (dry-run by default) ----
if [ "${UNINSTALL:-0}" = "1" ]; then
  case "$TARGET" in
    ""|"/"|"$HOME") echo "refusing to uninstall: target '$TARGET' is unsafe" >&2; exit 1 ;;
    "${HOME}/.product-scout"*) echo "refusing: $TARGET holds personal profiles, not skills" >&2; exit 1 ;;
  esac
  shopt -s nullglob
  matches=("$TARGET"/product-scout*/)
  shopt -u nullglob
  real=()
  for d in "${matches[@]}"; do
    [ -f "$d/SKILL.md" ] && real+=("$d")
  done
  if [ "${#real[@]}" -eq 0 ]; then
    echo "nothing to uninstall in $TARGET"
    exit 0
  fi
  echo "would remove ${#real[@]} skill folders from $TARGET:"
  for d in "${real[@]}"; do echo "  $(basename "$d")"; done
  echo "Your personal profiles in ~/.product-scout/profiles/ are never touched."
  if [ "${YES:-0}" != "1" ]; then
    echo
    echo "DRY RUN — nothing has been removed. Run again with --yes to apply."
    exit 0
  fi
  for d in "${real[@]}"; do
    rm -rf "$d"
    echo "removed: $(basename "$d")"
  done
  echo "Done — removed ${#real[@]} skill folders from $TARGET."
  echo "Restart your agent session so it re-scans its skills roots."
  exit 0
fi

# ---- install ----
if [ ! -d "$SRC" ]; then
  echo "error: skills/ directory not found next to this script" >&2
  exit 1
fi

WANTED=()
if [ -n "$ONLY" ]; then
  IFS=',' read -ra WANTED <<< "$ONLY"
  for w in "${WANTED[@]}"; do
    w="$(echo "$w" | tr -d '[:space:]')"
    if [ "$w" = "core" ]; then continue; fi
    if [ ! -d "$SRC/product-scout-$w" ]; then
      echo "error: unknown skill 'product-scout-$w' (see --list)" >&2
      exit 1
    fi
  done
fi

mkdir -p "$TARGET"

installed=0
skipped=0
for d in "$SRC"/product-scout*/; do
  name="$(basename "$d")"
  short="${name#product-scout}"
  short="${short#-}"
  if [ -n "$ONLY" ] && [ "$name" != "product-scout" ]; then
    keep=0
    for w in "${WANTED[@]}"; do
      [ "$w" = "$short" ] && keep=1
    done
    [ "$keep" = "0" ] && continue
  fi
  if [ -e "$TARGET/$name" ]; then
    if [ "${FORCE:-0}" = "1" ]; then
      if [ ! -f "$TARGET/$name/SKILL.md" ]; then
        echo "refusing to overwrite $TARGET/$name (no SKILL.md inside — not an installed skill copy)" >&2
        skipped=$((skipped + 1)); continue
      fi
      rm -rf "$TARGET/$name"
    else
      echo "skip (already installed — rerun with FORCE=1 to overwrite): $name"
      skipped=$((skipped + 1))
      continue
    fi
  fi
  cp -r "$d" "$TARGET/$name"
  echo "installed: $name"
  installed=$((installed + 1))
done

echo
echo "done — installed: $installed, skipped: $skipped"
echo "skills root: $TARGET"
echo "restart your agent session so it re-scans its skills roots."
