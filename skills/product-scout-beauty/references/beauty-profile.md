# Scientifically Useful Personal Data for a Personalized Beauty/Skincare Profile

> Family rule: where this file and the skill's SKILL.md disagree, SKILL.md's
> operative wording wins — the six guardrails and the load/offer/update rules
> are stated authoritatively in SKILL.md; this file explains and sources them.

**Scope.** What an AI shopping assistant may honestly collect (skin/hair self-report, photos, medical documents) to personalize beauty recommendations; which data points genuinely change recommendations, which are useless, and the honesty limits.

## Method note

Primary sources only: PubMed/PMC-indexed dermatology literature, guideline bodies (AAD, ACDS, IADVL, EU SCCS), and validated assessment instruments (Baumann Skin Type Questionnaire, Sensitive Scale-10, Fitzpatrick phototype, GEA acne scale). Claims cite the specific source; items resting on abstract-level or secondary summaries are marked **[unverified detail]**. Line between "descriptive support" and "diagnosis" is treated as a hard constraint throughout.

---

## 1. Skin typing — what is validated, and what self-report can actually deliver

- **Self-labeled skin type ("oily/dry/combination") is weak evidence.** Youn et al. compared subjective self-classification with Sebumeter (instrumental sebum) measurement and found subjective type does not match actual sebum output — simple self-classification is "of very limited use" for sebum level [Youn 2002].
- **Fitzpatrick phototype self-report is inaccurate for types III–VI.** Dermatologist-determined phototype beat self-report; rephrasing questions with concrete behavioral descriptors (specific sun-exposure scenarios, not "do you tan?") improved self-report accuracy [Eilers 2013]. Use behavior-anchored questions, not label-picking.
- **Baumann Skin Type Questionnaire (BSTQ):** retest accuracy ~86% with good sensitivity/specificity in a 2025 validation review [Brzozowska 2025]; a Korean study found it matched dermatologist evaluation **[unverified detail]**; a biometric-evaluation study concluded the 16-type system lacks sufficient biometric validation (self-report vs instrumented sebum/hydration) [Delavar 2026]. The hyperpigmentation dimension showed low sensitivity (12%) in one language-version validation (Polish) [Brzozowska 2025].
- **Sensitive skin is the best-validated self-report domain.** The Sensitive Scale-10 (10 items: stinging, burning, tingling) is a validated instrument with high internal consistency [Misery 2014; Legeas 2021]. Questionnaire-based sensitive-skin assessment and the lactic-acid stinging test (LAST) capture *different* subpopulations and are complementary [Pan 2021]; a recently validated screening questionnaire reached ~72.7% accuracy against LAST [sensitive-skin questionnaire validation].
- **Instrumental home measurements (teledermatology-grade devices) are reliable but not decision-critical.** GPSkin Barrier (patient-operated smartphone device) showed good test–retest reliability for TEWL (ICC 0.89) and stratum-corneum hydration (ICC 0.85), with acknowledged accuracy limits vs gold-standard devices (AquaFlux, Corneometer) [Grinich 2019; Grinich 2021]. Reliable ≠ actionable: no evidence these numbers change product choice beyond what behavior-anchored questions already give.
- **What actually predicts product fit (self-report):** reaction history to actives (e.g., retinoid irritation), tightness after washing, shine timing during the day, and triggers from a validated list — in rosacea patients the documented product triggers are alcohol (66%), witch hazel (30%), fragrance (30%), menthol (21%), peppermint (14%) [AAD rosacea triggers]. These concrete, behavior-based items outperform global labels [Eilers 2013; Pan 2021].

## 2. Photo-based assessment — what photos can and cannot support

