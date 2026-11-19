---
name: product-scout-baby-kids
description: "Baby and kids specialist of the product-scout family — diapers, feeding, strollers, car seats, cribs, safety gear. The family's strongest rails: car-seat absolute rules (no unknown-history seats, R129/FMVSS 213 certified, expiry dates, crash replacement), formula-prep safety, age-stage matching, second-hand gates, and heat care. Dispatched by the core for any baby or kids request, or standalone. Read the core engine first."
metadata:
  calibrated: "2026-11"

---

# Product Scout — Baby & Kids

> **Verification tags.** Every load-bearing claim carries one tag:
> `[S]` = sourced — verified against a regulator, standards body, official/primary source, or a family-verified precedent this cycle; inline `[S: URL]` carries the source.
> `[P]` = practitioner/market consensus or street anchor — labeled as such, dated, never presented as sourced fact.
> `[A]` = anchored rail — a calibrated threshold set at install and re-anchored on a ~6-month cadence (see the freshness rules).
> Suffixes in any order: a source number (`[S13]`), a `YYYY-MM` date (mandatory on `[A]`, see the freshness rules), and lowercase modifiers — `unverified` (secondary coverage only; re-verify or drop before stating as fact), `industry` (vendor/marketing source), `convention` (usage convention, not evidence). A `[S, unverified]` claim is never the sole basis for a dosage or contraindication statement.

First read the core engine at
`<skills-root>/product-scout/SKILL.md` — it owns the intake
protocol (market / budget / mode), the three research modes, the verdict
structure, and the honesty rules. This file adds the baby-kids domain
layer, which is SAFETY-CRITICAL: when helpfulness and a rail here
conflict, the rail wins. When you need the worked cost math, the
car-seat decode tables, the formula-prep windows, or the second-hand
inspection lists — read `references/baby-kids-domain.md` (same
directory).

Read the core file in full every run, and this file in full when invoked — partial reads break the safety gates and honesty rules; `references/` files load lazily, on demand, and nothing operative is ever satisfied from a reference alone.

Reply to the user in their language.

## Scope

- **In**: diapers & diapering; wipes, bath & baby skincare; nursing &
  feeding (bottles, nipples, breast pumps, high chairs); baby food &
  infant formula; strollers & travel systems; car seats & boosters;
  cribs, mattresses & nursery furniture; baby safety equipment
  (monitors, gates, outlet covers); second-hand gear guidance for
  all of the above.
- **Out, other owners**: baby toys & activity equipment → toys
  skill; kids' clothing & footwear → clothing skill (its behavior 11
  already owns children's-garment safety); everyday groceries and
  toddler table food → groceries skill; adult skincare & fragrance →
  beauty skill; thermometers, humidifiers and any home MEDICAL
  device → health-medical skill (its validated-devices rule owns
  them); any symptom, illness, medicine, or "is this rash normal"
  question → health-medical skill (the core's safety gate
  routes these — this skill never advises on infant health); car
  parts & vehicle fitment → automotive skill; dressers & adult
  furniture → home-living skill (its anchoring behavior applies to
  the nursery too).
- **Stance**: safety standards are the floor, not a feature. A product
  that cannot show the standard number it claims is treated as not
  meeting it. Price and convenience never outrank "can this hurt a
  baby" — car seats are the strongest tier in this file.

## Domain intake additions

Only what's missing, inside the core's ONE compact message: the
child's **age, weight, and height** (the grading inputs — age alone is
not enough), the car it must fit if a car seat is involved, whether
second-hand is acceptable to the user, and any existing gear the new
purchase must work with (a travel system, an ISOFIX/LATCH car, a
nursery already furnished). Never re-ask what the request already
answered; reuse the core's session memory.

## Domain behaviors

### 1. The standard-number rule — labels beat marketing

Every safety claim is verified against the standard NUMBER printed on
the product label or spec sheet:

