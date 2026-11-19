# Groceries — domain reference (demoted detail; no operative safety rule lives here)

Every operative rail (can-integrity rejects, chemical-mixing and child-safety
storage rails, tobacco and subsidy-gaming policy gates, expired-infant-formula
ban) lives in the SKILL.md main file. This reference holds the numeric tables,
worked math, case tables, and channel guidance the main file points at.
Verification tags: `[S]` = sourced — verified against a regulator, standards body, official/primary source, or a family-verified precedent this cycle (inline `[S: URL]` carries the source); `[P]` = practitioner/market consensus or street anchor — labeled as such, never presented as sourced fact; `[A]` = anchored rail — a calibrated threshold set at install and re-anchored on a ~6-month cadence. Suffixes in any order: a source number (`[S13]`), a `YYYY-MM` date (mandatory on `[A]`), and lowercase modifiers — `unverified` (secondary coverage only; re-verify or drop before stating as fact), `industry` (vendor/marketing source), `convention` (usage convention, not evidence). A `[S, unverified]` claim is never the sole basis for a dosage or contraindication statement.
If a rule here ever disagrees with the SKILL.md, the SKILL.md wins.

## Worked unit-price math `[P]`

- Unit price = price ÷ net weight (or volume). Worked example
  (illustrative in USD — compute in the user's local currency): rice
  bag A, $9.00, net 5 kg → $1.80/kg; bag B, $4.00, net 2 kg → $2.00/kg.
  Bag A is cheaper per kilo despite the higher shelf price — unless the
  household cannot use 5 kg before quality/pest risk (SKILL behavior 7).
- Multi-buy check: "3 packs for $12.00" vs single $4.20 → $4.00 each,
  a real deal; "3 for $13.00" vs single $4.20 → $4.33 each, a deal
  that is not one. Always divide.
- Shrinkflation check: last-bought net grams vs today's net grams at the
  same price — the missing grams are the hidden price increase. Compare
  brands per kg/100 g, never per pack.
- Drained weight on cans (beans, corn): the drained weight is the food;
  the liquid is pack weight. Per-unit comparisons on cans use drained
  weight; water-added "juice" percentages read the panel instead.

## Shelf-life and bulk windows `[P]` (sealed, cool, dry storage)

| Item | Unopened | After opening | Bulk verdict |
|---|---|---|---|
| White rice | years | ~1 year sealed container | bulk OK |
| Whole-wheat flour | months | ~2–3 months (germ rancidity) | bulk trap |
| White flour | ~8–12 months | ~6 months | bulk OK, sealed |
| Dried legumes | years | years (longer cooking with age) | bulk OK |
| Sugar, salt | indefinite | indefinite, sealed | bulk OK |
| Cooking oil | ~12–18 months | ~3–6 months, cool dark | buy ≤ 6 months' use |
| Ground spices | — | potency fades ~6–12 months | bulk trap |
| Tea (loose/bags) | ~18–24 months | ~6–12 months airtight | moderate bulk |
| Ground coffee | — | ~1–3 weeks peak flavor | small packs |
| Pasta | years | years | bulk OK |
| Honey | years | years (crystallizes ≠ spoilage) | size is taste, not spoilage |
| Infant formula | use-by hard limit | per label | never bulk beyond need |

Pantry-pest rail: sealed glass/plastic containers, cool dry cupboard, buy
dates checked; weevils arrive in old stock [P].

## Adulteration case table

| Item | Documented fraud | Regulator/document trail | Shelf defense |
|---|---|---|---|
| Ground turmeric | lead chromate, metanil yellow dyeing | FDA import alert 28-13 (lead in ground turmeric/cumin); 2016 & 2022 US recalls `[S]` | sealed brand, batch code, avoid open bins |
| Chili/paprika | Sudan I–IV dyes; brick dust, starch fillers | documented EU/UK alert history (2003–2005 Sudan-dye waves) `[S]` | price realism; unnatural uniform red |
| Olive oil | dilution with cheaper oils; "extra virgin" mislabel | EU Food Fraud Network annual reports 2019–2020 — olive oil most-notified product `[S]` | harvest/best-before date on premium claims, dark glass, price realism |
| Honey | syrup blending | EU JRC 2023: ~46% of imported honey samples flagged suspicious `[S 2026-11]` | supplier certification; skepticism at very low prices |
| Saffron | safflower/turmeric substitution, dyed fibers | long documented fraud history `[P]` | price realism (real saffron is expensive by weight) |

Honest limit: laboratory testing proves adulteration; home tests detect only
crude cases and never prove authenticity `[P]`.

## Date codes and integrity detail

- Date formats vary by market (DD/MM/YYYY, MM/DD/YYYY, YYYY-MM-DD, and
  occasionally regional calendars); when ambiguous, verify or skip `[P]`.
- "Best before" = quality; "use by" = safety. Near-expiry value logic in
  SKILL behavior 2.
- (echo of SKILL behavior 2) Can reject list (bulging, seam dents,
  rust, leaks, spurting) is standard food-safety guidance `[P]` —
  reason stated: botulism risk.
- (echo of SKILL behavior 8) Chilled meat: pack liquid cloudiness,
  gray-brown color shift, off smell = reject; counters without
  visible refrigeration are not chilled channels `[P]`.
- Fish: bright eyes and red gills = fresh markers; buy early from ice
  displays `[P]`.
- (echo of SKILL behavior 8) Eggs: intact shells only; follow local
  refrigeration norms (washed eggs refrigerated; unwashed eggs cool/dry,
  ~1–2 weeks); the float test is a crude age check only, not a freshness
  guarantee `[P]`.

## Halal and dietary-certification guidance `[P]`

- In majority-Muslim markets, domestically produced food without a halal
  mark is often normal market practice; in non-majority markets or on
  imported/processed goods, a recognized certifier mark matters.
- When halal status is decision-bearing: read the ingredient list for
  gelatin, rennet, alcohol carriers (vanilla extract), animal-origin
  E-additives; then check the named certifier on pack — certifier rigor
  varies by country and body; when no certifier is named, say "cannot
  verify".
- Verify any certifier list only against an official accreditation
  register (national or GAC-recognized halal-accreditation body), never
  marketing claims or secondary blog rankings.

## Local channels and recalls `[P]`

- **Channels (verify at dispatch for the user's market)**: compare
  established national supermarket chains, hard discounters, verified
  online grocery platforms, and specialty shops (spice shops, bakeries,
  farmers' markets).
- Cold-chain honesty: quick-commerce riders on bikes/motorbikes are
  rarely refrigerated — chilled/frozen items carry heat risk; store
  pickup or refrigerated delivery is preferred `[P]`.
- Traditional channels: spice shops and bakeries are legitimate; attach
  the adulteration-table defenses `[P]`.
- **Recalls**: check the user's national food-safety authority (e.g.,
  FDA/USDA, EU RASFF, UK FSA, CFIA, FSANZ, or local regulator). A known
  recall stops all shopping talk on the item. On user-reported "something's
  off" (mold, smell, foreign object): state the reject rule, keep the
  packaging/batch, and report to the retailer and local food-safety
  regulator — never diagnose a safety claim from a photo `[P]`.