- **Validated capability that exists:** smartphone-photo AI acne grading on the GEA scale — the first validated algorithm reached dermatologist-grade GEA agreement from smartphone photographs [Seité 2019]; later AI systems track lesion detection/severity vs physician image-based scoring [Li 2023]. This validates *severity description from photos under controlled conditions*, done by a validated model — not a lay assistant eyeballing a selfie.
- **General teledermatology evidence:** store-and-forward teledermatology achieves roughly 75–85% diagnostic concordance with in-person dermatologists, but concordance is lower and more variable with patient-submitted images than clinician-acquired ones, and image quality (lighting, focus, framing) is a key driver of discordance [Jiang 2022]. Practice guidelines standardize capture conditions for this reason [McKoy 2016].
- **What photos cannot honestly tell a shopping assistant:** hydration or sebum levels (no validated image-based method — these are instrument-measured parameters [Grinich 2019]); skin "type" (self-report is weak, image inference weaker [Youn 2002]); barrier function; any diagnosis. **[unverified detail]** — no published validation of inferring dryness/oiliness from casual selfies was found in this search.
- **Lighting/angle pitfalls:** color casts and exposure shift apparent redness/pigmentation; single-angle selfies hide lesion distribution; patient-acquired variability is documented as the main quality problem in teledermatology [Jiang 2022].
- **The line:** a non-clinical assistant may describe what is visible ("several raised bumps on the cheeks", "visible redness") as *descriptive support*, and may route the user to a dermatologist; it must not output condition labels, severity grades, or before/after efficacy verdicts from photos. Teledermatology's concordance figures belong to dermatologists reading standardized images, not to product recommenders [Jiang 2022].

## 3. Lab tests and medical documents — which ones change recommendations

- **Patch-test results: the highest-value document.** A positive patch test converts directly into an ingredient-avoidance list, cross-referenced against INCI labels: fragrance mix I/II positive → avoid fragrance/parfum/essential oils; methylisothiazolinone/methylchloroisothiazolinone (MI/MCI) → avoid isothiazolinone-preserved products; lanolin → avoid wool-fat derivatives; balsam of Peru flags fragrance/flavor cross-reactivity [Burkemper 2015; interpretive patient-education material **[unverified detail]**]. The ACDS CAMP database operationalizes exactly this translation — patch-test allergen codes → "safe product" lists [ACDS CAMP]. *What it does NOT change:* texture/price preferences, routine structure.
- **Ferritin and vitamin D in hair loss:** among routine labs in female pattern hair loss, ferritin was low in ~30.8% and vitamin D in ~25.9% of tested cases; thyroid/iron-capacity panels had low yield [Okhovat 2023]. Rasheed et al. found low ferritin/vitamin D associated with female hair loss and recommended screening both [Rasheed 2013]; Tamer et al. found significantly lower levels vs controls [Tamer 2020]. *What it changes:* only "if you have a known deficiency, address it medically; supplements are a health decision, not a beauty purchase". *What it does NOT change:* topical/minoxidil-type product selection, and low ferritin alone does not prove causation of the hair loss [Okhovat 2023].
- **Thyroid, zinc, full iron panels:** routine screening in classic pattern FPHL is low-yield; testing is indicated only with symptoms/signs of deficiency or systemic disease [Okhovat 2023]. Zinc-deficiency–hair-loss evidence in non-deficient populations is weak **[unverified detail]**. *Changes nothing in product recommendations.*
- **Hormonal panels for adult female acne:** indicated only with hyperandrogenism signs — irregular menses, hirsutism, scalp thinning, refractory or adult-onset severe acne [Farny 2025; Carmina 2022]. *What it changes:* nothing about OTC product selection; it determines whether the assistant should prompt a physician referral, not a different serum.
- **Vitamin D "for skin" generally:** no evidence it changes topical product choice; its only documented beauty-relevant link is the hair-loss screening context above [Rasheed 2013; Okhovat 2023].

## 4. Interaction/contraindication profile — the data that changes defaults

