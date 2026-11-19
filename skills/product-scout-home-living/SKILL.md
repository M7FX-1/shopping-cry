---
name: product-scout-home-living
description: "Home and living specialist of the product-scout family — furniture, mattresses, kitchenware, linens, decor, lighting, religious household items. Material safety (coatings, emissions), anti-tip anchoring for every household, dimension-planning method, durability grades, try-before-buy guidance, delivery and assembly checklist. Dispatched by the core for any home-goods request, or standalone. Read the core engine first."
metadata:
  calibrated: "2026-11"

---

# Product Scout — Home & Living

> **Verification tags.** Every load-bearing claim carries one tag:
> `[S]` = sourced — verified against a regulator, standards body, official/primary source, or a family-verified precedent this cycle; inline `[S: URL]` carries the source.
> `[P]` = practitioner/market consensus or street anchor — labeled as such, dated, never presented as sourced fact.
> `[A]` = anchored rail — a calibrated threshold set at install and re-anchored on a ~6-month cadence (see the freshness rules).
> Suffixes in any order: a source number (`[S13]`), a `YYYY-MM` date (mandatory on `[A]`, see the freshness rules), and lowercase modifiers — `unverified` (secondary coverage only; re-verify or drop before stating as fact), `industry` (vendor/marketing source), `convention` (usage convention, not evidence). A `[S, unverified]` claim is never the sole basis for a dosage or contraindication statement.

First read the core engine at
`<skills-root>/product-scout/SKILL.md` — it owns the intake
protocol (market / budget / mode), the three research modes, the verdict
structure, and the honesty rules. This file adds the home-living domain
layer. The numeric tables behind the rules below — furniture dimension
standards, foam-density and Martindale bands, resin codes, LED lumen
mappings — live in `references/home-living-domain.md` (same directory).

Read the core file in full every run, and this file in full when invoked — partial reads break the safety gates and honesty rules; `references/` files load lazily, on demand, and nothing operative is ever satisfied from a reference alone.

Reply to the user in their language.

## Scope

- **In**: indoor furniture (incl. mattresses; children's general
  furniture), kitchen & dining (cookware incl. pressure cookers,
  dinnerware, food storage),
  linens & bedding, bathroom textiles, decor & lighting (bulbs,
  fixtures, lamps), storage & organization, religious household items
  (prayer rugs, Quran printings, home devotionals).
- **Out**: appliances → appliances skill; nursery safety-critical items
  (cribs, car seats, feeding equipment) → baby-kids skill; outdoor/patio
  furniture, assembly tools, and paint →
  diy-garden; TVs and smart-home devices → electronics
  skill; household cleaning consumables → groceries; a Mushaf chosen
  as a reading edition (translation, commentary) is a books-media
  question — this skill owns the object purchase (print
  quality, paper, binding, format).
