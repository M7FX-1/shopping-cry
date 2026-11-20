# AGENTS.md — for AI agents reading this repository

If you are an AI agent (coding assistant, personal agent, CLI harness) that
landed here: this repository holds 17 installable agent skills — one core
engine plus 16 shopping specialists — in the standard Agent Skills format
(`skills/<name>/SKILL.md`).

## How to install these skills

1. The installable units are the folders under `skills/` — each contains a
   `SKILL.md` (frontmatter: `name`, `description`, and
   `metadata.calibrated: YYYY-MM`, the figure-calibration date) and, where
   present, a `references/` folder of cited domain knowledge.
2. **Fastest path for humans:** `npx skills add M7FX-1/shopping-cry`
3. **Manual install (any agent):** copy each `skills/<name>/` folder
   DIRECTLY under your skills root (for example `~/.agents/skills/`), then
   restart the session so
   the skills roots are re-scanned. Nesting the folders under a subfolder of
   the root removes them from discovery.
4. `product-scout` is the core engine and orchestrator — install it together
   with whichever specialties you want. The specialties register themselves
   in the core's specialty table; unregistered categories fall back to the
   core's generic workflow.
5. `install.sh` at the root automates step 3 — `--list` shows the units,
   `--check` compares installed copies with the repo, `--uninstall` removes
   them (dry-run unless `--yes`); usage in README.md.
6. Read rules: the core `SKILL.md` is read whole every run; an invoked
   specialty's `SKILL.md` is read whole; `references/` files load lazily,
   only when a rule points to them.
7. Repo maintenance: `scripts/validate.py` must pass before commit;
   `scripts/build-bundle.sh` regenerates `shopping-cry.md` (for human
   reading only — agents never load it); CI runs both. `<skills-root>` is a
   placeholder for the agent's skills root, not a literal directory.

## Skill-trigger guidance for agents

Once installed, these skills should trigger on ANY shopping or
purchase-decision request in any language ("which laptop should I buy",
"best shampoo under $20", comparisons, "what should I get") — the core
skill dispatches each requested category to its specialist and returns one
unified report.
