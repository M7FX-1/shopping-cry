# Groceries — domain reference (demoted detail; no operative safety rule lives here)

Every operative rail (can-integrity rejects, chemical-mixing and child-safety
storage rails, tobacco and ration policy gates, expired-infant-formula ban)
lives in the SKILL.md main file. This reference holds the numeric tables,
worked math, case tables, and channel detail the main file points at.
Verification tags: `[S]` = sourced — verified against a regulator, standards body, official/primary source, or a family-verified precedent this cycle (inline `[S: URL]` carries the source); `[P]` = practitioner/market consensus or street anchor — labeled as such, never presented as sourced fact; `[A]` = anchored rail — a calibrated threshold set at install and re-anchored on a ~6-month cadence. Suffixes in any order: a source number (`[S13]`), a `YYYY-MM` date (mandatory on `[A]`), and lowercase modifiers — `unverified` (secondary coverage only; re-verify or drop before stating as fact), `industry` (vendor/marketing source), `convention` (usage convention, not evidence). A `[S, unverified]` claim is never the sole basis for a dosage or contraindication statement.
If a rule here ever disagrees with the SKILL.md, the SKILL.md wins.

## Worked unit-price math `[P]`

- Unit price = price ÷ net weight (or volume). Worked example: rice bag
  A, EGP 90, net 5 kg → EGP 18/kg; bag B, EGP 40, net 2 kg → EGP 20/kg.
  Bag A is cheaper per kilo despite the higher shelf price — unless the
  household cannot use 5 kg before quality/pest risk (SKILL behavior 7).
- Multi-buy check: "3 packs for EGP 120" vs single EGP 42 → 120/3 = 40
  each, a real deal; "3 for EGP 130" vs single 42 → 43.3 each, a deal
  that is not one. Always divide.
- Shrinkflation check: last-bought net grams vs today's net grams at the
  same price — the missing grams are the hidden price increase. Compare
  brands per kg, never per pack.
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

- Date formats on Egyptian shelves mix day-month-year, Gregorian and
  Hijri production codes; when unclear, ask or skip `[P]`.
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
- (echo of SKILL behavior 8) Eggs: intact shells only;
  room-temperature retail is the Egyptian norm; use within ~1–2
  weeks; the float test is a crude age check only, not a freshness
  guarantee `[P]`.

## Halal certification guidance `[P]`

- Egyptian-made food without a halal mark is normal (default-market
  practice); the mark matters on imports and animal-origin ingredients.
- When halal status is decision-bearing: read the ingredient list for
  gelatin, rennet, alcohol carriers (vanilla extract), animal-origin
  E-additives; then the named certifier on pack — certifier rigor varies
  by country and body; when no certifier is named, say "cannot verify".
- Imported meat/poultry entering Egypt requires halal-slaughter
  certification (rule current as of [S 2026-11]; confirm with the
  importer before relying on it).
- A certifier list may be added later ONLY sourced from an official
  accreditation register (a national or GAC-recognized
  halal-accreditation body's published register), date-stamped `[S]`
  with the re-verify marker — never from marketing claims or
  secondary blog rankings (critic decision Q3).

## Egypt channels (verified existence 2026-11 — re-verify at dispatch)

- **Store chains** `[S]`: Carrefour Egypt (Majid Al Futtaim operator),
  Metro Markets and Kheir Zaman (Mansour Group), BIM, Spinneys,
  Fathalla, Seoudi.
- **Online** `[S]`: Noon Egypt, Amazon.eg, Jumia Egypt
  (family-verified marketplaces); Breadfast (24/7 delivery, Cairo/Giza,
  6,000+ items); Rabbit (~15–20 min quick commerce, Cairo).
- Cold-chain honesty: quick-commerce riders are not refrigerated —
  chilled/frozen risk purchases in heat; store pickup or refrigerated
  services preferred `[P]`.
- Traditional channels: attar/spice shops and bakeries are legitimate;
  attach the adulteration-table defenses `[P]`.
- Subsidy context: tamween goods and baladi bread sit at subsidized
  prices in a parallel system — price-gap context only; no gaming
  advice (policy gate, SKILL Scope).

## Recalls and food-safety incidents

- Egypt: NFSA (Law 1/2017) owns recalls and the early-warning system
  `[S]`. A known recall stops all shopping talk on the item.
- User-reported "something's off" (mold, smell, foreign object): state
  the reject rule, keep the packaging/batch, report to the retailer and
  NFSA channels — never diagnose a safety claim from a photo `[P]`.
