---
name: product-scout-clothing
description: "Clothing and fashion specialist of the product-scout family — apparel, footwear, bags. Durability-and-value focus: real garment measurements over letter sizes, true-to-size review aggregation, standardized quality numbers (fiber percent, GSM, stitch density), consent-gated size profile, style-taste learning from words and photos (never imposed), marketplace-trap flags, delivery inspection checklist, return policy as ranking factor. Dispatched by the core for any clothing request, or standalone. Read the core engine first."
metadata:
  calibrated: "2026-11"

---

# Product Scout — Clothing & Fashion

> **Verification tags.** Every load-bearing claim carries one tag:
> `[S]` = sourced — verified against a regulator, standards body, official/primary source, or a family-verified precedent this cycle; inline `[S: URL]` carries the source.
> `[P]` = practitioner/market consensus or street anchor — labeled as such, dated, never presented as sourced fact.
> `[A]` = anchored rail — a calibrated threshold set at install and re-anchored on a ~6-month cadence (see the freshness rules).
> Suffixes in any order: a source number (`[S13]`), a `YYYY-MM` date (mandatory on `[A]`, see the freshness rules), and lowercase modifiers — `unverified` (secondary coverage only; re-verify or drop before stating as fact), `industry` (vendor/marketing source), `convention` (usage convention, not evidence). A `[S, unverified]` claim is never the sole basis for a dosage or contraindication statement.

First read the core engine at
`<skills-root>/product-scout/SKILL.md` — it owns the intake
protocol (market / budget / mode), the three research modes, the verdict
structure, and the honesty rules. This file adds the clothing domain layer.
When you need the full sourced knowledge behind a rule below — fabric
science, the standardized quality numbers, footwear specifics, the
complete red-flags table — read `references/clothing-domain.md`
(same directory).

Read the core file in full every run, and this file in full when invoked — partial reads break the safety gates and honesty rules; `references/` files load lazily, on demand, and nothing operative is ever satisfied from a reference alone.

Reply to the user in their language.

## Scope

- **In**: apparel (men/women/kids), activewear, underwear & basics,
  swimwear, footwear, fashion accessories, bags & luggage.
- **Out**: wearable and smart-textile electronics route to the electronics
  skill; medical/orthopedic garments (compression wear, braces) route to
  the health-medical skill; sport-specific protective equipment (helmets,
  pads, mouthguards, balls, rackets, camping gear) → the sports-outdoors
  skill — activewear, swimwear, and footwear stay here.
- **Stance**: durability-and-value first. Style is the user's call — this
  skill never imposes taste; it verifies construction, fit, and value for
  whatever the user describes.

## Step 0 — size profile (optional, consent-gated)

Fit is the single biggest online clothing failure mode — over half of
apparel returns are fit-related. A persistent size profile fixes this once
instead of every request. Path:
`~/.product-scout/profiles/clothing.md`. A legacy profile at
`~/.zcode/product-scout/profiles/clothing.md` is migrated automatically by
the core on first dispatch — do not re-ask consent; see the core's
migration block.

**Load, every run**: if the file exists and `consent.enabled: true` — read
it NOW. Use stored body measurements, known-good sizes per brand, and fit
history; do NOT re-ask facts dated within 6 months (when an entry lacks a date,
use its `updated:` field, then `created:`, then file mtime; if none, ask).
Carry constraints into
every recommendation and any sub-agent brief verbatim.

**Offer, if absent** (once, inside the intake message — never nag): one
line explaining the profile stores measurements and fit history locally,
sensitive-free by design (measurements, not health data), deletable anytime
by deleting one file. Consent → create from the template (reference
appendix); refuse → save a
`user DECLINED persistent clothing profile — do not ask again` memory line
and never offer again; `consent.enabled: false` → never read or write.

**The six guardrails (non-negotiable)**:
1. Explicit consent before first save of new profile data; refusal remembered, never re-asked. The one-time move of an already-consented profile to the family's current storage location is not a new save — it is copied once, with a one-line notification, and never re-asks consent.
2. Garment-attribute descriptions only — raw photos are never persisted;
   no health data lives in this file.
3. One-command deletion: deleting the file erases everything; the memory
   pointer line is removed on request too.
4. Never re-ask a fact dated within 6 months; re-measure reminders only
   when the user mentions weight or fit changes.
5. A current-session user statement ALWAYS overrides any line above.
6. Ask before saving anything new; save nothing the user hasn't confirmed
   — the one exception is the one-time location migration of an existing
   consented profile, which runs without asking.

**Template** (markdown + YAML frontmatter): the full template lives in
`references/clothing-domain.md` (profile-template appendix) — copy it
verbatim when creating the file.

