# Appliances — Capacity Tables, Running-Cost Math, and Driver Detail

This is the demoted-companion reference for the product-scout-appliances
skill (install path: `references/appliances-domain.md`). Read it when a
verdict needs the numeric sizing tables, the Egypt tariff table with
worked running-cost examples, stabilizer sizing, or per-sub-domain
driver detail.

**No operative safety rule lives here**: every gas, electrical, and
installation rail stays in SKILL.md behaviors 4–8. If this file and the
skill ever disagree, the skill wins. Verification tags: `[S]` = sourced — verified against a regulator, standards body, official/primary source, or a family-verified precedent this cycle (inline `[S: URL]` carries the source); `[P]` = practitioner/market consensus or street anchor — labeled as such, never presented as sourced fact; `[A]` = anchored rail — a calibrated threshold set at install and re-anchored on a ~6-month cadence. Suffixes in any order: a source number (`[S13]`), a `YYYY-MM` date (mandatory on `[A]`), and lowercase modifiers — `unverified` (secondary coverage only; re-verify or drop before stating as fact), `industry` (vendor/marketing source), `convention` (usage convention, not evidence). A `[S, unverified]` claim is never the sole basis for a dosage or contraindication statement.

---

## Capacity sizing tables

- **Refrigerator/freezer `[P]`**: ~70–100 L of fresh+frozen capacity per
  person as the working band (a 2-person household lands ~250–300 L, a
  4–5-person household ~400–500 L); add freezer volume if the household
  batch-cooks or stores meat. Internal layout beats total liters:
  produce-heavy households need crisper space, frozen-goods households
  need a real freezer — match compartments to the stated habit.
- **Washer `[P]`**: ~6–7 kg drum for 1–2 people; 8–9 kg for a family of
  4–5; 10+ kg or a dryer for large households / baby laundry volume.
  Front-loader: better wash, gentler fabric, more service-sensitive
  electronics. Top-loader: cheaper, simpler repair, harsher on fabric —
  weigh against the local repair network (SKILL.md behavior 8).
- **Air conditioner `[P]`**: start from ~600–650 BTU/h per m² of floor
  area for a hot-climate room; adjust upward for west/sun-facing rooms,
  top floors, high ceilings, poor insulation (+10–25%); then round UP
  to the nearest real nameplate size. A 20 m² bedroom lands ~13,000–
  15,000 BTU (~1.25 ton) before adjustments; a 30 m² living room
  ~19,000–22,000. Verify against the nameplate BTU, never the headline
  (SKILL.md behavior 1); 1 ton = 12,000 BTU/h = 3.5 kW `[S]`.
- **Microwave `[P]`**: 20–25 L suits 1–3 people; 28–40 L for families
  or plate-sized dishes; wattage bands: 700–800 W budget, 900–1,100 W
  comfortable — cook-power, not input-power.

## Egypt residential tariff table — date-stamped `[S]`

Residential slabs (EGP/kWh) as verified 2026-11 against the regulator
(EgyptERA) and press coverage of the July 31, 2026 raise (~12% average;
rates moved twice during 2026 — April and July — so re-check at
dispatch before quoting numbers to the user):

| Slab (kWh/month) | EGP/kWh |
|---|---|
| 0–50 | 0.68 |
| 51–100 | 0.95 |
| 101–200 | 1.15 |
| 201–350 | 1.72 |
| 351–650 | ~1.95 |
| top tiers | up to 2.74 (flat, from 1,000 kWh+) |

**Marginal-rate rule** (SKILL.md behavior 3): an added appliance's
consumption lands in the household's top reached slab — use that slab's
rate for running-cost math and say the assumption.

**Worked examples** (illustrative, mark as estimates in output):

- *Fridge class swap*: an old unit at ~500 kWh/yr vs an A-class at
  ~200 kWh/yr → 300 kWh × 1.72 ≈ **EGP ~520/yr** — a class premium pays
  back over the fridge's life, especially at higher slabs.
- *AC season*: 18,000 BTU fixed-speed ~2.0 kW vs inverter averaging
  ~1.3 kW at equal duty → 0.7 kW × 8 h/day × 120 days ≈ 670 kWh × 1.95
  ≈ **EGP ~1,300/season** — before the hot-weather upper slabs, which
  push the real saving higher.
- *Inverter honesty*: "up to 60% savings" marketing assumes a light
  duty cycle; use measured kWh or the label, and present savings as a
  range tied to usage hours `[P]`.

## Stabilizer sizing `[P]`

- Size an AVR stabilizer by **motor start surge**, not running wattage:
  compressor appliances draw 3–5× running current at start — a fridge
  rated ~200W running needs a stabilizer rated ~1,000–1,500 VA; a
  1.5-ton AC (~2,000W) needs ~5,000–10,000 VA per the unit's start
  current. Check the appliance manual's stated start current where
  given.
- Prefer units with a stated wide input range (e.g., 140–260V) and a
  serviceable copper-wound transformer; the cheap electronic-relay
  type fails first.
- When in doubt between two VA ratings, take the larger — an undersized
  stabilizer overheats; never undersize a compressor appliance's
  stabilizer.
- Placement: not on thin extension cords; fridges on their own socket
  (echo of SKILL.md behavior 4 socket discipline).

## Small-appliance claims-inflation table `[P]`

| Claim | Reality check |
|---|---|
| Air-fryer "7L capacity" | Often total pot; usable basket ~60–70% of the figure — check basket dimensions |
| Blender "2L jar" | Usable liquid capacity lower; blades' effective volume is what matters |
| Heater "2000W" | Verify real draw vs the 16A socket ceiling (~3,500W); certification is SKILL.md behavior 4's gate — it is not mode-gated |
| Microwave "1200W" | Check cook-power (output) vs input draw — they differ ~30–40% |
| Kettle "fast boil" | Real driver is wattage (2,200W vs 1,800W) — compare the number, not the word |
| Air purifier "medical-grade" | Wellness claim — check CADR for room size; no medical standard applies |

## Per-sub-domain driver detail `[P]`

- **Fridge/freezer**: compressor type (inverter = quieter + efficiency),
  layout vs habits, gasket quality, service network first (behavior 8),
  freezer-on-top vs bottom vs side-by-side per kitchen fit.
- **Washer/dryer**: drum kg (table above), hard-water handling
  (behavior 6), spin speed vs fabric wear, parts availability for the
  exact model.
- **AC**: room-sized BTU (table above), T3 tropical rating for summer
  peaks, install-crew quality as the deciding variable (behavior 7),
  running-cost math (table above), filter cleaning cadence.
- **Range/oven**: gas vs electric per the kitchen's real connection
  (SKILL.md behavior 5 rails, incl. the flame-failure preference), oven
  size for the household's baking reality.
- **Dishwasher**: place settings vs household, salt/rinse-aid running
  cost in hard water, fit and install (behavior 7).
- **Water heater**: gas → behavior 5 rails first; electric → element
  scaling cadence (behavior 6), tank capacity vs household (~50 L
  1–2 people, ~80 L family `[P]`).
- **Small appliances**: certification gate + claims-inflation table +
  motor/element warranty (behavior 9); coffee/espresso judged on
  machine class and consumable cost per cup; vacuums on suction
  persistence and filter/spares availability, not wattage.