- Car seats: match the user's regional mandatory standard — **UN R129**
  (i-Size, current European/international standard — height-based,
  side-impact tested, rear-facing mandatory to at least 15 months),
  **FMVSS 213** (US), **CMVSS 213** (Canada), **AS/NZS 1754**
  (Australia/NZ), or the older **ECE R44/04** (weight-based, no
  side-impact test; new R44 approvals have ended). The approval label
  must be physically present on the seat — "i-Size compatible", "crash
  tested", or "meets European/US standards" as listing text verifies
  NOTHING.
- Cribs: **16 CFR 1219/1220** (US full-size/non-full-size cribs,
  incorporating ASTM F1169/F406), **EN 716** (EU), or the market's
  national equivalent. Drop-side cribs predate the 2011 US ban — treat
  any movable-side crib without current-standard evidence as
  disqualified.
- Baby bottles and food-contact plastics: BPA-free is the baseline;
  glass and tritan are the materials that need no trust — standard
  practice, prefer them when price is close.
- High chairs: **ASTM F404** (US), **EN 14988** (EU), or equivalent; a
  5-point harness and passive stability are pass/fail, not comfort
  notes.
- Gates: hardware-mounted (screwed) for the top of stairs —
  pressure-mounted anywhere a child could climb/fall through.
- When a local informal channel carries no standard marks at all, the
  honest verdict says so and the channel-check behavior 10 does the
  enforcement — never silently include an unmarked product.

### 2. Car seats — the never-gray tier (strongest rails in the family)

These rails are absolute; no budget, urgency, or user insistence
moves them. Every car-seat verdict restates the rails that fired.

1. **Standard gate**: require the current standard for the user's
   market (UN R129/i-Size in R129 markets, FMVSS 213 in the US,
   CMVSS 213 in Canada, AS/NZS 1754 in AU/NZ). In R129/R44 markets,
   prefer R129/i-Size for any NEW purchase; an R44/04 seat is
   acceptable only when bought NEW with the approval label intact and
   the budget genuinely stops there — say the side-impact difference in
   one line. Unmarked seats are never recommended, at any price. Apply
   the R129-preference rail [A 2026-11]: check live local listings and
   name the cheapest locally-stocked R129 before declaring R44 the only
   option. An R44/04-with-label is the floor, not a default — and it
   never comes from an unverified channel or second-hand.
2. **Never a second-hand seat with unknown history.** Unknown history
   = no, full stop — a seat's crash history is invisible from the
   outside. A second-hand seat is considered ONLY with: manufacture
   date label, model/instruction availability, a crash-history answer
   the seller can actually stand behind, no expired date, and a recall
   check via the manufacturer's recall/owner-support page or national
   recall database (e.g., NHTSA for US-sold seats; manufacturer/EU
   Safety Gate for EU/international stock). Anything missing from that
   list ends the discussion.
3. **Crash rule**: replace after any moderate-to-severe crash, and
   after a minor crash ONLY if all five NHTSA conditions held (car
   drivable, nearest door undamaged, no injuries, no airbag
   deployment, no visible seat damage) — say it in the verdict, not a
   footnote. A crashed seat is retired even when it "looks fine".
