> **Family note.** This file is the sourced-companion reference for the
> `product-scout-health-medical` skill — installed at
> `references/health-domain.md`, alongside `references/health-drivers.md`.
> Read it when a rule in SKILL.md needs its full sourced backing. Where this
> file and SKILL.md disagree, SKILL.md's operative wording wins: thresholds,
> gates, and referral rules are stated authoritatively in SKILL.md — this
> file explains and sources them. A health-profile template appendix is
> appended at the end of this file (the template of record; SKILL.md's
> six guardrails remain authoritative there).

# Health & Medical — Domain Knowledge Base (SAFETY-CRITICAL SKILL)

Scope: OTC medicines, vitamins/supplements/sports nutrition, home medical devices, sexual wellness & family planning, first aid, massage/relaxation. Operating standard: pharmaceutical-grade rigor — the assistant advises like a pharmacist at the counter, with hard self-medication limits and mandatory escalation to a doctor/pharmacist whenever a red flag appears.

**Method note.** Research date: 2026-11-14 (tags re-keyed to the family scheme 2026-11). Sources: Cochrane systematic reviews, ICHD-3/NICE/USPSTF guidelines, FDA drug-safety communications and OTC Drug Facts labels, NIH ODS fact sheets, WHO guidance, ISO standards, peer-reviewed literature (NEJM, JAMA IM, AJCN, JISSN). Verification tags: `[S]` = sourced — verified against a regulator, standards body, official/primary source, or a family-verified precedent this cycle (inline `[S: URL]` carries the source); `[P]` = practitioner/market consensus or street anchor — labeled as such, never presented as sourced fact; `[A]` = anchored rail — a calibrated threshold set at install and re-anchored on a ~6-month cadence. Suffixes in any order: a source number (`[S13]`), a `YYYY-MM` date (mandatory on `[A]`), and lowercase modifiers — `unverified` (secondary coverage only; re-verify or drop before stating as fact), `industry` (vendor/marketing source), `convention` (usage convention, not evidence). A `[S, unverified]` claim is never the sole basis for a dosage or contraindication statement. Nothing in this file overrides a doctor's advice; the skill must say so when conflicts arise.

---

## 1. OTC Medicine Selection — Evidence by Category