- **Isotretinoin:** common side effects are dryness (skin, lips, eyes) and increased photosensitivity; waxing, peels, and ablative procedures are contraindicated during treatment and 6 months after (drug labeling; guideline nuance: complications are rare and dose-related) [Mysore 2017]. *Changes:* barrier-repair routine, no stripping/exfoliating defaults, sun-protection emphasis.
- **Photosensitizing medications** (doxycycline, hydrochlorothiazide, and others): photosensitive drug eruptions account for up to ~8% of cutaneous adverse drug events; doxycycline phototoxicity is frequent in acne patients; HCTZ shows positive photopatch reports [Blakely 2019; Hofmann 2021]. *Changes:* daily-SPF insistence, warning against stacking phototoxic actives (e.g., AHAs) in summer.
- **Pregnancy/breastfeeding:** AAD lists retinoids (isotretinoin, tretinoin, tazarotene, adapalene/retinol OTC) as to-avoid; low-concentration topical salicylic acid is viewed as low-risk but often advised against as a precaution; azelaic acid, vitamin C, niacinamide, cautious benzoyl peroxide, and daily SPF are the pregnancy-compatible defaults [AAD pregnancy skincare]. *This single yes/no flag reshapes the whole actives shortlist.*
- **Atopic history / allergic diathesis:** fragrance contact allergy affects ~1–3% of the general population [de Groot 2020; SCCS opinion]; fragrance is a documented trigger of atopic-dermatitis flares, and AAD guidance is to choose products labeled "fragrance-free" (never merely "unscented", which may contain masking fragrance) [AAD AD skin care; AAD eczema-friendly products]. *Changes:* fragrance-free/essential-oil-free default, NEA Seal-type screening [NEA directory].
- **Known conditions that alter OTC defaults:** rosacea → avoid alcohol, witch hazel, fragrance, menthol, peppermint, scrubs; mineral sunscreens better tolerated [AAD rosacea triggers]. Melasma → photoprotection is foundational; tinted iron-oxide SPF 50+ because visible light worsens it [ISD 2024 melasma guidance; PMC5724303]. Seborrheic dermatitis → OTC zinc-pyrithione/ketoconazole shampoos are standard self-care **[unverified detail]**.
- **Topical steroids / immunosuppressants:** chronic use is associated with skin atrophy and fragility, arguing for gentle non-stripping defaults **[unverified detail — textbook principle, not from a retrieved source]**.

## 5. Product history — does past success/failure predict fit?

- **Yes, reaction history is the strongest self-report predictor.** A history of adverse cosmetic reactions is a defining marker of sensitive-skin status, and contact dermatitis is the most common cosmetic adverse effect (~1–5% of the population) [Yu 2026 **[unverified detail]**; Alyahya 2025 **[unverified detail]**].
- **Real-use testing supports the signal's specificity:** the repeated open application test (ROAT) — applying a product repeatedly under normal use — is less sensitive than patch testing but highly specific, with PPV ~100% and NPV ~70% for allergic contact dermatitis, minimum 10 days of use [Khambra 2020; Kaliyadan 2021]. A user's real-world reaction to a product is therefore strong *positive* evidence about that product's formula for them.
- **Structured questions that capture it best:** (a) which product caused the reaction and its formula family; (b) reaction pattern — immediate burning/stinging (irritant-type) vs delayed itching/persistent rash (allergic-type) [Pan 2021; Kaliyadan 2021]; (c) what worked before (success history); (d) reaction to specific actives (retinoid dermatitis → low-strength slow-intro defaults). Note the asymmetry: a positive reaction history is reliable; *no reaction* history does not prove tolerance of other formulas [Khambra 2020].

## 6. Privacy and data handling — treating uploads as health data

- **Skin/hair photos, medication lists, and lab documents are special-category health data.** GDPR Article 9(1) prohibits processing data revealing health (including images and documents revealing health status) unless an Article 9(2) exception applies — in a consumer app, that means explicit consent given for one or more specified purposes [GDPR Art. 9].
- **Apply Article 5 principles:** data minimization (collect only what changes recommendations), purpose limitation (beauty advice only), storage limitation [GDPR Art. 5].
- **Best-practice pattern:** consent before any storage; *store the derived profile, not raw documents* — extract decision-relevant fields (allergen list, deficiency flags, pregnancy status, medication names) and treat the uploaded PDF/photo as transient processing input; give the user deletion/erasure control over profile fields and derived data (GDPR right to erasure) [GDPR Art. 9; GDPR Art. 5; **[unverified detail: Art. 17 erasure cited from general knowledge]**].

---

## Proposed profile schema