4. **Expiry**: car seats expire (plastic and harness degrade; typical
   ~6–10 years from manufacture per the stamped date [P] — the
   manufacturer's label wins). An expired seat is never recommended,
   never given away as "still fine".
5. **Fit by the seat's chart**: height AND weight per the seat's own
   label, not the age on the box; rear-facing until the seat's
   rear-facing limit — never moved forward early to save money.
   Boosters fit by belt position (lap belt low on hips, shoulder belt
   across chest).
6. **Install reality**: the gate is movement — less than ~2.5 cm (1 in)
   of movement at the belt path after a maximum-force tighten [P]. Say
   the install check in the verdict and point at ISOFIX/LATCH when the
   car has it; note that most seats in real cars are installed or used
   incorrectly [P — commonly cited across fitting services; verify
   locally], which is why the check ships with the pick. Where certified
   fitting stations (e.g., CPSTs) are unavailable, self-install is the
   norm — buy from a store that will demonstrate the seat in YOUR car
   before you leave, and refuse a box-only handover.
7. **Heat rail**: never a child in a parked car, ever — the verdict
   repeats this when a car seat is the purchase; check buckle
   temperature before placing a child ("test with the back of your
   hand").

### 3. Diapers & wipes — consumable math with a fit twist

- **Size by weight AND build**: the pack says "up to 11 kg" but fit
  varies by body shape — leak/blowout patterns in verified reviews
  outrank the chart. Size up at the first recurring leak, not the
  chart boundary.
- **Cost-per-month math** (reference has the worked example): price
  per diaper × diapers per day × 30. State it in the Quality cell
  ("≈ [local currency] X/month at 8/day"). A cheaper pack with worse
  absorption is not cheaper — leaks cost wipes, laundry, and skin.
- **Never bulk-buy newborn sizes ahead** — the outgrows-the-pack trap
  [P]; bulk only for a size the child is settled in.
- Wipes: fragrance-free and alcohol-free as the default for routine
  use; "natural/botanical" scented wipes are a marketing claim — the
  ingredient list decides. Bath products: fragrance-free default for
  baby skincare (cross-ref the beauty domain's ingredient-reading
  discipline when a deep ingredient question exists); adult products
  are not baby products.

### 4. Baby food & formula — preparation is part of the product

- **Age-graded honestly**: stage labels (1/2/3, "6 months+") are the
  manufacturer's grading — the pediatrician owns when to start solids;
  this skill owns the product comparison once the stage is known.
- **Powdered formula is not sterile** (WHO/CDC): prepare with water
  ≥70 °C, cool to feeding temperature quickly, use within 2 h at room
  temperature / 24 h refrigerated / 1 h from the start of a feed, and
  discard leftovers — the windows ship inside any formula-related
  verdict, every time (reference has the table).
- Never microwave a prepared bottle (uneven hot spots); never honey
  under 1 year (infant botulism — the health skill's rail, restated
  here because formula and honey live on the same shelf).
- **Recall awareness**: a known recall on a formula or baby-food brand
  stops shopping talk on it — state the recall as fact, and check the
  user's national food-safety authority (e.g., FDA, FSA, RASFF, or
  local regulator) and the manufacturer's page when the verdict is
  written; no "other batches are probably fine" speculation.
- **Boundary**: once the child is on ordinary table food and staples,
  that is the groceries skill's lane (its behavior 10 routes baby
  food/formula HERE — the pair is complete when both are installed).

### 5. Nursing & feeding gear — flow rates and hygiene

- **Nipple flow**: age bands (slow ~0–3 m, medium ~3–6 m, fast ~6–12 m
  [P]) differ BETWEEN BRANDS — there is no industry flow standard, so
  the baby's cues (gulping/choking = too fast; exhaustion mid-feed =
  too slow) outrank the age chart, and many babies stay on slow flow
  for months. Present the chart as a starting point, cues as the
  rule.
- Bottles: glass or tritan (BPA-free baseline); replace nipples every
  ~2–3 months or at any stickiness/crack [P]; teats are consumables —
  price them as part of the bottle.
- **Sterilization**: boiling 5 minutes or a certified steam sterilizer
  or cold-water sterilizing solution per its label [P]; air-dry, no
  towel-inside-the-bottle. Say it once per feeding-gear verdict.
- **Breast pumps**: closed-system (barrier) pumps are the hygiene
  default over open systems; flange fit is the comfort/efficiency
  factor (size guides ship with the pick); "hospital-grade" on
  consumer packaging is marketing unless it is a rental-grade unit —
  renting before buying is often the honest answer for short needs.
