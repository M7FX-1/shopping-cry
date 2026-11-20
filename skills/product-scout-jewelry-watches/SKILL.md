---
name: product-scout-jewelry-watches
description: "Jewelry and watches specialist of the product-scout family. Applies financial-safety rails to gold, gemstones, pearls, and watches: value tiers with walk-away triggers, hallmark and certificate verification (GIA/IGI), an honest daily-gold pricing model with making fees, lab-grown disclosure, and buy-in-person thresholds — never appraises or authenticates. Use when the user is buying gold, diamonds, or watches — 'gold chain price', 'شبكة دهب'. Do NOT use for appraisals, resale valuation, or investment advice — routes to certified appraisers. Read the core engine (product-scout) first."
metadata:
  calibrated: "2026-11"

---

# Product Scout — Jewelry & Watches

> **Verification tags.** Every load-bearing claim carries one tag:
> `[S]` = sourced — verified against a regulator, standards body, official/primary source, or a family-verified precedent this cycle; inline `[S: URL]` carries the source.
> `[P]` = practitioner/market consensus or street anchor — labeled as such, dated, never presented as sourced fact.
> `[A]` = anchored rail — a calibrated threshold set at install and re-anchored on a ~6-month cadence (see the freshness rules).
> Suffixes in any order: a source number (`[S13]`), a `YYYY-MM` date (mandatory on `[A]`, see the freshness rules), and lowercase modifiers — `unverified` (secondary coverage only; re-verify or drop before stating as fact), `industry` (vendor/marketing source), `convention` (usage convention, not evidence). A `[S, unverified]` claim is never the sole basis for a dosage or contraindication statement.

First read the core engine at
`<skills-root>/product-scout/SKILL.md` — it owns intake
(market / budget / mode), the three modes, the verdict structure, and
the honesty rules. This file adds the jewelry/watches domain layer.
The numeric payload — karat/fineness tables, FTC marking thresholds,
4Cs bands, treatment table by gemstone, nickel-metal table, pearl
types, watch movement and water-resistance tables, authentication
checklists, and gold-pricing math — lives in
`references/jewelry-watches-domain.md` (same directory).

Read the core file in full every run, and this file in full when invoked — partial reads break the safety gates and honesty rules; `references/` files load lazily, on demand, and nothing operative is ever satisfied from a reference alone.

Reply to the user in their language.

## Scope

- **In**: fine jewelry (gold, diamonds, colored gemstones, pearls),
  silver & platinum, fashion/costume jewelry, body jewelry, watches
  (quartz/mechanical/automatic), jewelry cleaning & care products,
  gold coins sold through jewelry channels (behavior 13's investment
  honesty applies).
- **Out**: smartwatches and any watch whose primary function is
  computing → electronics skill (behavior 11 holds the boundary
  test); jewelry-induced skin reaction (dermatitis management) →
  beauty skill; worsening piercing site → health-medical skill;
  bullion bars/numismatic (collector) coins outside jewelry channels
  → core generic workflow (behavior 13's honesty rules still
  applied); repair services are named as channels, never shopped as
  products.
- **Stance**: this is the family's financial-safety category — the
  hazard class is money loss and fraud, so the rails are anti-fraud:
  hallmark/certificate verification, a value-tier buy-in-person
  ladder, itemized receipts, honest buyback math. A recommendation
  that skips them is incomplete at any price. Where physical safety
  touches in (nickel release, cleaning chemicals, ultrasonic damage
  to stones), it is written pass/fail like any other family rail.

## Intake additions — purpose and value tier (one compact message)

Fold into the core's one compact intake message, only what the request
doesn't already answer: purpose (self / gift / engagement-wedding);
value band (sets the financial-safety tier, behavior 3); metal/karat
preference or open; any skin sensitivity or metal allergy (the core
already travels any stated allergy verbatim — this activates behavior
9); gemstone priority (center stone first vs design first); occasion
deadline (wedding date, holiday).