| Field | Why it matters (changes recommendation) | Source |
|---|---|---|
| Sun-response behavior (burn vs tan scenarios) | Phototype proxy → SPF strength, pigment-risk messaging; self-label unreliable, behavior-anchored questions accurate [Eilers 2013] | Self-report |
| Shine timing through the day / tightness after washing | Better proxies for sebum/dryness than the "oily/dry" label, which misclassifies vs Sebumeter [Youn 2002] | Self-report |
| Stinging/burning sensitivity (SS-10-style items) | Validated sensitive-skin measure → fragrance-free, minimal-irritant defaults [Misery 2014; Pan 2021] | Self-report |
| Known diagnoses (rosacea, melasma, acne, atopic dermatitis, seborrheic dermatitis) | Each condition flips specific defaults: rosacea triggers list [AAD rosacea], melasma iron-oxide SPF [ISD 2024], AD fragrance-free [AAD AD] | Self-report (declared, not inferred) |
| Pregnancy/breastfeeding status | Retinoid exclusion list, salicylic-acid caution, pregnancy-safe actives [AAD pregnancy] | Self-report |
| Medication flags (isotretinoin, doxycycline/HCTZ-type photosensitizers, topical steroids, immunosuppressants) | Fragility/dryness routine, SPF insistence, peel/wax warnings [Mysore 2017; Blakely 2019] | Self-report (optionally document) |
| Patch-test allergen list (fragrance mix I/II, MI/MCI, lanolin, balsam of Peru…) | Direct ingredient-avoidance filtering against INCI labels — the highest-value document field [Burkemper 2015; ACDS CAMP] | Document |
| Known deficiencies (ferritin, vitamin D) in hair-loss context | Referral prompt + "supplements are medical, not beauty"; does not alter topical picks [Okhovat 2023; Rasheed 2013] | Document |
| Hormonal workup flag (hyperandrogenism signs) | Referral routing only; no OTC change [Farny 2025] | Self-report |
| Facial photos (optional, standardized guidance) | Descriptive support only ("visible redness on cheeks"); no grading/diagnosis claims by the assistant [Jiang 2022; Seite 2019] | Photo |
| Product history: reacted products + formula family, reaction pattern, hero products | Strong predictor of tolerance (PPV ~100% for ROAT-confirmed reactions); sets fragrance-free/irritant-free defaults [Khambra 2020] | Product history |
| Consent & deletion record | Legal precondition for any health-data field above [GDPR Art. 9] | System |

## Honesty limits — what the assistant must NOT claim

1. **No diagnosis from photos.** It may describe visible features ("redness on the cheeks", "small bumps"); it must not say "you have rosacea/acne grade 2". Even validated AI grading (GEA) is a dermatologist-comparison tool [Seité 2019; Jiang 2022].
2. **No sebum/hydration/"skin type" verdicts from photos.** These are instrument-measured parameters; no validated image-based method exists, and self-labels are already unreliable [Youn 2002; Grinich 2019] **[unverified detail: absence of image-based validation based on this search]**.
3. **No lab-value interpretation.** A ferritin number is not a hair-loss diagnosis, and low ferritin does not prove causation [Okhovat 2023]. The assistant may only note "flag for physician discussion".
4. **No causality claims for lab changes** ("take vitamin D and your skin will improve" — unsupported; vitamin D only changes referral/supplement decisions in documented deficiency [Rasheed 2013; Okhovat 2023]).
5. **No severity grading or before/after efficacy verdicts** from user photos — lighting, angle, and exposure confound comparisons, and concordance data belong to dermatologist-read standardized images [Jiang 2022].
6. **No treatment of a patch-test list as complete.** Patch-tested panels cover a limited allergen series; absence of a positive result ≠ tolerance of all other ingredients [Burkemper 2015 **[unverified detail: panel scope]**].
7. **No medication-interaction diagnosis.** The assistant may apply documented defaults (isotretinoin → no waxing/peels [Mysore 2017]; photosensitizer → SPF [Blakely 2019]) but must defer conflicts to a pharmacist/physician.
8. **No "personalized" over-claim.** Questionnaire-based sensitive-skin screening is only ~70–75% accurate against objective provocation tests [Pan 2021; sensitive-skin questionnaire validation] — frame outputs as filtered suggestions, not certainties.

## Sources