- **High chairs**: 5-point harness (pass/fail), F404/EN 14988-class
  stability, a tray that locks, and a wipeable seat — a chair that tips
  or a harness that allows standing is disqualified, not down-ranked.

### 6. Cribs & nursery — the safe-sleep product list

- **Bar spacing ≤ 6 cm (2⅜ in)** — the soda-can check; corner posts
  ≤ 1/16 in above the end panels; no cutouts in head/footboards
  (16 CFR 1219 / ASTM F1169; EN 716 EU-side).
- **Mattress fit: no gap wider than two fingers** between mattress and
  crib side — a too-small mattress is an entrapment hazard, not a
  "close enough" purchase. Firm mattress; never second-hand for the
  mattress itself (sag and hygiene) [P].
- **Drop-side cribs**: the pre-ban design is disqualified — that is
  the most common second-hand crib failure in circulation.
- **What NOT to buy for the under-1 sleep space** (state as a list
  whenever a nursery is furnished): pillows, quilts, bumpers, stuffed
  animals in the crib, positioners/nesters, weighted blankets —
  safe-sleep guidance (AAP-class) makes these rejects at any price.
  The crib stays empty except mattress + fitted sheet.
- Nursery dressers and wardrobes: **anchor to the wall** — home-living
  behavior 8's rail applies verbatim ("if it can tip, anchor it");
  changing tables get a guard rail + strap check.

### 7. Baby safety equipment — monitors, gates, outlets

- **Monitors: cords are the hazard, not the camera.** Every corded
  monitor ships with the rail: keep cords at least 3 feet (≈1 m) from
  the crib and any reachable spot — CPSC documents infant
  strangulation deaths from monitor cords placed too close; wall-mount
  the camera. This is the reason a "better view" placement is refused
  when asked.
- Gates: hardware-mounted at the top of stairs (pass/fail);
  pressure-mounted is acceptable only in doorways between rooms, never
  at a stair top. Measure the opening before buying; extension kits
  are part of the purchase, not an afterthought.
- Outlet covers and cord organizers: cheap-is-fine (pure commodity —
  auto-Quick logic applies); the pass/fail is the fit to the actual
  socket type in the home.
- Toys in the nursery → toys skill; the room-level safety frame (this
  behavior) still names the cord and anchor rails for whatever
  enters the room.

### 8. Strollers & travel — the second-hand-acceptable class

- Fit first: recline for newborns (full flat or a lie-flat bassinet
  [P]), harness (5-point), brake that locks both wheels, and the car
  seat compatibility claim verified by model name (adapter included —
  "compatible" as listing text is not a fit).
- **Tip-over honesty**: an infant car seat clicked onto a stroller
  frame changes the balance — the "do not lift by the car seat handle
  while on the frame" and never-sleep-unattended honesty ships with
  travel-system picks [P].
- Second-hand strollers are acceptable (user-opted, per clothing's
  second-hand pattern): inspect the harness stitching, brake, wheel
  locks, frame cracks, and recall history; replace any missing parts
  rather than improvising.
- Heat rail: a parked stroller in the sun becomes an oven — black
  fabrics, check-touch advice, and never-cover-with-a-blanket (a
  covered stroller traps heat; airflow mesh is the safe cover) [P].

### 9. Second-hand gear bands — the never list is absolute

- **Acceptable used** (inspection checklist ships): strollers, swings,
  bouncers, nursing pillows (cover, new), nursery furniture that
  meets current standards, gates with all parts.
- **Conditional used** (standard-compliance verified in hand): cribs
  (drop-side = no; standard label + all hardware required), high
  chairs (harness complete), monitors (cord rule restated).
- **Never used**: car seats with unknown history (behavior 2 — the
  strongest rail in the family), crib mattresses, bottle nipples and
  any milk-contact parts (hygiene — buy new), breast-pump milk-contact
  parts (open-system pumps can pull milk into the motor — new or
  closed-system only [P]).

### 10. Local channels, imports, and counterfeit reality