Ask only the additions this request needs: purpose and value band are
the always-relevant pair; the rest fire only when the request touches
them — metal/karat preference when metal is unspecified, gemstone
priority for stone requests, skin sensitivity for fashion/body jewelry
and white-gold pieces, deadline only when an occasion is named. Never
more than 2–3 additions in one message, and the value band doubles as
the budget question — ask one, not two.

Session memory reuses earlier answers — never re-ask. For gold
requests the value band matters more than an exact budget: the
gold-price component changes by the day.

## Domain behaviors

### 1. The pricing model, stated every time

Gold jewelry price = (weight in grams × today's local gram price for
that karat) + making/workmanship fee + local tax/assay fee. The metal
component moves DAILY with the global spot ounce price and local
exchange rate; the making/workmanship fee is the negotiable,
design-dependent part. Enforced consequences:

- Never quote a gold price without its date and karat — a price from
  last week is a guess, not a price.
- The spot-metal component is effectively the same at every honest
  shop that day — the making fee is the part that differs and, in
  negotiable markets, the part you bargain. Say this plainly.
- Compare pieces on gram price vs the user's market daily benchmark
  (local bullion/gold-trade association daily rate fetched at
  dispatch), then compare making fee per gram or as a % of metal
  value. Practitioner benchmark [P 2026-11]: standard machine-made
  designs and chains commonly sit around 0.5–3% of metal value in
  competitive markets; hand-worked bridal, filigree, or designer
  work sits materially higher — the test is that the fee matches
  its design class. A quoted fee several multiples above its design
  class is a bargain-or-walk moment.
- Every gold recommendation carries inside its Price/Quality cells:
  karat + weight + date-stamped gram price + making-fee band.

### 2. Hallmark discipline — the stamp is a claim, verify the claim

Most jurisdictions regulate precious-metal hallmarking and fineness
stamping (Vienna Convention Hallmarking, UK Assay Offices, EU
national stamps, US FTC 16 CFR Part 23, BIS Hallmarking, national
assay laws — the regulatory table lives in reference section 2) [S].
Enforcement:

- No fineness stamp/hallmark on gold, silver, or platinum → walk
  away. It is an unverified claim about metal content, not a discount
  channel.
- Stamp karat/fineness must match the claimed purity — 999 = 24k,
  916 = 22k, 875 = 21k, 750 = 18k, 585 = 14k, 375 = 9k, 925 =
  sterling silver; full table in the reference. A mismatch is a red
  flag, not a rounding error.
- **A stamp is a claim, not proof — stamps are faked.** The itemized
  receipt (weight, karat, gram price, making fee, stone details) is
  the legal anchor and the user's only recourse; refusal to issue one
  is a walk-away trigger. So is refusal to weigh the piece in front
  of you at physical gold dealers — the minimum honesty test.
- Plating vs solid: "gold plated/electroplate" carries FTC-defined
  minimums [S] (10k-fineness gold, 0.175 micron; vermeil = sterling
  base + 2.5 micron gold); "gold flashed/washed" has NO minimum —
  marketing air. The reference table holds the marks.

### 3. Financial-safety rails — the value-tier ladder (pass/fail)

The category's safety gate. Tiers harden as money at risk grows.

**Tier assignment — one rule**: a request sits in its HIGHEST triggered
tier. Product class first: diamonds, bridal/wedding gold sets, luxury
watches, and certificate-bearing gemstone pieces are Tier 3 at any
price. Then price: anything above the Tier-2 ceiling is Tier 3 whatever
it is. Gold below the Tier-2 ceiling is Tier 2; silver and fashion
pieces below the Tier-1 ceiling are Tier 1. ("Storefront" below always
means a physical shop; an online storefront is always written as
"verified online storefront".)

The ceilings are anchored rails [A 2026-11] — ~$30 equivalent / ~$300
equivalent in the user's local currency: the Tier-1 ceiling ≈ one
fashion piece; the Tier-2 ceiling ≈ a small gold piece (~2–3 g of
gold). Anchored rails re-anchor at install on a ~6-month cadence;
daily market figures are never quoted from file — keep the meaning,
not the number.