1. Youn SW et al. (2002). Evaluation of facial skin type by sebum secretion: discrepancies between subjective descriptions and sebum secretion. https://pubmed.ncbi.nlm.nih.gov/12236886
2. Eilers S et al. (2013). Accuracy of self-report in assessing Fitzpatrick skin phototypes. JAMA Dermatol. https://jamanetwork.com/journals/jamadermatology/fullarticle/1737180
3. Brzozowska A et al. (2025). BSTQ validation review. https://pmc.ncbi.nlm.nih.gov/articles/PMC12163966
4. Misery L et al. (2014). A new ten-item questionnaire for assessing sensitive skin: the Sensitive Scale-10. Acta Derm Venereol. https://medicaljournalssweden.se/actadv/article/view/6447
5. Legeas C et al. (2021). Cut-off scores for sensitive skin on the Sensitive Scale-10. https://pmc.ncbi.nlm.nih.gov/articles/PMC9309873
6. Pan Y et al. (2021). Questionnaire and lactic acid sting test play different roles in skin sensitivity characterization. https://pmc.ncbi.nlm.nih.gov/articles/PMC8449876
7. Grinich EE et al. (2019). Validation of a smartphone application-enabled device for skin barrier measurement. https://pubmed.ncbi.nlm.nih.gov/30942506
8. Grinich EE et al. (2021). Patient-operated device vs AquaFlux/Corneometer. https://pubmed.ncbi.nlm.nih.gov/33665909
9. Seite S et al. (2019). AI algorithm for acne grading from smartphone photographs (GEA scale). Exp Dermatol. https://pubmed.ncbi.nlm.nih.gov/31446631 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6972662
10. Li Y et al. (2023). AI-powered acne grading system vs physician scoring. Front Med. https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2023.1255704/full
11. Jiang B et al. (2022). Store-and-forward images in teledermatology (review). https://pmc.ncbi.nlm.nih.gov/articles/PMC9302578
12. Burkemper JP (2015). Contact dermatitis, patch testing, and allergen avoidance. Missouri Medicine 112(4):296–300. https://pubmed.ncbi.nlm.nih.gov/26455061 *(URL corrected and verified 2026-11 — prior PMC ID pointed to an unrelated article)*
13. ACDS Contact Allergen Management Program (CAMP). https://www.contactderm.org/resources/acds-camp
14. Okhovat JP et al. (2023). Utility of laboratory testing in patients with female pattern hair loss. https://pubmed.ncbi.nlm.nih.gov/31306723
15. Rasheed H et al. (2013). Serum ferritin and vitamin D in female hair loss. Skin Pharmacol Physiol. https://karger.com/spp/article/26/2/101/295720
16. Tamer F et al. (2020). Serum ferritin and vitamin D levels in hair loss. https://pmc.ncbi.nlm.nih.gov/articles/PMC7394174
17. Farny L (2025). Adult female acne: when and why to consider a hormonal evaluation. https://pubmed.ncbi.nlm.nih.gov/40145185
18. Carmina E et al. (2022). Female adult acne and androgen excess. J Endocr Soc 6(3):bvac003. https://pmc.ncbi.nlm.nih.gov/articles/PMC8826298 *(URL corrected and verified 2026-11 — prior PMC ID pointed to an unrelated article)*
19. Mysore V et al. (2017). Standard guidelines of care: performing procedures in patients on isotretinoin. https://pmc.ncbi.nlm.nih.gov/articles/PMC5820835
20. Blakely KM, Drucker AM, Rosen CF (2019). Drug-induced photosensitivity — an update. Drug Saf 42(7):827–847. https://link.springer.com/article/10.1007/s40264-019-00798-6 **[unverified detail: canonical URL; text verified via mirrored PDF]** https://allergolyon.fr/wp-content/uploads/2020/09/7.15.2-blakely2019-Drug%E2%80%90Induced-Photosensitivity.pdf
21. Hofmann GA et al. (2021). Drug-induced photosensitivity: culprit drugs, mechanisms, prevention. https://pmc.ncbi.nlm.nih.gov/articles/PMC7898394
22. AAD. Pregnancy skin care (safe/unsafe ingredients). https://www.aad.org/public/everyday-care/skin-care-secrets/routine/pregnancy-skin-care
23. AAD. Rosacea: skin care and trigger management. https://www.aad.org/public/diseases/rosacea/triggers
24. AAD. Atopic dermatitis skin care (fragrance-free, not unscented). https://www.aad.org/public/diseases/eczema/types/atopic-dermatitis/skin-care
25. AAD. How can I find eczema-friendly products? https://www.aad.org/public/diseases/eczema/childhood/triggers/friendly-products
26. National Eczema Association. Eczema-friendly product directory / Seal of Acceptance. https://nationaleczema.org/eczema-products
27. de Groot AC (2020). Fragrances: contact allergy and other adverse effects. Dermatitis. https://journals.lww.com/10.1097/DER.0000000000000463
28. EU SCCS. Opinion on fragrance allergens in cosmetic products (1–3% general-population prevalence). https://health.ec.europa.eu/scientific-committees/scientific-committee-consumer-safety-sccs_en **[unverified detail: opinion document URL located from citation index]**
29. Khambra N et al. (2020). Correlation of patch test with ROAT (PPV ~100%, NPV ~70%). Indian J Dermatol Venereol Leprol. https://ijdvl.com/correlation-of-patch-test-with-repeated-open-application-test-in-patients-with-suspected-hair-dye-dermatitis *(PPV/NPV figures verified 2026-11)* ; Kaliyadan F et al. (2021). Standardization of repeated open application testing. https://pmc.ncbi.nlm.nih.gov/articles/PMC9131969
30. ISD (2024). Melasma guideline (photoprotection/tinted iron-oxide SPF 50+ first-line). https://pmc.ncbi.nlm.nih.gov/articles/PMC5724303
31. GDPR Art. 9 (special-category health data). https://gdpr-info.eu/art-9-gdpr
32. GDPR Art. 5 (minimization, purpose limitation, storage limitation). https://gdpr-info.eu/art-5-gdpr
33. McKoy K, Antoniotti NM, Armstrong A, et al. (2016). Practice Guidelines for Teledermatology. Telemed J E Health. https://pubmed.ncbi.nlm.nih.gov/27690203 *(verified 2026-11)*
34. Delavar S (2026). Biometric Evaluation of Baumann Skin Typing. Skin Res Technol 32:e70338. https://pmc.ncbi.nlm.nih.gov/articles/PMC13074428 *(verified 2026-11)*
35. Sensitive-skin screening questionnaire validation (~72.7% accuracy vs LAST; 68.9% sensitivity, 78.9% specificity at cut-off ≥3). https://journals.pagepress.net/dr/article/view/10944 *(verified 2026-11)*