- **Stance**: measure first, materials second, style never imposed —
  this skill verifies construction, safety, and value for whatever the
  user describes, and never lectures taste (clothing's taste-neutrality
  rule, without clothing's taste-learning loop).

## No profile, by design

Fit here is measured per room, not per body: purchase frequency is low
(a sofa every decade), the decisive numbers are per-request room
dimensions, and nothing sensitive needs remembering. No persistent
profile. The intake folds in, only when missing: room/doorway
dimensions if the user has them, children in the home (hardens the
anchoring rails, never gates them — behavior 8), and budget tier.
Session memory reuses earlier answers in the conversation.

## Domain behaviors

### 1. Materials and joinery over finish

Furniture quality is materials truth, and a listing's silence is a
signal (clothing behavior 1's logic, applied to wood):

- **Know what you're buying**: solid wood (durable, can warp with
  humidity), plywood (strong per weight, layered), MDF (uniform and
  cheap, heavy, sags under load, swells with water). "Solid wood" on
  cheap furniture often means solid-wood frame + MDF panels or veneer
  over MDF — ask which parts are solid; the answer is worth a verdict
  line.
- **Emissions standards**: pressed woods carry urea-formaldehyde
  resins. The verifiable marks are **E1 (≤0.1 ppm, European)** and
  **CARB Phase 2 / US TSCA Title VI** compliance (the strictest
  widely-published limits); "E0" appears as a stricter claim but is a
  marketing grade unless certified. Where no standard is declared on
  premium-priced pressed-wood furniture, say the emissions claim is
  unverifiable. Air new pressed-wood furniture before heavy use; for
  children's rooms prefer certified board or solid wood.
- **Joinery and hardware**: mortise-and-tenon/dovetail joints and metal
  runners beat staples, glue, and plastic slides; soft-close hinges and
  runners are the first things to fail — test in-hand or in zoomed
  photos. Weight-capacity claims without a test standard are marketing.
- **Glass furniture**: tabletops and cabinet doors must be tempered
  safety glass (the word "tempered" or a marked standard — treat
  unmarked heavy glass as a fail); inspect edges for chips (chipped
  tempered glass can fail suddenly); never place hot pans directly on
  a glass top.

### 2. Upholstery durability is numeric

- **Martindale rub counts** for upholstery fabric: <10,000 decorative
  only; 10,000–15,000 light domestic; **15,000–25,000 everyday family
  sofas**; 25,000–30,000 heavy residential; 30,000+ contract grade
  (bands verified 2026-11). Wyzenbeek double-rubs are a different test
  — never convert or compare across the two. A premium-priced sofa
  that publishes no rub count is unverifiable-marketing.
- **Frames**: kiln-dried hardwood best, pine acceptable at budget,
  particleboard frames sag — ask, and weigh the answer in the Quality
  cell.
- **Seat foam**: high-resilience foam ≥30 kg/m³ survives daily sitting;
  low-density foam (<25 kg/m³) flattens within a couple of years
  (practitioner bands). Cushion rebound after a sit-test is the
  visible proxy.
- **Try before buying where possible** (behavior 3's protocol): sit
  10–15 minutes, check frame creak, cushion recovery, seam stress.

### 3. Mattresses — density, springs, try-before-buy

- **Foam density predicts lifespan**: budget foam <25 kg/m³ flattens
  early; 30–40 kg/m³ is decent daily use; 45–50+ kg/m³ memory/HR is
  the premium band (practitioner — densities are rarely published;
  ask, and treat silence as a downgrade signal).
- **Springs**: Bonnell/continuous = budget, transfers partner motion;
  pocket springs = isolate motion and conform; wire gauge (lower
  number = thicker = firmer) matters more than spring count
  (practitioner).
- **Match firmness to sleeper**: sleep position + body weight decide
  (heavier sleepers need firmer/higher-density support); there is no
  universal "best mattress" — say so instead of ranking one.
- **Try-before-buy IS the method**: lie 10–15 minutes in your usual
  sleep position, with your own pillow if possible. Check whether the
  user's market offers sleep-trial return windows or exchange-only
  policies — where returns are exchange-only, the showroom test is the
  primary risk control, not an optional extra. Say this explicitly when
  recommending a mattress.
- **Labels and airing**: flammability labels (e.g., US 16 CFR
  1632/1633, UK BS 7177) are mandatory in their respective markets and
  a quality signal elsewhere; air a new mattress 24–72h for
  off-gassing; CertiPUR-US / CertiPUR-EU foam certification is a bonus.
  Read sag-warranty terms ("10-year warranty" covering only dips
  ≥3–4 cm is the common fine print) — replace ~7–10 years or at visible
  sag regardless of warranty.

### 4. Cookware coatings — the safety lines

- **PTFE non-stick**: inert at normal cooking; begins to degrade above
  ~260°C (500°F) releasing fumes — polymer fume fever in humans,
  lethal to pet birds. The operative rails: never preheat an empty
  non-stick pan on high (empty pans exceed the line in minutes),
  ventilate when searing, replace pans that flake or scratch badly.
  These lines ship with every non-stick recommendation.
- **"PFOA-free" is table stakes, not a feature**: PFOA was globally
  eliminated under the Stockholm Convention in 2019 — new-stock
  cookware claiming it as an advantage is dressing up compliance as a
  benefit. "PFOA-free" does not mean PFAS-free; PTFE pans are still
  PTFE.
- **"Granite/diamond/stone" coatings** are PTFE with mineral particles
  — a marketing name, judged as PTFE (practitioner consensus); judge
  coating thickness and brand serviceability instead.
- **Ceramic (sol-gel)** coatings: PFAS-free, but shorter real-world
  coating life — budget replacement cycles, don't sell "forever".
- **The buy-once options**: stainless 18/10 (304) — neutral, durable,
  induction-capable with a magnetic base (magnet test); cast iron —
  generational, needs seasoning; anodized aluminum beats bare aluminum
  (which reacts with acid). Induction buyers: verify the base, not the
  "induction-ready" word.
- **Pressure cookers (stove-top and electric multi-cookers)**: never
  fill above ⅔ — ½ for legumes, rice, and anything that foams; never
  force-open a lid under pressure (wait for full depressurization);
  inspect the gasket, vent, and secondary safety valve before every
  use and replace hardened gaskets on schedule; never leave a
  stove-top cooker unattended on high heat. These lines ship with
  every pressure-cooker or multi-cooker recommendation.

### 5. Food-contact plastics

- **Resin codes are the guide**: PP (#5) is the microwave-safe default;
  HDPE (#2)/LDPE (#4) fine for storage; PET (#1) single-use only; PS
  (#6) foam — never heated; PC (#7) legacy BPA carrier — avoid for
  food. Full table in the reference file.
- **Heat is the accelerant**: microwave only what is labeled
  microwave-safe; never reheat takeaway containers or fatty/hot food
  in unlabeled plastic — migration scales with heat, fat, and time
  (practitioner). Glass/ceramic for reheating is the cheap upgrade.
- Scratched, cloudy, or stained containers: replace — surface breakdown
  is the signal. "BPA-free" on products that were never BPA-carriers
  is marketing noise; the resin code outranks the word.

### 6. Linens, towels and bathroom textiles

- **Thread count is a myth beyond ~400**: 200–400 TC is the sweet spot;
  higher numbers are achieved by multi-ply yarn inflation — a thinner,
  worse fabric with a bigger number (practitioner consensus). Fiber
  quality and weave beat the number: percale (crisp, breathable —
  hot-climate default) vs sateen (silky, warmer).
- **Egyptian cotton**: only the gold Egyptian Cotton™ seal (CEA /
  Bureau Veritas verified) is trustworthy — the clothing domain doc
  owns the full authenticity analysis; cross-reference it, never
  re-research. "1000 TC 100% Egyptian cotton" at a low price is the
  documented red flag.
- **Towels: GSM is the real number** — 400–500 gsm everyday, 500–600
  gsm plush; combed or zero-twist cotton holds loop structure; in
  humid bathrooms prefer mid-GSM for faster drying (mold avoidance,
  below).
- **Bath mats**: anti-slip backing is a fall-prevention rail, not a
  comfort feature — pass/fail in recommendations.
- **Bathroom moisture & mold**: prefer quick-dry materials and washable
  fabric curtains over sealed plastic; hang towels spread out; mildew
  smell on arrival is a return-window item. Cross-reference the
  appliances skill for exhaust fans — ventilation is the root fix.
- Kids' nursery bedding and sleepwear are the baby-kids skill's
  territory; general children's bedding follows this behavior.

### 7. Lighting — lumens, temperature, color

- **Buy lumens, not watts**: the mappings (60W ≈ 800 lm, 75W ≈ 1,100
  lm, 100W ≈ 1,600 lm) are the usable shorthand. Efficacy: ≥80 lm/W
  decent, ≥100 lm/W good LED (practitioner bands); check the lumen
  figure on the box, not the "equivalent" claim.
- **Color temperature by room**: 2700K warm for living rooms and
  bedrooms; 4000K neutral for kitchens, bathrooms, work surfaces;
  5000–6500K daylight for task/reading corners. Keep a room's bulbs
  one temperature — mixed temperatures read as broken lighting.
- **CRI**: ≥80 fine for general rooms; ≥90 where color matters
  (dressing areas, art). LED lifespan: compare stated hours
  (15,000–25,000 is the normal band) and dimmer compatibility; cheap
  drivers flicker — a visible flicker on video is a disqualifier
  (deep PWM analysis belongs to the electronics skill).

### 8. Tip-over anchoring and children's furniture — pass/fail rails

- **Anchor every tall unit, in every household**: dressers, wardrobes,
  bookcases, and shelving tip when climbed or when drawers are pulled
  loaded — anchor them to the wall regardless of brand claims and
  regardless of whether children live here (ASTM F2057-23 under the
  STURDY Act, 2023 — stable with drawers open and loaded, anchor kit
  and warnings included; it carries no household-composition
  condition). "If it can tip, anchor it" is the rail. Children in the
  home harden the rail further (climbable drawers, blind cords, low
  units under TVs) — never gate it.
- **TV anchoring**: the electronics skill owns the TV-specific rail —
  this skill owns the furniture side: sturdy low units, straps, no
  climbable drawers beneath a TV.
- **Bunk beds**: guardrails on both sides with proper gaps, age ≥6 for
  the top bunk (practitioner; EN 747 / ASTM F1427 are the reference
  standards where present); the top-bunk mattress must stay below the
  guardrail top — ask the manufacturer's maximum mattress height and
  treat silence as a downgrade; check ladder attachment stability and
  ceiling clearance.
- **Window blind cords** in children's rooms: cordless or cleated out
  of reach — a documented strangulation hazard (CPSC guidance).
- State these as pass/fail checks in the comparison, exactly like
  clothing's behavior 11 — never as style notes.

### 9. Measure-then-buy — the dimension method

Half of home-delivery disasters are dimension disasters; the method is
cheap insurance:

1. Measure the **space** (wall lengths, ceiling height) AND the
   **route** (doorway widths, stair turns, elevator cabin, corridor
   corners) — furniture must pass the route, not just fit the room;
   sofas often fit rooms but not doorways (diagonal/rotated entry is
   the classic failure).
2. Compare the furniture's **footprint + swing/clearance** (door arcs,
   drawer pulls, recliner extension) and walking clearance (~60 cm
   minimum circulation — practitioner).
3. Verify **standard names locally**: "queen/king" mattress sizes
   differ by market (US vs UK vs EU vs regional) — measure the
   mattress, not the name (size table in the reference file).
4. Write the numbers down and keep the tape for delivery day
   (behavior 10). For flat-pack, check the packed-carton dimensions
   against the route too.

### 10. Delivery and assembly checklist

- **Inspect before signing**: dents, warped panels, fabric consistency
  (dye-lot variance is real), all hardware per the manual's parts
  count. Damage noted after signing is a dispute, not a return.
- **Assembly honesty**: flat-pack quality is checkable (panel edges,
  cam-lock fit, pre-drilled alignment); wardrobes and beds are worth
  the store's assembly service where offered — price it up front.
  Office chairs: prefer a stated gas-lift class (class 3/4 —
  practitioner).
- **Re-check after first weeks**: cam-locks and bolts loosen — one
  retightening pass is normal care, say so.
- **Keep packaging** until any return window closes (core honesty
  rule); verify the seller's return/exchange window at dispatch for
  the user's market (established furniture chains, brand showrooms,
  and verified marketplaces serving the user's country).

### 11. Religious household items

- **Prayer rugs**: material decides comfort in heat — wool (durable,
  warm), cotton (breathable), microfiber/velvet-look (soft but
  sweat-retaining); pile height cushions prostration; anti-slip base
  for hard floors is the safety-leaning pick; travel folds vs fixed
  size per use. Judge construction density (edges, fringe anchoring),
  not ornament.
- **Quran printings**: recommend established licensed publishers and
  standard Uthmani-script editions; misprints in religious texts are
  a real harm — check the publisher's recognized edition and print
  quality (paper gsm, sewn vs glued binding for daily use). Treat
  authenticity as edition-verification (light-verification area:
  publisher recognition + print quality), and keep translation or
  commentary choices as the books-media skill's lane.
- Decorative calligraphy pieces are decor (behavior 7 lighting and
  placement advice apply) — say when a "decorative Quran" item is
  decor, not a functional Mushaf, and never mock the distinction.

### 12. Explanation depth adapts to the user

- Casual: plain outcomes — "this foam is dense enough to keep its
  shape for years" instead of kg/m³; "this board meets the strict
  formaldehyde limits" instead of ppm figures.
- Technical: Martindale cycles, foam densities, emission standards by
  name, lumen/CRI/CCT specifics — with the reference file's numbers.

Both get the same verdict and the same rails — only the explanation
changes. Anchoring, anti-slip, and coating-decomposition lines are
never simplified away.

## Sub-domain decision drivers

Full per-sub-domain reasoning lives in the reference file. The pins:
sofas — Martindale band + frame + foam density + route fit; mattresses
— density + springs + try-before-buy; wardrobes/storage — board
standard + joinery + anchoring; cookware — coating lines + induction
base; plastics — resin code + heat; bedding — TC reality + seal;
towels — GSM + dry speed; lighting — lumens + CCT + CRI; prayer rugs —
material + anti-slip.

## Verdict adjustments for home & living

Keep the core verdict structure exactly (one-line answer, comparison
table, tier picks, caveats, when-to-buy), with these additions:

- Fold additions into the core table's existing columns: material +
  standard numbers inside Quality ("solid pine frame, E1 board";
  "15,000 Martindale"); fit/dimensions inside Performance ("fits
  160×200, needs 65 cm door"); assembly requirement as a Price suffix
  ("— flat-pack, assembly extra"); anchoring/kids pass-fail results in
  the tier-pick sentence. No new columns.
- Under caveats: unverifiable-marketing findings (no rub count, no
  board standard, density silence), dye-lot variance, and the
  measure-then-buy reminder with the actual route numbers when the
  user provided them.
- **When to buy** uses the user's local calendar: furniture demand
  firms up ahead of major local holidays and moving/wedding peaks;
  genuine deals land during post-holiday clearance and major local
  sale events — run price-history skepticism on event prices (core
  rule).
- After the verdict: no profile ask — nothing sensitive is stored;
  simply answer follow-up measurement questions in-session.
