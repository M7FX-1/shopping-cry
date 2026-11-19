# Automotive — Decoding Tables, Verification Detail, and Driver Detail

This is the demoted-companion reference for the product-scout-automotive
skill (install path: `references/automotive-domain.md`). Read it when a
verdict needs the oil-spec tables, the tire-code worked example, load
index numbers, battery date-code reading, the counterfeit checklist,
or per-sub-domain driver detail.

**No operative safety rule lives here**: the fitment protocol, the
safety-critical tier, the fluid-mixing rails, tire-age limits, and
fake-part warnings stay in SKILL.md behaviors 1–8. If this file and
the skill ever disagree, the skill wins. Verification tags: `[S]` = sourced — verified against a regulator, standards body, official/primary source, or a family-verified precedent this cycle (inline `[S: URL]` carries the source); `[P]` = practitioner/market consensus or street anchor — labeled as such, never presented as sourced fact; `[A]` = anchored rail — a calibrated threshold set at install and re-anchored on a ~6-month cadence. Suffixes in any order: a source number (`[S13]`), a `YYYY-MM` date (mandatory on `[A]`), and lowercase modifiers — `unverified` (secondary coverage only; re-verify or drop before stating as fact), `industry` (vendor/marketing source), `convention` (usage convention, not evidence). A `[S, unverified]` claim is never the sole basis for a dosage or contraindication statement.

---

## Oil specification tables

**SAE viscosity decode** `[S]` (SAE J300 convention):

- The number before `-W` is the cold-start grade (lower = flows at
  colder starts); the number after is the hot operating grade.
- Common grades vary by engine and climate: 0W-20 (modern Japanese/
  hybrid/fuel-economy engines), 5W-30 / 5W-40 (European and broad
  gasoline fleets), 10W-40 (older engines, hot climates).
- Choose exactly what the manual lists — the manual's tolerance
  ranges are the only legitimate alternates `[S]`.

**API categories** `[S]` (api.org):

| Category | Engine | Note |
|---|---|---|
| API SP | gasoline | current since May 2020; LSPI + chain-wear protection; supersedes SN backward-compatibly |
| API SN | gasoline | 2010–2020 generation |
| API SN Plus | gasoline | 2018 interim — LSPI protection for turbo DI |
| API CK-4 / FA-4 | diesel | current diesel classes |

**ACEA classes** `[S]`:

| Class | Meaning |
|---|---|
| A3/B4 | stable, stay-in-grade gasoline/diesel oil (older Euro cars) |
| A5/B5 | fuel-economy, low-HTHS |
| C2 / C3 | mid-SAPS, particulate-filter-compatible (C3 = mid-SAPS, high HTHS ≥3.5) |
| C5 / C6 | low-viscosity low-SAPS (0W-20 class) |

**OEM approvals** `[S]`: VW 504.00/507.00, MB 229.51/229.52, BMW
LL-04, Ford WSS-M2C913 — where the manual names one, the approval
outranks API/ACEA alone; the approval list is printed on the bottle
back label.

**Fluid-mixing rails live in SKILL.md behavior 3** (oil top-up,
brake-fluid glycol-class rule, coolant chemistry families). Power
steering vs ATF: only where the manufacturer says ATF `[P]`.

## Tire code — worked example `[S]`

**205/55 R16 91V**, read left to right:

| Element | Value | Meaning |
|---|---|---|
| 205 | 205 mm | section width |
| 55 | 55% | sidewall height as % of width |
| R | radial | construction |
| 16 | 16 in | rim diameter |
| 91 | ≈ 615 kg | load index per tire `[S]` |
| V | 240 km/h | speed rating (H = 210, T = 190, W = 270) `[S]` |

- Load-index band examples `[S]`: 85 ≈ 515 kg, 91 ≈ 615 kg, 95 ≈
  690 kg, 100 ≈ 800 kg, 102 ≈ 850 kg.
- Replacement rule: placard size or manufacturer-approved
  alternative; load/speed at-or-above OE (SKILL.md behavior 4).
- **DOT date code** `[S]` (Michelin/NHTSA guidance): the **last four
  digits** of the DOT string = week + year. "2523" = week 25 of
  2023. Tires carry one date; pairs mismatched by years = re-check
  per tire.
- Age guidance `[S]` (attribution split): NHTSA TireWise says some
  vehicle and tire manufacturers recommend replacing tires six to
  10 years old regardless of tread; the 10-year absolute ceiling is
  tire-manufacturer guidance, not NHTSA's own figure.

## Batteries — reading and buying detail

- **Date codes are brand-specific** `[P]`: many brands stamp a
  circular sticker or embossed dot (month/year, sometimes a letter+
  number code) — ask the seller for the code and read it with the
  brand's key; refuse to decode-blind when the seller stalls.
