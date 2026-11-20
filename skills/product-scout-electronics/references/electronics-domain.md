# Electronics & Tech Purchases — Domain Knowledge Base

> Family rule: where this file and the skill's SKILL.md disagree, SKILL.md's
> operative wording wins — spec claims, update-policy numbers, and red-flag
> rules are stated authoritatively in SKILL.md; this file explains and
> sources them.

## Method note

- Researched against primary and secondary sources: manufacturer support/spec pages (Google, Samsung, Apple, Microsoft, Xiaomi, NVIDIA), independent test labs (RTINGS, NotebookCheck, TFTCentral, DXOMARK, GSMArena), and benchmark vendors' own methodology docs (Primate Labs/Geekbench, UL/3DMark). Research date: 2026-11-08.
- Verification status: claims are cited inline with URLs. Items that could not be traced to a first-party methodology page or official policy are marked **[unverified]**. Where sources conflict (e.g., Xiaomi's update tiers), the conflict is noted. Vendor marketing pages were used only to document what the vendor promises, never to grade the vendor's own products.
- Scope: phones, laptops, TVs/monitors, audio, cameras, gaming hardware, wearables, components/peripherals across all global markets.

---

## 1. Spec literacy map — what predicts experience vs marketing noise

### 1.1 Phones

| Spec | Verdict | Evidence |
|---|---|---|
| SoC generation + tier (e.g., Snapdragon 8/7/6/4 series, Dimensity 9/8/7/6) | Predicts performance, efficiency, camera ISP, and how long the phone stays smooth. Tier digit = market positioning; "s" variants are lower-binned derivatives marketed as near-flagship — check the actual chip, not the badge. | https://en.wikipedia.org/wiki/List_of_Qualcomm_Snapdragon_systems_on_chips |
| Megapixel count | Mostly noise. GSMArena shows 48MP+ Quad-Bayer sensors "can't offer much more detail than a 12MP sensor" due to binning; real drivers are sensor size, pixel size, OIS, and processing. | https://www.gsmarena.com/quad_bayer_sensors_what_they_are_and_what_they_are_not-news-38468.php |
| Sensor size + OIS + processing | The actual camera predictors. GSMArena's camera comparisons weigh sensor area (~3.6x area advantage decides ultra comparison outcomes) and stabilization. | https://www.gsmarena.com/oppo_find_x8_ultra_vs_samsung_galaxy_s25_ultra_vs_xiaomi_15_ultra-review-2878.php |
| Storage class | UFS 3.1 ≈ 2,100/1,200 MB/s read/write; UFS 4.0 ≈ 4,200/2,800 MB/s with ~46% better power efficiency — but a same-brand UFS 3.1 vs 4.0 A/B test showed an 11.2 GB copy only ~7 s faster; daily app launches barely differ. UFS 4.0 matters most for installs, big transfers, 4K video. eMMC (~400 MB/s) on cheap phones is a real bottleneck. | https://www.notebookcheck.net/How-does-Notebookcheck-test-laptops-and-smartphones-A-behind-the-scenes-look-into-our-review-process.15394.0.html ; UFS numbers per JEDEC-class reporting **[unverified primary JEDEC doc]** |
| RAM amount/type | Chase capacity tier (8 GB fine, 12 GB comfortable for power users); LPDDR generation matters less than SoC tier. RAM is rarely a differentiator beyond ~8 GB. | General expert consensus **[no single lab methodology]** |
| Display | Predictors: panel type (LCD vs OLED — OLED wins contrast/HDR), measured peak nits (outdoor visibility), refresh (90-120 Hz), PWM dimming frequency (flicker-sensitive users should pick high-frequency PWM or DC dimming; TFTCentral documents PWM strain mechanisms). | https://tftcentral.co.uk/articles/pulse_width_modulation ; https://www.rtings.com/tv/tests/picture-quality/hdr-peak-brightness |
| Battery | mAh alone is noise; efficiency (SoC node + display) and thermal design decide runtime. Judge by standardized tests, not capacity. | https://www.gsmarena.com/how_we_test_gsmarena_battery_life_test_20-news-60650.php |

### 1.2 Laptops

- CPU tier suffix predicts thermals/battery better than model number: Intel U-series = efficiency, H/HS/HX = performance with shorter battery life; misunderstanding suffixes is the classic mis-buy. https://www.tomshardware.com/laptops
- CPU generation matters more than core count for responsiveness; old chips in new shells are a recurring trap (see section 5).
- Storage: NVMe PCIe SSD (3,000+ MB/s) vs eMMC (~400 MB/s, soldered) is a "night-and-day" difference — eMMC on any laptop above the cheapest tier is a red flag. **[expert consensus; measure via NotebookCheck SSD DB]** https://www.notebookcheck.net/Benchmarks-and-Test-Results.5431.0.html
- RAM: 16 GB is the 2025/26 standard recommendation; 8 GB only for light use; many thin laptops solder LPDDR so you cannot upgrade later — verify before buying 8 GB. https://www.pcmag.com/explainers/ram-reality-check-how-much-memory-does-your-pc-actually-need-in-2026
- Display: judge by measured brightness (nits), contrast, PWM, and sRGB coverage — NotebookCheck measures all per review; laptop marketing "nits" are often measured differently than labs. https://www.notebookcheck.net/Our-Rating-Criteria.2120.0.html
- Battery: judge by measured WLAN/video runtime, not Wh capacity or vendor hours. NotebookCheck's rating criteria explicitly weight realistic WiFi/video runtimes. https://www.notebookcheck.net/Our-Rating-Criteria.2120.0.html
- Serviceability: replaceable SODIMM slots + accessible M.2 extend useful life; soldered everything = a disposable device. **[expert consensus]**

### 1.3 TVs & monitors

- Panel tech: OLED (WOLED/QD-OLED) = per-pixel light, near-infinite contrast, near-instant response (WOLED response "significantly faster than even the fastest QLED"); QLED/Mini-LED = higher peak brightness, no burn-in risk. Neither is universally "better" — match to room light. https://www.rtings.com/tv/learn/oled-vs-qled
- Measured peak brightness (HDR, in nits across window sizes) — the marketing number is usually a tiny-window record; RTINGS publishes measured values. https://www.rtings.com/tv/tests/picture-quality/hdr-peak-brightness
- Input lag (ms at your resolution/refresh) — decisive for gaming; RTINGS measures with dedicated hardware. https://www.rtings.com/tv/tests/inputs/input-lag
- HDMI 2.1 bandwidth (40-48 Gbps) per port enables 4K@120Hz + VRR for PS5/Series X; many TVs only give full bandwidth on 1-2 ports — check port map. https://www.rtings.com/tv/learn/hdmi-2-1
- PWM/flicker and OLED VRR flicker: measurable and matters to sensitive users; TFTCentral tests WOLED vs QD-OLED flicker behavior. https://tftcentral.co.uk/articles/exploring-and-testing-oled-vrr-flicker
- Burn-in risk: real but manageable; RTINGS runs a multi-year OLED burn-in torture test with measured luminance loss. https://www.rtings.com/tv/tests/longevity/burn-in
- Noise: "8K," dynamic-contrast marketing numbers, and inflated "motion rate" figures. Size should come from viewing distance math: 4K detail is only resolvable within ~1.2-1.6x diagonal (65" ≈ 4 ft for full 4K detail). https://www.rtings.com/tv/reviews/by-size/size-to-distance-relationship

### 1.4 Audio

- Sound quality: frequency-response-to-target and distortion, measured on rigs — RTINGS measures impedance/sensitivity and rates against a target curve. https://www.rtings.com/headphones/learn/how-we-test
- ANC: real isolation curves across frequency, not a marketing dB claim. https://www.rtings.com/headphones/learn/what-is-anc
- Bluetooth codec + latency: measured per codec (SBC/AAC/aptX/LDAC); codec choice affects latency far more than price tier. https://www.rtings.com/headphones/learn/bluetooth-tests-score
- Noise: "driver size (mm)" and premium-codec badges without measurement; also price-as-quality assumptions — RTINGS' distortion research shows audibility limits complicate "better spec = better sound." https://www.audiosciencereview.com/forum/index.php?threads/rtings-study-on-distortion-audibility-in-headphones-and-iems.69349

### 1.5 Cameras (dedicated)

- Sensor size (format), lens aperture, IBIS/OIS, and AF system predict results; MP count is secondary at fixed sensor size (same GSMArena principle as phones). https://www.gsmarena.com/quad_bayer_sensors_what_they_are_and_what_they_are_not-news-38468.php **[camera-body-specific: no dedicated lab methodology cited — unverified beyond phone analog]**
- Video specs: bitrate, codec (H.265/10-bit), and rolling shutter/AF during video matter more than "8K" badge capability — DPReview's camera reviews score these directly (e.g., praising 10-bit capability while criticizing "quite poor" rolling shutter, independent of resolution badges). [S 2026-11 — DPReview EOS R50 V review: https://www.dpreview.com/reviews/canon-eos-r50-v-review]

### 1.6 Gaming hardware

- GPUs: architecture generation + VRAM capacity/type predict game performance; RTX 50-series data shows generation-over-generation uplift can be small (RTX 5070 ≈ +5% raster over 4070 Super) — check measured benchmarks, not naming. https://en.wikipedia.org/wiki/GeForce_RTX_50_series
- Consoles: real predictors are GPU tier + SSD speed + whether the TV chain supports HDMI 2.1/VRR. https://www.rtings.com/tv/learn/hdmi-2-1
- Gaming laptops: GPU wattage (TGP) within the same GPU model changes performance materially; chassis cooling > GPU name. **[expert consensus — NotebookCheck reviews measure per-unit]** https://www.notebookcheck.net/Our-Rating-Criteria.2120.0.html

### 1.7 Wearables

- WatchOS/Wear OS support window, sensor set (ECG/SpO2), GPS accuracy, and battery-in-days (Garmin-class) predict satisfaction; step-count and "sports mode count" are noise. https://endoflife.date/apple-watch **[Garmin: no official fixed policy — unverified; re-checked 2026-11 — Garmin publishes no EOL page and endoflife.date does not cover Garmin]**

---

## 2. Update-support lifespans (2024-2026 state)

Software support is a first-class purchase criterion: it defines security exposure, resale value, and how many years the device stays usable. Verified commitments:

| Brand / category | Commitment | Source |
|---|---|---|
| Google Pixel 8+ | 7 years OS + security (from US store availability); Pixel 6 era = 5 years | https://support.google.com/pixelphone/answer/4457705?hl=en |
| Samsung Galaxy (Jan 2024 policy) | Up to 7 years security; S24/S25, Z Fold/Flip 6+, Tab S10+ = 7 gen OS + 7 yr security; A56/A36 = 6 yr; budget models 2 OS gens | https://security.samsungmobile.com/workScope.smsb |
| Apple iPhone | No published year count; de facto ~6-7 major iOS versions (iPhone XR/XS: 6 majors, dropped at iOS 26) + longer security patches; parts/service ~5+ yrs; "obsolete" = 7 yrs after last sale, then no service/parts | https://www.apple.com/os/ios ; https://support.apple.com/en-us/102772 ; https://endoflife.date/iphone |
| OnePlus flagship (12/13) | 4 major Android versions + 6 years security (shipped version not counted); R-series ~4 OS + 5-6 yr security; portfolio minimum 3 yr security | https://www.bgr.com/2247704/oneplus-phones-that-have-software-support-until-2029 |
| Xiaomi | Official floor: "at least 2 years" security after first shipment; per-model EOL list on trust.mi.com (newer flagships listed to 2032); Redmi/POCO historically 2-3 OS + 3-4 yr security. Conflicting third-party claims of 5-6 yr policies **[treat as unverified until listed per model]** | https://trust.mi.com/misrc/updates/phone |
| Windows PCs | Windows 10 support ended 2025-10-14 (ESU paid extension); Windows 11 requires TPM 2.0/Secure Boot/8th-gen+ Intel or Ryzen 2000+ — old-but-cheap laptops can be cut off from the OS entirely | https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025 |
| TVs | Samsung: 7 years Tizen OS + security updates for 2024+ models (previously ~5; LG historically ~2, most brands unpublished) | https://www.bgr.com/2290606/how-long-will-samsung-smart-tv-get-software-updates |
| Smartwatches | Apple Watch ≈ 4-5 majors (watchOS 27 dropped Series 8/Ultra 1/SE 2 ≈ 4 yrs); Garmin: no fixed policy, in practice feature updates ~2-3+ yrs (popular lines longer, per community firmware tracking) **[unverified — no official page; re-checked 2026-11, still none]** | https://endoflife.date/apple-watch |

Why it matters: a phone with 2 years of updates can be insecure and unsellable while a same-price phone with 7 still has value; TVs are replaced far less often than phones, so TV firmware windows matter more than people assume; Windows hardware requirements mean CPU generation is a longevity spec, not just a speed spec.

---

## 3. Benchmarks & evidence hierarchy

What each trusted source measures:

- **Geekbench 6/7** (Primate Labs): CPU responsiveness, single/multi-core composite from real-workload sub-tests; official internals doc. Caveat: multi-core uses shared-memory workloads — many-core designs underperform vs real throughput; v7 recalibrated baselines and added AI workloads. https://www.geekbench.com/doc/geekbench6-benchmark-internals.pdf
- **AnTuTu**: holistic device score (CPU/GPU/memory/UX/storage). Weakness: repeatedly gamed — Realme GT banned 3 months (2021), Samsung/Geekbench banned Galaxy S22-class devices (2022) for benchmark-detection boosting, Huawei/Honor caught boosting for benchmark apps. Treat AnTuTu as a ranking hint, never a decision-maker. https://www.mensxp.com/technology/smartphones/86880-smartphone-companies-caught-cheating-on-benchmark-apps.html
- **3DMark (Wild Life/Steel Nomad)**: cross-platform GPU stress with sustained-load segments — the right tool for gaming claims.
- **DXOMARK camera**: lab + perceptual protocol; overall = Photo, Zoom, Bokeh, Preview, Video sub-scores; ~90-page reports. Protocol v6 elevated HDR/portrait/zoom to match real use. https://www.dxomark.com/what-we-test-camera ; https://www.dxomark.com/how-we-test
- **RTINGS**: measurement-driven TV/audio reviews — measured HDR peak brightness, EOTF tracking, input lag by resolution/refresh, per-codec headphone latency, multi-year OLED burn-in test. https://www.rtings.com/tv/tests/picture-quality/hdr-peak-brightness ; https://www.rtings.com/headphones/learn/how-we-test
- **GSMArena**: phone battery Life Test 2.0 — call/web/video/gaming at standardized brightness → Active Use Score (idle drain excluded, unlike the old Endurance Rating). https://www.gsmarena.com/how_we_test_gsmarena_battery_life_test_20-news-60650.php
- **NotebookCheck**: per-unit display measurements, noise/thermal, WLAN battery runtime; standardized across thousands of devices with a public database. https://www.notebookcheck.net/How-does-Notebookcheck-test-laptops-and-smartphones-A-behind-the-scenes-look-into-our-review-process.15394.0.html
- **TFTCentral**: monitor panel deep-dives (PWM, VRR flicker, coating). https://tftcentral.co.uk/articles/exploring-and-testing-oled-vrr-flicker
- **Tom's Hardware**: component-level analysis and long-running review practice; AnandTech archives (ended 2024) remain a primary reference for SoC/GPU deep dives. https://www.tomshardware.com/laptops

**Evidence hierarchy for any electronics claim:**

1. Independent lab measurement (RTINGS, NotebookCheck, TFTCentral, DXOMARK lab protocols)
2. Reputable expert review with hands-on testing (GSMArena, Tom's Hardware, AnandTech archives)
3. Aggregated user reviews / community data (volume + recency weighted)
4. Vendor spec sheet / marketing claim — never sufficient alone; benchmarks can be gamed (see AnTuTu history above)

Rank decisions: when levels conflict, prefer the higher level; when only marketing exists for a claim, mark it unverified in your own reasoning.

---

## 4. Market structure & pricing dynamics

### 4.1 Release cadences

- **Flagship phones**: annual (Sept-Oct for Apple/Pixel; Jan-Feb for Galaxy S). Prices fall most ~2-3 months before the successor launches as retailers clear stock; the successor's launch triggers an official $100-200+ cut on the previous model. https://www.techradar.com (deal coverage; cadence **[general retail reporting, no single canonical page]**)
- **GPUs**: NVIDIA has kept a ~2-year major cadence (RTX 20→30→40→50; Blackwell announced CES 2025) with mid-cycle SUPER refreshes; AMD RDNA and Intel Arc follow similar ~2-year spacing. https://en.wikipedia.org/wiki/GeForce_RTX_50_series
- **CPUs**: annual ticks (Intel/AMD mobile) — "buy last gen at discount" usually wins outside top-tier needs. [P 2026-11 — stable buying heuristic commonly reported by deal/laptop buying guides and launch-cycle coverage]
- **TVs**: CES announces in January; street availability spring (Mar-Jun); the best value window is Feb-Apr when last year's flagships are cleared. Major sale events have the lowest absolute prices but skew to mid/entry models. **[aggregated buying-guide reporting]**

### 4.2 When buying is smart

- Post-successor-launch purchase of the previous generation is the highest value-per-currency play (supported by the phone price-drop data above).
- Sale seasons (Black Friday / White Friday / Singles' Day / Prime Day / back-to-school) for accessories and mid-tier gear; launch windows are the worst time for flagship buyers (early-adopter premium + firmware immaturity).

### 4.3 Regional & grey-import checks (verify per user market)

- **Telecom / IMEI registration & band support**: several countries require imported phones to register their IMEI with the national telecom authority or pay import fees within a grace window; check cellular bands and local registration rules before recommending a grey-market handset. [P 2026-11 — varies by country; verify the exact rule and fee at dispatch]
- **Warranty**: officially imported units get manufacturer warranty via authorized local service centers; grey/parallel imports usually fall outside local warranty or depend on "international warranty" the local distributor may not honor (see INTA overview: https://www.inta.org/topics/parallel-imports). [P 2026-11]
- **Power**: verify local mains voltage/plug compatibility (120V/60Hz vs 220–240V/50Hz) — irrelevant for dual-voltage chargers ("100-240V" on the label), critical for single-voltage devices.
- **Region locks**: streaming-app availability, keyboard layouts, and cellular band support can differ between regional SKUs. [P, unverified per-SKU — check the specific SKU at dispatch]
- **After-sales as a purchase factor**: brands with thin local service coverage turn cheap purchases into expensive repairs; prefer brands with documented local service in the user's market. [P — general guidance]

---

## 5. Common buyer mistakes & red flags

1. **Megapixel chase** — 200MP phone cameras are binned down; sensor size/OIS/processing decide quality. Fix: read lab comparisons, ignore MP. https://www.gsmarena.com/quad_bayer_sensors_what_they_are_and_what_they_are_not-news-38468.php
2. **RAM chasing / future-proofing overspend** — paying flagship prices for specs you won't use; 16 GB is enough for most laptops; "future-proof" usually means "pay now for performance that gets cheaper later." https://www.pcmag.com/explainers/ram-reality-check-how-much-memory-does-your-pc-actually-need-in-2026
3. **eMMC sold as "fast storage"** — eMMC ≈ 400 MB/s vs NVMe 3,000+ MB/s; listings say "SSD" or "fast flash" for eMMC. Fix: require "NVMe PCIe SSD." **[expert consensus]**
4. **Refresh-old-chip-in-new-shell** — last year's SoC re-shelled and sold as new-gen (also "s"-tier chips marketed as flagship). Fix: check the actual chipset model, not the model name or marketing. https://en.wikipedia.org/wiki/List_of_Qualcomm_Snapdragon_systems_on_chips
5. **No-name brands with inflated spec sheets** — firmware can lie: fake RAM/storage/Android version/CPU model on cheap tablets; fake-capacity USB/SD (16 GB chip reporting 2 TB) corrupts data silently. Fix: Fake Device Test / CPU-Z cross-check for devices; H2testw (Windows) or F3 (Linux/macOS) for flash; treat "2TB for $20" as counterfeit by definition. https://industrialmonitordirect.com/blogs/knowledgebase/detecting-fake-usb-drives-with-h2testw-complete-guide
6. **Refurbished sold as new** — letter grades (A/B/C) describe cosmetics only; Amazon Renewed has 4 tiers (Premium/Excellent/Good/Acceptable) with 90-day guarantee; Apple Certified Refurbished = new battery/shell, 1-year warranty, "F" model prefix. If a "new" phone's warranty clock started months ago, it was used. Fix: check warranty start date + model prefix. https://www.amazon.com/gp/help/customer/display.html?nodeId=GRAS7M4E8YJCLWH7
7. **Counterfeit units** — fake iPhones/Galaxy units exist; verify IMEI and serial on the manufacturer's coverage page before/after purchase. **[procedure guidance]**
8. **Benchmark-trusting purchases** — scores gamed by OEMs (banned devices list above). Fix: look for sustained-load and thermals, not peak scores. https://www.mensxp.com/technology/smartphones/86880-smartphone-companies-caught-cheating-on-benchmark-apps.html
9. **Ignoring update windows** — especially TVs and budget Android; see section 2.
10. **TV size/distance mismatch and HDMI port assumptions** — wrong panel for the room; only some ports have HDMI 2.1 bandwidth. https://www.rtings.com/tv/reviews/by-size/size-to-distance-relationship

---

## 6. Sub-domain decision drivers (questions that determine the right purchase)

### Phones
1. Which SoC generation/tier exactly (chip model, not phone model)?
2. How many OS/security years remain or are promised (section 2)?
3. Camera priorities: main sensor size/OIS vs zoom vs selfie — which does the user actually shoot?
4. Display: OLED vs LCD, PWM sensitivity, measured brightness for outdoor use?
5. Battery: measured Active Use Score, not mAh?
6. Storage: UFS 3.1+ confirmed; enough capacity (no hybrid slots)?
7. Regional: local carrier bands / IMEI rules? local warranty?

### Laptops
1. Workload class (browsing/office vs dev vs gaming vs video editing) → CPU tier and GPU necessity?
2. CPU suffix U/P/H and generation — matched to workload and battery needs?
3. RAM 16 GB minimum, and is it soldered?
4. Storage NVMe (not eMMC), and second M.2 slot for expansion?
5. Battery: measured WLAN runtime vs user's mobility?
6. Display: measured nits/contrast/PWM for the user's environment?
7. OS longevity: meets Windows 11 requirements (TPM 2.0 etc.)?
8. Serviceability: SODIMM/M.2 access, local service?

### TVs / monitors
1. Viewing distance → size (RTINGS distance chart)?
2. Room light: bright room → high-brightness LED/Mini-LED; dark room → OLED?
3. Gaming: HDMI 2.1 on the ports you'll use, 120 Hz, VRR, measured input lag?
4. Content: HDR (measured nits/EOTF) vs mostly SDR broadcast?
5. OS/app availability + firmware update window (7 yrs Samsung 2024+)?
6. Burn-in tolerance for the user's usage pattern (static UI)?
7. Monitor-specific: PWM/flicker sensitivity, coating (matte vs glossy)?

### Audio
1. Use case: commuting (ANC + isolation curves), desk (comfort + mic), sports (fit/rating)?
2. Codec/latency needs (gaming/video = low-latency codec; Apple ecosystem = AAC behavior)?
3. Measured sound signature vs target — bass-heavy vs neutral?
4. Battery + charging case math for true wireless?
5. Mic quality for calls (measured, not claimed)?
6. Multipoint/OS compatibility?

### Cameras
1. Stills or video primary? (video → codec/bitrate/AF, not stills MP)
2. Sensor format vs portability tradeoff?
3. Lens ecosystem for the mount (bodies die, lenses persist)?
4. IBIS needed (handheld low light)?
5. Battery/charging workflow, dual card slots (professional use)?

### Gaming hardware
1. Target resolution/refresh (1080p/1440p/4K) → GPU tier and VRAM?
2. TV/monitor chain supports 120 Hz + VRR (HDMI 2.1 port map)?
3. For laptops: GPU TGP and thermals, not the GPU name?
4. Console vs PC: exclusives, subscription ecosystem, TV space?
5. Controller/accessory latency and platform pairing?

### Wearables
1. Phone ecosystem lock (Apple Watch = iPhone only; Wear OS pairing)?
2. Update window remaining (4-5 yrs Apple; Garmin indefinite — community-reported, no official page **[unverified]**)?
3. Battery days vs charge-night habit?
4. Health sensors actually used (ECG/SpO2/GPS accuracy)?
5. Ruggedness/water rating for the user's sport?

### Components / peripherals
1. PSU quality (watts + tier) over RGB; do not cheap out?
2. Storage endurance/warranty (TBW) vs capacity?
3. Peripherals: switch/latency type for use, wired vs wireless latency measured?
4. Compatibility chain (motherboard BIOS for new CPUs, RAM speed support)?

---

## Evidence hierarchy summary

| Level | Source class | Examples | Use for |
|---|---|---|---|
| 1 | Independent test labs | RTINGS, NotebookCheck, TFTCentral, DXOMARK | Display/brightness/lag/ANC/battery/camera measurements |
| 2 | Expert reviews w/ testing | GSMArena, Tom's Hardware, AnandTech archives | Real-world behavior, comparisons, longevity |
| 3 | Aggregated user reviews | Retail/owner reviews, community forums | Reliability patterns, after-sales reality |
| 4 | Vendor claims | Spec sheets, marketing pages, AnTuTu-style scores | Starting point only; verify or discard |

Rule: a purchase recommendation should rest on level 1-2 evidence for its decisive claims; anything sourced only at level 4 is marked unverified.

## Red flags checklist (catches)

| Red flag | Catch it by |
|---|---|
| Big MP camera as headline | Check sensor size + OIS + lab shots |
| "SSD"/"fast flash" wording | Require explicit "NVMe PCIe"; eMMC = walk away |
| Same name, old chip | Verify exact chipset model on GSMArena/vendor page |
| Unbelievable capacity/price | H2testw/F3 for flash; Fake Device Test for devices |
| "New" at suspicious price, box opened | Check warranty start date, IMEI/serial, refurb grade disclosure |
| Score-based claims (AnTuTu) | Prefer sustained/thermal and lab measures |
| Unpublished update policy | Assume short support; check section 2 pages |
| Grey import at "great" price | Check local IMEI/carrier rules and local warranty confirmation |
| Only some HDMI ports full 2.1 | Port map per model on RTINGS/vendor |
| "Future-proof" upsell | Buy for today's workload + update window, not specs you won't use |

---

## Sources

- GSMArena camera/battery methodology: https://www.gsmarena.com/quad_bayer_sensors_what_they_are_and_what_they_are_not-news-38468.php ; https://www.gsmarena.com/oppo_find_x8_ultra_vs_samsung_galaxy_s25_ultra_vs_xiaomi_15_ultra-review-2878.php ; https://www.gsmarena.com/how_we_test_gsmarena_battery_life_test_20-news-60650.php
- RTINGS: https://www.rtings.com/tv/tests/picture-quality/hdr-peak-brightness ; https://www.rtings.com/tv/tests/inputs/input-lag ; https://www.rtings.com/tv/learn/oled-vs-qled ; https://www.rtings.com/tv/learn/hdmi-2-1 ; https://www.rtings.com/tv/tests/longevity/burn-in ; https://www.rtings.com/tv/reviews/by-size/size-to-distance-relationship ; https://www.rtings.com/headphones/learn/how-we-test ; https://www.rtings.com/headphones/learn/what-is-anc ; https://www.rtings.com/headphones/learn/bluetooth-tests-score
- NotebookCheck: https://www.notebookcheck.net/How-does-Notebookcheck-test-laptops-and-smartphones-A-behind-the-scenes-look-into-our-review-process.15394.0.html ; https://www.notebookcheck.net/Our-Rating-Criteria.2120.0.html ; https://www.notebookcheck.net/Benchmarks-and-Test-Results.5431.0.html
- TFTCentral: https://tftcentral.co.uk/articles/pulse_width_modulation ; https://tftcentral.co.uk/articles/exploring-and-testing-oled-vrr-flicker
- DXOMARK: https://www.dxomark.com/what-we-test-camera ; https://www.dxomark.com/how-we-test
- Geekbench: https://www.geekbench.com/doc/geekbench6-benchmark-internals.pdf
- Update policies: https://support.google.com/pixelphone/answer/4457705?hl=en ; https://security.samsungmobile.com/workScope.smsb ; https://www.apple.com/os/ios ; https://support.apple.com/en-us/102772 ; https://www.bgr.com/2247704/oneplus-phones-that-have-software-support-until-2029 ; https://trust.mi.com/misrc/updates/phone ; https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025 ; https://www.bgr.com/2290606/how-long-will-samsung-smart-tv-get-software-updates ; https://endoflife.date/apple-watch ; https://endoflife.date/iphone
- Market/technical references: https://en.wikipedia.org/wiki/GeForce_RTX_50_series ; https://en.wikipedia.org/wiki/List_of_Qualcomm_Snapdragon_systems_on_chips ; https://www.pcmag.com/explainers/ram-reality-check-how-much-memory-does-your-pc-actually-need-in-2026 ; https://www.tomshardware.com/laptops
- Fraud/parallel imports: https://industrialmonitordirect.com/blogs/knowledgebase/detecting-fake-usb-drives-with-h2testw-complete-guide ; https://www.amazon.com/gp/help/customer/display.html?nodeId=GRAS7M4E8YJCLWH7 ; https://www.inta.org/topics/parallel-imports ; https://www.mensxp.com/technology/smartphones/86880-smartphone-companies-caught-cheating-on-benchmark-apps.html