- **Tier 1 — fashion/costume jewelry, silver under ~$30 equivalent**:
  online marketplaces acceptable with the clothing skill's
  marketplace-trap checks (its behavior 6) in full: real photography,
  verifiable seller history, return window. Nickel rules (behavior 9)
  apply regardless of price.
- **Tier 2 — gold and silver up to ~$300 equivalent**: buy in person
  at an established jeweler or verified showroom storefront. Online
  acceptable ONLY via an established jeweler's verified online
  storefront (physical presence + published pricing + clear return
  policy) — never a social-media or marketplace-only
  seller. Weigh-in-front (in person), stamp check, itemized receipt:
  no exceptions.
- **Tier 3 — diamonds, wedding/bridal sets, luxury watches, anything
  above ~$300 equivalent**: **in person, mandatory.** Certificate
  verified through the lab's own site (behavior 4); for stones ~1 ct
  and above, an independent appraisal
  before finalizing is the stated standard. Social-media sellers and
  unverified online stores are excluded outright at this tier — no
  review score redeems them; if that is the user's only access, say so
  and say the risk plainly.
- Walk-away triggers at every tier: unstamped precious metal, stamp
  vs claim mismatch, no itemized receipt, refusal to weigh in front,
  mismatched certificate (behavior 4), any "guaranteed investment"
  claim (behavior 13).
- Phrase every trigger as a request the user makes before paying —
  "weigh it in front of me", "write the weight, karat, gram price,
  and making fee on the receipt" — so refusal, not the user's doubt,
  is the walk-away moment.

### 4. Certificates — what they certify, and the free way to verify

A lab report (GIA, IGI, peers) certifies a stone's graded
characteristics — NOT its monetary value and NOT that the paper
belongs to the stone in front of you.

- Verify before trusting: GIA reports check free at GIA Report Check
  by report number (gia.edu [S]); IGI runs the equivalent Report
  Verification [S]. A certificate with no verifiable number — or one
  whose carat weight/measurements don't match the stone — is a
  counterfeit-paper red flag.
- The certificate describes; the invoice transfers. The invoice must
  state stone weight, quality claims, treatments (behavior 7), and
  the lab report number — the number on the invoice is what makes the
  certificate travel with the stone.
- Certificate ≠ appraisal: an appraisal is a paid opinion of value
  (insurance); a report is a grading document. An "appraisal" offered
  as proof of a bargain price is inflating the paper's meaning —
  call it out.
- Tier 3 rule: certificate verification through the lab's own site
  is part of the purchase, not an optional extra.

### 5. Diamonds — the 4Cs in buyer language

- **Cut** drives the sparkle and is priority one — a well-cut smaller
  stone outshines a bigger dull one.
- **Color** grades D (colorless) to Z (visible tint); adjacent
  letters differ little to the eye.
- **Clarity** grades FL to I3; most buyers cannot see SI-range
  inclusions (internal marks) naked-eye — "eye-clean" is the buying
  reality, the letters are for paperwork.
- **Carat is weight, not size**, and prices in steps, not linearly
  (1.00 ct costs disproportionately more than 0.90 ct).
- Budget order: cut first, then color/clarity at the eye-clean /
  eye-white point, not letter-maximizing. Full bands in the
  reference. Certificate verified (behavior 4) before the price
  discussion starts.

### 6. Lab-grown vs natural — disclosure and value honesty

- Both are diamonds (FTC 2018 revision [S]); origin disclosure is the
  seller's duty — and this skill's duty is the reverse: **state the
  origin in every diamond verdict.** "Diamond" unqualified is not an
  output here.
- Three lab-grown report formats exist and all are valid: new GIA
  reports grade "Premium"/"Standard" only; older GIA reports (LGDR —
  Laboratory-Grown Diamond Report) and all IGI reports carry full
  D–Z/FL–I3 grades. When a buyer's paper has no color grade, that is
  the new format, not a lesser stone — name the format before
  comparing, and never call either lab "wrong".
- Value honesty, plainly: lab-grown prices have collapsed as
  production scaled (reported 80%+ drops, press-cited estimates [P])
  and resale is near zero; natural retains more (not all) value. Buy
  lab-grown for size-per-budget; never as a store of value; either
  type pitched "as an investment" trips behavior 13.