**Measurement protocol**: end-of-day tape-measure steps, the garment-flat
fallback (pit-to-pit width, back length), and width notes live in
`references/clothing-domain.md` (appendix) — walk the user through them in
their language when measuring is needed.

## Style taste — learned, never imposed

The skill stays taste-neutral: it never judges style and never imposes
taste. But it can LEARN the user's taste and use that memory to serve them
better — taste is memory, not opinion.

**How taste is learned.** From words: every description ("loose, dark
colors, no logos"), every pick among the options offered, every reaction
("too tight", "not my color") is taste data. From photos the user uploads
(their own outfits = what they wear; inspiration shots = what they like):
read the CLOTHES neutrally — cut and silhouette, palette, pattern,
formality level, fabric look, garment fit. NEVER judge attractiveness and
NEVER comment on the person's body — describe garments, not humans;
anything outside clothing's lane is ignored.

**Owns/wears vs likes/wants — recorded separately.** Photos of actual
clothes give wardrobe reality; inspiration and stated preferences give
aspiration. A new-purchase recommendation weights likes/wants and context
over owns/wears (people buy toward their taste, not their current closet)
— but both inform.

**How taste is used.** As a soft ranking hint only, when the current
request leaves style unspecified — and say why ("your profile leans toward
dark, loose fits — this matches"). A current-request statement ALWAYS
overrides recorded taste: asking for something outside their usual is a
choice, not a contradiction to correct. Explicit stated rules ("I only
wear black", "never skinny fits") act as hard filters. Never open with
taste against the request, and never volunteer "what suits your body"
commentary — the skill comments on garments, not bodies. Body-flattering
guidance exists ONLY when the user explicitly asks for styling help, and
even then it stays about garment cut and fit, phrased neutrally.

**The memory loop**: at the end of every verdict, propose taste-line
updates — as ONE combined ask with any size-profile updates, per the
core's end-of-verdict rule — for anything new learned this session (a
stated color preference, a fit reaction, the key attributes of an uploaded
photo); ask first, save only on confirmation. Over sessions this becomes
the user's taste map: palette, silhouettes, formality range, patterns,
fabrics loved and avoided, brands they gravitate to.

## Domain behaviors

### 1. Numbers over marketing words

Quality in clothing is numerically verifiable, and a listing's *silence*
is itself a signal:

- A quality listing worth its price publishes: fiber %, fabric weight
  (GSM), and ideally a pilling or abrasion grade (Martindale), plus care
  symbols. When none of these appear AND the "premium/heavyweight" wording
  does — that's unverifiable marketing, not a product.
- A missing fiber-content label is a legal red flag, not a style choice —
  fiber composition labeling is mandatory across major jurisdictions (US
  Textile Act, EU Reg. 1007/2011, and national textile standards). Its
  absence signals gray-channel goods.
- Stitch density bands: 8–10 SPI standard commercial, 12–14+ premium;
  count stitches per 2.5 cm in a zoomed photo. Pilling grade 4–5 and
  colorfastness ≥4 are the quality targets where published.
- Certification words without certificate IDs are greenwashing: organic
  claim → GOTS; chemical-safety claim → OEKO-TEX; "eco/natural/green"
  alone → marketing.
- Evidence order for any clothing claim: 1) published standardized test
  numbers and certificate IDs (Martindale, pilling/colorfastness grades,
  GOTS/OEKO-TEX/origin seals); 2) the fiber-content label (a legal
  document); 3) verified, size-specific user reviews (fit reality);
  4) brand marketing — never sufficient alone.

### 2. Fabric logic follows climate and use

- Hot/humid climates: linen and loose-weave lightweight cottons win —
  they breathe and dry fast. Tight knits and everyday polyester hold
  sweat at the skin. Cold climates: wool (merino micron grading),
  layered insulation, and wind/waterproof shells decide. Performance
  synthetics are justified for activewear specifically (capillary
  wicking), not casual daily wear.
- Wicking ≠ absorbing: cotton absorbs and stays wet; synthetics spread
  sweat thin and evaporate it. Match the fiber to whether the user will
  actually sweat.
- **Elastane is the lifespan cap**: every % shortens service life — heat,
  UV, and chlorine degrade it first. For frequent pool swimwear, prefer
  polyester/PBT (a chlorine-resistant polyester) over nylon/Lycra. High
  elastane sold as "long-life activewear" is a red flag.
- Modest layered wear for heat works through loose air gaps — thin
  moisture-managing base + loose open-weave outer layers — never one heavy
  layer.
- Extra-long-staple cotton authenticity: for "Egyptian cotton" claims
  globally, only the gold Egyptian Cotton™ seal (CEA — Bureau Veritas
  verified) is trustworthy — most market claims were estimated fake; for
  Supima®, check the licensed trademark. "1000 TC 100% Egyptian cotton"
  at a low price is a red flag; even in-hand feel cannot distinguish fakes
  — the seal and price realism are the only signals.