- **AGM vs flooded** `[S]` (battery-maker guidance): AGM — sealed
  spill-proof, vibration-resistant, higher cycle life, faster
  charging, required for start-stop and commonly for high-electrical-
  load cars; flooded — cheaper, serviceable tops on some markets,
  fine for ordinary cars.
- CCA sizing: match OE rating or above; a much-larger CCA battery
  rarely helps and may not fit the tray `[P]`.
- Terminal orientation (polarity left/right) and base-hold-down type
  differ by market/car — the tray fit is part of fitment `[P]`.
- Extreme heat or extreme cold shortens battery life; treat warranty
  months and local replacement availability as key value signals `[P]`.

## Counterfeit checklist — parts and fluids `[S]` where noted

Documented global context `[S]`: OECD flags counterfeit auto parts
(brake pads, airbags, filters, lubricants) as a top dangerous-goods
category within a ~US$467B total global counterfeit trade (2021).
Checklist:

1. Price sanity: far below every other channel = presumed fake for
   oil, brakes, filters (SKILL.md behavior 8's rule).
2. Channel: authorized distributor / brand service / verified retail
   for safety and fluid classes.
3. Packaging: batch code present and legible; seal intact; print
   quality; brand's QR/hologram verification where offered (Bosch
   automotive packages carry the KeySecure hologram/code — verified
   via Bosch's KeySecure authentication page; oil brands are
   introducing QR/scratch verification).
4. Physical: oil = golden/amber, uniform, no cloudiness; pads =
   backing plate stamping + R90 approval number (where applicable);
   filters = media density and intact bypass.
5. After-fit signals: engine noise/overheating after a cheap oil
   change, brake dust storms or fade after cheap pads — drain/
   replace and rebuy through a real channel `[P]`.

## VIN quick facts `[S]`

- 17 characters, standardized 1981+; the 10th character = model year
  (cycle of 30; I, O, Q excluded from the alphabet).
- Model-year codes (examples): A = 1980/2010, B = 1981/2011, ...
  L = 1990/2020, M = 1991/2021, N = 1992/2022, P = 1993, R = 1994,
  S = 1995, T = 1996, V = 1997, W = 1998, X = 1999, Y = 2000.
- The full 17-character VIN ties to the exact build only through a
  manufacturer catalog or a lookup service — the year character is a
  cross-check, not a fitment system (SKILL.md behavior 1's gates).

## Sub-domain driver detail

- **Filters** `[P]`: oil filter = media quality + bypass valve
  integrity (counterfeit point); air filter = pleat density; cabin
  filter = activated-carbon layer for high-pollution/dust cities.
  Replace on interval, not on failure — a clogged filter's cost is
  paid at the fuel pump and the engine.
- **Wipers** `[P]`: beam/hybrid blades outperform framed in heat,
  dust, and snow/ice; replace on streak/squeak.
- **Car care** `[P]`: spray wax after washes or periodic sealant for
  UV and road-salt protection; pH-neutral shampoo (dish soap strips
  wax); covers — breathable multi-layer beats tarp (trapped moisture
  + UV transmission); interior UV protectant for dash longevity.
- **Jump starters** `[S]` (NOCO/AutoZone guidance): peak amps
  marketing — check cranking-amp ratings for the car class; reverse-
  polarity protection + spark-proof clamps as required features;
  keep the unit charged; connection order red→positive, black→
  unpainted ground, power last, reverse disconnect.
- **OBD readers** `[P]`: read-codes is the user domain; live-data
  and bi-directional tools are workshop territory; cheap readers
  that "clear all" without fixing are the false-economy.
- **Roof racks/towing** `[P]`: match the car's approved mounting
  points; roof-load rating (car) < rack rating — the car is the
  limit; tow-bar ratings with the car's homologation; load rails are
  standard-safety, not marketing.
- **Motorcycle** `[P]`: chain + sprockets replaced as matched sets
  (wear pairs); drive-chain tension per manual; battery = AGM class
  common; oil = JASO MA2 spec for wet-clutch bikes (motorcycle
  standard alongside API).
- **Bring-your-own-part** `[P]`: agree the part supplier with the
  workshop before purchase; some workshops guarantee labor only on
  their own parts; the OEM-dealer path costs most but carries the
  cleanest recourse chain.

## Market & availability notes `[P]`

- Parts prices move with supply-chain and import costs — check
  current local listings at dispatch; old-generation parts (facelift
  cycles) drop sharply and are often legitimate value for older cars.
- Local fleet popularity decides availability and lead time: common
  mass-market models have fast, affordable parts locally; niche
  imports cost more and wait longer.
- For urgent consumables (batteries, tires, belts), local same-day
  availability and warranty exchange matter as much as brand prestige.
