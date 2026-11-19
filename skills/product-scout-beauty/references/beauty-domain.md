# Beauty & Personal Care — Domain Knowledge Base (AI Shopping Assistant)

> Family rule: where this file and the skill's SKILL.md disagree, SKILL.md's
> operative wording wins — thresholds, gates, and referral rules are stated
> authoritatively in SKILL.md; this file explains and sources them.

## Method note

- Scope: skincare, makeup, haircare, fragrance, men's grooming. Standard of rigor: claims traced to peer-reviewed dermatology literature, guideline bodies (AAD, ISO, SCCS/EU, FDA, national regulators) or named cosmetic-chemistry experts; consumer/brand sources used only for conventions (shade systems, fragrance tiers) and labeled as such.
- Research date: 2026-11-13. Verification status: all URLs retrieved via live web search this session; items that could not be traced to a primary source are marked **[unverified]** or **[industry source]** (marketing/consumer site, not independent).
- Global applicability: applies regulatory checks, channel safety, climate matching, and skin-of-color photoprotection across any market the user shops in.
- This file is decision-support knowledge, not medical advice; referral rules are in "Safety rails."

## 1. Active-ingredient science

| Active | Mechanism | Evidence level | Effective range | Key conflicts / cautions |
|---|---|---|---|---|
| Vitamin C (L-ascorbic acid) | Antioxidant; collagen synthesis support; tyrosinase inhibition (brightening) | Good (multiple RCTs; JCAD systematic review) | 10–20%; skin saturates ~20%, above it more irritation, no gain [1](https://pmc.ncbi.nlm.nih.gov/articles/PMC5605218) [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC7909477) [3](https://jcadonline.com/clinical-applications-of-vitamin-c-in-dermatology-a-systematic-review) | Unstable in water at neutral pH; needs pH ≲3.5, opaque/airless packaging; oxidizes with air/heat/light [4](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552410); do not stack with niacinamide *flush-era* myth — actually compatible (see §5) |
| Vitamin C derivatives (SAP, MAP, THD ascorbate, AA2G) | Convert to LAA in skin; more stable, less potent | Moderate (formulation studies) | SAP 1–5% usable at skin-neutral pH; THD ascorbate lipid-soluble, highly stable **[concentration evidence weaker than LAA — unverified specifics]** [1](https://pmc.ncbi.nlm.nih.gov/articles/PMC5605218) | Prefer LAA for max evidence; derivatives for sensitive skin / hot climates |
| Retinol | Converted to retinal→retinoic acid; regulates keratinization, collagen, pigment | Moderate for wrinkles (weak-to-mild per systematic review) [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC8675340) | 0.1% entry; 0.3% ≈ sweet spot (≈1% efficacy, better tolerated; Mellody 2022) **[no direct URL retrieved — unverified]**; 0.1% vehicle-controlled improvement wks 4–12 [6](https://pmc.ncbi.nlm.nih.gov/articles/PMC11344648) | Retinization (redness/flaking) and "purging" (~4 wks); start 2×/week [6](https://pmc.ncbi.nlm.nih.gov/articles/PMC11344648) |
| Retinaldehyde (retinal) | One conversion step from retinoic acid | Moderate; less irritating than tretinoin, better efficacy/tolerability balance among OTC retinoids [7](https://pmc.ncbi.nlm.nih.gov/articles/PMC2699641) [8](https://pmc.ncbi.nlm.nih.gov/articles/PMC8750127) | 0.05–0.1% typical OTC **[range: industry convention — unverified]** | Same photosensitivity rules; more potent than retinol |
| Adapalene 0.1% (gel) | Synthetic retinoid, RAR-β/γ selective | Strong (Rx-grade trials); only retinoid switched OTC (US, Differin 2016) [8](https://pmc.ncbi.nlm.nih.gov/articles/PMC8750127) [9](https://pmc.ncbi.nlm.nih.gov/articles/PMC9618501) | 0.1% OTC; 0.3% Rx | Less irritant than tretinoin (Brand 2003, PMID 12963899); proven stable with benzoyl peroxide (Epiduo) [10](https://pmc.ncbi.nlm.nih.gov/articles/PMC2958193) |
| Tretinoin 0.025–0.1% | Active retinoic acid | Strongest (decades of RCTs) [7](https://pmc.ncbi.nlm.nih.gov/articles/PMC2699641) | Rx-only in most jurisdictions (see Safety rails) | Pregnancy contraindication; max irritation in class |
| Glycolic acid (AHA) | Smallest AHA; dissolves corneocyte bonds; dermal effects at higher use | Good (multiple reviews/RCTs) [11](https://pmc.ncbi.nlm.nih.gov/articles/PMC11268769) [12](https://www.mdpi.com/2079-9284/10/5/131) | Leave-on 5–10% home use **[convention]**; efficacy is pH- and free-acid-dependent: at pH 3, 24-h absorption of 5% cream 27% vs 3.5% at pH 7 [13](https://labmuffin.com/fact-check-friday-why-does-ph-matter-for-ahas-and-bhas) | Most irritating AHA; over-exfoliation risk; raise sparingly |
| Lactic acid (AHA) | Same, larger molecule, NMF component → hydrating | Good; slightly better tolerated than glycolic [14](https://pubmed.ncbi.nlm.nih.gov/19245467) [11](https://pmc.ncbi.nlm.nih.gov/articles/PMC11268769) | 5–12% leave-on **[convention]** | Preferred for dry/sensitive |
| Salicylic acid (BHA) | Lipid-soluble; comedolytic, anti-inflammatory | Conditional (low-quality evidence) per AAD 2024 — weaker than BP but recommended for comedonal acne [15](https://www.aad.org/member/clinical-quality/guidelines/acne) | 0.5–2% OTC ceiling (US/many markets) | Pregnancy: ≤2% topical accepted by most guidance [16](https://www.aad.org/public/everyday-care/skin-care-secrets/routine/pregnancy-skin-care); avoid high-% peels in pregnancy |
| Niacinamide | Precursor of NAD/NADP; anti-inflammatory, sebum reduction, barrier ceramide synthesis, pigment transfer inhibition | Good (RCTs): 4% ≈ clindamycin 1% in acne [17](https://pmc.ncbi.nlm.nih.gov/articles/PMC3142702); 5% + 2.5% BPO > BPO alone [18](https://pmc.ncbi.nlm.nih.gov/articles/PMC8594539) | 2–5% evidenced for acne/barrier; >10% adds little and may flush **[upper range: convention — unverified]** | Very low conflict; good "universal" active |
| Azelaic acid | Anti-inflammatory, antimicrobial, anti-tyrosinase; C. acnes & M. furfur | Good: systematic review — 15%/20% > vehicle for rosacea, acne, melasma; often equivalent to comparators [19](https://pubmed.ncbi.nlm.nih.gov/37550898) [20](https://pmc.ncbi.nlm.nih.gov/articles/PMC11512533) | 10% OTC (US), 15–20% (Rx/OTC by market) | Best tolerability choice in pregnancy-era pigmentation plans (with derm OK) |
| Peptides (signal peptides, e.g., palmitoyl pentapeptide-4 / Matrixyl) | Signal fibroblasts → collagen | Weak-to-moderate: best-studied cosmetic peptide class; controlled studies show modest wrinkle reduction (e.g., Matrixyl 3000 −14% roughness/56 d — [industry-funded figure]) [21](https://pmc.ncbi.nlm.nih.gov/articles/PMC11762834) [22](https://www.sciencedirect.com/science/article/pii/S1773224723009395) | Manufacturer-specific **[often undisclosed — treat claims as marketing]** | Safe; cannot replace retinoids |
| Ceramides (barrier lipids) | Replace deficient stratum-corneum lipids; reduce TEWL | Good: clinical reports in AD; hydration +26%, TEWL −15% vs comparator in RCT [23](https://pmc.ncbi.nlm.nih.gov/articles/PMC9293121) | Formulation-dependent (1:1:1:1 lipid ratio is the classic design) **[ratio: patent/industry — unverified]** | None; core of barrier repair |
| Hyaluronic acid | Humectant/film; MW determines depth: <100 kDa penetrates, >1,000 kDa stays on surface [24](https://pmc.ncbi.nlm.nih.gov/articles/PMC12731180) | Moderate | Multi-weight blends; apply on damp skin, seal with occlusive | In dry air can pull water from skin if not sealed **[mechanistic consensus — unverified]** |
| Zinc oxide / titanium dioxide (mineral filters) | Broad UVB+UVA; ZnO broadest; photostable; modern nano forms mostly *absorb* UV, not reflect [25](https://www.ncbi.nlm.nih.gov/books/NBK587270) [26](https://www.bbc.com/future/article/20250718-which-kind-of-sunscreen-should-you-use) | Strong (GRASE — only 2 filters so classified by FDA) [27](https://www.fda.gov/drugs/understanding-over-counter-medicines/questions-and-answers-fdas-regulatory-actions-over-counter-sunscreen) | US: up to 25% each (monograph cap) | White cast (high depths); ideal for sensitive/rosacea/post-procedure |
| Chemical filters (avobenzone, octocrylene, etc.) | Absorb UV; avobenzone UVA but photounstable without stabilizers | Strong protection data; safety "more data needed": FDA 2019 proposed rule — only ZnO/TiO2 GRASE; oxybenzone etc. pending; systemic plasma absorption above threshold (Matta, JAMA 2020) but absorption ≠ demonstrated harm [27](https://www.fda.gov/drugs/understanding-over-counter-medicines/questions-and-answers-fdas-regulatory-actions-over-counter-sunscreen) [28](https://jamanetwork.com/journals/jama/fullarticle/2759002) | Per monograph caps | Endocrine questions (oxybenzone) unresolved [29](https://www.ewg.org/sunscreen/report/the-trouble-with-sunscreen-chemicals); EU filters (Tinosorb S/M, Uvinul A+) more photostable **[industry/regulatory consensus]** |

Known pairing conflicts:

- Retinol + AHA/BHA same session: compounding irritation and barrier damage — separate nights. **[expert consensus, not RCT — see retinoid irritancy review]** [6](https://pmc.ncbi.nlm.nih.gov/articles/PMC11344648)
- Benzoyl peroxide + retinol: BP is an oxidizer; classic teaching says it degrades retinol (not adapalene). Direct study found **no degradation of tretinoin 0.05% gel** with BP (Del Rosso 2010) [10](https://pmc.ncbi.nlm.nih.gov/articles/PMC2958193); still, simplest safe default: BP morning, retinoid night.
- Vitamin C + niacinamide: compatible (the "flush" came from 1960s raw-ingredient heat; modern formulas fine). **[expert consensus, Lab Muffin]** [30](https://labmuffin.com/fact-check-friday-why-does-ph-matter-for-ahas-and-bhas)
- Copper peptides + strong acids/vitamin C: theoretical incompatibility; **[unverified — no RCT]**.

## 2. Skin-type matching & safety

- Oily/acne-prone: gel-lotion vehicles, BP (strong AAD recommendation) + retinoid cores [15](https://www.aad.org/member/clinical-quality/guidelines/acne); niacinamide for sebum [17](https://pmc.ncbi.nlm.nih.gov/articles/PMC3142702); non-soap syndet cleansers.
- Dry: cream/ointment vehicles (AAD: ointments seal moisture best, lotions for oily/humid) [31](https://www.aad.org/public/everyday-care/skin-care-basics/dry/pick-moisturizer); ceramide-based [23](https://pmc.ncbi.nlm.nih.gov/articles/PMC9293121); syndet bars pH ~5.5 vs soap pH 9–11 [32](https://pmc.ncbi.nlm.nih.gov/articles/PMC8954092).
- Sensitive/rosacea: fragrance-free (not "unscented") per AAD; NRS survey trigger rankings — alcohol 66%, witch hazel 30%, fragrance 30%, menthol 21% [33](https://www.aad.org/public/diseases/rosacea/triggers/tips) [34](http://www.rosacea.org/patients/skin-care-and-cosmetics); mineral sunscreen preferred; azelaic acid 15% has rosacea evidence [19](https://pubmed.ncbi.nlm.nih.gov/37550898).
- Combination: split-zone strategy (rich cream dry zones, gel T-zone); avoid full-face AHA daily.
- Melasma-prone / skin of color: PIH risk from *any* inflammation — prioritize low-irritation actives and strict photoprotection; melanin-rich (Fitzpatrick III–VI) skin disproportionately affected [35](https://pmc.ncbi.nlm.nih.gov/articles/PMC2921758) [36](https://skinofcolorsociety.org/discover-patients-public/public-education/pih). In high-UV regions, photoprotection is the foundation of all melasma therapy; triple cream (HQ 4%/tretinoin/fluocinolone) is Rx first-line; azelaic 20% > vehicle in melasma [38](https://www.aad.org/public/diseases/a-z/melasma-treatment) [39](https://pmc.ncbi.nlm.nih.gov/articles/PMC5724303) [19](https://pubmed.ncbi.nlm.nih.gov/37550898). Tinted/mineral SPF defends against visible light, which triggers melasma [38](https://www.aad.org/public/diseases/a-z/melasma-treatment).
- Patch-testing protocol: AAD method — quarter-sized spot twice daily for 7–10 days on non-face skin; test one new product at a time [40](https://www.aad.org/public/everyday-care/skin-care-secrets/prevent-skin-problems/test-skin-care-products). Fast 24/48/72-h forearm check catches immediate reactions only; delayed allergy can appear after 1–2 weeks **[consumer guidance consensus]** [41](https://www.theinkeylist.com/blogs/news/why-do-i-need-to-do-a-patch-test).
- Fragrance is the top cosmetic allergen: EU mandates declaration of 26 fragrance allergens (>0.001% leave-on / >0.01% rinse-off), expanded to >80 entries by Regulation (EU) 2023/1545 (compliance: 31 Jul 2026 new products / 2028 existing) [42](https://eur-lex.europa.eu/eli/reg/2023/1545/oj) [43](https://single-market-economy.ec.europa.eu/sectors/cosmetics/cosmetic-products-specific-topics/fragrance-allergens-labelling_en).
- Pregnancy: stop all topical retinoids (incl. retinol cosmetics, adapalene) once pregnant; ≤2% salicylic acid widely accepted, high-%/peel-grade avoided; azelaic acid and low-strength glycolic/lactic commonly recommended substitutes [44](https://www.aad.org/public/diseases/acne/derm-treat/pregnancy) [16](https://www.aad.org/public/everyday-care/skin-care-secrets/routine/pregnancy-skin-care) [45](https://pmc.ncbi.nlm.nih.gov/articles/PMC9823189) [46](https://pmc.ncbi.nlm.nih.gov/articles/PMC3114665). Benzoyl peroxide: guidance split — some conservative sources avoid **[unverified as formal ACOG position]** [16](https://www.aad.org/public/everyday-care/skin-care-secrets/routine/pregnancy-skin-care).

## 3. Claims vs regulation

| Claim | Legal reality | What it does NOT mean |
|---|---|---|
| "Hypoallergenic" | No federal standard; "means whatever a particular company wants it to mean" (FDA) [47](https://www.fda.gov/cosmetics/cosmetics-labeling-claims/hypoallergenic-cosmetics) | Tested for low allergy; won't cause reactions |
| "Dermatologically tested" | Unregulated claim; no required protocol/result disclosure **[FDA labeling-claims framework: FDA does not pre-approve claims]** [48](https://www.fda.gov/cosmetics/cosmetics-labeling/cosmetics-labeling-claims) | Dermatologist-approved, or tested on 100 people, or effective |
| "Non-comedogenic" | No FDA-recognized test standard **[expert/legal analyses]** [49](https://pmc.ncbi.nlm.nih.gov/articles/PMC8954092) (see also FDA allergens page caveat) [50](https://www.fda.gov/cosmetics/cosmetic-ingredients/allergens-cosmetics) | Pore-safe for everyone; rabbit-ear assays are poor predictors **[unverified as formal position]** |
| "Clinical" | Undefined in cosmetics; signals only that the brand ran some study, often uncontrolled/industry-run **[unverified — consumer-law commentary]** | Peer-reviewed, controlled, or replicated |
| "Clean / natural" | No legal definition anywhere; brand-defined exclusion lists; greenwashing risk [51](https://www.dermatologytimes.com/view/social-media-mythbusters-clean-skin-care) [52](https://erleia.com/pages/what-is-clean-beauty) | Safer, non-toxic, or environmentally regulated |
| Cruelty-free logo | Depends on certifier: Leaping Bunny = fixed cut-off date + supplier monitoring + audits + annual recommitment (gold standard); PETA = signed corporate statement only [53](https://www.leapingbunny.org/Web/Web/content/standard.aspx) [54](https://www.crueltyfreekitty.com/cruelty-free-101/leaping-bunny-vs-peta) | PETA logo = audited supply chain |

- SPF/UVA systems: labeled SPF is an in-vivo human test (ISO 24444:2019) [55](https://www.iso.org/standard/72250.html); UVA-PF via ISO 24442/24443; Asian PA grades map to PPD (PA++++ = PPD ≥16) **[grading mapping — unverified table]**; EU requires UVA-PF ≥ 1/3 of SPF; UK Boots stars = UVA:UVB ratio (5★ ≈ 90%+) **[ratio table — unverified]** [56](https://blog.ansi.org/ansi/iso-24444-2019-in-vivo-determination-of-spf). Reality check: consumers apply 20–50% of the 2 mg/cm² test dose, so real-world SPF is a fraction of the label; ~20–60% of regular users never reapply [57](https://pmc.ncbi.nlm.nih.gov/articles/PMC7759112) [58](https://www.sciencedirect.com/science/article/pii/S0278691523004957). Australia's 2025 "sunscreengate" showed some retail-tested SPFs miss their labels [59](https://www.tga.gov.au/resources/explore-topic/sunscreens/sunscreen-spf-testing-information-consumers).
- Cosmetic vs drug boundary: intent-based in major regulatory systems (US FDA, EU, UK, Australia, etc.). "Moisturizes/cleanses/beautifies" = cosmetic; "treats acne/dandruff, antiperspirant, SPF" = OTC drug/quasi-drug claims [60](https://www.fda.gov/cosmetics/cosmetics-laws-regulations/it-cosmetic-drug-or-both-or-it-soap) [61](https://www.fda.gov/cosmetics/cosmetics-laws-regulations/cosmetics-us-law). Skin-lightening claims push a product toward drug territory; FDA states there are no FDA-approved OTC skin-lightening products [62](https://www.fda.gov/consumers/skin-facts-what-you-need-know-about-skin-lightening-products/skin-product-safety).
- National notifications: check the user's market regulatory system (e.g., EU CPNP, US MoCRA, UK SCPN, or national cosmetics notification portals) when verifying compliance.

## 4. Counterfeit & channel safety

- Prevalence: UK IPO found toxic substances (mercury, lead, arsenic, methanol) in 40% of seized counterfeit beauty products; press investigations report very high fake rates on open marketplaces ("over 65%" per The Times, 2025 — treat figure as press estimate, not audited stat) [67](https://www.gov.uk/government/news/ipo-campaign-launched-as-toxins-found-in-counterfeit-beauty-products) [68](https://observer.co.uk/news/business/article/the-toxic-cost-of-counterfeit-beauty-products) [69](https://www.thetimes.com/life-style/beauty/article/cosmetics-sold-online-amazon-ebay-fake-2zvj3sdk9).
- Verification: buy from licensed pharmacies, authorized beauty retailers, and official brand storefronts; check batch codes/QR with brand channels.
- PAO symbol (open jar, "12M") = safe-use window after first opening; used when shelf life >30 months, otherwise printed expiry; derived from stability + preservative-efficacy (challenge) testing [71](https://www.certifiedcosmetics.com/product/common-tests/period-after-opening-pao-test).
- Storage: L-ascorbic acid oxidizes fastest in water at near-neutral pH and with air/light/heat — choose opaque/airless packaging, store cool & dark, discard when dark orange/brown [4](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552410) [72](https://www.phyto-c.com/blogs/news/oxidized-vitamin-c-serum-color-guide).

## 5. Common mistakes & red flags

- "Natural = safe": oxidized fragrance terpenes are potent allergens — linalool/limonene autoxidize on air exposure into hydroperoxides; ~4.7% of patch-tested dermatitis patients react to oxidized linalool [74](https://pmc.ncbi.nlm.nih.gov/articles/PMC6587870) [75](https://pubmed.ncbi.nlm.nih.gov/12084079) [76](https://dermnetnz.org/topics/hydroperoxides-of-limonene-and-linalool).
- Over-exfoliation: daily acids/scrubs strip barrier lipids → stinging, persistent tightness, redness, reactivity; fix by stopping all exfoliants and rebuilding with ceramide moisturizer + SPF [77](https://pmc.ncbi.nlm.nih.gov/articles/PMC5608132) [78](https://blog.dermaquestclinical.com/signs-of-over-exfoliation-and-how-to-fix-it).
- Undisclosed concentrations: INCI lists are descending-order above 1% only; below the "1% line" order is free, so "0.5% retinol" claims may hide trace amounts **[INCI rule is law; enforcement of actives claims varies — unverified per-market]** [79](https://www.cosmebio.org/en/reports/INCI-list-how-to-read-ingredient-list-cosmetics).
- Whitening/bleaching dangers (documented global harm): unregulated lightening creams contain unsafe hydroquinone or mercury levels → irritation, rebound, exogenous ochronosis; international survey found 67% of lightening-cream users were treating PIH/melasma/acne; FDA warns OTC lighteners may contain undeclared hydroquinone or mercury [80](https://pmc.ncbi.nlm.nih.gov/articles/PMC12335261) [81](https://www.sciencedirect.com/science/article/pii/S2352647520301416) [62](https://www.fda.gov/consumers/skin-facts-what-you-need-know-about-skin-lightening-products/skin-product-safety). Topical-steroid whitening creams: documented misuse harm (steroid-dependent skin, rebound) [82](https://doctorabad.com/uptodate/d/topic.htm?path=topical-skin-lightening-agents-complications-associated-with-misuse).
- Hydroquinone status: reclassified by FDA as not-GRASE-for-OTC under the CARES Act reforms (2020) → US OTC removal; 4% now prescription-only (Tri-Luma is the sole FDA-approved HQ combo, short-term use) [83](https://practicaldermatology.com/topics/pigmentary-disorders/hydroquinone-in-2021/23592) [84](https://www.fda.gov/drugs/drug-safety-communications/fda-works-protect-consumers-potentially-harmful-otc-skin-lightening-products).
- Influencer-hype traps: single-influencer "holy grail" claims, before/after filters, uncontrolled n=1 "clinical" studies; counter with the evidence hierarchy (§6). Retinol "purging" beyond ~8 weeks or true cystic flares = stop/refer, not push through **[expert consensus]**.
- Banned ingredients to screen for: mercury compounds in skin creams, unsafe HQ levels, banned colorants — flagged via UK IPO seizures, FDA warnings [67](https://www.gov.uk/government/news/ipo-campaign-launched-as-toxins-found-in-counterfeit-beauty-products) [62](https://www.fda.gov/consumers/skin-facts-what-you-need-know-about-skin-lightening-products/skin-product-safety).

## 6. Evidence hierarchy & trusted sources

Tier order for verifying any product decision (most → least reliable):

1. **Peer-reviewed dermatology / guidelines** (JAAD, PMC/PubMed RCTs & systematic reviews, AAD, ISO, SCCS, FDA/national regulators): tells you mechanism, effect size, safety, regulatory caps. Rarely names specific SKUs.
2. **Guideline summaries & expert reviews** (AAD patient pages, DermNet, Skin of Color Society, NRS): same science, patient-usable framing.
3. **Qualified cosmetic chemists / science communicators** — Dr. Michelle Wong (Lab Muffin, chemistry PhD; myth-busting against peer-reviewed sources) and Stephen Alain Ko (KindofStephen, formulator; formula/ingredient mechanics): tell you formulation logic, pH, packaging, myth-vs-fact. Not primary evidence; use to interpret tier 1 [85](https://labmuffin.com/fact-check-friday-why-does-ph-matter-for-ahas-and-bhas) [86](https://kindofstephen.com).
4. **Ingredient databases** (INCIDecoder, CosDNA): parse INCI, flag comedogenic/irritancy citations, expose "1% line" — but they cannot see real concentrations, formula interactions, or extract potency; CosDNA irritancy scores are low-quality proxies [87](https://incidecoder.com) [88](https://cosdna.com) [79](https://www.cosmebio.org/en/reports/INCI-list-how-to-read-ingredient-list-cosmetics).
5. **Aggregated user reviews**: texture, shade-range, real-use failure modes; no efficacy signal beyond placebo.
6. **Brand marketing / influencer content**: tells you positioning and price, nothing verified about performance.

## 7. Sub-domain decision drivers

Decision logic = the 5–8 questions that pin the right SKU. "Concentration check" means inspect INCI position/claim; "actives check" means map against §1.

**Cleanser**
1. Skin type/condition (dry → cream/syndet, oily → gel, rosacea → fragrance-free syndet) [32](https://pmc.ncbi.nlm.nih.gov/articles/PMC8954092) [33](https://www.aad.org/public/diseases/rosacea/triggers/tips).
2. pH/surfactant class (soap pH 9–11 vs syndet ~5.5 — pick syndet) [32](https://pmc.ncbi.nlm.nih.gov/articles/PMC8954092).
3. Active need (BP 2.5–10% wash for trunk acne; salicylic 2% for comedones) [15](https://www.aad.org/member/clinical-quality/guidelines/acne).
4. Wears makeup/SPF daily? (needs true removal, but double-cleansing with surfactants twice = over-stripping **[expert consensus]**).
5. Fragrance/allergen load.

**Moisturizer**
1. Vehicle by skin type: ointment (very dry), cream (daily dry), lotion/gel (oily/humid) [31](https://www.aad.org/public/everyday-care/skin-care-basics/dry/pick-moisturizer).
2. Barrier actives: ceramides [23](https://pmc.ncbi.nlm.nih.gov/articles/PMC9293121), glycerin, petrolatum, dimethicone [31](https://www.aad.org/public/everyday-care/skin-care-basics/dry/pick-moisturizer).
3. Actives compatibility (rich creams buffer retinoid irritation — commonly recommended **[expert consensus]**).
4. Fragrance/dyes (avoid for sensitive) [31](https://www.aad.org/public/everyday-care/skin-care-basics/dry/pick-moisturizer).
5. Face vs body grading; climate (hot/humid → lighter; cold/dry → richer).

**Serum (by goal)**
- Brightening: LAA 10–20% or azelaic 10–20%; THD/SAP derivatives if heat/light exposure is uncontrolled [1](https://pmc.ncbi.nlm.nih.gov/articles/PMC5605218) [19](https://pubmed.ncbi.nlm.nih.gov/37550898).
- Anti-acne: niacinamide 2–5%, azelaic 10–15%; Rx tier = adapalene/clindamycin [17](https://pmc.ncbi.nlm.nih.gov/articles/PMC3142702) [19](https://pubmed.ncbi.nlm.nih.gov/37550898).
- Anti-aging: retinol 0.1–0.3% (start), retinaldehyde, peptides as adjunct [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC8675340) [7](https://pmc.ncbi.nlm.nih.gov/articles/PMC2699641) [21](https://pmc.ncbi.nlm.nih.gov/articles/PMC11762834).
- Barrier: ceramides, multi-weight HA, panthenol; fragrance-free [23](https://pmc.ncbi.nlm.nih.gov/articles/PMC9293121) [24](https://pmc.ncbi.nlm.nih.gov/articles/PMC12731180).
- Cross-checks: patch test [40](https://www.aad.org/public/everyday-care/skin-care-secrets/prevent-skin-problems/test-skin-care-products); pregnancy screen (§ Safety rails).

**Sunscreen**
1. Skin type: oily → gel/fluid; dry → cream; sensitive/rosacea/melasma/post-procedure → mineral (ZnO/TiO2) [27](https://www.fda.gov/drugs/understanding-over-counter-medicines/questions-and-answers-fdas-regulatory-actions-over-counter-sunscreen) [34](http://www.rosacea.org/patients/skin-care-and-cosmetics).
2. Broad-spectrum proof: SPF 30+, EU UVA logo or PA++++ (PIH/melasma need strong UVA protection) [55](https://www.iso.org/standard/72250.html).
3. Cosmetic elegance (white cast vs depth of skin tone — drives adherence) **[expert consensus]**.
4. Context: daily UV index; reapplication reality (2–3× during outdoor exposure; most users never reapply) [57](https://pmc.ncbi.nlm.nih.gov/articles/PMC7759112) [58](https://www.sciencedirect.com/science/article/pii/S0278691523004957).
5. Water resistance if swimming; fragrance-free if reactive.

**Makeup — foundation**
1. Depth (fair→rich): match jawline/neck in daylight **[industry convention]** [89](https://www.maybelline.com/makeup-tips/face/face-makeup-tutorials-for-beginners/how-to-find-a-foundation-shade-for-your-skin-tone).
2. Undertone: warm (golden/yellow), cool (pink), neutral, olive (green-grey cast, its own axis) [90](https://janeiredale.com/blogs/makeup-blog/how-to-match-foundation-to-undertone) [91](https://color-analysis.app/blog/foundation-for-olive-skin-guide).
3. Skin-type finish: oily → matte/serum-light; dry → dewy/cream; textured → breathable skin-finish **[industry convention]**.
4. Coverage need (sheer→full) and SPF content (bonus, not replacement).
5. Shade range availability (brands with 30+ shades); fragrance/acne-safety of formula.
6. Undertone × depth matrix is the reliable two-axis system; single-axis "tone" charts fail for olive/deep skin [91](https://color-analysis.app/blog/foundation-for-olive-skin-guide).

**Haircare**
1. Scalp type first (oily/dry/flaky ≠ hair length): dandruff/seborrheic dermatitis → Zn-pyrithione 1% (where permitted) or ketoconazole 2% (superior in severe cases, RCT) [92](https://pubmed.ncbi.nlm.nih.gov/12476017/).
2. Hair damage state: broken/stretchy → protein (hydrolyzed keratin); dry/brittle → moisture; alternate to avoid protein overload (hard, brittle) **[expert consensus — no RCTs]**.
3. Styling/heat load → heat protectants, silicone polish vs volume.
4. Wash frequency + local water hardness (hard-water mineral buildup).
5. Sulfate need: sulfate-free milder but less effective on heavy silicone buildup **[expert consensus]**.

**Fragrance**
1. Concentration tier: EDC ~1–5% (1–3 h) < EDT 5–15% (3–4 h) < EDP 15–20% (4–8 h) < Extrait 20–40% (8 h+) — higher = longer longevity, not necessarily louder sillage (extraits often sit close) **[tier table: industry convention across houses]** [93](https://delacourte.com) [94](https://www.scerto.com).
2. Climate: heat amplifies projection → lighter/cleaner profiles; cold dampens projection → richer bases.
3. Note family vs occasion (citrus/fresh day, woody/amber evening, gourmand cold weather) **[industry convention]**.
4. Longevity vs sillage preference; skin chemistry variability.
5. Authenticity channel: testers sold loose = counterfeit risk; buy sealed, authorized [67](https://www.gov.uk/government/news/ipo-campaign-launched-as-toxins-found-in-counterfeit-beauty-products).

**Men's grooming — shaving/beard**
1. PFB/ingrown tendency (curly hair, darker skin): electric shaver/trimmer over blade razor; single sharp blade; with the grain; never dry; AAD tips [95](https://dermnetnz.org/topics/pseudofolliculitis-barbae) [96](https://www.aad.org/public/everyday-care/skin-care-basics/hair/razor-bump-remedies) [97](https://jamanetwork.com/journals/jamadermatology/fullarticle/2791583).
2. Skin sensitivity: sensitive → electric, fragrance-free shave cream, alcohol-free aftershave.
3. Beard care: beard-specific cleanser + leave-in conditioner/oil for coarse hair; dandruff-style scale under beard = seborrheic → ketoconazole [92](https://pubmed.ncbi.nlm.nih.gov/12476017/).
4. Equipment: razor (closest, most irritation) vs electric (safest for PFB) vs safety razor (advanced technique) [95](https://dermnetnz.org/topics/pseudofolliculitis-barbae).
5. Persistent PFB: refer (Rx retinoid/BPO combos, laser) [96](https://www.aad.org/public/everyday-care/skin-care-basics/hair/razor-bump-remedies).

## Evidence hierarchy — summary table

| Tier | Source type | Reliably tells you | Never trust it for |
|---|---|---|---|
| 1 | Peer-reviewed derm lit + AAD/ISO/FDA/SCCS | Mechanism, effect sizes, safety, legal caps | Which specific SKU to buy |
| 2 | DermNet, NRS, SoCS, guideline patient pages | Usable interpretation of tier 1 | Product choice |
| 3 | Lab Muffin, KindofStephen | Formulation logic, pH, packaging, myth-busting | Primary evidence |
| 4 | INCIDecoder, CosDNA | INCI parsing, allergen/comedogen flags, 1% line | True concentrations, interactions, efficacy |
| 5 | User reviews | Texture, shade range, failure modes | Efficacy, safety |
| 6 | Brand/influencer marketing | Price, positioning, availability | Anything performance-related |

## Red-flags checklist (summary table)

| Flag | Why it matters | Action |
|---|---|---|
| Whitening/bleaching creams (HQ, steroids, mercury, "fast results") | Ochronosis, steroid damage, heavy-metal poisoning [80](https://pmc.ncbi.nlm.nih.gov/articles/PMC12335261) [62](https://www.fda.gov/consumers/skin-facts-what-you-need-know-about-skin-lightening-products/skin-product-safety) | Refuse; refer to derm for pigmentation Rx |
| Marketplace/third-party sellers, unsealed testers | 40% of seized fakes contain toxins [67](https://www.gov.uk/government/news/ipo-campaign-launched-as-toxins-found-in-counterfeit-beauty-products) | Pharmacy/authorized channel only |
| "Cures/treats" language on a cosmetic | Illegal drug claim in major jurisdictions [60](https://www.fda.gov/cosmetics/cosmetics-laws-regulations/it-cosmetic-drug-or-both-or-it-soap) | Treat as non-compliant; prefer regulated/notified products |
| "Hypoallergenic / clean / natural" as the only safety claim | No legal definition [47](https://www.fda.gov/cosmetics/cosmetics-labeling-claims/hypoallergenic-cosmetics) [51](https://www.dermatologytimes.com/view/social-media-mythbusters-clean-skin-care) | Read INCI + fragrance allergen list instead |
| Daily acids + retinol stacked nightly | Over-exfoliation, barrier failure [77](https://pmc.ncbi.nlm.nih.gov/articles/PMC5608132) | Space nights; rebuild barrier first |
| Essential-oil-heavy "natural" formulas for sensitive skin | Oxidized linalool/limonene allergenicity [75](https://pubmed.ncbi.nlm.nih.gov/12084079) | Fragrance-free substitute |
| No concentration given for a hero active ("retinol complex") | May be below effective dose [79](https://www.cosmebio.org/en/reports/INCI-list-how-to-read-ingredient-list-cosmetics) | Check INCI position; prefer labeled % |
| Dark orange/brown vitamin C | Oxidized, pro-oxidant risk [4](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552410) [72](https://www.phyto-c.com/blogs/news/oxidized-vitamin-c-serum-color-guide) | Discard; recommend airless/opaque next time |
| Past PAO window / no PAO or expiry printed | Preservative failure risk [71](https://www.certifiedcosmetics.com/product/common-tests/period-after-opening-pao-test) | Don't buy/replace |

## Safety rails

- **Pregnancy**: stop all topical retinoids (tretinoin, adapalene, retinol, retinal) and isotretinoin (absolutely contraindicated oral retinoid); avoid high-% salicylic peels; ≤2% salicylic acceptable; prefer azelaic acid, glycolic/lactic low-strength, BP only with clinician sign-off; confirm with OB/derm [44](https://www.aad.org/public/diseases/acne/derm-treat/pregnancy) [16](https://www.aad.org/public/everyday-care/skin-care-secrets/routine/pregnancy-skin-care) [45](https://pmc.ncbi.nlm.nih.gov/articles/PMC9823189).
- **Rx-only / referral-to-pharmacist ingredients**: tretinoin, tazarotene, trifarotene, hydroquinone 4%, triple-combination melasma cream, oral tranexamic acid, topical steroids — the assistant must never suggest sourcing these OTC [83](https://practicaldermatology.com/topics/pigmentary-disorders/hydroquinone-in-2021/23592) [84](https://www.fda.gov/drugs/drug-safety-communications/fda-works-protect-consumers-potentially-harmful-otc-skin-lightening-products) [39](https://pmc.ncbi.nlm.nih.gov/articles/PMC5724303).
- **Refer to a dermatologist when**: nodular/cystic or scarring acne; suspected rosacea or perioral dermatitis; sudden widespread reaction/angioedema (urgent); melasma not responding to OTC + SPF after 3 months; any persistent pigmented lesion (rule out malignancy); eczema flares needing anti-inflammatory therapy; PFB unresponsive to technique change [38](https://www.aad.org/public/diseases/a-z/melasma-treatment) [96](https://www.aad.org/public/everyday-care/skin-care-basics/hair/razor-bump-remedies) [15](https://www.aad.org/member/clinical-quality/guidelines/acne).
- **Assistant-level rules**: never recommend hydroquinone or steroid-containing lighteners; never combine "treat/cure" language with cosmetic recommendations; always flag retinoids in pregnancy; always route actives-buying first-timers to patch-testing advice [40](https://www.aad.org/public/everyday-care/skin-care-secrets/prevent-skin-problems/test-skin-care-products).

## Sources

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC5605218 — Topical vitamin C review (Telang 2017)
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC7909477 — 10–20% clinically effective range
3. https://jcadonline.com/clinical-applications-of-vitamin-c-in-dermatology-a-systematic-review — JCAD systematic review
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC10552410 — Ascorbate aqueous stability/pH
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC8675340 — Retinol OTC evidence systematic review
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC11344648 — Retinoid irritancy reduction strategies
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC2699641 — Retinoids in skin aging (Mukherjee 2006)
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC8750127 — Clinician's guide to topical retinoids
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC9618501 — Retinoids in antiaging treatments
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC2958193 — Del Rosso 2010: no tretinoin degradation with BPO
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC11268769 — AHA efficacy/safety review (2024)
12. https://www.mdpi.com/2079-9284/10/5/131 — Topical AHA formulations review
13. https://labmuffin.com/fact-check-friday-why-does-ph-matter-for-ahas-and-bhas — AHA pH dependence
14. https://pubmed.ncbi.nlm.nih.gov/19245467 — Smith 1996: glycolic vs lactic
15. https://www.aad.org/member/clinical-quality/guidelines/acne — AAD acne guideline (2024 update)
16. https://www.aad.org/public/everyday-care/skin-care-secrets/routine/pregnancy-skin-care — AAD pregnancy skin care
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC3142702 — Niacinamide 4% vs clindamycin 1% RCT
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC8594539 — BPO 2.5% + niacinamide 5% RCT
19. https://pubmed.ncbi.nlm.nih.gov/37550898 — Azelaic acid systematic review (King 2023)
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC11512533 — Azelaic acid mechanisms review (2024)
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC11762834 — Peptides for skin aging (2025)
22. https://www.sciencedirect.com/science/article/pii/S1773224723009395 — Anti-aging peptides (industry-published figures)
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC9293121 — Ceramide preparations in AD (Kono 2021)
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC12731180 — Hyaluronic acid forms/MW (Zanchetta 2025)
25. https://www.ncbi.nlm.nih.gov/books/NBK587270 — UV filters overview (NCBI)
26. https://www.bbc.com/future/article/20250718-which-kind-of-sunscreen-should-you-use — Mineral filters absorb UV
27. https://www.fda.gov/drugs/understanding-over-counter-medicines/questions-and-answers-fdas-regulatory-actions-over-counter-sunscreen — FDA sunscreen GRASE Q&A
28. https://jamanetwork.com/journals/jama/fullarticle/2759002 — Matta 2020: plasma absorption
29. https://www.ewg.org/sunscreen/report/the-trouble-with-sunscreen-chemicals — EWG endocrine concerns (advocacy source)
30. https://labmuffin.com/fact-check-friday-why-does-ph-matter-for-ahas-and-bhas — Lab Muffin methodology
31. https://www.aad.org/public/everyday-care/skin-care-basics/dry/pick-moisturizer — AAD moisturizer selection
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC8954092 — Soaps vs syndets (Mijaljica 2022)
33. https://www.aad.org/public/diseases/rosacea/triggers/tips — AAD rosacea skin care tips
34. http://www.rosacea.org/patients/skin-care-and-cosmetics — NRS ingredient trigger survey
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC2921758 — PIH review (Davis 2010)
36. https://skinofcolorsociety.org/discover-patients-public/public-education/pih — Skin of Color Society PIH
38. https://www.aad.org/public/diseases/a-z/melasma-treatment — AAD melasma treatment
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC5724303 — Medical management of melasma (Sarkar 2017)
40. https://www.aad.org/public/everyday-care/skin-care-secrets/prevent-skin-problems/test-skin-care-products — AAD patch-test protocol
41. https://www.theinkeylist.com/blogs/news/why-do-i-need-to-do-a-patch-test — Patch-test timing (industry source)
42. https://eur-lex.europa.eu/eli/reg/2023/1545/oj — Regulation (EU) 2023/1545 fragrance allergens
43. https://single-market-economy.ec.europa.eu/sectors/cosmetics/cosmetic-products-specific-topics/fragrance-allergens-labelling_en — EC fragrance allergens page
44. https://www.aad.org/public/diseases/acne/derm-treat/pregnancy — AAD acne in pregnancy
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC9823189 — Retinoids in pregnancy review (2022)
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC3114665 — Safety of skin care in pregnancy (Bozzo 2011)
47. https://www.fda.gov/cosmetics/cosmetics-labeling-claims/hypoallergenic-cosmetics — FDA: no standards for "hypoallergenic"
48. https://www.fda.gov/cosmetics/cosmetics-labeling/cosmetics-labeling-claims — FDA labeling claims
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC8954092 — Cleanser review
50. https://www.fda.gov/cosmetics/cosmetic-ingredients/allergens-cosmetics — FDA allergens page
51. https://www.dermatologytimes.com/view/social-media-mythbusters-clean-skin-care — Dermatology Times on "clean" claims
52. https://erleia.com/pages/what-is-clean-beauty — Clean beauty unregulated (industry source)
53. https://www.leapingbunny.org/Web/Web/content/standard.aspx — Leaping Bunny standard
54. https://www.crueltyfreekitty.com/cruelty-free-101/leaping-bunny-vs-peta — Leaping Bunny vs PETA
55. https://www.iso.org/standard/72250.html — ISO 24444:2019 SPF test
56. https://blog.ansi.org/ansi/iso-24444-2019-in-vivo-determination-of-spf — ANSI explainer
57. https://pmc.ncbi.nlm.nih.gov/articles/PMC7759112 — Sander 2020: application dose & SPF reality
58. https://www.sciencedirect.com/science/article/pii/S0278691523004957 — Norman 2023: reapplication behavior
59. https://www.tga.gov.au/resources/explore-topic/sunscreens/sunscreen-spf-testing-information-consumers — TGA sunscreengate response
60. https://www.fda.gov/cosmetics/cosmetics-laws-regulations/it-cosmetic-drug-or-both-or-it-soap — FDA cosmetic vs drug
61. https://www.fda.gov/cosmetics/cosmetics-laws-regulations/cosmetics-us-law — FDA cosmetics & US law
62. https://www.fda.gov/consumers/skin-facts-what-you-need-know-about-skin-lightening-products/skin-product-safety — FDA skin lightening safety
67. https://www.gov.uk/government/news/ipo-campaign-launched-as-toxins-found-in-counterfeit-beauty-products — UK IPO counterfeit toxins
68. https://observer.co.uk/news/business/article/the-toxic-cost-of-counterfeit-beauty-products — Observer counterfeit investigation
69. https://www.thetimes.com/life-style/beauty/article/cosmetics-sold-online-amazon-ebay-fake-2zvj3sdk9 — Times 65% fake estimate (press)
71. https://www.certifiedcosmetics.com/product/common-tests/period-after-opening-pao-test — PAO testing
72. https://www.phyto-c.com/blogs/news/oxidized-vitamin-c-serum-color-guide — Vitamin C oxidation colors (brand source)
74. https://pmc.ncbi.nlm.nih.gov/articles/PMC6587870 — Limonene/linalool hydroperoxide sensitization (Dittmar 2018)
75. https://pubmed.ncbi.nlm.nih.gov/12084079 — Sköld 2002: linalool autoxidation
76. https://dermnetnz.org/topics/hydroperoxides-of-limonene-and-linalool — DermNet on oxidized terpenes
77. https://pmc.ncbi.nlm.nih.gov/articles/PMC5608132 — Epidermal barrier review (Del Rosso 2016)
78. https://blog.dermaquestclinical.com/signs-of-over-exfoliation-and-how-to-fix-it — Over-exfoliation signs (brand source)
79. https://www.cosmebio.org/en/reports/INCI-list-how-to-read-ingredient-list-cosmetics — INCI descending order & 1% line
80. https://pmc.ncbi.nlm.nih.gov/articles/PMC12335261 — HQ levels in unregulated lightening creams (2025)
81. https://www.sciencedirect.com/science/article/pii/S2352647520301416 — Pollock 2021: skin-lightening survey (67% treating PIH)
82. https://doctorabad.com/uptodate/d/topic.htm?path=topical-skin-lightening-agents-complications-associated-with-misuse — Lightening-agent complications
83. https://practicaldermatology.com/topics/pigmentary-disorders/hydroquinone-in-2021/23592 — Hydroquinone CARES Act status
84. https://www.fda.gov/drugs/drug-safety-communications/fda-works-protect-consumers-potentially-harmful-otc-skin-lightening-products — FDA OTC lightener action
85. https://labmuffin.com/fact-check-friday-why-does-ph-matter-for-ahas-and-bhas — Lab Muffin (Dr. Michelle Wong)
86. https://kindofstephen.com — KindofStephen (Stephen Alain Ko)
87. https://incidecoder.com — INCIDecoder
88. https://cosdna.com — CosDNA
89. https://www.maybelline.com/makeup-tips/face/face-makeup-tutorials-for-beginners/how-to-find-a-foundation-shade-for-your-skin-tone — Shade depth × undertone (brand source)
90. https://janeiredale.com/blogs/makeup-blog/how-to-match-foundation-to-undertone — Undertone matching (brand source)
91. https://color-analysis.app/blog/foundation-for-olive-skin-guide — Olive undertone axis
92. https://pubmed.ncbi.nlm.nih.gov/12476017/ — Piérard-Franchimont 2002: ketoconazole 2% vs ZPT 1% RCT
93. https://delacourte.com — Fragrance concentration tiers (industry source)
94. https://www.scerto.com — Fragrance tiers (industry source)
95. https://dermnetnz.org/topics/pseudofolliculitis-barbae — DermNet PFB
96. https://www.aad.org/public/everyday-care/skin-care-basics/hair/razor-bump-remedies — AAD razor bumps
97. https://jamanetwork.com/journals/jamadermatology/fullarticle/2791583 — JAMA Dermatology shaving review (2022)