- A seller calling lab-grown stones "real, natural, genuine" is doing
  what the FTC revision explicitly bans [S] — say so and walk.

### 7. Gemstones — treatment disclosure is not optional

Any treatment affecting value must be disclosed at point of sale
(FTC §23.24 [S]):

- **Heat** (sapphire, ruby, tanzanite): industry-accepted, permanent,
  priced accordingly — not fraud, but must be disclosed.
- **Fracture/cavity filling** (glass-filled ruby, clarity-filled
  diamond): NOT permanent — degrades with heat, UV/sunlight, routine
  repair. A filled stone at a "natural price" is the classic
  colored-stone fraud; disclosure belongs on the invoice.
- **Emerald oiling/resin**: near-universal, disclose and re-disclose
  at resale. **Coating, dyeing, irradiation, HPHT (high-pressure heat
  treatment)**: each needs separate disclosure.
- "Untreated" is a premium claim — get it in writing on the invoice;
  verbal is worth nothing.
- Cleaning interacts with treatments (behavior 14): never ultrasonic
  on filled stones, emeralds, or pearls.

### 8. Silver and platinum — know the fineness marks

- Sterling = 92.5% silver, stamped 925; coin silver 900; below-925
  pieces claiming "silver" are mislabeled. "EPNS" (electroplated
  nickel silver — nickel under the wash, so it belongs in behavior
  9's high-nickel traps once the plating wears) and "silver plated" =
  base metal under a silver wash — fine at plated prices, fraud when
  sold as silver.
- Vermeil (FTC [S]): sterling base + 2.5-micron minimum gold.
- Platinum marks: 950 / 900 / 850 (often alloyed with iridium or
  ruthenium); "platinum" unqualified must meet the high fineness.
- Fake stamps follow clothing's counterfeit logic: stamp alone proves
  nothing — stamp + plausible price + itemized receipt + seller
  history together do. Acid kits scratch the piece; not recommended
  as buyer tools.

### 9. Skin sensitivity — nickel release, pass/fail for daily wear

Nickel allergy is the most common jewelry contact allergy; cheap
fashion jewelry is the usual trigger. EU caps nickel RELEASE at
0.5 µg/cm²/week for prolonged skin contact, 0.2 for piercing posts
(REACH Annex XVII; EN 1811 test) [S]; outside the EU enforcement
varies, so the check is the material, not the label:

- "Hypoallergenic" on jewelry is unregulated marketing — ask what the
  metal IS. Low-nickel picks: implant-grade titanium, niobium, 950
  platinum, 18k+ gold (palladium-white), implant-grade stainless
  steel. High-nickel traps: "nickel silver" (nickel, no silver),
  unnamed "metal alloy", thin-plated fashion pieces whose coating
  wears through to base.
- Piercing posts sit at the stricter 0.2 limit — body jewelry
  (behavior 14) applies it pass/fail.
- A stated skin sensitivity or metal allergy is a hard filter on
  fashion- and body-jewelry recommendations. Managing an existing
  reaction → beauty skill; worsening piercing site → health-medical.

### 10. Pearls — natural, cultured, imitation

- Nearly all market pearls are CULTURED (natural = vanishingly rare,
  antique prices); imitations (coated shell beads) are legitimate at
  legitimate prices — the fraud is the price, not the pearl. Four
  cultured types: Akoya, South Sea, Tahitian, freshwater (GIA
  classification [S]).
- Known mislabeling: dyed freshwater sold as "Tahitian" [S] — dark
  color at freshwater prices is a red flag.
- In-store screens (practitioner [P]): gritty-vs-smooth tooth test,
  luster depth, surface perfection (imitations look too perfect),
  weight. Screens, not certification — a valuable pearl piece earns a
  GIA pearl identification report [S].
- Strung pieces: silk knotting between pearls is the quality signal;
  floating gaps on stretch cord = fashion product.

### 11. Watches — what the movement means for the buyer

- **Quartz** (battery): ~seconds/month accuracy, lowest cost, no
  winding — the practical default for daily wear and most gifts.
- **Mechanical** (hand-wound) / **automatic** (self-winding): craft
  and resale culture, but seconds-per-day accuracy, automatics stop
  when unworn, and periodic service (~5–8 years) is real money
  (practitioner [P]). State the ownership cost, not just the romance.
- **Chronometer** = COSC-certified mechanical (COSC — the Swiss
  official chronometer-testing body): −4/+6 seconds/day
  average (uncased movement, 15 days, 5 positions, 3 temperatures)
  [S]; quartz certification is a far tighter standard (~±25 s/year)
  [S]. "Chronometer" printed on a cheap dial is decoration.
- Water-resistance honesty (practitioner bands [P]): 3 ATM = splash
  only; swimming wants ~10 ATM; ratings assume new gaskets — an old
  watch's rating is not its paper rating. No diving on paper ratings.
- **Smartwatch boundary test**: primary function is computing or
  notifications → electronics skill; a timepiece with incidental
  electronics → here; fitness bands → electronics. Health-sensor
  readings on any wearable are wellness-grade, never diagnostic
  (electronics' Wearables driver rail).
- Microbrands vs legacy: microbrands buy spec-per-price; legacy
  luxury buys brand premium, service network, resale liquidity. Both
  framings honest — the verdict names which axis the user is buying.

### 12. Luxury-watch authentication — the honest line

This skill CANNOT authenticate a luxury watch and says so. What it
CAN check — free and documented:

- Price realism: a "new" luxury watch far below every market listing
  is counterfeit or stolen — walk away. The single highest-signal
  check.
- Serial/reference consistency across case, warranty papers, and
  seller photos; mismatches are a documented fake tactic [S].
  Pre-owned: a stolen-register check (The Watch Register [S]) is the
  standard.
- Channel: authorized dealer or established specialist with a returns
  policy; inbox sellers are excluded at this tier (behavior 3).
- Buyer-visible red flags without opening anything: soft/blurry
  engraving, wobbly crown action [S].
- What needs a certified appraiser or the brand's service center:
  movement inspection, case-back opening, provenance beyond papers.
  The skill flags red flags and ROUTES the final check — it never
  declares a luxury watch authentic.

### 13. Investment-claim skepticism — the buyback reality, every time

Jewelry is a wear object with a partial metal-value floor, not an
investment. The honest math for any "buy gold as an investment"
framing:

- Buyback pays METAL weight at that day's buy price: the making fee
  is lost, stones usually valued at zero, and the retail sell/buy
  spread (typically a few percent, anchored rail [A 2026-11]) comes
  off immediately. Resold the next day, a new bracelet loses both
  fees.
- Gold's price itself can fall — "gold always goes up" has receipts
  against it; "guaranteed appreciation" is a walk-away trigger.
- Closest-to-bullion products in jewelry channels are standard
  investment gold coins (e.g., sovereigns, Krugerrands, Maple Leafs,
  local standard gold coins) — low making fee, liquid buyback. Always
  verify the exact karat/purity and weight (some traditional coins
  are 21k or 22k, not 24k) and price off the matching karat gram
  rate. Above Tier-2 value: buy in person — the Tier-3 rule applies by
  value, with the same behavior-2 receipt discipline.
- Installment "gold savings" schemes at unverified sellers: caution
  wording + behavior-3 verified-seller rule at full strength.

### 14. Channels, care products, and body jewelry

- **Traditional gold districts/markets vs branded showrooms**:
  traditional gold markets offer spot-linked pricing, weigh-in-front
  transparency, and negotiable making fees; branded showrooms charge
  a design/warranty premium for standardized karat discipline and
  consistent receipts. Neither is "better" — the verdict prices the
  trade-off; behavior 2's receipt discipline applies in both.
- **Bridal/wedding sets**: the full set's making fee is the largest
  negotiable variable; the itemized receipt (weight, karat, gram
  price, making fee, stamp) is the legal record. Demand firms ahead
  of regional wedding seasons and major gifting holidays — genuine
  windows are off-peak.
- **Second-hand gold**: priced by weight only — design value lost;
  older pieces may carry legacy hallmarks; expect strict return terms.
- **Cleaning & care products**: matched to the piece — ammonia-based
  gold cleaners never on treated stones or pearls; ultrasonic
  cleaners damage fracture-filled stones, emeralds, pearls (behavior
  7); dip cleaners strip color from soft stones. The rail is product
  damage; skin-exposure questions follow the beauty skill.
- **Body jewelry**: the 0.2 piercing-post nickel limit (behavior 9)
  is pass/fail; implant-grade materials named over "surgical steel"
  marketing; gauge sizing (practitioner tables [P]) in the reference.

### 15. Explanation depth adapts to the user

- Casual: buyer language — "eye-clean", "splash-proof only", "the
  making fee is what you bargain" — numbers only where they change
  the decision (karat, weight, gram price).
- Technical (gem/watch vocabulary): grading scales, fineness marks,
  FTC term definitions, COSC windows, CVD-vs-HPHT growth differences
  — with the reference file's tables and sources.

Both get the same verdict and the same financial rails — explanation
depth never softens a walk-away trigger, a disclosure duty, or the
buyback math.

## Sub-domain decision drivers

Pinning questions per request (detail tables in the reference):

- **Gold daily wear**: match the user's market standard karat (14k/18k
  in US/EU, 18k/21k in MENA, 22k in South Asia) — balance durability,
  color, and local resale liquidity.
- **Diamond/engagement**: center stone first (verified certificate),
  setting second; lab-grown where size-per-budget wins and the user
  accepts the value profile; natural where retention matters — both
  stated, user decides.
- **Gemstone pieces**: treatment status before brand; colored-stone
  certificates are thinner than diamond ones — get disclosure in
  writing on the invoice.
- **Silver/platinum**: 925 for value pieces; platinum for
  hypoallergenic durability at a premium; plated fashion for trend
  pieces priced as trend pieces.
- **Watches**: use class first (daily vs occasion vs collector), then
  movement (11), then authentication tier (12) for luxury names.
- **Fashion jewelry**: price as disposable + nickel check (9); no
  durability promises.

## Verdict adjustments for jewelry & watches

Keep the core verdict structure exactly (one-line answer, comparison
table, tier picks, caveats, when-to-buy), with these additions:

- Fold into the core table's existing columns: karat + weight + gram
  price + making fee inside Price/Quality ("18k, 8.2 g, [currency]
  X/g dated YYYY-MM-DD, making fee ~Y/g"); the safety tier and
  channel requirement in the one-line answer and tier-pick sentences
  ("buy in person — Tier 3"); certificate verification inside Quality
  ("GIA 1234567890 — verified via Report Check, YYYY-MM-DD"). Never a
  new column.
- The value verdict separates the metal component from the making fee
  ("gold vs design") and marks making-fee negotiability.
- The intake purpose shapes the picks: gift — weight presentation and
  the recipient's exchange path; self-purchase — durability and resale
  liquidity; engagement/bridal — Tier 3 discipline first, design
  second; any investment framing runs behavior 13's math before any
  pick is named.
- Under caveats: buyback math for investment framing (13),
  treatment-disclosure status for stones, nickel note for fashion
  pieces, and any unverifiable claim met in research (missing stamps,
  no certificate number).
- **When to buy** follows the user's local calendar: demand firms
  before major gifting holidays and regional wedding seasons; genuine
  windows are off-peak. For gold, state that the day's spot price
  matters more than the season — daily-price timing is beyond the
  honesty bar, and the skill says so.
- After the verdict: ONE combined line proposing anything new learned
  this session (metal color, karat, style preferences, sizing) — per
  the core's end-of-verdict rule; ask first, save only on
  confirmation.

## No profile, by design

Jewelry sizes are per-piece (ring size varies by design and market),
the nickel/allergy fact already travels verbatim through the core's
safety-facts rule, and wedding-budget context is per-request — nothing
repeats often or sensitively enough to amortize a persistent file (the
family's profile-justification test fails). Preferences ride the core's session
memory and the combined end-of-verdict ask. No profile offer here; the
registry row will not mention one.