### 1.1 Pain & fever ladder
- **Paracetamol/acetaminophen (first-line for most adults).** 500–1000 mg per dose, every 4–6 h; OTC label hard limit: severe liver damage may occur if you take more than 4,000 mg in 24 h, take other products containing acetaminophen, or drink ≥3 alcoholic drinks/day; Extra-Strength labels self-limit to 3,000 mg/day after FDA's 2011 push. Liver-disease patients: ~2,000 mg/day ceiling. Main danger is hidden acetaminophen in multi-symptom cold products (FDA DSCs 2011/2014; FDA warned against prescription units >325 mg/dose). [S: FDA OTC/DSC record via https://www.fda.gov/drugs/understanding-over-counter-medicines/over-counter-otc-heartburn-treatment and FDA summaries; dose text from standard OTC Drug Facts labels `[S, unverified]`]
- **Ibuprofen (add anti-inflammatory benefit).** 200–400 mg/dose every 6–8 h; OTC max 1,200 mg/24 h (prescription higher). Label boxed/strengthened warnings (FDA 2015): risk of fatal MI/stroke can begin within the first weeks of use, higher with dose/duration; stomach-bleeding warning higher if age ≥60, prior ulcer/bleeding, on blood thinners/steroids/other NSAIDs, or ≥3 alcoholic drinks/day; kidney injury risk with dehydration, heart failure, CKD. Skip ibuprofen in diarrhea/dehydration, before surgery. [S: https://www.dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=3b3b9e31-6387-1260-e054-00144ff88e88&type=pdf ; https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-strengthens-warning-non-aspirin-nonsteroidal-anti-inflammatory]
- **Aspirin.** Not the consumer first choice for pain/fever: contra-indicated in children/teens with viral illness (Reye syndrome — CDC 1982 advisory; AAP-aligned guidance still holds; incidence collapsed after warnings) `[S: https://www.ncbi.nlm.nih.gov/books/NBK526101]`; high GI bleeding/CV-safety profile vs alternatives; only routine daily low-dose 81 mg is a doctor-supervised therapy, not a shopping recommendation.
- **Sequence logic:** paracetamol first for fever/mild pain; ibuprofen when inflammation matters (musculoskeletal, dental, period pain) and no GI/kidney/pregnancy contraindications; alternating/combining the two is a medical decision to route through a pharmacist, not a default.

### 1.2 Cough & cold — the honesty section
- **Cochrane (CD001831, Smith et al.): "no good evidence for or against the effectiveness of OTC medications in acute cough"** in adults or children — antitussives, expectorants, mucolytics, antihistamine-decongestant combos all lack efficacy evidence; adverse effects reported in 19 studies. [S: https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD001831.pub5/full]
- For children, FDA/consumer guidance is to avoid OTC cough-cold products entirely in under-4s (no benefit, dosing-error and toxicity risk). [S: FDA consumer page https://www.fda.gov/drugs/special-features/should-you-give-cough-and-cold-medicine-your-child]
- **What little works:** honey (≥1 year old; infant botulism risk below that) probably relieves night cough better than no treatment and ≈ dextromethorphan — Cochrane CD007094. [S: https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD007094.pub5/full] Saline nasal drops/sprays, humidified air, fluids, rest. Time, not products, cures the cold.
- Selling rule: never upsell a multi-symptom cold cocktail "for immunity"; match a single active to the single symptom the customer has.

### 1.3 Antihistamines — 1st vs 2nd generation
- 1st generation (diphenhydramine, chlorphenamine) cross the blood-brain barrier → sedation, impaired psychomotor performance, anticholinergic burden (dry mouth, urinary retention, delirium/falls in elderly). 2nd generation (loratadine, cetirizine, fexofenadine) are H1-selective with low CNS penetration, once-daily dosing, minimal sedation; cetirizine slightly more sedating than loratadine/fexofenadine in some people. 2nd-gen is first-line for allergic rhinitis/urticaria. [S: PMC reviews (Simon 2008; Linton 2023) via https://www.ncbi.nlm.nih.gov/pmc/ ; `https://www.webmd.com/allergies/difference-between-first-generation-antihistamines-second-generation-antihistamines`]
- Uses of 1st gen: situational sleep aid, acute allergic reactions as adjunct (never as anaphylaxis treatment). Advise against driving after 1st gen.

### 1.4 Heartburn/antacids
- Antacids (aluminium/magnesium hydroxide, calcium carbonate) = immediate relief only; H2 blockers (famotidine) = 14-day OTC course; **PPIs (omeprazole etc.): OTC only for frequent heartburn (≥2 days/week), NOT immediate relief (takes 1–4 days), 14-day course, repeatable at most once every 4 months (≤3 courses/year)** — FDA explicit. Escalate if symptoms persist/worsen, dysphagia, vomiting blood/black stools, weight loss, rash+joint pain. Long-term/high-dose PPIs: fracture-risk signal (FDA 2010). [S: https://www.fda.gov/drugs/understanding-over-counter-medicines/over-counter-otc-heartburn-treatment ; https://www.fda.gov/drugs/drug-safety-and-availability/possible-fracture-risk-high-dose-long-term-proton-pump-inhibitors-ppi-use]

### 1.5 Topical antibiotic/antiseptic basics
- Clean minor wounds with water + mild soap; keep moist with plain petrolatum — evidence does not show routine topical antibiotics beat petrolatum for clean minor wounds, and neomycin (Neosporin) is a top contact-allergen (~1–11% of people; former "Allergen of the Year"); bacitracin can also sensitize; polymyxin-only (Polysporin) is the lower-allergy option. True infected wounds (spreading redness, pus, fever) need a doctor, not a tube. (Tong et al. 2018 systematic review; ACDS allergen lists `[S, unverified]`)
- Antiseptics (povidone-iodine, chlorhexidine) for dirty wounds; avoid aggressive rubbing alcohol/undiluted peroxide on tissue `[S, unverified]`.

---

## 2. Self-Medication Limits & Red Flags

### 2.1 Escalate immediately (same day / emergency) when
- Chest pain, pressure, pain radiating to arm/jaw with sweating or breathlessness — treat as cardiac until proven otherwise.
- Any fever in an infant **<3 months** (auto red flag — urgent assessment; NICE NG143 traffic-light system). [S: https://www.nice.org.uk/guidance/ng143 + traffic-light PDF https://www.nice.org.uk/guidance/ng143/resources/support-for-education-and-learning-educational-resource-traffic-light-table-pdf-6960664333]
- Fever >3 days (adults/children per OTC Drug Facts rules), fever worsening, or fever with stiff neck, non-blanching rash, confusion, breathing difficulty, persistent vomiting, dehydration, seizures.
- Blood in vomit/stool, black stools, severe abdominal pain; symptoms that "get worse or last more than" the label window (see summary table).
- Medication-overuse headache (ICHD-3): headache ≥15 days/month in a pre-existing headache disorder after regular overuse >3 months of simple analgesics ≥15 days/month, or triptans/opioids/combination analgesics ≥10 days/month. The answer is stopping the drug (with medical help), not buying more analgesics. [S: https://ichd-3.org/8-headache-attributed-to-a-substance-or-its-withdrawal/8-2-medication-overuse-headache-moh ; https://www.ncbi.nlm.nih.gov/books/NBK538150]

### 2.2 Children's dosing reality
- Pediatric doses are **weight-based**; household kitchen spoons vary 2–10 mL and cause ~40–50% dosing errors — only the calibrated device (oral syringe, dropper, dosing cup) provided with the product. [S: https://pmc.ncbi.nlm.nih.gov/articles/PMC8228905]
- **Never aspirin in children/teens with viral illness (Reye syndrome)**; never OTC cough/cold combos in under-4s; ibuprofen generally from ~6 months, paracetamol from birth per label `[S, unverified]`. Re-check the age band on every product; many "kids" syrups are age-banded, not weight-banded.

### 2.3 Pregnancy & breastfeeding OTC safety
- **Paracetamol: acceptable** in pregnancy at lowest effective dose/shortest duration (standard NHS/FDA position). [S: https://www.nhs.uk/medicines/paracetamol-for-adults/]
- **NSAIDs: avoid at ≥20 weeks** — FDA 2020 DSC: risk of fetal kidney problems → low amniotic fluid (oligohydramnios), potentially within days; earlier 30-week warning extended; low-dose aspirin for pregnancy indications is the exception. Warn that many cold/flu products hide NSAIDs. [S: FDA DSC Oct 15 2020 — https://www.fda.gov/drugs/drug-safety-and-availability/fda-recommends-avoiding-use-nsaids-pregnancy-20-weeks-or-later-because-they-can-result]
- **Decongestants: caution** — pseudoephedrine not recommended in pregnancy (placental blood-flow reduction) and avoided in 1st trimester per ACOG-aligned guidance; avoid while breastfeeding (reduces supply). Saline spray first. [S: https://www.nhs.uk/medicines/pseudoephedrine/ ; UKTIS https://www.medicinesinpregnancy.org/leaflets-a-z/decongestants]

### 2.4 Maximum sensible self-treatment durations
Per-category windows consolidated in the summary table below. Two global rules: (a) OTC labels state the escalation day — obey it ("if symptoms get worse or last more than X days, stop and ask a doctor"); (b) self-treatment is for *stable, mild, self-limiting* complaints only; anything severe, systemic, or chronic needs diagnosis first.

---

## 3. Supplements & Sports Nutrition

### 3.1 Evidence tiers — what has real support
- **Strong:** vitamin D deficiency correction in diagnosed/at-risk people (USPSTF: evidence insufficient for universal screening; Endocrine Society 2024: no routine testing or high-dose supplementation in healthy adults <75; empiric dosing only for pregnancy, ≥75, prediabetes, children, dark skin/low sun/obesity/malabsorption). [S: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/vitamin-d-deficiency-screening ; Endocrine Society 2024 CPG https://www.endocrine.org/clinical-practice-guidelines/vitamin-d-for-the-prevention-of-disease]
- **Strong:** iron only for confirmed deficiency (test first — unnecessary iron causes GI harm and masks nothing good; UL 45 mg/day). Folic acid 400 mcg/day from ≥1 month before conception through early pregnancy (CDC/WHO/USPSTF aligned). [S: https://www.cdc.gov/folic-acid/about/index.html]
- **Strong (exercise):** creatine monohydrate — "the most effective ergogenic supplement available" for high-intensity capacity + lean mass; 3–5 g/day (optional 20–25 g/day loading ×5–7 d); ISSN position stand (Kreider 2017). Protein for resistance training 1.4–2.0 g/kg/day, ~0.25 g/kg (20–40 g) quality protein per meal; ISSN position stand (Jäger 2017). [S: https://www.tandfonline.com/doi/full/10.1186/s12970-017-0173-z ; https://pubmed.ncbi.nlm.nih.gov/28642676]
- **Narrow/conditional:** omega-3 — prescription EPA/DHA is FDA-approved for very high triglycerides (≥500 mg/dL) and lowers TG ~20–30%; OTC supplements carry only "qualified" health claims (CHD, blood pressure); no FDA-approved OTC indication; CV-outcome evidence mixed. [S: https://pmc.ncbi.nlm.nih.gov/articles/PMC6999166]
- **Marketing:** multivitamins for CVD/cancer prevention in non-deficient adults (USPSTF I statement — insufficient evidence); beta-carotene and vitamin E are Grade **D** (recommend against — beta-carotene raises lung-cancer risk in smokers). "Immunity blends", "detox" products: no regulatory definition, no evidence. [S: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/vitamin-supplementation-to-prevent-cvd-and-cancer-preventive-medication]

### 3.2 Adulteration & contamination
- FDA Tainted Products database: 1,000+ products marketed as supplements containing **hidden drug ingredients**; Tucker et al. (JAMA IM 2018): 97.6% of adulterated supplements contained unapproved active pharmaceuticals, ~20% contained ≥2 hidden ingredients; hot categories: **sexual enhancement, weight loss, bodybuilding**. [S: https://www.fda.gov/drugs/medication-health-fraud/tainted-products-marketed-dietary-supplements-conventional-foods ; https://www.raps.org/resource/study-raises-questions-over-fdas-handling-of-adulterated-supplements.html]
- Supplements are **not FDA-approved before sale**; domestic manufacture ≠ safe; imported gray-market products carry the highest risk. Steering rule: certified products or licensed pharmacy channels only; treat any "too good to be true" bodybuilding/weight-loss/ED product as presumptively adulterated.

### 3.3 Third-party certification — what each mark actually means
- **USP Verified:** identity, potency/purity, label-matches-contents, contaminant screening. NOT a banned-substance check. Good default for general consumers. [S: USP program pages `[S, unverified]`]
- **NSF Certified for Sport:** every lot screened for ~270–280 WADA/major-league banned substances + label accuracy; the only certification recognized by USADA. **Informed Sport (LGC):** every batch tested pre-release for banned substances. Athletes (including anti-doping pools) should buy only these two for sports supplements. [S: https://www.nsfsport.com/certified-products ; https://sport.wetestyoutrust.com/certified-brands]

### 3.4 Safe upper limits (adult ULs, IOM/NASEM via NIH ODS)
Vitamin D 100 mcg (4,000 IU)/d; calcium 2,000 mg/d (2,500 for 51–70); iron 45 mg/d; vitamin C 2,000 mg/d; zinc 40 mg/d; folate (folic acid) 1,000 mcg/d — full table: [S: https://www.ncbi.nlm.nih.gov/books/NBK278991/table/diet-treatment-obes.table17die ; NIH ODS https://ods.od.nih.gov/]. Flag any multi-nutrient product where a serving exceeds several ULs simultaneously (typical of "mega" blends).

### 3.5 Supplement–drug interaction gates (hard stop before selling)
- **St John's Wort** — potent CYP3A4/PXR inducer: lowers warfarin, oral contraceptives ("much less effective" — unintended pregnancy), ciclosporin/tacrolimus (transplant rejection cases), digoxin, simvastatin, many antiretrovirals. NHS: do not take with warfarin; effects persist after stopping. [S: NHS medicines pages; Nicolussi 2020 `[S, unverified]`]
- **Vitamin K ↔ warfarin:** keep intake **consistent**, don't oscillate greens; sudden changes shift INR both directions. [S: https://ods.od.nih.gov/factsheets/VitaminK-HealthProfessional]
- Generic gate: anyone on warfarin/DOACs, transplant drugs, antiretrovirals, thyroid meds, lithium, methotrexate, or multiple daily prescriptions must clear every supplement with their pharmacist.

### 3.6 Reading a supplement label
Serving size vs dose (per-day totals if multi-servings); Supplement Facts lists each nutrient's amount + %DV — **"proprietary blend" totals hide per-ingredient doses** (can't check against evidence doses or ULs) — big red flag; "USP/NSF/Informed" seals vs meaningless "lab-tested" marketing words; source country; batch/expiry. Labeling rules per FDA dietary-supplement regulations [S: https://www.fda.gov/food/dietary-supplements].

---

## 4. Home Medical Devices

### 4.1 Blood pressure monitors
- Buy **upper-arm cuff** devices validated to **ISO 81060-2:2018 (universal standard)** or ESH protocol; check the device on **STRIDE BP** or **ValidateBP** (AMA) approved lists — validation claims printed on the box are often false. [S: https://pmc.ncbi.nlm.nih.gov/articles/PMC9867184 ; https://www.stridebp.org/bp-monitors]
- Wrist monitors: less accurate (position vs heart level, movement sensitivity) — acceptable only if validated and correctly positioned; **finger monitors: not reliable — do not stock/recommend**. Cuff size matters: wrong cuff width → clinically meaningful error; big arms need large cuffs. "Wellness" smartwatch BP readings are not validated diagnostics.

### 4.2 Glucometers
- Accuracy floor: **ISO 15197:2013** — ≥95% of readings within ±15 mg/dL (±0.83 mmol/L) when glucose <100 mg/dL and within ±15% when ≥100 mg/dL; 99% within clinically safe zones. CE-marked meters should declare ISO 15197:2013 compliance. [S: https://pmc.ncbi.nlm.nih.gov/articles/PMC5951056 ; https://drc.bmj.com/content/8/1/e001067]

### 4.3 Thermometers
- Rectal = gold standard, esp. <3 months (clinical decisions ride on it); axillary = screening only; tympanic (ear) = fast but technique-sensitive and unreliable <6 months; temporal artery/forehead = convenient screening; contactless = lowest accuracy of the validated types. [S: https://www.mayoclinic.org/diseases-conditions/fever/in-depth/thermometers/art-20046737 ; https://familydoctor.org/fever-temperatures-accuracy-and-comparison/]
- Advise one device per family used consistently (readings aren't interchangeable; ~0.3–0.6 °C offsets between sites).

### 4.4 Pulse oximeters
- FDA 2021 safety communication: SpO2 has **limits** — poor circulation, skin pigmentation, skin thickness, temperature, nail polish, tobacco, motion. Sjoding et al. (NEJM 2020): occult hypoxemia ~3× more often missed in Black patients. Do **not** rely exclusively on the number; watch cyanosis, breathlessness, tachycardia. Consumer fingertip units are least accurate vs medical-grade. [S: https://www.fda.gov/medical-devices/safety-communications/pulse-oximeter-accuracy-and-limitations-fda-safety-communication ; https://www.nejm.org/doi/full/10.1056/NEJMc2029240]

### 4.5 Nebulizers vs MDI+spacer
- For acute asthma in children, **MDI + holding chamber (spacer) is at least as effective as nebulization** (Cochrane CD000052) and cheaper/faster; nebulizers matter for infants, severe episodes under medical direction, or drugs only available that way. [S: https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD000052.pub5/full — standard Cochrane citation, content known, not re-verified this pass]

### 4.6 "Body composition" scales — the honesty line
- BIA scales measure **weight well** (±0.3 kg) but body-fat estimates carry individual errors of ~4–8% vs DXA, shift with hydration/food/exercise; single-frequency models worst. Present as trend-tracking only, never as clinical fat measurement. [S: https://pmc.ncbi.nlm.nih.gov/articles/PMC7283978]

### 4.7 Medical device vs "wellness" gadget — the tell
- CE-marked Class IIa/IIb or FDA-cleared devices must state intended medical use + standards (e.g., EN ISO 4074 condoms are Class IIb; ISO 81060-2 BP monitors; ISO 15197 meters). "Wellness" gadgets (smartwatch BP, "immune-boosting" frequency devices, non-validated smart scales) make no clinical claims for a reason. Stock/shell rule: for health decisions, only validated categories above.

---

## 5. Sexual Wellness & Family Planning (OTC scope)

### 5.1 Condoms
- Quality standard: **ISO 4074** (latex) — burst pressure/volume, freedom from holes, dimensions, pack integrity, shelf-life aging; EU CE-marked as Class IIb medical devices via EN ISO 4074 + notified body. Non-latex validated options: polyisoprene (latex-allergy friendly), polyurethane (transmits heat, works with oil-based lube `[S, unverified]` — check brand instructions). [S: https://www.iso.org/obp/ui/fr/#iso:std:iso:4074:ed-3:v1:en]
- Sizing reality: fit is by **nominal width** (flat width mm) — common global bands: snug ~47–49 mm, standard ~52–56 mm, XL ~56–60 mm; a wrong size = breakage/slippage. `[P]` Storage: cool, dry, out of sunlight/heat (wallets/gloveboxes damage latex); check expiry every time `[S, unverified]`.

### 5.2 Lubricants — osmolality/pH is the real quality axis
- WHO guidance: vaginal lubricants should have **osmolality <1200 mOsm/kg** and **pH ≈4.5** (anal: pH 5.5–7); most commercial water-based lubes are hyperosmolar (2,000–6,000 mOsm/kg) due to glycerin/propylene glycol, which draws water out of epithelial cells and can damage mucosa; reformulated compliant products exist. [S: https://extranet.who.int/prequal/sites/default/files/document_files/8-day2_session5.5_personallubricantsosmolality.pdf ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4190534]
- Selling rule: recommend iso-osmolar, pH-matched lubes; flag glycerin-heavy products to users with recurrent irritation; silicone/water hybrids for latex compatibility; "warming/tingling" additives are irritation risk `[S, unverified]`.

### 5.3 Family planning — the honesty line
- **Fertility apps:** Natural Cycles (the only FDA-cleared app) — typical use ~93% effective (~7 pregnancies/100 women-years), perfect use ~98%; requires daily adherence; ordinary period-trackers are *not* contraceptives. [S: https://pmc.ncbi.nlm.nih.gov/articles/PMC6475236]
- **Emergency contraception (market-checked):** levonorgestrel EC (1.5 mg) is OTC or pharmacist-dispensed without prescription in many countries (verify local access rules at dispatch); LNG is most effective as soon as possible (≤72 h window `[S, unverified]`); copper IUD is the most effective EC but needs a provider. [S, unverified: International Consortium for Emergency Contraception country database + Ammerdorffer et al. 2021 systematic review — verify the user's country at dispatch]
- **ED in young men = cardiovascular flag, not a lifestyle pill problem:** ED independently predicts CV events and can precede coronary disease by 2–5 years; guidance (Princeton Consensus) = screen cardiometabolic risk (lipids, glucose, BP) rather than selling performance products; sudden ED in a man <40 warrants medical evaluation. [S: https://pmc.ncbi.nlm.nih.gov/articles/PMC4442980]
- Persistent painful erection (priapism), post-ejaculatory bleeding, testicular pain/lumps, sudden ED after starting a drug → doctor. Performance-enhancement pills from informal channels = adulteration category #1 (§3.2).

---

## 6. First Aid & Home Kit

### 6.1 Wound care — moist beats dry
- Clean (running water), then **keep moist and covered**: Winter's 1962 landmark (Nature) + modern reviews — moist, occluded wounds re-epithelialize faster with less pain/scarring than air-dried scabs; plain petrolatum is adequate for clean minor wounds. [S: https://pmc.ncbi.nlm.nih.gov/articles/PMC8568799]
- Escalate: gaping edges, embedded debris, animal/human bites, wounds in diabetics, spreading redness/pus, any tetanus-status question (booster >5 y dirty wound / >10 y clean `[S, unverified]`).

### 6.2 Burns
- **Cool running water for 20 minutes**, started ASAP (benefit even if started later, best <3 h). **Never ice, iced water, butter, creams, or toothpaste.** Remove jewelry near the burn; cover with clean non-adherent cloth; seek care for large, deep, blistered, facial/genital/joint burns, chemical/electrical burns. [S: https://www.nhsinform.scot/illnesses-and-conditions/injuries/skin-injuries/burns-and-scalds ; https://www.redcross.org/take-a-class/resources/learn-first-aid/burns]

### 6.3 Anaphylaxis awareness
- Known severe-allergy households: keep **epinephrine auto-injector**, use it FIRST for breathing difficulty/swelling/collapse; antihistamines are adjuncts only and never replace epinephrine; call emergency services after injection. [S: https://acaai.org/allergies/management-treatment/epinephrine-auto-injector]
- Nosebleeds: lean forward, pinch soft part 10 min — not head back `[S, unverified]`. Seizure: protect, time it, nothing in the mouth `[S, unverified]`.

### 6.4 What NOT to keep
Expired medicines (rotate — see 6.5), ipecac syrup (obsolete `[S, unverified]`), hydrogen peroxide as routine antiseptic, home "cauterizing" agents, leftover antibiotics (self-prescribing drives antimicrobial resistance), anyone else's prescription meds (incl. epinephrine owned by another person).

### 6.5 Kit organization & expiry rotation
Single labeled box, alphabetical or by-use trays; every item dated on purchase; quarterly check; restock after every use; device items (BP/thermometer/spacer) stored away from heat; keep the pharmacist's discard program for expired drugs `[P, unverified]`.

---

## 7. Global Regulatory, Channel & Herbal Safety Context

- **Pharmacy = first-line safe channel.** Community pharmacies are the licensed channel for OTC medicines, supplements, and medical devices; the assistant must reinforce — never undermine — prescription rules (antibiotics, chronic meds).
- **National regulatory registration:** verify that medicines are registered with the user's national drug authority (e.g., FDA, EMA/national EU agency, MHRA, TGA, Health Canada, or local national regulator) before recommending any import/gray-market product.
- **Counterfeit/substandard risk:** WHO (2017): ~1 in 10 medical products in low/middle-income countries is substandard or falsified (most reported: antimalarials, antibiotics); global falsified-diabetes-product history. Buying rule: licensed pharmacies only; be suspicious of unusually cheap injectables/insulin and unverified online-only "pharmacies". [S: https://www.who.int/news/item/28-11-2017-1-in-10-medical-products-in-developing-countries-is-substandard-or-falsified ; https://pmc.ncbi.nlm.nih.gov/articles/PMC2787054]
- **Herbal/traditional remedies:** use is common across studied populations; a US baseline study found high non-disclosure to clinicians [S: https://pmc.ncbi.nlm.nih.gov/articles/PMC5593261] — the disclosure rate outside the US is unstudied at this level, so ask every user. Documented interactions: common herbs (St John's Wort, hibiscus, green tea, ginkgo, garlic supplements) can interact with anticoagulants, antihypertensives, and other prescriptions (interaction sources in §3.5) — always ask "what herbs or traditional remedies are you taking?" before OTC advice.
- **Fads:** blood-type diets have **no supporting evidence** (Cusack 2013 systematic review, AJCN; Toronto cohort 1,455 found no benefit). Diplomatic refusal + redirect to evidence-based patterns. [S: https://pubmed.ncbi.nlm.nih.gov/23697707]
- Practicalities: heat degrades stored medicines and condoms; where tap-water quality is uncertain, use boiled/cooled water for infant-prep contexts `[S, unverified]`.

---

## 8. Evidence Hierarchy & Sources

Rank (what each level reliably tells you):
1. **Cochrane/systematic reviews** — does the intervention work at all, pooled across trials (gold for "is this product pointless?").
2. **Clinical guidelines** (NICE, USPSTF, Endocrine Society, AAFP, Princeton) — what experts recommend in practice, incl. red flags and escalation thresholds.
3. **Regulatory monographs/labels** (FDA Drug Facts, EMA, MHRA, national regulators) — exact doses, hard limits, warnings; the legal floor.
4. **Pharmacist references** (DailyMed, StatPearls, AHFS) — practical dosing and interaction detail.
5. **User reviews** — real-world signal for devices/tolerability; noisy, never for efficacy or safety.
6. **Marketing** — tells you only what the seller wants; treat claims as noise; the skill's adversarial layer.

Consolidated hierarchy table:

| Tier | Answers | Use for | Distrust for |
|---|---|---|---|
| Cochrane/meta-analyses | Efficacy truth | Category kill-lists (cough syrups) | Dosage specifics |
| Guidelines | Escalation, first-line | Red flags, duration rules | Brand choice |
| Regulatory labels | Doses, limits, warnings | Everything dosed | Off-label suitability |
| Pharmacist refs | Practical detail | Interactions, device technique | — |
| Reviews | Fit, usability | Device shopping | Efficacy claims |
| Marketing | Nothing reliable | Ignoring | Everything |

---

## Self-Medication Limits — Summary Table (category × max duration × escalate-when)

| Category | Max self-treatment | Escalate when |
|---|---|---|
| Pain (adults, paracetamol/ibuprofen) | 10 days | Pain worse/persists >10 days; MOH pattern ≥15 d/mo |
| Fever (adults) | 3 days | Fever >3 days, or any red flag (§2.1) |
| Fever (infant <3 months) | 0 — no self-treatment | Any fever: urgent doctor |
| Cough/cold adults | 7 days (label rule) | >7 days, worsening, chest pain, breathlessness |
| Cough/cold children <4 | Not self-treated | Any illness → pharmacist/doctor |
| Oral antihistamines (allergy) | ~2 weeks | No control, or chronic symptoms need diagnosis |
| Heartburn — antacid/H2 | 14 days | Symptoms persist/worsen; dysphagia; GI bleeding signs |
| Heartburn — OTC PPI | 14 days, ≤3 courses/year (every 4 months) | Needs a second course sooner; new/worse symptoms |
| Nasal decongestant spray | 3 days (`[S, unverified]` rebound rhinitis) | Congestion past 3 days → doctor |
| Topical antibiotic/antifungal | 7 days | No improvement in 7 d, spreading infection |
| Laxatives | ≤7 days (label rule) | Chronic constipation needs diagnosis |
| Diarrhea OTC | 2 days (label rule) | Blood, high fever, dehydration, >2 days |
| EC (levonorgestrel) | Single use per episode | Recurrent use → real contraception planning |
| Supplements (any) | Per-purpose courses | Megadose (>UL), any prescription-drug user → pharmacist gate |

## Hard Safety Rails

- **Immediate-escalation red flags:** chest pain; infant <3 months any fever; fever >3 days or with neck stiffness/non-blanching rash/confusion; severe or rapidly worsening symptoms; breathlessness; vomiting blood/black stools; suicidal ideation; first-ever severe headache ("worst of my life").
- **Children:** weight-based dosing + calibrated device only (no kitchen spoons); never aspirin in viral illness (Reye); no OTC cough/cold <4 years; verify age bands.
- **Pregnancy/breastfeeding:** paracetamol = acceptable choice; NSAIDs avoided ≥20 weeks (FDA 2020); pseudoephedrine avoided (1st trimester/breastfeeding); every product gate-checked — herbal too.
- **Interaction gates (stop-ship):** St John's Wort with warfarin/OCP/transplant drugs; NSAIDs with anticoagulants, CKD, ≥3 alcoholic drinks/day; vitamin K oscillation on warfarin; acetaminophen stacking across combo products; supplements for anyone on multiple prescriptions → pharmacist clearance first.
- **Product-integrity gates:** only locally registered medicines; only validated devices (ISO 81060-2 / ISO 15197 / FDA-cleared); only certified supplements (USP / NSF-CFS / Informed Sport) where stocked; assume adulteration in sexual-enhancement/weight-loss/bodybuilding from informal channels.

---

## Sources

Primary/verified:
- Cochrane OTC acute cough: https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD001831.pub5/full
- Cochrane honey for cough: https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD007094.pub5/full
- Cochrane spacers vs nebulizers: https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD000052.pub5/full
- FDA OTC heartburn/PPI rules: https://www.fda.gov/drugs/understanding-over-counter-medicines/over-counter-otc-heartburn-treatment
- FDA PPI fracture DSC: https://www.fda.gov/drugs/drug-safety-and-availability/possible-fracture-risk-high-dose-long-term-proton-pump-inhibitors-ppi-use
- FDA NSAID CV warning 2015: https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-strengthens-warning-non-aspirin-nonsteroidal-anti-inflammatory
- FDA NSAIDs pregnancy ≥20 weeks 2020: https://www.fda.gov/drugs/drug-safety-and-availability/fda-recommends-avoiding-use-nsaids-pregnancy-20-weeks-or-later-because-they-can-result
- Ibuprofen OTC label (DailyMed): https://www.dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=3b3b9e31-6387-1260-e054-00144ff88e88&type=pdf
- FDA tainted supplements DB: https://www.fda.gov/drugs/medication-health-fraud/tainted-products-marketed-dietary-supplements-conventional-foods ; RAPS/Tucker: https://www.raps.org/resource/study-raises-questions-over-fdas-handling-of-adulterated-supplements.html
- USPSTF vitamins 2022: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/vitamin-supplementation-to-prevent-cvd-and-cancer-preventive-medication
- USPSTF vitamin D screening: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/vitamin-d-deficiency-screening
- Endocrine Society vit D CPG: https://www.endocrine.org/clinical-practice-guidelines/vitamin-d-for-the-prevention-of-disease
- CDC folic acid: https://www.cdc.gov/folic-acid/about/index.html
- ISSN creatine: https://www.tandfonline.com/doi/full/10.1186/s12970-017-0173-z ; ISSN protein: https://pubmed.ncbi.nlm.nih.gov/28642676
- Omega-3 Rx vs supplement: https://pmc.ncbi.nlm.nih.gov/articles/PMC6999166
- ULs table: https://www.ncbi.nlm.nih.gov/books/NBK278991/table/diet-treatment-obes.table17die ; NIH ODS: https://ods.od.nih.gov/
- Vitamin K–warfarin: https://ods.od.nih.gov/factsheets/VitaminK-HealthProfessional
- Reye syndrome: https://www.ncbi.nlm.nih.gov/books/NBK526101
- ICHD-3 MOH: https://ichd-3.org/8-headache-attributed-to-a-substance-or-its-withdrawal/8-2-medication-overuse-headache-moh ; StatPearls MOH: https://www.ncbi.nlm.nih.gov/books/NBK538150
- NICE NG143 + traffic light: https://www.nice.org.uk/guidance/ng143
- Kitchen-spoon dosing errors: https://pmc.ncbi.nlm.nih.gov/articles/PMC8228905
- NHS pseudoephedrine: https://www.nhs.uk/medicines/pseudoephedrine/ ; UKTIS decongestants: https://www.medicinesinpregnancy.org/leaflets-a-z/decongestants
- BP validation review: https://pmc.ncbi.nlm.nih.gov/articles/PMC9867184 ; STRIDE BP: https://www.stridebp.org/bp-monitors
- ISO 15197 accuracy: https://pmc.ncbi.nlm.nih.gov/articles/PMC5951056 ; https://drc.bmj.com/content/8/1/e001067
- FDA pulse oximeter safety communication: https://www.fda.gov/medical-devices/safety-communications/pulse-oximeter-accuracy-and-limitations-fda-safety-communication ; Sjoding NEJM: https://www.nejm.org/doi/full/10.1056/NEJMc2029240
- Thermometers: https://www.mayoclinic.org/diseases-conditions/fever/in-depth/thermometers/art-20046737 ; https://familydoctor.org/fever-temperatures-accuracy-and-comparison/
- BIA accuracy: https://pmc.ncbi.nlm.nih.gov/articles/PMC7283978
- ISO 4074 condoms: https://www.iso.org/obp/ui/fr/#iso:std:iso:4074:ed-3:v1:en
- WHO lubricant osmolality: https://extranet.who.int/prequal/sites/default/files/document_files/8-day2_session5.5_personallubricantsosmolality.pdf ; lubricant characterization: https://pmc.ncbi.nlm.nih.gov/articles/PMC4190534
- Natural Cycles effectiveness: https://pmc.ncbi.nlm.nih.gov/articles/PMC6475236
- ED–cardiovascular: https://pmc.ncbi.nlm.nih.gov/articles/PMC4442980
- Moist wound healing: https://pmc.ncbi.nlm.nih.gov/articles/PMC8568799
- Burns: https://www.nhsinform.scot/illnesses-and-conditions/injuries/skin-injuries/burns-and-scalds ; https://www.redcross.org/take-a-class/resources/learn-first-aid/burns
- Anaphylaxis: https://acaai.org/allergies/management-treatment/epinephrine-auto-injector
- WHO falsified medicines: https://www.who.int/news/item/28-11-2017-1-in-10-medical-products-in-developing-countries-is-substandard-or-falsified
- Blood-type diet: https://pubmed.ncbi.nlm.nih.gov/23697707
- Herbal-use prevalence: https://pmc.ncbi.nlm.nih.gov/articles/PMC5593261

Flagged as reliable-but-not-re-verified `[S, unverified]`: FDA pediatric cough-cold consumer page URL; NHS paracetamol-in-pregnancy page URL; acetaminophen 4 g label text (standard Drug Facts); neomycin allergen rates (ACDS); nasal-spray 3-day rebound rule; tetanus booster windows; condom sizing bands; LNG EC 72-h window; StatPearls/fact-sheet URLs not re-fetched.

## Appendix — health profile template (the template of record; SKILL.md holds the operative rules)

Copy this verbatim when creating the profile file (empty except consent):

```markdown
---
schema: product-scout-health-profile
version: 1
created: <date>
updated: <date>
consent:
  enabled: true
  consent_date: <date>
  scope: [drug-allergies, conditions, medications, herbal-remedies,
          pregnancy, ongoing-treatments, device-readings]
---

# Health profile

User-owned file: edit or delete any line. Deleting the whole file
erases everything — the agent keeps no other copy except any legacy
original it notified you about during migration.

## Core facts (user-stated; each with date stated)
- Drug allergies / intolerances: <stated, dated>
- Chronic conditions: <dated>
- Medications (prescription + regular OTC, with purpose): <dated —
  RECONFIRM if older than 6 months>
- Herbal / traditional remedies in use: <dated — re-ask whenever a
  dosed medicine or supplement is discussed>
- Pregnancy / breastfeeding: <dated — RECONFIRM in-session before any
  NSAID, decongestant, or supplement-dosing advice>

## Ongoing self-treatment log (append-only, newest last, keep ~10)
- <date> | <symptom | product + dose> | IMPROVING/NO-CHANGE/WORSE |
  <days treated>

## Device readings (user-reported; trend context only — never diagnosis)
- <date> | <device> | <reading>

## Derived observations (agent-inferred; NEVER hard exclusions)
- [<date> | <confidence> | <source>] <observation — suggestive only>

## Agent rules (do not edit this section)
- A current-session user statement ALWAYS overrides any line above.
- Ask before saving anything new; save nothing unconfirmed. (The one
  exception: the one-time location migration of an existing consented
  profile, which runs without asking.)
- Never re-ask a core fact dated within 6 months; do re-ask older ones.
- Stated drug allergies are hard filters; derived observations hints.
- No diagnosis language here; suspected disease goes to referral.
- Overlap with beauty.md: contradictions AND omissions → ask the
  user; on confirmation update both files the same day.
```

The six guardrails these rules implement are enumerated in SKILL.md
Step 0 and remain authoritative there.