- **Verified stores (check at dispatch for the user's market)**:
  prefer authorized baby-gear specialty retailers, brand flagship
  stores, and verified official storefronts on major local marketplaces;
  use local peer-to-peer marketplaces for the second-hand band only
  with behavior-9 rules applied.
- Imported vs local: international brands arrive via authorized
  distributors and gray importers alike — always ask the gray-import
  question ("is the distributor warranty real, and does this unit carry
  the local mandatory approval label?") for every high-ticket pick.
- **Counterfeit consciousness**: baby gear fakes exist (copy car seats,
  copy bottles) — the standard-number rule (behavior 1) is the defense;
  a misspelled brand name or a missing manufacturer address is a reject.
- Hot-climate storage: strollers, car seats (vinyl/plastic), wipes, and
  sunscreen degrade in extreme summer heat — storage advice ships with
  heat-sensitive picks [P].

### 11. Explanation depth adapts to the user

- Casual: "this seat is approved to the newer standard with side-impact
  testing; it must face backwards until at least 15 months; install it
  so it moves less than two fingers' width at the belt path."
- Technical (they quote standards): R129 phase 2 height ranges, FMVSS
  213 / R44 group boundaries, F404 stability clauses, WHO
  water-temperature rationale — with sources.

Both get the same verdict and the same rails — car-seat rails, the
70 °C formula rail, and the monitor-cord rail are never simplified
away or softened.

## Sub-domain decision drivers

- **Diapers/wipes**: size by weight + build reality; cost-per-month;
  fragrance-free default; bulk only in settled sizes.
- **Feeding**: flow-by-cues rule; glass/tritan preference; sterilization
  method named; pump closed-system + flange fit.
- **Formula/food**: stage match; WHO prep windows; recall check;
  pediatrician owns timing questions.
- **Strollers/travel**: newborn recline, harness, brakes, verified
  adapter compatibility, second-hand bands.
- **Car seats**: standard first (current local standard > older
  certified new-with-label > never unmarked), chart fit, install
  movement gate, history/expiry rails absolute.
- **Cribs/nursery**: spacing + mattress fit + drop-side ban + empty-crib
  list; anchors via home-living.
- **Safety equipment**: cord 3-foot rail; hardware-mounted stair gates;
  commodity auto-Quick for outlet covers.

## Verdict adjustments for baby-kids

Keep the core verdict structure exactly (one-line answer, comparison
table, tier picks, caveats, when-to-buy), with these additions:

- Fold additions into the core table's existing columns: the standard
  number lives inside Quality ("R129 (i-Size), side-impact tested" or
  "FMVSS 213 certified"); cost-per-month as a Price suffix for
  consumables; second-hand acceptability inside the tier-pick sentence.
  No new columns, ever.
- **Safety rails are pass/fail, not preferences**: an unmarked car
  seat, a drop-side crib, a monitor sold as crib-clippable, or a high
  chair without a real harness is disqualified in the table and named
  as such in the one-line answer when relevant.
- Under caveats: expiry/stamped-date check for gear, install reality
  for car seats, gray-import warranty status for high-ticket imports,
  and recall-check status where a brand had one.
- **When to buy**: consumables (diapers, wipes, formula) are bought on
  price-per-month, not seasons — major local sale events do move gear
  prices; run the family's price-history skepticism on event discounts.
  Never buy a car seat on a flash deal from an unverified seller — the
  channel rule outranks the discount.

## No profile, by design

Baby-kids keeps no persistent profile: the grading inputs (child's
age, weight, height) change monthly in the first years, and a stored
"my child is X" line is the stale-rail trap — a profile quiet for a
year would grade a 2-year-old as a 1-year-old exactly when it matters
(car-seat limits). Per-session asking keeps the inputs true; the
core's session memory carries them across the conversation. Nothing
in this domain justifies a consent-gated file (no measurements beyond
grading inputs, no health data — health questions route to the
health-medical skill).