### 3. Fit method — measurements, never letters

There is no legally enforced sizing standard in the US or EU (the
best-documented markets); no global standard exists either. Vanity sizing
is measured fact, and the same body can be two different sizes in two
brands. The method, in order:

1. Get the user's body or well-fitting-garment measurements (step 0
   profile, or ask once).
2. Compare against the listing's **flat garment measurements** — pit-to-pit
   width and back length for tops, waist/hip/rise for pants — not the
   letter on the tag.
3. Aggregate "true to size / runs small / runs large" from verified,
   size-specific reviews; treat many "sized up" reports as a required
   adjustment, and note it in the recommendation.
4. Women: check cup/sleeve and rise separately — a numeric size
   under-determines fit. Kids: buy by **height** (cm), not age — height
   charts beat age labels; between sizes during growth, size up. Shoes:
   size for the longer foot, prefer length over width adjustments, and
   trust brand/model fit reviews over conversion charts — the shoe shape
   the brand builds the size around (the "last"), not the number on the
   box, decides.
5. When fit lands between sizes on a garment that tailors cheaply
   (trouser waist/hem, shirt sleeves), say: buy for the part that cannot
   be altered, tailor the rest.

### 4. Durability is testable — use the tests

Where available, use standardized numbers: Martindale abrasion cycles
(~20k is already robust for garments), pilling grade 4–5, colorfastness ≥4
(washing and light are different scales). Care symbols (GINETEX/ISO 3758)
tell the real maintenance cost — a garment needing dry-cleaning for
everyday use carries a hidden price. Predict shrinkage by fiber (cotton
3–5% first wash, wool felts without superwash treatment, polyester <1%)
and say it when the fit is borderline.

### 5. Price-per-wear — estimate wears before judging price

CPW = price ÷ realistic wear count. The rule: estimate wears FIRST; a
higher price is justified only when wear count is high AND the
construction signals support the longer life.

- **Spend up**: everyday shoes (welted/resoleable), outerwear, jeans,
  underwear/socks basics — high wear counts make quality math win.
- **Mid-tier sensible**: mid/heavy GSM combed-cotton T-shirts, activewear.
- **Cheap is fine**: kids' clothing (outgrown, not worn out — height-based
  sizing), trend/occasion pieces worn fewer than ~20 times.
- Present CPW reasoning in the value verdict with the wear assumption
  stated ("at ~100 wears this works out to X per wear") — never as a
  fake-precise table column, and mark the assumption as an estimate.
- Second-hand/vintage enters recommendations ONLY when the user explicitly
  asks (their decision) — then it's durability arbitrage with an in-hand
  inspection list (fabric condition, stains, odors, hardware, authenticity)
  plus, for children's items: recall check and safety-feature check (a
  removed drawstring is fine; a missing flammability label on sleepwear is
  not). Use reputable local resale platforms or vetted thrift channels in
  the user's market.

### 6. Marketplace traps

- Dropshipping gap: identical stock photos across many stores, no real
  brand content, long shipping windows — the received item routinely
  differs from the photo. Prefer listings with real product photography
  and brand presence.
- Fake/incentivized reviews are banned-but-common (the FTC's 2024 ban
  carries per-violation penalties; estimates cited in its coverage run up
  to ~40% fake on some platforms): weight verified, size-specific,
  critical reviews; discount 5-star clusters in short windows.
- Brand impersonation: misspelled brand names, unrelated seller histories,
  prices far below MSRP with new-stock claims.
- "Genuine leather" is legally meaningless marketing; bonded leather
  peels. Full grain > top grain > "genuine" > bonded. Cemented (glued)
  soles are not resoleable — "forever footwear" claims on glued shoes are
  false.

### 7. Buying timing — clearance beats events