## Appendix — beauty profile template (the template of record; SKILL.md holds the operative rules)

Copy this verbatim when creating the profile file (empty except consent):

```markdown
---
schema: product-scout-beauty-profile
version: 1
created: <date>
updated: <date>
consent:
  enabled: true
  consent_date: <date>
  scope: [allergies, conditions, pregnancy, medications, product-history]
---

# Beauty profile

User-owned file: edit or delete any line. Deleting the whole file erases
everything — the agent keeps no other copy except any legacy original it
notified you about during migration.

## Core facts (user-stated; each with date stated)
- Skin type: <behavior-derived, dated>
- Allergies / sensitivities: <stated, dated>
- Conditions under management: <dated>
- Pregnancy: <dated — RECONFIRM if older than 6 months>
- Medications: <volunteered, dated — RECONFIRM if older than 6 months>

## Product history (append-only log, newest last, keep last ~10)
- <date> | <product> | WORKING/FAILED | <why>

## Derived observations (agent-inferred; NEVER hard exclusions)
- [<date> | <confidence> | <source>] <observation — suggestive only>

## Agent rules (do not edit this section)
- A current-session user statement ALWAYS overrides any line above.
- Ask before saving anything new; save nothing the user hasn't confirmed.
- The one exception: the one-time location migration of an existing
  consented profile, which runs without asking.
- Never re-ask a core fact dated within 6 months; do re-ask older ones.
- Stated allergies are hard filters; derived observations are soft hints.
- Reconfirm pregnancy in-session before ANY retinoid-adjacent advice.
```

The six guardrails these rules implement are enumerated in SKILL.md Step 0
and remain authoritative there.