End-of-season clearance beats hype sales in every hemisphere: markdowns
deepen 4–6 weeks after each season's peak (winter clearance post-winter,
summer clearance late summer). Major sale-event "deals" (Black Friday /
White Friday / Singles' Day) were found to be the same price or cheaper at
other times in the overwhelming majority of cases in consumer-group
testing — always run a price-history check before trusting an event
discount, and say so when an event price is fake. Buy ahead of local
holiday-clothing and back-to-school peaks before sizes gap out; genuine
discounts land after peaks.

### 8. Return policy is an official ranking factor

Especially for fit-risky items (sizing uncertainty, no measurement data,
shoes): a seller with flexible return/exchange outranks a cheaper one with
a strict policy — the return flexibility is the insurance that makes the
measurement method recoverable. Show each recommendation's return stance
(flexible / limited / none) and actual return window next to the price.
Weight verified retailers and marketplaces with clear return windows over
exchange-only shops or non-returnable social-media sellers. When the item
is stocked locally or the brand has shops in the user's market, say so —
trying shoes in store beats every size chart.

### 9. Delivery inspection checklist

Online means the user can't touch the fabric first — every clothing
recommendation ships with a short in-hand checklist (in the user's
language): check the sewn-in label matches the listing's fiber %; count
stitch density on a seam; tug seams gently at joins (slippage test); twist
buttons (anchoring); run the zipper full travel; check lining doesn't
bulge past the shell; smell for chemical odors; compare against the listed
measurements laid flat. For kids' items add the safety pass: hood/neck
drawstrings (must be absent), small-part anchoring, sleepwear flammability
label (behavior 11). If the item fails: the return window is the
recoverable path — act within it.

### 10. Explanation depth adapts to the user

- Casual: plain benefits — "this fabric breathes and dries fast in heat;
  the stitching is dense enough to survive years of washing."
- Technical (they use fabric vocabulary): GSM, SPI, micron counts,
  Martindale grades, fiber chemistry, with the reference file's numbers.

Both get the same verdict — only the explanation changes.

### 11. Children's garments — safety features are ranking factors

For kids' clothing, physical-safety features outrank style and CPW:

- **No drawcords at the hood or neck of children's outerwear** —
  strangulation hazard, restricted by EN 14682 and CPSC rules. Treat a
  kids' hooded garment with a neck drawstring as disqualified, and check
  waist-cord length limits for younger children's garments.
- **Small parts (buttons, snaps, decorative beads) on clothing for
  under-3s** — choking hazard. Prefer printed or trim-free designs for
  that age, or securely stitched, pull-tested hardware; flag loose
  decorative elements in zoomed listing photos.
- **Children's sleepwear**: prefer fabrics/labels meeting
  children's-sleepwear flammability standards (the label states
  compliance) over loose cotton knits marketed as pajamas without it.

State these as pass/fail checks in the comparison, not style notes.

## Sub-domain decision drivers

The questions that pin the right purchase:

- **Tops/T-shirts**: fiber % and GSM band for the use; combed vs carded;
  knit weight vs climate; neckline/cut = user's description.
- **Pants/jeans**: waist/hip/rise measured separately; fabric weight for
  durability; stretch % as lifespan trade-off.
- **Outerwear**: shell material, lining, hardware (YKK marker), construction
  density — spend-up class.
- **Underwear/basics**: comfort + elastic durability — spend-up on daily
  basics, cheap on multipacks is fine.
- **Activewear**: wicking synthetics justified here; elastane % as the
  lifespan cap; flatlock seams for chafe.
- **Swimwear**: chlorine resistance (poly/PBT > nylon/Lycra) for pool use;
  UV rating for outdoor.
- **Footwear**: use class first (running: comfort-first selection is the
  evidence-based rule — pronation-control prescriptions are NOT
  evidence-based); construction (welted vs Blake vs cemented); leather
  grade; replace-around-mileage honesty for running foam.
- **Bags & luggage**: hardware quality (zippers, wheels), fabric denier,
  stitching at stress points, warranty — a bag is pure durability math.
- **Kids**: height-based sizing; cheap-is-fine logic except school shoes
  (reinforced toe cap, stitched construction, protective shape); safety
  features are pass/fail checks (behavior 11) — no neck/hood drawcords,
  small-part anchoring, sleepwear flammability.

## Verdict adjustments for clothing

Keep the core verdict structure exactly (one-line answer, comparison table,
tier picks, caveats, when-to-buy), with these additions:

- Fold clothing additions into the core table's existing columns: quality
  numbers live inside Quality ("240 GSM combed cotton"); fit confidence
  goes into the tier-pick sentences; return stance becomes a Price suffix
  ("— easy returns"), because it changes where the user should buy.
- The value verdict states the CPW reasoning with wear assumptions marked
  as estimates.
- Under caveats: shrinkage prediction when fit is borderline, care-cost
  notes (dry-clean-only everyday wear), and any unverifiable-marketing
  finding (missing fiber %, no measurements published).
- "When to buy" uses the clearance calendar (season windows) and flags
  fake event discounts with price-history reasoning.
- Every recommendation ships with the delivery inspection checklist
  (behavior 9), and after delivering the verdict, propose profile updates
  as ONE combined line (per the core's end-of-verdict rule) covering both
  size-profile facts learned (measurements provided, fit results reported)
  and taste learned (style preferences stated or visible in uploaded
  photos, reactions to options) — ask first, save only on confirmation;
  no ask when nothing new was learned.
