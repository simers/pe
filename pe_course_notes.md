# Private Equity — Full Course Notes

**Companion to:** `pe_course_progress.md` (the progress checklist + quick-reference summary).
**This file:** the complete written content of every lesson and deep-dive, in the order covered. New lessons are appended here as we go.

> Diagrams shown in chat are rendered here as tables or described figures so the notes stand alone.

---

## Table of Contents — Module 1

1. [1.1 History & Evolution of PE](#11-history--evolution-of-private-equity)
2. [1.2 Fund Structure, Management & the GP/LP Relationship](#12-fund-structure-management--the-gplp-relationship)
3. [Deep dive — The J-curve with real funds](#deep-dive--the-j-curve-with-real-funds)
4. [Deep dive — Return metrics: DPI, RVPI, TVPI, MOIC, IRR](#deep-dive--return-metrics-dpi-rvpi-tvpi-moic-irr)
5. [1.3 PE Within the Alternatives Ecosystem](#13-pe-within-the-alternatives-ecosystem)
6. [1.4 The Current State of PE in Emerging Markets](#14-the-current-state-of-pe-in-emerging-markets)
7. [1.5 Common Investment Strategies](#15-common-investment-strategies)
8. [Deep dive — Real-world strategy examples (2025)](#deep-dive--real-world-strategy-examples-2025)
9. [Deep dive — Secondaries: LP-led vs GP-led, and who buys](#deep-dive--secondaries-lp-led-vs-gp-led-and-who-buys)
10. [Deep dive — Discount to NAV](#deep-dive--discount-to-nav)

---

## 1.1 History & Evolution of Private Equity

**Core definition (anchor for the whole asset class):** PE firms raise money from outside investors to buy companies that aren't publicly traded, improve them over several years, and sell them for more than they paid. Everything else (fund structure, debt, fees, jargon) serves that loop.

**The eras:**

- **Origins (1940s–70s) — patient money.** First recognizable PE firm: American Research and Development Corporation (ARD), founded 1946 (Georges Doriot, with Ralph Flanders and Karl Compton; Doriot is the figure remembered as the driving force and "father of venture capital"). Defining win: a ~$70,000 investment in Digital Equipment Corporation (1957) that grew to hundreds of millions — proof that a small equity check into a private company could return many multiples. Seeded the venture-capital branch.
- **1980s — the LBO boom + leverage.** KKR founded 1976 (Kohlberg, Kravis, Roberts, ex-Bear Stearns). Key insight: buy companies mostly with *borrowed money* (a leveraged buyout), using the company's own cash flows/assets as collateral; the small equity slice gets magnified returns. Fuel = high-yield "junk" bonds pioneered by Michael Milken at Drexel Burnham Lambert. Emblematic deal: KKR's 1988 takeover of RJR Nabisco (~$25B, a record for nearly two decades; the book *Barbarians at the Gate*). This era is the source of PE's aggressive reputation.
- **1990s–2000s — institutionalization.** Drexel collapsed (1990); the industry professionalized. Blackstone (1985), Carlyle, Apollo built durable institutions. Pensions, endowments, sovereign wealth funds began allocating seriously → bigger funds. Mega-deals returned in the mid-2000s credit boom, then froze in 2008.
- **2010s–today — mainstream.** The big firms went public (Blackstone 2007; KKR, Apollo, Carlyle after) and became "alternative asset managers" spanning credit, real estate, infrastructure. Near-zero rates made cheap debt abundant; fundraising exploded; trillions in **dry powder** (committed-but-uninvested capital) accumulated. From 2022, sharply higher rates made debt expensive again, slowing deals/exits and pushing firms toward continuation funds, secondaries, and lending against portfolios.

**Throughline:** PE has always been (1) buying private companies, (2) using leverage to amplify returns, (3) holding for years to improve before selling. The 1980s gave it leverage + reputation; the 1990s–2000s gave it discipline + scale; the 2010s made it mainstream.

---

## 1.2 Fund Structure, Management & the GP/LP Relationship

**The fund is a legal vehicle, not a company** — almost always a *limited partnership* with two roles:

- **General Partner (GP)** = the PE firm's entity. Makes every investment decision; sources deals; manages portfolio companies; decides when to sell. Commits some of its own money — the **GP commitment**, usually 1–5% of the fund ("skin in the game"). Traditionally bears unlimited liability.
- **Limited Partners (LPs)** = outside investors supplying ~95%+ of capital. Passive (no say in individual deals); liability limited to what they commit. Types: public/corporate pension funds, university endowments, foundations, sovereign wealth funds, insurance companies, funds-of-funds, family offices, wealthy individuals.

Nuance: "the firm" = a **management company** (employs professionals, collects the management fee) + a **GP entity** (collects the profit share). The firm sits on the GP side.

**Commitments vs. calls.** LPs *commit* (a legal promise to provide up to X), then the GP *calls* capital (drawdowns) as deals are found, usually over a ~5-year investment period. So committed capital ≠ invested capital; dry powder = committed but not yet called. **Fund life ~10 years**, often with 1–2 year extensions, in two phases: investment period (~yrs 1–5, buying/calling) and harvest period (~yrs 5–10, improving/selling/returning).

**The economics — "2 and 20."** The GP earns money two ways:

1. **Management fee** (~2%/yr): on a $1B fund, ~$20M/yr. Covers salaries/overhead. Paid *regardless of performance* — steady income.
2. **Carried interest ("carry," ~20%)**: the GP's share of *profits*. The real prize and the alignment mechanism — only materializes if LPs make money.

**The distribution waterfall** (the order money is paid out):

1. **Return of capital** — LPs get back 100% of what they put in (incl. fees).
2. **Preferred return (hurdle)**, typically ~8% annualized — LPs must earn this minimum before the GP shares upside.
3. **GP catch-up** — once LPs have the preferred return, GP receives a burst of profits until it reaches its 20% share of profits distributed so far.
4. **Carried-interest split** — thereafter 80% LP / 20% GP.

So "2 and 20 with an 8% hurdle" = the whole compensation model in one phrase.

**Real fee-drag anchor (KKR, 2026).** KKR disclosed that its predecessor North America funds returned **23% gross / 19% net IRR** and **2.1× gross / 1.8× net MOIC** over the past decade. That gap — ~4 points of IRR and ~0.3× of MOIC — *is* the "2 and 20" fee drag, in a real GP's own numbers: the gross-to-net wedge, no longer abstract. (It also sets the bar: ~19% net IRR is roughly what LPs expect — which is exactly why the Cascade base case's 16.8% at 9.0× reads as *sub-hurdle* in 5.5.)

**The J-curve.** Early in a fund's life, LP returns are *negative* (fees charged, no exits/markups yet); later, exits turn returns sharply positive — tracing a "J." Why PE is a patient, long-horizon game; connects back to ARD's "patient money."

**Practice takeaways:**
- The remaining uncalled portion of a commitment = **uncalled / unfunded commitment** (distinct from aggregate *dry powder*). A fund still *calling* capital is in its **investment period**.
- Waterfall subordinates GP carry to LPs being made whole first; the 8% hurdle is *annualized*, so the dollar hurdle depends on time deployed.
- Fee-on-committed-capital can tempt a GP to raise an ever-larger fund even if a smaller one would return more per dollar. Alignment tools = carry **plus** the GP commitment ("skin in the game").

---

## Deep dive — The J-curve with real funds

**Data source:** U.S. public pensions must disclose their PE holdings (CalPERS Private Equity Program, as of Sept 30, 2025). These are real public disclosures, but **point-in-time figures that move every quarter** — treat the exact DPI/IRR/TVPI numbers below as a Sept-2025 snapshot, not current marks. Caveat: a true J-curve is *one fund's* path over ~10 years, which no single disclosure shows — so we use a **space-for-time substitution**: the *same manager's funds at different ages* to trace the shape. CalPERS warns vintage-2021+ funds are too young for meaningful performance analysis, and interim IRRs alone aren't great predictors.

**Example 1 — Clearlake Capital Partners (one firm, three ages):**

| Fund | Vintage | Age | DPI (cash returned) | Net IRR | TVPI |
|---|---|---|---|---|---|
| Clearlake VII | 2022 | ~3 yrs | ~0.00× (≈nothing back) | 4.1% | 1.11× |
| Clearlake V | 2018 | ~7 yrs | 1.39× (past break-even) | 32.3% | 1.96× |
| Clearlake III | 2012 | ~13 yrs | 2.86× (fully harvested) | 40.7% | 2.88× |

The progression — almost nothing back → past break-even → ~3× cash returned — *is* the J-curve. The 2022 fund isn't worse than the 2012 fund; it's earlier on the same curve.

**Example 2 — Silver Lake (tech buyouts), same pattern:**

| Fund | Vintage | Age | DPI | Net IRR |
|---|---|---|---|---|
| Silver Lake VI | 2021 | ~4 yrs | 0.22× | 9.1% |
| Silver Lake V | 2018 | ~7 yrs | 0.62× | 11.6% |
| Silver Lake IV | 2013 | ~12 yrs | 1.81× | 20.9% |

**The trough, live:** 2022-vintage funds below cost on paper — e.g. Arsenal Capital Partners VI (~0.93×, −3.6% IRR) and Tiger Global's 2022 fund (~0.82×, −5.9%). That's normal trough behavior (fees paid, companies bought but not improved/sold), *not* necessarily failure. At year ~3 you can't distinguish "normal J-curve" from "underperforming" — which is exactly why LPs don't judge funds by early IRR.

**Figure (the J-curve):** cumulative cash returned to LPs starts at break-even, dips below it in years ~2–4 (capital called + fees, no exits), crosses back above break-even around year ~6–7, and climbs well above by years ~12–13. Clearlake VII sits in the trough; Clearlake V just past break-even; Clearlake III high on the curve.

---

## Deep dive — Return metrics: DPI, RVPI, TVPI, MOIC, IRR

Two families: **multiples** (how much money came back — ignore time) and **IRR** (how fast it compounded — all about time). You need both.

**Multiples** (all map to the CalPERS columns):
- **DPI — Distributions to Paid-In** = (cash returned) ÷ (cash in). *Realized*, in-hand. DPI 1.0× = money back.
- **RVPI — Residual Value to Paid-In** = (value still held in the fund) ÷ (cash in). *Unrealized* paper mark (the GP's estimate).
- **TVPI — Total Value to Paid-In** = DPI + RVPI = (total value) ÷ (cash in). The "Investment Multiple." Realized + unrealized.
- **MOIC — Multiple on Invested Capital** = deal-level cousin of TVPI (total value ÷ capital invested in one company). The headline multiple in an LBO.

**Anatomy example (Clearlake V):** $114.8M paid in, $160M returned, $225M total value → TVPI 1.96× = DPI 1.39× (cash) + RVPI 0.57× (still held).

**Why the DPI vs. RVPI split matters:** RVPI is the GP's *opinion* of unsold companies; DPI is incontrovertible cash. A fund can show a gorgeous TVPI that's mostly RVPI — great on paper, unpaid in cash. Hence **"DPI is the new IRR"**: in slow-exit markets LPs prize actual cash returned.

**IRR (internal rate of return)** = the annualized rate that sets NPV of all cash flows to zero ("what bank-account rate would replicate this?"). **Exquisitely timing-sensitive:**
- $100 → $200 in **3 years** ⇒ IRR ≈ **26%**
- $100 → $200 in **7 years** ⇒ IRR ≈ **10%**
Same 2.0× multiple; very different IRR.

**When multiples and IRR disagree — real example:**

| Fund | TVPI | DPI | Net IRR |
|---|---|---|---|
| Clearlake III (2012) | 2.88× | 2.86× | 40.7% |
| Silver Lake IV (2013) | 2.78× | 1.81× | 20.9% |

Near-identical TVPI, but Clearlake's IRR is double *and* it returned far more cash (2.86× vs 1.81×). IRR and DPI agree Clearlake delivered more; the *misleading* number here is TVPI, because Silver Lake's TVPI leans on ~0.97× of unrealized RVPI. (Caveat: Silver Lake's book is still open — that unrealized value could be realized at/above the mark or written down.)

**Honest nuance:** IRR can be *flattered* by tactics that delay capital calls (subscription credit lines), which shrinks the time the clock runs — a reason LPs cross-check IRR against DPI.

**Mental model:** TVPI = how good it looks on paper; DPI = how much is actually in your pocket; IRR = how fast it got there. When they disagree, the disagreement *is* the information.

---

## 1.3 PE Within the Alternatives Ecosystem

**Alternatives** = everything beyond the traditional public-stock/public-bond "60/40": private equity, private credit, real estate, infrastructure, hedge funds, commodities. LPs accept the headaches for three reasons: the **illiquidity premium**, **diversification** (low/lagged correlation to public markets), and **access** (most companies are private).

**Organize the map by two questions — life-cycle and capital structure.**

*Equity life-cycle continuum (all "own a slice," different maturity/risk):*
- **Venture capital (VC):** earliest; startups, often unprofitable; minority stakes; no leverage; power-law outcomes.
- **Growth equity:** middle; proven model needing capital to scale; minority/majority; little/no debt.
- **Buyout / LBO:** mature end; control stakes; heavy leverage. **This is what "PE" means in this course.**

*Terminology trap:* broadly "PE" = VC + growth + buyout; colloquially "PE" = buyout.

*Capital-structure axis:*
- **Private credit / direct lending:** you *lend* rather than own — paid before equity, contractual interest, lower risk. Often the *debt* in a buyout deal (two sides of the same transaction). Exploding as banks pulled back.
- **Real assets:** real estate and infrastructure (roads, utilities, data centers, renewables) — long-life, stable, often inflation-linked cash flows; lower on the risk/return scale.

**Risk/return spectrum (lower→higher):** Private credit → Infrastructure → Real estate → Buyout → Growth → Venture. (Left = paid first/debt; right = paid last/equity.)

**Hedge funds — the structural outlier:** mostly trade *liquid, public* securities; *open-ended* (money in/out periodically), not a 10-year drawdown fund. Capital calls, the J-curve, and DPI largely don't apply.

**How LPs bucket it:** a *strategic asset allocation* across the map. Two governing ideas — a return-seeking sleeve (buyout/growth/venture) vs. income/defensive sleeve (credit/infra/core real estate), and the **illiquidity budget** (a pension must keep enough liquid to pay obligations, capping how much can be locked up).

**Convergence:** Blackstone, KKR, Apollo, Carlyle, Ares now span the whole map (credit, RE, infra, insurance) — why "alternative asset managers."

**Practice takeaways:**
- Lender vs equity in the same company: lender is higher in the structure and lower-risk; equity has higher expected return. Consistent, not contradictory — **return is the price of risk**: the lender accepts a *capped* return for getting paid first; equity is the residual claimant, last in line but with uncapped upside.
- Hedge funds use open-ended structures because liquid assets → frequent valuation → investors can come and go → no need to lock up capital.
- Minority stake + unprofitable startup + no debt = **venture** (in the narrow sense), even if the firm calls itself "PE."

---

## 1.4 The Current State of PE in Emerging Markets

*(Current data searched ~June 2026.)* EM = developing economies (India, Brazil, Southeast Asia, Africa, parts of LatAm, historically China). EM weakens nearly every developed-market assumption.

**Structural differences:**

1. **Leverage often unavailable** (shallow debt markets) → EM PE is frequently *minority growth equity*, not leveraged buyout. Returns come from the business *growing*, not financial engineering. (Private credit is growing in EM to reduce bank dependence.)
2. **Currency risk — the defining hazard.** LPs measure in hard currency; companies earn local. Depreciation hollows out dollar returns even on a great operational result (see the currency-math table below). Hence the preference for hard-currency/export revenue.
3. **Exits harder/slower** (shallow IPO markets, fewer buyers) — the #1 investor concern in APAC. Reliance on trade sales (+60% YoY), secondaries (~25% of deals), continuation funds; longer holds.
4. **Political/regulatory/rule-of-law risk** — capital controls (can you get money out?), expropriation, policy intervention. China example: government investment funds with policy objectives and even "guaranteed-return" pressure; disputes more frequent/volatile.
5. **Information quality** — less audited financials, more informal economy → harder diligence; premium on on-the-ground presence.
6. **Market structure** — family/founder-owned targets reluctant to cede control → minority stakes, governance rights, founder alignment.

**Currency math — why FX is the defining hazard.** LP return (in USD) = local-currency return × (1 − currency depreciation):

| Local-currency return | Currency move | USD return to the LP |
|---|---|---|
| 2.0× (great) | −50% (halves) | **1.0×** — the entire gain erased |
| 2.5× (great) | −40% (×0.60) | **1.5×** — two-thirds of the win survives |
| 2.0× | 0% (stable / hedged) | 2.0× — full gain retained |

A hurdle rate can't fix this (it prices risk, it doesn't control it) — the real mitigants are hard-currency/export revenue (a natural hedge) and explicit FX hedging.

**Bull case = growth/demographics.** India is the standout: most-cited "best opportunities" EM in Preqin's 2024/2025 surveys; ~$78B committed to India PE/VC since 2020; PwC estimates >⅓ of new Asian PE capital is directed to India; demographic tailwind (rising working-age population vs declining in China/Europe), low inflation volatility.

**Headline = a rotation** away from China (geopolitics, regulatory unpredictability, exit difficulty) toward India and others. (Japan is the other big Asian story but is *developed*, not EM.)

**Global backdrop:** fundraising ~$480B in 2025 (third straight annual decline); capital concentrating in the largest managers; Bain's "12 is the new 5" — the cheap-debt/easy-multiple-expansion era is over, so deals demand far faster EBITDA growth (felt acutely in EM).

**Three value-creation levers (preview):** earnings growth, multiple expansion, leverage/debt paydown. EM leans almost entirely on growth.

**Key judgment:** a **hurdle rate prices risk** (an IRR threshold for sharing upside) but does **not control** risk. A higher hurdle doesn't recover capital a currency collapse destroyed, beat capital controls, or reverse an expropriation. Real mitigation = FX hedging + hard-currency revenue; treaty-jurisdiction structuring (e.g., Singapore/Mauritius); political-risk insurance (MIGA, US DFC); staged capital; pre-arranged exits; governance/minority rights; local partners. A too-high hurdle can even *misalign* incentives (a GP hopelessly below hurdle has zero carry either way → may "swing for the fences").

---

## 1.5 Common Investment Strategies

The toolbox *inside* PE, organized by: company maturity, health, transaction type, and whether you even buy an operating company.

**By maturity (recap):** venture → growth → buyout.

**Buyout playbooks:**

1. **Buy-and-build (platform + add-ons)** — the dominant modern strategy. Buy a larger *platform*, then acquire smaller *add-ons* ("bolt-ons") and stitch them together. Engine = **multiple arbitrage**: small firms trade at low multiples; a large professionalized platform commands a higher multiple, so the same earnings are worth more at scale. *(Worked just below the playbooks.)*
2. **Carve-out** — buy a non-core *division* from a larger corporation. Opportunity: a neglected "orphan" run better standalone, often at an attractive price. Challenge: disentanglement (IT, HR, supply chain) → handled via a **Transition Services Agreement (TSA)** while you stand up your own functions.
3. **Take-private (public-to-private)** — buy a listed company and delist it. Thesis: a mispriced/under-managed public company fixable away from quarterly scrutiny. Large and equity-intensive; drives megadeals.
4. **Turnaround / distressed / special situations** — buy troubled companies (or their debt) and fix them. *Distressed-for-control:* buy the debt cheaply, convert to equity through restructuring/bankruptcy. Different (restructuring) skillset; counter-cyclical.

**Buy-and-build — the multiple-arbitrage math.** Buy small and cheap, combine, sell big at a higher multiple. Same $35M of earnings, simply re-rated:

| Step | EBITDA | × multiple | = EV |
|---|---|---|---|
| Platform (buy) | $20M | 8.0× | $160M |
| 5 add-ons (buy) | $15M | 5.0× | $75M |
| **Own after roll-up** | **$35M** | **6.7× blended** | **$235M** |
| Exit (sell as one platform) | $35M | 10.0× | $350M |
| **Value created** | | | **+$115M** |

That ~$115M is **purely the re-rating** — before any organic growth, synergies, or debt paydown, which stack on top.

**Strategies where you don't buy an operating company:**

5. **Secondaries** — buy an existing *stake in a fund*. **LP-led** (an LP sells its commitment) and **GP-led** (continuation funds — a GP moves a prized asset into a new vehicle). Buying a *mature* fund skips the early fees-without-distributions years → shallower, shorter J-curve and faster cash back.
6. **Co-investment & fund-of-funds.** Co-investment: an LP invests directly alongside the GP in a specific deal, usually fee-free, lowering blended cost. Fund-of-funds: a manager building a diversified portfolio of other PE funds (extra fee layer, instant diversification).

**The three value-creation levers (as styles):** financial engineering (leverage) / multiple arbitrage (buy low, sell at a higher multiple) / operational improvement (grow EBITDA). The industry has shifted decisively toward **operational** value creation — captured by Bain's phrase **"12 is the new 5."**

**What "12 is the new 5" actually means (Bain).** It's a rule of thumb for how much harder deals must work now. In the 2010s "golden decade," cheap debt and steadily rising multiples did most of the work, so a typical buyout needed only ~**5% annual EBITDA growth** to hit the standard **2.5× MOIC over five years.** Today — borrowing costs ~8–9%, less leverage, and record-high *but stagnant* entry multiples (no multiple expansion left to harvest) — the same 2.5× requires ~**10–12% annual EBITDA growth.** The operational bar roughly **doubled**, because the other two levers stopped contributing:

| Return lever | 2010s "golden decade" | Today |
|---|---|---|
| Leverage (cheap debt) | big contributor (near-zero rates) | smaller (rates ~8–9%, lower leverage) |
| Multiple expansion | big contributor (multiples rising) | ~zero (multiples high but flat) |
| **EBITDA growth required** | **~5% / yr** | **~10–12% / yr** |
| …to hit the same target | 2.5× MOIC over 5 yrs | 2.5× MOIC over 5 yrs |

In plain terms: you now have to *actually grow the business* to earn the return the market used to hand you for free. That's why value creation has moved from financial engineering to operations — and it's what Modules 5–7 build toward. *(Bain, Global Private Equity Report.)*

**Practice takeaways:**

**Buy-and-build math (a second worked case).** Entry versus exit:

| Step | EBITDA | × multiple | = EV |
|---|---|---|---|
| Platform (buy) | $40M | 9.0× | $360M |
| Add-ons (buy) | $12M | 6.0× | $72M |
| **Total entry** | **$52M** | 8.3× blended | **$432M** |
| Exit (sell) | $52M | 11.0× | $572M |
| **Value created** | | | **+$140M** |

All of it from re-rating (no organic growth assumed). Where the $140M comes from — the multiple lift applied to each piece:

| Source | EBITDA | multiple lift | value created |
|---|---|---|---|
| Platform | $40M | 9× → 11× (+2.0×) | $80M |
| Add-ons | $12M | 6× → 11× (+5.0×) | $60M |
| **Total** | | | **$140M** |

- Buy-and-build needs a *cash-generative platform* to lever and to build around; an unprofitable startup has no EBITDA, so it's **venture**, not buy-and-build.
- A secondary stake in a 7-year-old fund skips the trough → DPI starts almost immediately; often bought at a discount to NAV, lifting returns further.

---

## Deep dive — Real-world strategy examples (2025)

*A small cluster of firms (Thoma Bravo, Vista, Silver Lake) dominates large-cap tech buyouts — hence the repetition.*

1. **Buy-and-build — Thoma Bravo (software consolidation).** Its predecessor is credited with coining "buy and build"; 565+ software/tech transactions by 2026. 2025 add-on mechanic: acquired PROS Holdings (~$1.4B, $23.25/share, completed Dec 2025) — running its travel unit as a standalone platform ("PROS Travel") while folding its B2B unit into existing portfolio company Conga (B2B→Conga expected Q1 2026); and agreed to buy Verint (~$2B enterprise value, $20.50/share all-cash, announced Aug 2025, expected close early 2026) to combine with portfolio company Calabrio (which TB had bought from KKR in 2021). *[Both re-verified against SEC filings and company press releases, Jun 2026.]*
2. **Carve-out — Thoma Bravo buys Boeing's Digital Aviation Solutions** (Jeppesen, ForeFlight, AerData, OzRunways) for **$10.55B** all-cash (announced Apr 2025; closed late 2025). Became standalone "Jeppesen ForeFlight." Included data-sharing/continuity principles (the TSA logic) and was financed with a ~$4B direct-lending package (private credit funding a buyout).
3. **Take-private — Thoma Bravo takes Dayforce private** (HR/HCM software): **$12.3B**, $70/share, 32% premium; called the largest standalone enterprise-software deal led by a financial sponsor.
4. **Turnaround/distressed — Platinum Equity / Aventiv Technologies:** debt-for-equity recapitalization (Apr 2025) of a prison-communications tech company. (Cerberus = archetypal distressed/turnaround firm.)
5. **Secondaries (GP-led) — Vista Equity Partners / Cloud Software Group:** record **$5.6B** continuation vehicle (2025). Tech was the fastest-growing corner of GP-led secondaries (~24% of H1 2025 deal value).
6. **Co-investment — Abu Dhabi Investment Authority alongside Thoma Bravo in Dayforce:** a "significant minority investment" by a sovereign-wealth LP directly in the deal. (Golub Capital: 400+ equity co-investments, $1.7B+ over 20 years.)

*Note:* the Thoma Bravo–Dayforce deal is simultaneously a take-private **and** a co-investment — strategy labels describe facets of a deal, not exclusive boxes.

---

## Deep dive — Secondaries: LP-led vs GP-led, and who buys

**Two transactions, one word:**
- **LP-led** — an existing LP sells its fund stake to a specialist buyer (this creates the "buy a mature fund, skip the trough" dynamic). Buyer steps into the fund, inheriting the stake + unfunded commitment.
- **GP-led** (continuation vehicles) — the GP moves a star asset into a new vehicle with fresh secondary capital; existing LPs roll over or cash out.

**Who buys into mature funds (specialist secondaries buyers):** Ardian, Lexington Partners (~$55B), Coller Capital (~$35B), HarbourVest (~$115B), Blackstone Strategic Partners (>$100B), Apollo's S3, KKR, GCM Grosvenor, StepStone. Scale: **Ardian raised $30B for ASF IX — the largest secondaries fund ever**, avg deal size ~$2B; backers include CalSTRS, PA SERS, NYC ERS, and a $4B ADIA commitment. (Loop: pensions fund the buyers who buy other pensions' stakes.)

**Marquee LP-led deal:** May 2025 — **NYC's five pension systems sold ~$5B of PE stakes, Blackstone lead buyer** (likely the largest PE secondaries deal ever by dollar value). Sold positions in 125+ funds across 74 managers; Blackstone took 95%+; roster trimmed to ~45. Motivation = "strategic realignment" (less overhead, more co-investing) — *not* distress.

**Who sells:** over-allocated institutions (when public markets fall, the private allocation balloons as a share of the total — the "denominator effect" — pushing past target). Yale reportedly ran a large process around the same time. 2025 global secondaries volume hit a record ~$226B (+41%).

**Broadening buyer base:** private-wealth clients (22% of Ardian's fund, up from 11%) via evergreen funds; Canadian mega-pensions as repeat players on both sides; family offices.

**Why buyers want mature stakes:** "no J-curve" + immediate diversification; stakes already late in the holding period (exitable sooner); avoids "blind-pool" risk (you can see the actual companies); usually bought at a discount to NAV. **LP-led is actually the larger share of the market** despite GP-led grabbing headlines.

---

## Deep dive — Discount to NAV

**NAV (net asset value)** = the GP's reported estimate of what the fund's holdings are worth, net of liabilities, divided to your stake. It's an **appraisal, not a market price** — marked quarterly with comps/DCF/recent deals, typically a quarter stale.

**Discount to NAV** = price paid vs. reported NAV.
> **Discount = 1 − (Price ÷ NAV)**  ·  **Price = NAV × (1 − discount)**

**Examples:**
- $50M stake at 85% of NAV (15% discount) → pays $42.5M.
- $10M stake at a 20% discount → pays $8M ("80 cents on the dollar").
- Premium: $10M trophy stake → pays $10.6M (6% premium, 106% of NAV).

**Real anchors:** single-asset continuation vehicles priced ~99.5% of NAV (near par, late-2022 to mid-2025); LP-led stakes historically ~15–20% discounts; venture-secondary discounts compressed from ~46% (late 2023) to ~3% a year later, swinging to a ~6% average premium by Q1 2025. Pricing ranges by quality and market balance and can flip to a premium.

**Why LP-led stakes trade at a discount:**
1. **Liquidity isn't free** (the biggest reason) — the buyer provides an early exit from a 10-year illiquid asset; the discount is the seller's cost of jumping the queue.
2. **NAV is the GP's estimate** — stale and self-marked, so buyers demand a margin of safety, pricing to *their* view of value.
3. **Unfunded commitments** — the buyer inherits future capital-call obligations and prices that in.
4. **Remaining fees + time** — even a mature fund still charges fees and takes time to exit.
5. **Diligence/friction cost** — underwriting 100+ companies, GP consents, legal/tax.
6. **It's how the buyer manufactures return** — buying below NAV is a structural head-start toward a target IRR/MOIC.
Supply/demand and quality set the level: seller floods widen discounts; trophy assets/top GPs can trade at par or a premium.

**NAV-markup nuance ("NAV squeezing"):** accounting lets a buyer immediately re-mark a purchased stake up to the GP's reported NAV — so paying $8M for a $10M-NAV stake books an instant $2M paper gain, flattering a secondary fund's early numbers. Combined with buying mature, near-harvest assets, this is precisely why secondaries dampen the J-curve: enter below face value, late in the life, with cash coming back soon.

---

*End of content through Module 1.5 + deep-dives. New lessons append below as we cover them.*

---

## 1.6 LBO Analysis, Hurdle Rates and Returns

The LBO return engine: **buy a company with a thin equity slice + a lot of debt; over the hold, three forces grow the equity.**

**Sources & Uses (simplified):** sources = debt + equity; uses = purchase price + fees. At entry, **Enterprise Value (EV) = Debt + Equity**. Debt does most of the lifting, so the equity check is small relative to price.

**The three value levers (since Equity = EV − Net Debt):**
1. **EBITDA growth** — more earnings → more EV at any multiple.
2. **Debt paydown (deleveraging)** — cash flow repays debt; every $1 of debt repaid → +$1 of equity, even with zero growth.
3. **Multiple change** — exit multiple higher than entry (expansion) adds value; lower destroys it.

**Illustrative example (round numbers, NOT a real deal):**
- Entry: $100M EBITDA × 10× = $1,000M EV; financed $500M debt + $500M equity.
- 5-yr hold: EBITDA → $150M; debt paid down $500M → $300M; exit at 10× (flat).
- Exit: $150M × 10× = $1,500M EV; exit equity = $1,500 − $300 = $1,200M.
- **MOIC = 2.4×; IRR ≈ 19%.**
- Value bridge: +$500M from EBITDA growth ($50M × 10×), +$200M from debt paydown, $0 from multiple → equity $500M → $1,200M.

**MOIC ↔ IRR ↔ time (worth memorizing):**

| MOIC | 3-yr | 5-yr | 7-yr |
|---|---|---|---|
| 2.0× | ~26% | ~15% | ~10% |
| 2.5× | ~36% | ~20% | ~14% |
| 3.0× | ~44% | ~25% | ~17% |

**Exit-multiple sensitivity (the biggest swing).** Hold ENTRY FIXED (already bought at 10× → equity check $500M, exit debt $300M, exit EBITDA $150M) and vary ONLY the exit multiple — what a *future* buyer pays you (at exit you're the seller, financing nothing):

| Exit multiple | Exit EV | − Exit debt | = Exit equity | MOIC | IRR (5-yr) |
|---|---|---|---|---|---|
| 8× | $1,200M | (300) | $900M | 1.8× | ~12.5% |
| 10× (= entry) | $1,500M | (300) | $1,200M | 2.4× | ~19% |
| 12× | $1,800M | (300) | $1,500M | 3.0× | ~24.6% |

A 2-turn swing in the exit multiple moves IRR ~12 points — which is why every model ends in a sensitivity table. The entry stays 10× throughout, so note: buying *and* selling at the same multiple contributes **zero** from the multiple (it washes out). Multiple change only adds value when exit ≠ entry (the multiple-arbitrage point from 1.5).

**Leverage amplifies both ways:** finance 70/30 ($300M equity) instead of 50/50 → exit equity ~$1,000M on $300M → ~3.3× / ~27% IRR (vs 2.4×/19%). More debt = smaller check = bigger return *if it works*; but more interest, thinner cushion, and equity can go to zero if EBITDA falls. Leverage concentrates value/loss onto a smaller base; it doesn't create value.

**Hurdle rate = an IRR threshold.** The 8% preferred (lesson 1.2) is the IRR a deal/fund must clear before the GP earns carry. Base deal's 19% clears 8% → carry on the excess; a 6% IRR deal earns the GP no carry.

**Real anchor — Blackstone × Hilton (2007–2018):** bought for $26B (~$20.5B debt + ~$5.6B equity) at the 2007 peak; crisis hit, Hilton briefly technically insolvent; Blackstone held, restructured, hired CEO Chris Nassetta, shifted to asset-light franchising + international expansion; IPO 2013; full exit 2018; **~$14B profit, ~3× MOIC, ~16% IRR over ~11 years** — the most profitable LBO ever.
- Lesson 1: *operational* value creation (not leverage/multiple tricks) carried it (ties to 1.5).
- Lesson 2: a great multiple over a long hold = modest IRR (3× but ~16%). Naive 3^(1/11) ≈ 10.5%; actual ~16% higher because capital was returned in tranches from the 2013 IPO (earlier cash → higher IRR).
- Lesson 3: survival is a strategy — *not selling* at the 2009 trough (enabled by the locked-up fund structure) turned a near-wipeout into a triumph.

**Cautionary mirror:** TXU / Energy Future Holdings (KKR/TPG/Goldman, 2007, ~$45B incl. assumed debt; ~$32B deal value per Dealogic) went bankrupt in 2014, ~−100% return. Same era, same heavy leverage, opposite outcome. TXU held the **"largest LBO ever"** title for 18 years — until Electronic Arts in 2025.

**New record — Electronic Arts (Sept 2025):** EA was taken private for **$55B** by Saudi Arabia's **Public Investment Fund (PIF)**, **Silver Lake**, and Jared Kushner's **Affinity Partners** — now the largest LBO ever, eclipsing TXU. Funded with ~**$36B of equity** (PIF the majority, rolling over its existing ~10% EA stake) + **$20B of debt from JPMorgan**; EA holders get $210/share, a 25% premium. A modern *club deal* pairing sovereign wealth with tech-focused PE, buying a videogame maker in a sector that had cooled after its pandemic boom. Note the structure is **more equity than debt** — at this size the record is the *ticket*, not the leverage ratio.

---

## 1.7 Leverage as a Tool for Value Creation

Built on the EBITDA primer below. Core idea: **leverage = using borrowed money so a small slice of your own money controls a large asset, magnifying your return on that money — up AND down.**

**Part 1 — the core intuition (amplification).**
Leverage doesn't *create* the gain — it **concentrates the whole gain (or loss) onto a smaller slice of your own money**. The loan is a fixed amount, repaid first, so every dollar the asset moves lands entirely on your equity.

*House analogy — a $500k house, up and down:*

| Outcome | All cash ($500k of your money) | 20% down ($100k yours + $400k mortgage) |
|---|---|---|
| Rises to $600k → you keep | $600k = **+20%** | $600k − $400k = $200k = **+100%** |
| Falls to $400k → you keep | $400k = **−20%** | $400k − $400k = $0 = **−100%** (wiped) |

Same $100k swing in the house's value — the mortgaged buyer feels it **5× as hard**, because their own stake is 5× smaller.

*Company version — a $1,000M deal ($100M EBITDA × 10×):*

| Exit value | All-equity ($1,000M in) | 60% debt ($400M equity + $600M debt) |
|---|---|---|
| $1,200M (+20%) → equity | $1,200M = **+20%** | $1,200M − $600M = $600M = **+50%** |
| $700M (−30%) → equity | $700M = **−30%** | $700M − $600M = $100M = **−75%** |
| $600M (−40%) → equity | $600M = **−40%** | $600M − $600M = $0 = **−100%** (wiped) |

*The general rule — amplification factor = 1 ÷ (equity as % of price):*

| Equity share of price | Amplification | A +20% asset move → | A −20% asset move → |
|---|---|---|---|
| 100% (all-equity) | 1.0× | +20% | −20% |
| 40% | 2.5× | +50% | −50% |
| 30% | 3.33× | +67% | −67% |
| 20% (house, 20% down) | 5.0× | +100% | −100% |

**The one line to remember:** the less of your own money you put in, the harder every move hits it — leverage multiplies returns *symmetrically* (up and down), which is exactly why it is both the engine of LBO returns and the source of their risk.

**Part 2 — the debt stack (why the borrowed money is layered).** The debt isn't one loan; it's layers with different risk/price, so the company can raise MORE total debt than any single cautious lender would give. Ordered by **seniority** = payout order in a liquidation (same waterfall idea as LP distributions in 1.2). Higher = paid first = safest = lowest rate; lower = paid later = riskier = higher rate; equity dead last.

Example $600M debt (illustrative rates): Senior secured 1st-lien term loan $400M @ ~8.5% (secured, paid 1st) → Second lien $150M @ ~12% → Mezzanine $50M @ ~14% (+warrants, unsecured, last debt) → Equity $400M (dead last). Liquidation for $500M: senior recovers 100% ($400M), second lien 67% ($100M), mezz 0%, equity 0%. The recovery gradient IS why lower layers charge more.

**Part 3 — the other benefits of debt (beyond amplification).**

**1. Interest tax shield.** Interest is **tax-deductible**; money paid to equity (dividends) is *not*. So borrowing shifts cash that would have gone to the tax authority into the deal instead. Same $100M EBIT, 25% tax rate, $600M of debt at 10% ($60M interest):

| $M | No debt | With $600M debt @ 10% |
|---|---|---|
| EBIT | 100 | 100 |
| − Interest | 0 | (60) |
| = Pre-tax income | 100 | 40 |
| − Tax @ 25% | (25) | (10) |
| = Net income | 75 | 30 |

The debt cut the tax bill from $25M to $10M — a **$15M/yr cash saving**, the "tax shield." *Shortcut:* annual shield = **interest × tax rate** = $60M × 25% = $15M.

*The deeper point — debt is cheaper than its coupon.* Because the government effectively refunds (tax rate) of every interest dollar, the true cost of debt is **rate × (1 − tax rate)**:

| $600M debt @ 10% | Headline | After the tax shield |
|---|---|---|
| Annual interest cost | $60M (10.0%) | $45M (**7.5%**) |

A 10% coupon really costs 7.5% after tax — which is why valuation models discount debt at its **after-tax cost**, and part of why leverage is financially attractive.

*Caveats (revisited in Module 3):* the shield is only worth something if the company has enough profit to *use* the deduction (no taxable income → no shield), and tax law **caps** interest deductibility (US: broadly ~30% of EBITDA), so you can't lever up indefinitely just to harvest tax savings.

**2. Discipline effect** — heavy debt forces management to generate cash every quarter (or default), cutting waste and empire-building (Jensen's free-cash-flow theory).

**3. Deleveraging** (from 1.6) — paying down debt steadily converts enterprise value into equity value over the hold.

**Part 4 — limits & risks (the other edge).** Core danger: **interest is fixed; performance is not.** 
- **Coverage fragility:** $100M EBITDA, $60M interest → 1.67× coverage; a 30% EBITDA dip (→$70M) drops coverage to 1.17× and cash-after-interest from $40M → $10M. A modestly bad year for the business becomes existential for the balance sheet (Part-1 amplification in reverse). Below 1.0× = can't pay = default.
- **Covenants:** *maintenance* (tested every quarter regardless — e.g., max leverage/min coverage; stricter, lender-friendly) vs *incurrence* (only triggered by an action — new debt, dividend, acquisition). Cheap-money era → "cov-lite" (few maintenance covenants) became norm; good for sponsors, riskier for lenders.
- **Floating-rate exposure:** senior term loan = SOFR + spread; SOFR spike 2022–23 auto-raised interest → squeezed coverage industry-wide → drove leverage down 6–7× to 4–5×.
- **Refinancing / maturity walls:** LBO debt matures ~5–7 yrs, must be refinanced; a frozen credit market at maturity = punishing rates or can't refinance.
- Real bookend: Hilton (survived, triumph) vs TXU/Energy Future Holdings (~$45B, bankrupt 2014 — the largest LBO for 18 years, until Electronic Arts's $55B take-private in 2025). Same tool, opposite outcomes.

**Current market (verified ~Jun 2026):** entry ~11.7× EV/EBITDA avg (Q1 2025); leverage ~4–5× (down from 6–7× pre-2022); debt cost ~9–11%; equity ~45–55% (up) → more reliance on operational value creation. **Real anchor:** Verint (~$2.7B leveraged loan, refis Calabrio too; Verint EBITDA ~$249.5M; Calabrio debt = SOFR+ unitranche held by private credit — Golub/HPS/Monroe) → private credit (1.3) + floating-rate debt (1.7) funding a buy-and-build add-on (1.5).

## Deep dive — Two ways to die from leverage: Situational Awareness vs TXU
Leverage doesn't *create* the loss — a broken thesis does. But leverage converts "wrong" into "wiped out," and *how* the leverage is structured decides whether you die in **six days** or **seven years**. Two real blow-ups, same disease, opposite tempos.

**The two bets.**
- **Situational Awareness (2026)** — a *hedge fund* that ran ~$225M into ~$45B in under two years (up 439% net through June) on a concentrated AI-infrastructure bet: long the AI winners (SK Hynix, CoreWeave, Nebius…), short the presumed losers, at **~4x gross leverage** plus options.
- **TXU / Energy Future Holdings (2007)** — for 18 years *the* largest LBO in history (~$45B; KKR, TPG, Goldman Sachs), a leveraged bet by a PE consortium that natural-gas-set power prices in Texas would stay high, making TXU's baseload generation hugely profitable. **~$8B equity, ~$40B debt** (~5:1).

**Both theses reversed.** Fracking collapsed natural-gas prices from 2008 → TXU's margins evaporated. A July-2026 AI-infrastructure selloff (the Philadelphia Semiconductor index ~−29% from its peak) hit *both* sides of Situational's book at once.

**But they died completely differently:**

| | Situational Awareness (hedge fund) | TXU / EFH (LBO) |
|---|---|---|
| Leverage | ~4x gross, via prime-broker **margin** | ~5:1 debt/equity, via **termed** loans & bonds at the company |
| Marked to market? | **daily** | **no** — until a realization event |
| What triggered the end | **margin calls** — collateral fell, brokers demanded cash | **maturity wall** — serviced interest for 7 yrs, couldn't repay/refinance **principal** |
| Speed of death | **~6 days** (forced block sale to Citadel at a >10% discount) | **~7 years** (2007 buyout → 2014 Chapter 11) |
| Equity outcome | fund $45B → ~$10B; down 67% on the month | sponsor equity ~$8B **wiped**; KKR wrote off ~90%; Buffett lost ~$873M on the bonds |
| Could waiting have saved it? | **Yes, ironically** — many holdings *rebounded* the day after the forced sale; arguably "early, not wrong" | **No** — the thesis was structurally broken (shale wasn't a dip) |

**The lesson is in the last row** — the two distinct dangers of leverage:
- **Margin / liquidity leverage (hedge fund)** can kill you *even when you're right but early*: daily marks + callable loans force you to sell at the bottom, crystallizing a loss a patient, unlevered holder would have ridden out. Situational's stocks rebounding the next day is the cruelest possible proof.
- **Termed leverage (LBO)** buys you *time* to be right — TXU serviced its debt for seven years — but time can't save a permanently broken thesis, and the debt load removes any margin for error in the meantime.

**Why the LBO structure looks "safer" — and why that's misleading.** The PE structure genuinely prevents the 6-day death: no daily marks, no margin calls, term debt that can't be yanked on a price dip. But the same illiquidity that blocks the fast death is what produces the *slow* one (TXU's grind; the zombie-fund trap). PE doesn't shrink leverage risk — it **trades a fast, violent, visible risk for a slow, grinding, hidden one.**

**The punchline — illiquidity is the whole trade.** What survived Situational's collapse? Its one **illiquid, unmarked, un-callable** position: a ~$5B stake in Anthropic. It couldn't be margin-called or force-sold, so it lived, and the fund reportedly continues as "a private investment vehicle" built around it. In its crisis, the hedge fund's salvation was the one asset that behaved like a **private-equity** holding. That is the entire PE bargain in a single fact: illiquidity is what saves you from the run — and exactly what can trap you afterward.

*(Sources: WSJ, "His Wedding Guests Were Arriving—Just as His $45 Billion Fund Was Falling Apart," Jin, Rudegeair, Zuckerman & Gardizy, July 31 2026, plus CNBC / FT / Bloomberg, July 2026; TXU/EFH: Harvard Business School case, contemporaneous financial press, and Berkshire Hathaway disclosures. Figures are point-in-time.)*

## Deep dive — EBITDA basics (foundation)

**EBITDA = Earnings Before Interest, Taxes, Depreciation & Amortization.** Add back four things to profit to isolate core operating performance:
- **Interest** — depends on financing (how much debt), not operating quality. Strip it out.
- **Taxes** — depend on jurisdiction/structure/past losses, not operations.
- **Depreciation** (physical assets) & **Amortization** (intangibles) — *non-cash* accounting charges; no cash leaves in the year recorded.

→ EBITDA = operating profit before those, a rough proxy for cash the business throws off.

**Build (income statement, top-down):**

| Line | $ |
|---|---|
| Revenue | 400 |
| − COGS | (250) |
| = Gross profit | 150 |
| − SG&A (opex) | (50) |
| **= EBITDA** | **100** |
| − D&A | (20) |
| = EBIT (operating income) | 80 |
| − Interest | (20) |
| = Pre-tax income | 60 |
| − Taxes (25%) | (15) |
| = Net income | 45 |

Bottom-up check: EBITDA = Net income 45 + Taxes 15 + Interest 20 + D&A 20 = **100**. ✓

**Why PE cares:** (1) proxy for cash to service debt; (2) apples-to-apples comparison across companies regardless of financing/taxes (crucial when you're about to change the financing); (3) the unit of measurement — valuation is quoted as EV/EBITDA multiples, leverage as *turns* of EBITDA.

**Honest caveat:** EBITDA ≠ cash flow. It ignores real cash costs — actual interest, actual taxes, and especially **capex** (cash to replace worn-out assets). Depreciation exists *because* assets wear out, so adding it back flatters capital-heavy businesses. Sharper measures: EBITDA − capex, free cash flow. Always ask "what's the capex?" (**Adjusted EBITDA** = EBITDA with one-time/non-recurring items added back — legitimate for truly one-off items, abused when recurring costs get excluded; ties to Quality of Earnings, Module 3.2.)

**Turns & interest coverage (built on EBITDA):**
- A "turn" = one multiple of EBITDA. Turns of leverage = Total Debt ÷ EBITDA. ($100M EBITDA → 5 turns = $500M debt; 6.5 turns = $650M.)
- Interest coverage = EBITDA ÷ annual interest. 2.0× = comfortable; ~2×+ is what lenders want; 1.0× = all operating profit eaten by interest.
- Interest = debt × rate, so the same debt costs more as rates rise. $100M-EBITDA company:

| Debt | Rate | Interest | Coverage |
|---|---|---|---|
| 5 turns ($500M) | 5% | $25M | 4.0× |
| 6.5 turns ($650M) | 5% | $32.5M | 3.1× ✓ |
| 5 turns ($500M) | 10% | $50M | 2.0× ✓ |
| 6.5 turns ($650M) | 10% | $65M | 1.5× ✗ thin |

→ Rates ~doubling (5%→10%) turned a healthy 6.5-turn structure into a too-thin one, forcing leverage down (~5 turns) and equity up. The business didn't change; the cost of its debt did.

---

## 1.8 Introduction to Valuation Methods (DCF, Comparables & Multiples)

**Fundamental question:** what is a company *worth* (≠ the asking price)? Two philosophies: **relative** (comps — what similar companies are worth) and **intrinsic** (DCF — worth based on its own future cash).

### Method 1 — Comparables & Multiples (relative)
- A **multiple** = Value ÷ a financial metric. Workhorse = **EV/EBITDA** ("trades at 10× EBITDA" → EV = 10 × EBITDA). Like valuing a house by $/sq ft.
- **EV vs Equity Value** (foundational): **Enterprise Value** = value of the whole business (all capital providers) = Equity Value + Net Debt. **Equity Value** = EV − Net Debt. Match metric to layer: *pre-interest* metrics (Revenue, EBITDA, EBIT) belong to everyone → pair with **EV**; *post-interest* metrics (net income/EPS) belong to shareholders → pair with **Equity/Price** (P/E). Mixing them (EV/net income, Price/EBITDA) = classic error.
- Two types: **trading comps** (similar *public* companies' current multiples) vs **transaction/precedent comps** (multiples *paid* in recent M&A — run *higher* due to control premium).
- **Process:** pick comps → find their EV/EBITDA → take median → × your EBITDA = implied EV → − net debt = implied equity. *Ex:* $100M EBITDA; comps 9/10/11/12× (median 10.5×) → EV $1,050M − $200M net debt = $850M equity.
- Pros: fast, market-grounded, easy to communicate. Cons: garbage-in/garbage-out (comparability is a judgment); inherits current market sentiment.

### Method 2 — DCF (intrinsic)
**Core idea:** a company is worth the present value of every dollar of cash it will generate for the rest of its life.

**Define the terms first (this is where g finally gets pinned down):**

| Term | Symbol | What it is |
|---|---|---|
| Free cash flow | FCF | Cash left after taxes and reinvestment (capex + working-capital changes) — the cash EBITDA ignores |
| Discount rate | r (= WACC) | Converts future dollars into today's; opportunity cost + risk. For a company, the blended cost of debt + equity |
| Terminal (perpetuity) growth rate | **g** | **The "forever rate"** — the constant rate at which FCF is assumed to grow *in perpetuity*, after the explicit forecast ends. Must be **below r**, and modest (≤ long-run GDP/inflation, ~2–3%): no company can outgrow the whole economy forever |
| Terminal value | TV | The value of *all* cash flows beyond the explicit forecast window, captured in a single number |
| Enterprise value | EV | PV of the explicit FCFs + PV of the terminal value |

**Step 1 — Time value of money.** Future cash is worth less than cash today: **PV = Future ÷ (1 + r)ⁿ**.

| $100 discounted at r = 10% | Year 1 | Year 2 | Year 3 | Year 5 |
|---|---|---|---|---|
| Present value | $90.9 | $82.6 | $75.1 | $62.1 |

**Step 2 — The five steps of a DCF.** (A) project FCF (~5 yrs) → (B) discount each year to PV → (C) add the **terminal value** → (D) sum = Enterprise Value → (E) − net debt = equity value.

**Terminal-value formula (Gordon growth):** TV = final FCF × (1 + g) ÷ (r − g), then discounted back to today. It values a cash-flow stream growing at **g forever**, discounted at **r** — which is exactly why **g must stay below r**: if g ≥ r the denominator (r − g) hits zero or goes negative and the value explodes to infinity.

**Worked example** — FCF grows $100M → $140M over 5 years; r = 10%, g = 2%, net debt = $200M:

| Year | FCF ($M) | Discount factor @ 10% | PV ($M) |
|---|---|---|---|
| 1 | 100 | 0.909 | 90.9 |
| 2 | 110 | 0.826 | 90.9 |
| 3 | 120 | 0.751 | 90.2 |
| 4 | 130 | 0.683 | 88.8 |
| 5 | 140 | 0.621 | 86.9 |
| **PV of explicit FCFs** | | | **447.7** |
| Terminal value at yr 5 = 140 × 1.02 ÷ 0.08 = 1,785; PV = 1,785 × 0.621 | | | **1,108.3** |
| **Enterprise value** | | | **1,556** |
| − Net debt | | | (200) |
| **Equity value** | | | **1,356** |

**The punchline:** terminal value is **$1,108M of the $1,556M EV = 71%** of the answer. So roughly two-thirds of the valuation rests on the two assumptions buried inside the terminal value (r and g) — the DCF's central weakness. Nudge g from 2% to 3% (holding r) and the value jumps sharply; that's why practitioners run r/g sensitivity tables and treat any single-point DCF with suspicion.

**Pros:** fundamentals-based; ignores market sentiment. **Cons:** "torture the assumptions" — tiny changes in r and g swing the value enormously (that 71% is why).

### Method 3 (synthesis) — the football field & the LBO angle
**Football field.** Each method yields a *range*, not a point, and they rarely agree → plot the ranges side-by-side and find the **convergence zone** = the defensible value that frames negotiation and goes to the investment committee.

| Method | Illustrative EV range | Note |
|---|---|---|
| Trading comps | $900M – $1,150M | public peers; no control premium |
| Precedent transactions | $1,050M – $1,300M | M&A multiples *paid* → higher (control premium) |
| DCF | $1,050M – $1,350M | intrinsic; swings with r and g |
| LBO (max a PE buyer can pay) | $850M – $1,100M | the walk-away ceiling — usually the lowest |
| **Convergence zone** | **~$1,050M – $1,100M** | where the methods overlap = defensible value |

**LBO analysis** asks a *different question*: not "what is it worth?" but "what's the **max a PE buyer can PAY** and still hit target return (~20–25% IRR / ~2.5–3× MOIC)?" Run the LBO model **backwards** — fix the required return + exit assumptions, solve for the highest entry price = the PE firm's **walk-away ceiling**. Usually the *lowest* range, because financial buyers need a return while strategics can pay more for **synergies** (why PE often loses auctions to corporates). Ties together EBITDA (1.7), leverage (1.6–1.7), MOIC/IRR (1.6), exit multiple (1.6).

#### Worked example — solving for the walk-away ceiling
The required return is an **input**, not an output; fix it (and the exit assumptions), then solve backward for the highest entry price. Setup:

| Assumption | Value |
|---|---|
| Entry EBITDA | $100M |
| Debt at entry (leverage) | 5.0× = $500M |
| Hold period | 5 years |
| EBITDA at exit | $130M (30% cumulative growth) |
| Debt repaid over hold | $200M ($500M → $300M) |
| Exit multiple | 10.0× |
| **Required return** | **2.5× MOIC** |

**Step 1 — exit equity (independent of entry price).** What a future buyer pays minus the debt still outstanding: (130 × 10.0) − 300 = **$1,000M**. Note the entry price does *not* appear here.

**Step 2 — max equity check (work back from the hurdle).** MOIC = exit equity ÷ entry equity, so the most equity the firm can invest = 1,000 ÷ 2.5 = **$400M**. Any more and the deal returns less than 2.5×.

**Step 3 — add back the debt to get the ceiling.** Price = equity + debt = 400 + 500 = **$900M = 9.0× EBITDA**. That's the walk-away ceiling: pay more and the firm misses its 2.5× target.

*Forward check:* enter at $900M = $500M debt + $400M equity; exit equity $1,000M; MOIC = 1,000 ÷ 400 = **2.5× ✓** — exactly the hurdle.

**Sensitivity — the ceiling is an output, so every assumption moves it.** Raising the required return to 3.0× drops max equity to $333M and the ceiling to **$833M / 8.3×** (demand more profit → pay less). More leverage *raises* the ceiling — but by **less than the debt added**, because higher entry debt also leaves more debt at exit (and more interest eats future paydown):

| | Base (5×) | 6× · paydown held $200M | 6× · realistic (interest eats ~$45M of paydown) |
|---|---|---|---|
| Entry debt | 500 | 600 | 600 |
| Debt repaid | 200 | 200 | ~155 |
| Exit debt | 300 | 400 | ~445 |
| Exit equity (130×10 − exit debt) | 1,000 | 900 | ~855 |
| Max equity (÷ 2.5) | 400 | 360 | ~342 |
| **Ceiling (+ entry debt)** | **900 (9.0×)** | **960 (9.6×)** | **~942 (9.4×)** |

**Two forces on leverage:** (1) more debt funds more of the same check → ceiling **up**; (2) more debt left at exit → less exit equity → ceiling **down**. Adding a turn of debt ($100M) raised the ceiling only ~$60M (fixed paydown) or ~$42M (once interest reduces paydown) — leverage lifts the ceiling with **diminishing returns**. This is the model-level version of the discipline point: every extra turn lets you bid more, but quietly thins the exit equity you're dividing by your return — exactly how bids built on optimistic leverage/exit assumptions get stuck (the zombie-fund risk).

---

# 2 — The Private Equity Deal Process

## 2.1 Anatomy of the Deal Process: Stages, Workstreams & Responsibilities

**Mental model:** a deal is a FUNNEL — each stage narrows the field (bidders drop) *and* deepens info + commitment. You spend serious time/money only as confidence grows (cheap low-commitment steps first; expensive steps last).

**Origination:** *auction/intermediated* (seller's bank runs a competitive process; most sizable deals; higher price for seller) vs *proprietary/off-market* (1-on-1, negotiated via relationship; less competition — the prize every firm chases).

**Stages (auction version):**
1. **Sourcing** — find the deal.
2. **Teaser + NDA** — teaser = anonymous 1–2 pager; sign NDA (confidentiality) to unlock detailed info.
3. **Round 1: CIM → IOI** — CIM = detailed ~50–100pg selling document; submit **IOI** = non-binding preliminary bid (a price range).
4. **Round 2: management presentations + data room → LOI** — LOI = firmer bid; non-binding on price but usually grants (binding) **exclusivity**.
5. **Confirmatory diligence + financing + SPA negotiation** (during exclusivity) — the deep, expensive work.
6. **Signing** — sign the SPA (binding contract).
7. **Closing** — funds flow, ownership transfers; gap between signing→closing for regulatory approvals (e.g., antitrust).
8. **Post-close** — value creation / 100-day plan.

**Key pattern:** commitment escalates **non-binding** (teaser, IOI, LOI) → **binding** (SPA). The **SPA is the first & only binding commitment to buy.** Document order: **NDA → CIM → IOI → LOI → SPA**. (LOI is non-binding on price but its exclusivity clause is binding.)

**Workstreams (parallel — run simultaneously during Stage-5 diligence to fit the limited exclusivity window):**
- **Commercial** — market attractiveness & competitive position (strategy consultant).
- **Financial / Quality of Earnings** — is reported EBITDA real & sustainable? working-capital needs (accountants; Module 3.2).
- **Legal** — contracts, litigation, IP, corporate structure (law firm; also drafts the SPA).
- **Tax** — deal structuring & exposures.
- **Operational / IT** — operations, systems, supply chain.
- **Financing** — line up the debt stack with lenders (1.7).
- All feed the deal team's **model + investment thesis**. Purpose of diligence = **confirm or KILL the thesis** (find deal-breakers before buying, not after).

**Responsibilities (PE deal-team hierarchy):**
- **Associate / Analyst** — builds the LBO model, crunches numbers, coordinates workstreams, drafts the IC memo (engine room).
- **VP / Principal** — the "quarterback"; runs the deal day-to-day, manages associates + advisors, main point of contact.
- **Partner / MD** — sources via relationships, leads negotiation, presents to IC, joins the board post-close.
- **Investment Committee (IC)** — senior partners who approve/reject at key gates (before binding bids, before signing); the **IC memo** makes the case. Deal team's job = "get it through IC."
- **Third parties / advisors** (buy-side): M&A bank, accountants (QoE/tax), lawyers (legal DD + SPA), commercial consultants, lenders. (Detailed in 2.4.) Sell-side has its own team (sell-side bank runs the auction, etc.).

---

## 2.2 Deal Documents

**Organizing idea:** each document solves a specific problem of TRUST & COMMITMENT (seller reveals info without harm if buyer walks; buyer commits progressively). Full arc: Teaser → NDA → CIM → IOI → LOI → IC memo → **SPA** → (commitment letter / credit agreement, TSA) → funds flow. First six = *getting to* a deal; SPA *is* the deal; rest = *execute* it.

**Pre-binding documents (in order):**
- **Teaser** (seller's bank) — anonymous 1–2 pager. Job: attract buyers *without* revealing the company is for sale (secrecy protects staff/customers/competitive position). Non-binding.
- **NDA** — first thing signed; confidentiality + use-only-to-evaluate → unlocks detailed info. Watch for *non-solicit* (no poaching) + *standstill* (no hostile takeover). **Binding.**
- **CIM** (Confidential Information Memorandum, seller's bank) — 50–100+ pg: business, market, management, historicals, and management PROJECTIONS. **KEY MINDSET: it's a SALES DOCUMENT** (written by the seller's advisor, whose pay rises with the price); projections = "hockey stick." Read it as *claims to be tested*, not truth — diligence exists to test them. Non-binding.
- **IOI** (Indication of Interest, buyer) — first written bid, NON-BINDING: valuation *range*, assumptions, financing sources, timeline. Job: get to round 2.
- **LOI** (Letter of Intent, buyer) — round-2 bid: specific *price*, structure, financing, + request for **exclusivity**. Split personality: **price non-binding, exclusivity + confidentiality binding.** Exclusivity ("no-shop," ~30–60 days) = buyer gets sole access; seller gets buyer's commitment to spend real diligence money. Makes Stage-5 possible.
- **IC memo** (deal team, INTERNAL) — the case to the Investment Committee: thesis (why this co/now/how we make money), valuation & returns (LBO — MOIC/IRR), structure/financing, diligence findings, honest **risks & mitigants**. Where all of Module 1 converges.

**The binding contract — SPA (Sale & Purchase Agreement):** the first document that legally commits you to buy. Five components:
1. **Purchase price + adjustment** — agree an EV, but the seller *receives* equity value = EV − net debt, adjusted for **actual net debt & working capital at CLOSING** (business keeps operating in the gap). Mechanisms: *completion accounts* (post-close true-up) or *locked box* (price fixed at an earlier balance-sheet date).
2. **Reps & warranties** — seller's formal statements of FACT (financials accurate, no undisclosed litigation, owns IP, law-compliant); allocate risk — if false, buyer has a claim.
3. **Covenants** — promises about BEHAVIOR; esp. interim ("run the business in the ordinary course, nothing drastic" between sign & close).
4. **Conditions to closing** — must be true before closing is obligatory: regulatory/antitrust approval, no **Material Adverse Change (MAC)**, reps still true.
5. **Indemnification** — remedy for breached reps (seller compensates buyer; caps/baskets/survival). Increasingly **R&W insurance** (buyer claims against a policy vs chasing the seller).

- **SPA vs APA:** SPA = buy the SHARES/equity (get all assets AND liabilities); APA = buy specific ASSETS (assume only chosen liabilities). Buyers often prefer asset deals (cleaner + tax step-up); sellers prefer share deals. Full treatment Module 3.4.

**Closing mechanics documents:**
- **Financing docs:** *debt commitment letter* = lender's binding promise to fund (proves the money is there) + term sheet; *credit agreement* = the actual detailed loan contract at close (rate, covenants [1.7], maturity, security); *equity commitment letter* = the fund's equity slice.
- **TSA (Transition Services Agreement):** carve-outs only — parent keeps providing shared services (IT, payroll, HR) for a transition period while the buyer builds its own (Boeing/Jeppesen).
- **Funds flow (memo/statement):** the closing "money map" — every dollar wired on closing day: SOURCES (fund equity + lender debt) and USES (pay seller, repay old debt, pay fees). = the Sources & Uses from 1.6 made real; ensures everyone's paid the exact right amount simultaneously.

**Signing → closing gap:** sign SPA → [gap: satisfy conditions — regulatory approval, financing finalized, no MAC, reps hold; seller runs the business "in the ordinary course"] → Closing (funds flow, ownership transfers) → Day 1+: TSA (carve-outs) + 100-day plan.

---

## 2.3 Key Terms and Points of Negotiation

**Master frame:** every term = a buyer-vs-seller tug-of-war. Buyer wants lower effective price + more protection; seller wants higher net proceeds + more certainty. The headline price is only ONE lever — the effective price hides in the mechanisms.

**Part 1 — Price fights ("how much & in what form"):**
- **Headline price** — usually a multiple (EV/EBITDA); fights over "the multiple" or "which EBITDA" (adjusted add-backs) ARE price fights (→ QoE, Module 3).
- **Form of consideration:** *all cash* (seller certainty); **earnout** = part of price contingent on hitting future targets — bridges a valuation gap ("you get the extra $X if you hit the numbers"); lets each side "be right"; elegant but contentious (measurement, control, accounting games). **Rollover equity** = seller/management reinvests proceeds into the new deal — aligns incentives, cuts the buyer's cash need, signals belief.
- **Price mechanism / working-capital peg (the hidden price fight):** deals are "cash-free, debt-free" (seller keeps cash, clears debt); working capital needs a normal level to operate → agree a **target/"peg"**; price adjusts ± vs actual WC at closing. Without a peg the seller could *starve* the business (collect receivables, delay payables, run down inventory) → the peg protects the buyer; where it sits moves the effective price by millions. *Locked box* (price fixed at earlier date) vs *completion accounts* (post-close true-up).
- Effective-price bridge: EV − net debt ± WC = equity value; then − rollover − escrow − earnout = **cash to seller at close**. Headline ≠ cash-in-pocket (ex: $500M EV → $250M cash now).

**Part 2 — Risk fights:**
*"What if something's wrong?" (reps + indemnities):*
- **Reps scope:** buyer wants BROAD; seller wants NARROW + qualified ("to seller's knowledge," materiality qualifiers) — each qualifier shifts risk to the buyer.
- **Indemnification package** (money if a rep breaks), four dials: **cap** (max seller liability — seller low, buyer high), **basket/deductible** (threshold before recovery; *true deductible* = recover only the excess above it), **survival period** (how long reps last — seller short, buyer long; fundamental reps + tax survive longer), **escrow/holdback** (price parked to fund claims).

Worked example — $5M basket (true deductible) and $50M cap:

| Claim size | Recovery | Why |
|---|---|---|
| $3M | $0 | below the $5M basket — buyer bears it |
| $40M | $35M | above basket → recover the excess ($40M − $5M) |
| $70M | $50M | exceeds the cap → recovery capped at $50M |

(A *tipping* basket instead of a true deductible pays from dollar one once crossed — so the $40M claim would recover the full $40M. The basket *type* is itself negotiated.)
- **R&W insurance (RWI):** a third-party insurer covers rep breaches instead of clawing back from the seller → seller exits "clean" (low/no escrow, low cap), buyer still protected; now standard in mid/large PE deals (buyer-vs-insurer, not buyer-vs-seller).

*"What if it doesn't close?" (certainty):*
- **MAC (Material Adverse Change) clause:** buyer can walk if the business is materially damaged in the gap. Seller wants NARROW (carve-outs: industry-wide/pandemic/macro don't count); buyer wants BROADER. Famously hard to invoke (sellers usually win).
- **Financing "out":** can the buyer walk if debt falls through? Sellers hate it → competitive buyers offer committed financing with NO financing out (on the hook to close regardless).
- **Reverse termination / break fee:** buyer pays the seller if it fails to close → gives the seller deal certainty (a price for walking).
- **Certainty-vs-price tradeoff:** sellers often accept a slightly LOWER but more-certain bid (no financing out, tight conditions, strong break fee) over a higher, shakier one. Certainty of close is itself worth money.

**Buyer vs seller directions:** reps (broad vs narrow) · cap (high vs low) · basket (small vs big) · escrow (big vs small) · survival (long vs short) · MAC (broad vs narrow) · financing out (keep vs remove) · break fee (low vs high).

---

## 2.4 The Role of Third Parties & Their Functions

**Why third parties:** a PE deal team is LEAN (~3–5 people) → it *rents* specialized expertise per deal. They provide (1) **expertise** the small team lacks (securities law, tax, forensic accounting, industry knowledge), (2) **capacity** to run many workstreams under a tight clock, (3) independent **credibility/validation** — the IC and lenders trust a Big-4 QoE or a top consultant's market study far more than the deal team's own numbers. Independence *is* the product.

**The cast (maps onto the 2.1 workstreams):**
- **Investment bank / M&A advisor** — *sell-side*: runs the auction, writes teaser + CIM, manages the process, maximizes price. *buy-side*: advises the buyer (less common — PE firms often self-source).
- **Lawyers** — legal DD (contracts, litigation, IP, structure), draft/negotiate the SPA + all docs, manage regulatory/antitrust.
- **Accountants** — financial DD / **Quality of Earnings** (validate EBITDA & working capital) + tax structuring (Big-4 or specialist).
- **Consultants (strategy)** — **commercial DD** (market attractiveness, competitive position, growth credibility); sometimes operational/value-creation work.
- **Lenders** (banks + private-credit funds) — provide the debt stack (1.7); run their own diligence before committing.
- **Specialists** — insurance, environmental, IT/tech, HR/benefits.
- **Others:** R&W insurance brokers/underwriters, escrow agents, (public deals) proxy solicitors; regulators (a party, not an advisor); target management (key counterparty — rollover/MIP).

**Sell-side vs buy-side:** the same *types* of advisor sit on both sides — every deal = two advisory teams facing off.
**Cost/timing:** advisors are expensive (fees into the millions) → engaged heavily only AFTER exclusivity (cheap steps first, expensive steps last — 2.1).

---

## Deep dive — Reading a real software income statement (Dayforce, FY2024)

*One of the most instructive real examples in the course. Real figures from Dayforce's reported FY2024 results (last full year public, before the Thoma Bravo take-private). $ in millions.*

### 1. The income statement

| Line | FY2024 |
|---|---|
| Recurring revenue (subscriptions) | 1,517.3 |
| Professional services & other | 242.7 |
| **Total revenue** | **1,760.0** |
| Cost of revenue — Recurring | (352.7) |
| Cost of revenue — Professional services | (291.0) |
| Cost of revenue — Product development (R&D) | (223.8) |
| Cost of revenue — D&A | (80.4) |
| **Total cost of revenue** | **(947.9)** |
| **Gross profit** | **812.1** |
| Selling & marketing | (342.0) |
| General & administrative | (366.0) |
| **Operating profit (EBIT)** | **104.1** |
| Interest expense, net | (40.6) |
| Other expense, net | (25.9) |
| Income before taxes | 37.6 |
| Income tax | (19.5) |
| **Net income** | **18.1** |

### 2. What comprises COGS ("cost of revenue") — software has no raw materials; COGS = cost of *delivering the service*
- **Recurring $352.7M** — cloud hosting/infrastructure, customer support, third-party data, money-movement for payroll.
- **Professional services $291.0M** — salaries of implementation consultants who onboard customers.
- **Product development / R&D $223.8M** — engineers building/maintaining the software.
- **D&A $80.4M** — depreciation of equipment + some amortization.
- **Quirk:** Dayforce puts R&D + D&A *inside* COGS (most SaaS report R&D as a separate opex line below gross profit). This makes headline GAAP gross margin look like **46%** ($812.1 ÷ $1,760.0), but the true SaaS "Cloud recurring gross margin" is **78.9%**. Same company, 33-pt swing purely from classification → always ask "margin *defined how?*" (the QoE mindset).

### 3. What comprises SG&A
- **Selling & marketing $342.0M** — sales comp + commissions, advertising (2024 = first mass-ad campaign under the new brand), marketing/events.
- **General & administrative $366.0M** — exec/finance/legal/HR/IT/facilities, plus a large slug of amortization of acquired intangibles and SBC.

### 4. Where the clean textbook chain BREAKS for real software
Idealized chain: Rev − COGS = GP → − SG&A = EBITDA → − D&A = EBIT → − int & tax = NI. In reality:
- Revenue − COGS = Gross profit ✓ (1,760.0 − 947.9 = 812.1).
- Gross profit − SG&A = **104.1 = EBIT (operating profit), NOT EBITDA** — because D&A ($80.4) and R&D were already removed up in COGS.
- **EBITDA is not a line** — reconstruct it: NI + interest + tax + total D&A = 18.1 + 40.6 + 19.5 + **209.8** = **288.0**. Total D&A ($209.8) >> the $80.4 shown on the face; the rest = amortization of acquired intangibles scattered in G&A → pull D&A from the **cash-flow statement**, not the income statement.

### 5. The software-profitability chasm: $18M net income → $501M "Adjusted EBITDA"
Same year, same company: GAAP net income **$18.1M (1.0% margin)** vs **Adjusted EBITDA $501.5M (28.5% margin)**.
Bridge: NI 18.1 → +interest & tax 60.1 → +D&A 209.8 → **EBITDA 288.0** → +SBC & related 156.6 → +one-off items 56.9 → **Adjusted EBITDA 501.5**.
The gap is almost entirely huge non-cash charges: **D&A $209.8M** (mostly amortization of past acquisitions) + **SBC $156.6M**. Knowing which metric someone means is the whole game in software.

### 6. Adjusted EBITDA → Free Cash Flow (the reconciliation, incl. working capital)
Adjusted EBITDA is NOT cash. The naive "Adj EBITDA − capex − interest − tax" ($501.5 − 109.6 − 45.3 − 56.4 = **$290.2**) does NOT equal FCF (**$171.5**). Full bridge:

| Adjusted EBITDA → FCF | $M |
|---|---|
| Adjusted EBITDA | 501.5 |
| − Cash interest paid | (45.3) |
| − Cash taxes paid | (56.4) |
| − Working-capital & operating-item investment | (106.0) |
| − Other timing / non-cash items, net | (12.7) |
| **= Operating cash flow** | **281.1** |
| − Capital expenditures | (109.6) |
| **= Free cash flow** | **171.5** |

The ~$118.7M the naive formula misses = **working capital −$106.0M** + ~$12.7M other timing. The WC drag (what a growing subscription business does with cash):
- Growing receivables −$48.0M (earned but not yet collected).
- **Deferred sales commissions −$43.9M** (SaaS hallmark: commissions paid *upfront* on multi-year deals but expensed over the contract life → real cash out now).
- Cash earnout (contingent consideration) payment −$20.9M (Adj EBITDA had added it back).
- Other operating items, net +$6.8M.

**Lesson:** working capital is a *hidden, recurring* cash drain for GROWING companies (fund more receivables + prepay more commissions every year). Adj EBITDA ignores it; FCF captures it — which is why FCF ($171.5M) is less than half of Adj EBITDA ($501.5M). Never proxy cash as "EBITDA minus a few items" in an LBO; build actual cash flow *including Δ working capital* (→ Module 3 Net Working Capital).

### 7. Capex breakdown ($109.6M)
- **Property, plant & equipment $14.3M (13%)** — offices, servers, leaseholds.
- **Software & technology $95.3M (87%) = capitalized software development** — engineering cost recorded as an asset/investment (not expensed), then amortized later → feeds the D&A above.
- Total product/tech investment ≈ expensed R&D $223.8M + capitalized $95.3M ≈ **$319M**; the expense-vs-capitalize split is an accounting **judgment**. **QoE flag:** capitalizing more software flatters current EBITDA/earnings (less expense now) but inflates capex + future D&A. For software, **capex ≈ capitalized R&D, not factories.**

### 8. Accrual vs cash (two subtleties you'll hit constantly)
- *Why the EBITDA bridge uses accrual interest/tax but the FCF bridge uses cash:* EBITDA is an ACCRUAL earnings metric (un-does the income statement) → add back **accrual** interest $40.6M + tax $19.5M. FCF is a CASH metric → subtract **cash actually paid** (interest $45.3M, tax $56.4M).
- *Interest:* small gap ($40.6 accrual vs $45.3 cash ≈ $4.7M) — timing/netting.
- *Tax:* **big and important — book tax expense $19.5M vs cash tax paid $56.4M**, driven by a **$34.1M non-cash deferred tax benefit** that lowered book tax but not the cash bill. → "tax expense" ≠ "taxes paid" (deferred taxes = Module 3). This deferred-tax difference is what sits in the FCF bridge's "other timing" line, so the two bridges reconcile.

### 9. Why it matters for the LBO (the payoff)
Thoma Bravo's ~$12.3B take-private ≈ **7× revenue / ~25× adjusted EBITDA** — rich multiples, justified by ~98% gross revenue retention + a recurring-revenue base you'd see in the CIM. But a Quality-of-Earnings team scrutinizes the **$213M of add-backs**: are "one-time" items truly one-time? And **SBC is a real economic cost (dilution)** — adding it back to reach "$501M EBITDA" flatters cash generation. That add-back skepticism = Module 3's Quality of Earnings.

**Big takeaways:** (1) COGS/margins depend on classification — always ask "defined how?" (2) EBITDA isn't a line; reconstruct it from the D&A in the cash-flow statement. (3) The GAAP-vs-adjusted chasm (non-cash D&A + SBC) is the software story. (4) Adj EBITDA ≠ cash — working capital + capex + cash interest/tax turn $501M of Adj EBITDA into $171M of FCF. (5) "Expense" ≠ "cash" (deferred tax; capitalized software). (6) All of this is what Quality of Earnings exists to catch.

---

## Deep dive — Why SBC and "one-offs" are added back (the add-back debate)

**Unifying logic:** every add-back argues "this cost shouldn't count against sustainable operating earnings." A legitimate one passes at least one test: **non-cash, non-recurring, or non-operating**. Adjusted EBITDA answers the buyer's real question: *"if I owned this next year, what would it actually earn?"* The abuse: **Adjusted EBITDA is NOT defined by GAAP — the seller writes the definition.**

**Stock-based compensation (SBC):**
- *For:* **non-cash** — granting $1M of stock creates a $1M GAAP expense but no cash leaves. Passes the non-cash test cleanly.
- *Against:* it's a **real economic cost — dilution**. You're paying with ownership; existing owners are diluted. Buffett: *"If compensation isn't an expense, what is it? And if expenses shouldn't go into the calculation of earnings, where in the world should they go?"* Practical test: stop granting stock → you must pay MORE cash salary. Also **utterly recurring** (granted every year) → fails the non-recurring test.
- *PE wrinkle:* in a take-private the public RSU program genuinely goes away (cashed out at close) and is replaced by a **management incentive plan (MIP)** — options paying only at exit. So a buyer may accept the add-back — but QoE asks: what's the **replacement cost** of retaining this workforce?

**"One-offs" — the logic:** the **multiple effect**. A one-time $10M lawsuit at a 10× multiple would wrongly cut valuation by $100M for an event that never recurs → normalize. 
*Dayforce's actual stated exclusions:* FX gains/losses, SBC + related employer taxes, severance charges, restructuring consulting fees, pension-termination costs (frozen U.S. plan), DataFuzion earnout fair-value adjustments, lease abandonment, other non-recurring items.
*The broader menu:* restructuring (severance, closures, consulting) · transaction costs (banker/legal/accounting, IPO) · legal (settlements, fines) · non-operating (FX, impairments, earnout fair-value swings) · owner-related in private cos (excess owner salary, family jet, sponsor management fees) · **pro-forma/forward-looking (run-rate synergies, annualized new-customer revenue) ← the danger zone: not removing a past cost but ADDING hypothetical future profit.**

**How large can they get?**
- **Dayforce (mainstream, credible):** EBITDA $288.0M → Adj EBITDA $501.5M = **$213.5M of add-backs = 74% uplift** (SBC alone ~$157M ≈ 54%).
- **WeWork (the legendary extreme, per its SEC filing):** FY2017 revenue $866.4M, **net loss $(933.5)M**, **"Community Adjusted EBITDA" $233.1M** — it stripped out not just ITDA but **marketing, G&A, and development/design costs**, turning a $933M loss into a $233M "profit." Covenant Review's Adam Cohen: he'd never seen the phrase in his life. When add-backs include your sales & marketing, you're measuring a fantasy.

**Defensibility spectrum (best → worst):** truly one-time (settled lawsuit, one M&A fee) → non-cash D&A (uncontroversial) → owner-related in private cos (real, but verify *replacement* cost) → **SBC (contested: non-cash but recurring + dilutive)** → **serial "one-offs"** (restructuring every year isn't non-recurring — Dayforce booked restructuring in BOTH 2023 and 2024) → **run-rate synergies / ordinary opex (fantasy)**.

**Credit agreements:** lenders define their own **"Credit Facility EBITDA"** (Dayforce's does) which routinely permits **projected synergy** add-backs — typically capped ~25% of EBITDA with an 18–24 month realization window → covenant compliance can rest on savings that haven't happened yet.

**Why it matters (the punchline):** **every $1 of accepted add-back is multiplied into purchase price.** At 10×, $1M of add-back = $10M of price. Dayforce's $213.5M of add-backs at ~25× = billions of valuation. That's why sellers push add-backs and buyers pay Big-4 to interrogate every one → **Quality of Earnings (Module 3).**

---

# 3 — Leverage, Accounting Diligence & Deal Structuring

## 3.1 Leveraged Finance, Private Credit & Capital Structures

### Part 1 — The two markets (where the debt actually comes from)
**The core distinction: originate-to-DISTRIBUTE vs originate-to-HOLD.**
- **Broadly Syndicated Loans (BSL):** a bank commits the whole loan, then **syndicates** it — sells pieces to hundreds of institutional investors (**CLOs**, mutual funds, insurers, hedge funds). The loan then **trades** (has a market price). Bank = middleman.
- **Private Credit / Direct Lending:** a credit fund (Ares, Blue Owl, Golub, HPS, Blackstone) lends directly and **holds the loan to maturity**. One lender or a small "club." No syndication, no trading, no ratings.

| | BSL | Private credit |
|---|---|---|
| Provider | Bank arranges → sells to many | A fund lends + holds |
| # lenders | Hundreds | One / small club |
| Trades? | Yes | No |
| Price | Cheaper | ~100–150 bps more |
| Speed/certainty | Slower; **"market flex"** (bank can change price/terms if it can't sell) | Fast, certain, confidential |
| In trouble | Herd hundreds of anonymous holders | One phone call |
| Best for | Large, well-known borrowers | Mid-market, complex, speed-critical |

**Why pay MORE for private credit:** certainty of close (no syndication risk / market flex — ties to 2.3 deal certainty), speed + confidentiality (no ratings, no roadshow), flexibility (will underwrite messy stories — carve-outs with no standalone audited history, roll-ups, lumpy EBITDA), and workout dynamics (renegotiate with one lender who knows you).

**Unitranche = private credit's signature innovation:** collapses the whole stack (senior 8.5% / 2nd lien 12% / mezz 14%) into **ONE loan at ONE blended rate** — one doc, one lender, fast. (= what Calabrio's SOFR+ unitranche held by Golub/HPS/Monroe was.)

**Current state (verified ~Jul 2026):** direct lending now **matches BSL at $1.5–2T**, forecast **$3T by 2028**; private credit grew from ~$806B (2018) → ~$1.6T (2023–24); BSL also grew to ~$1.4T — **not zero-sum, both expanded**. 2025: BSL spreads tightened to **lowest since the 2008 GFC**; record **PC/MM CLO issuance $43.1B**; buyout-financing direct lending deals fell to 214 (from 248). **Traffic runs both ways:** $34.1B of direct-lender loans refinanced INTO BSL (record) *and* direct lenders refinanced $36.9B of syndicated loans (record). **Convergence:** JPMorgan announced a **$50B expansion of direct lending** (Feb 2025); direct lenders write jumbo deals (Ares $3.3B Ardonagh unitranche; $2.2B Foundation Risk Partners; KKR Credit $1.1B). Best understood as **one interconnected ecosystem, not discrete alternatives** — sponsors run both processes in parallel.

### Part 2 — How a leveraged loan is priced
**Rate = benchmark + spread.**
- **SOFR (Secured Overnight Financing Rate)** = the benchmark = broad measure of cost of borrowing cash overnight collateralized by U.S. Treasuries; published daily by the NY Fed; **replaced LIBOR**. The **risk-free price of money**; moves with Fed policy; **nobody negotiates it**. **SOFR = 3.63% (July 14, 2026).**
- **Spread (credit margin)** = the premium for your credit risk. **Negotiated**, then **fixed for the life of the loan**. Quoted in **basis points** (1bp = 0.01%; 100bps = 1%). "S+475" = SOFR + 4.75%.
- *Real example today:* SOFR 3.63% + spread 4.75% = **all-in 8.38%**; on $500M debt ≈ $42M/yr interest.
- **Only the spread is fixed — SOFR floats** (resets every 1–3 months). Fed hikes SOFR to 5.5% → your rate auto-becomes 10.25%, no renegotiation. **= the exact mechanism of the "floating-rate exposure" risk (1.7); what mauled borrowers in 2022–23.**
- **SOFR floor:** a minimum SOFR (e.g., 0.50%/1.00%) so lenders still earn if rates collapse. **OID (original issue discount):** lender funds $99, you owe $100 → extra yield; a sweetener to help a loan sell.

**"Spreads tightened to lowest since 2008" — what it means:** *tightening = spread gets SMALLER = borrowers pay less* (widening = opposite). **Why: supply/demand for loans, NOT credit quality** — record CLO formation ($43.1B) = record money raised to buy loans, while LBO supply shrank (214 buyout deals vs 248) → too much capital chasing too few deals → lenders compete on price → spreads fall → **repricing/refinancing wave** (borrowers demand lower spreads or refinance away).

**The market gap, in real deals:** BradyPLUS $2.8B TLB at **S+350** (BSL) vs median PE-backed acquisition deal **S+475** (private credit) vs Mitratech $2B+ unitranche **S+475** → **~125bp gap** = the concrete price of private credit's speed/certainty. Two-way traffic: BradyPLUS jumped TO BSL (save ~125bps); Mitratech's unitranche refinanced BSL loans.

**KEY INSIGHT — decompose every rate headline into its two independently-moving parts:**

| | SOFR (Fed policy) | Spread (lender competition) | All-in |
|---|---|---|---|
| 2021 | ~0.05% | tight | ~4% |
| 2023 | ~5.3% | wide | ~10% |
| Today | **3.63%** | tightest since 2008 | **~8.4%** |
*(2021/2023 SOFR approximate; 3.63% actual.)*
→ "Spreads lowest since 2008" does NOT mean debt is cheap: lenders charge their smallest risk premium in 17 yrs, but SOFR is still 3.63% → ~8.4% all-in vs ~4% in 2021. **The lenders got cheaper; the money didn't.** This is why leverage sits at 4–5 turns not 6–7 — coverage math runs off the ALL-IN rate, and spread compression can't fix a 3.63% benchmark. Always ask: *is this a benchmark story or a spread story?*

---

## 3.2 EBITDA, Working Capital & the Quality of Earnings

### Part 1 — Quality of Earnings (QoE)
**What it is:** an accounting firm's forensic exam of the target's earnings, commissioned by the buyer during exclusivity (workstream #2, lesson 2.1). **NOT an audit.**
- **Audit asks:** "do these financials comply with GAAP?" (backward-looking compliance).
- **QoE asks:** "how much of this EBITDA is **real, sustainable, repeatable** — what will this business actually earn for me next year?" (economic reality).
- A company can pass an audit cleanly and still have terrible earnings quality.

**Central output = the EBITDA bridge:**

| | What | Reliability |
|---|---|---|
| **Reported EBITDA** | what the books say | fact |
| **Adjusted EBITDA** | ± non-cash / non-recurring / non-operating normalizations | judgment |
| **Pro forma / run-rate EBITDA** | ± things that haven't happened yet (full-yr effect of an acquisition, planned savings, synergies) | speculation |
Seller markets on #3; buyer underwrites near #2. **That gap is the negotiation.**

**KEY INSIGHT — QoE is BIDIRECTIONAL.** Beginners think "add-backs" (EBITDA up). Buy-side QoE hunts equally for **negative adjustments** (EBITDA down) that sellers never volunteer:
- **Understated costs** — founder pays himself $200k; a market CEO costs $600k → −$400k *forever*.
- **Missing standalone costs (the carve-out killer)** — a division inside a parent doesn't pay for its own CFO, audit, insurance, IT; standalone it does → often millions of new recurring cost.
- **One-time BENEFITS left in** — a large one-off order, insurance recovery, supplier rebate → strip OUT.
- **Deferred maintenance** — capex starved to flatter cash flow; you must catch up.
- **Revenue-recognition timing** — sales pulled forward ("channel stuffing") borrowing from next year.
→ Buy-side QoE frequently *lowers* the CIM's number. At 10×, every $1M = $10M of price.

**Signature technique — "proof of cash":** tie reported revenue/EBITDA back to actual **bank statements**. Revenue can be manufactured on paper; cash deposits can't. *Earnings are an opinion; cash is a fact.*

**Sell-side QoE:** sellers now commission their own before launching the auction — to find/fix problems first and **control the add-back narrative**. But it's paid for by the seller (2.2 mindset) → buyers read it, then do their own anyway.

**Worked example:** seller reports $20M Adj EBITDA. QoE finds: (a) founder salary $200k vs market CEO $600k → **−$400k**; (b) $1.5M genuinely one-time legal settlement expensed → **+$1.5M** (add back — *in the seller's favor; good QoE is accuracy, not lowballing — that's what makes your number defensible*); (c) $2M revenue from a single non-repeating order → **−$2M**; (d) seller added back $1M "restructuring" but it's booked every year for 4 years → **−$1M** (note the mechanic: you're *removing the seller's add-back*, not removing a cost — the cost is real & recurring so it belongs IN EBITDA). Net **−$1.9M → adjusted EBITDA $18.1M.** At 10×: price $200M → **$181M** (~10% of the price found). *3 of 4 moved DOWN — the typical shape.*

### Part 2 — Net Working Capital (NWC)
**Definition (deal version — operating NWC, EXCLUDING cash & debt, because deals are "cash-free, debt-free"):**
**NWC = (Receivables + Inventory) − Payables**

**Intuition:** you pay suppliers BEFORE customers pay you. NWC = cash **permanently trapped** in running the business (stuck in inventory on shelves + unpaid invoices) — cash you can never use for debt service.

**The killer property: NWC GROWS WITH THE BUSINESS.** +20% revenue → ~+20% receivables & inventory. **Growth eats cash** — a fast-growing, profitable company can still run out of money. (= Dayforce's −$48M receivables + −$43.9M deferred commissions.)

**Why PE cares — two reasons:** (1) **in the model** — a real cash outflow that cuts cash available for debt service; ignore it and you overstate cash flow + understate default risk. (2) **in the deal** — the **NWC peg** (2.3), and QoE's job is to SET it.

**The peg:** agree a **target** for "normal" NWC, usually a **trailing-12-month average** (smooths seasonality — a retailer in November ≠ February). At closing: actual **above** target → buyer pays **more**; **below** target → price **reduced**. **Every dollar of the peg is a dollar of price** — set it $5M too low and the buyer overpays $5M invisibly, with no change to headline EV. Sellers argue low peg; buyers argue high. Needs 24–36 months of monthly data to find "normal."

**The nastiest fight: "is that DEBT or WORKING CAPITAL?"** Price = EV − **net debt** ± WC, so reclassifying an item as **debt-like** cuts the price dollar-for-dollar. Buyers hunt debt-like items in current liabilities:

| Item | Seller says | Buyer says |
|---|---|---|
| Accrued bonuses | working capital | **debt-like** — a fixed obligation I inherit |
| Deferred revenue | working capital | **debt-like** — I must deliver service I got no cash for |
| Unpaid capex / deferred maintenance | working capital | **debt-like** — a bill already come due |
| Earnouts from past deals | working capital | **debt-like** — someone else's IOU |
Fought line by line in the QoE report; one of the highest-value fights in a deal.

---

## 3.3 M&A Accounting, Purchase Price Allocation & Tax Implications

### Part 1 — Purchase Price Allocation (PPA): where acquired intangibles come from
**Question PPA answers:** you paid $X for a company — on YOUR new balance sheet, what did you buy? Accounting requires itemizing it.
**The rule that changes everything:** you record what you bought at **FAIR VALUE, not the seller's book value** (their book value is history — what *they* paid years ago). = **purchase accounting / acquisition method**; the itemization = **PPA**.

**Three steps:** (1) total purchase price; (2) identify EVERY identifiable asset + liability, each at fair value; (3) leftover (price − fair value of identifiable net assets) = **goodwill** (the **plug** that balances the equation).

**KEY ASYMMETRY — PPA CREATES assets never on the seller's books:**
> **Internally developed** intangibles (your own brand, customer relationships) generally CANNOT be capitalized (marketing/selling expensed as incurred → asset never appears). But **acquired** intangibles MUST be recognized at fair value.

→ A 30-yr-old brand shows **$0** on the seller's books; the day you buy it, it appears on YOUR books at fair value. Same brand, visible only because it changed hands. (This is also why tangible net assets can exceed book equity — fair-value **step-up** on real estate/equipment above depreciated book.)

**Typical identifiable intangibles created:** customer relationships (usually biggest), developed technology/software, trade name/trademarks, non-competes, backlog.

**Worked example — $500M for a software company with $50M of book net assets.** Record each identifiable asset at fair value; goodwill is whatever is left over:

| PPA component ($mm) | Fair value | Note |
|---|---|---|
| Tangible net assets | 50 | at fair value (may be stepped up from book) |
| Customer relationships | 180 | usually the largest intangible |
| Developed technology | 90 | |
| Trade name / trademarks | 40 | |
| Non-compete | 10 | |
| **Identifiable net assets** | **370** | sum of the above |
| **Goodwill (the plug)** | **130** | = 500 price − 370 identifiable |
| **Purchase price** | **500** | what you paid |

**$320M of intangibles** (180 + 90 + 40 + 10) materialized on your books that were nowhere on the seller's — visible only because the assets changed hands.

**What goodwill really is:** the amount paid above fair value of everything identifiable — assembled workforce, synergies, reputation, going-concern value… **and sometimes overpayment** (→ goodwill impairment = public confession a deal failed).

**Crucial treatment difference:** identifiable intangibles have finite lives (customer relationships ~10yr, tech ~5yr) → **amortized** (annual P&L charge). **Goodwill is NOT amortized** — sits indefinitely, tested annually for **impairment** (written down in a lump if the business underperforms).

### Part 2 — The amortization thread (closes the Dayforce loop)
**Every identifiable intangible amortizes over its life** = new non-cash D&A that did not exist before the deal. For a $300M manufacturer acquisition:

| Acquired intangible | Fair value | Useful life | Annual amortization |
|---|---|---|---|
| Customer relationships | $90M | 10 yr | $9.0M |
| Trade name | $25M | 15 yr | $1.7M |
| Developed technology | $15M | 5 yr | $3.0M |
| Goodwill | $50M | indefinite | $0 (not amortized) |
| **Total new D&A** | | | **~$13.7M/yr** |

Operations are identical, but reported earnings now carry ~$13.7M/yr of amortization that is purely an **artifact of being acquired.**

**DAYFORCE LOOP CLOSED:** Dayforce reported $209.8M total D&A but only $80.4M on the face; net income just $18.1M. **Ceridian/Dayforce grew by acquisition** (Dayforce, PowerPay, DataFuzion…). Each acquisition → PPA → pile of customer-relationship + tech intangibles → each amortizes for ~a decade. **Amortization of acquired intangibles = the bulk of the ~$129M "scattered through G&A"** that crushed GAAP net income to $18M → *precisely why* these companies are valued on EBITDA/adjusted EBITDA (which add it back).

**Deep truth about acquisitive companies:** amortization of acquired intangibles makes a serial acquirer's GAAP earnings look terrible even when the business is healthy. It's real accounting but not a real *cash* cost (cash was paid ONCE at acquisition; amortization just spreads it on paper). = the strongest *legitimate* case for EBITDA over net income. But the same add-back logic sellers use legitimately here is what they ABUSE elsewhere — same tool, honest & dishonest uses.

**PE kicker:** when YOU buy in an LBO, a **brand-new PPA** happens on your purchase, resetting intangibles to fair value at YOUR (premium) price → usually an even bigger intangible + goodwill stack. Buy/sell/buy again → fresh goodwill each time. → GAAP net income is ~useless for LBO analysis; everyone works in **EBITDA, cash flow, enterprise value** instead.

## Deep dive — When goodwill *exceeds* the price: Boeing / Spirit AeroSystems (2026)
A real, extreme case of the 3.3 formula. Boeing bought its fuselage supplier Spirit for ~**$8.4B** (Dec 2025). Normally identifiable net assets are positive and goodwill is a slice of the price. Here they came out **negative** — so goodwill exceeds what Boeing paid:

| $B | Dec 31, 2025 | Jun 30, 2026 |
|---|---|---|
| Consideration paid | 8.4 | 8.4 |
| + Net identifiable **deficit** (liabilities > assets, at fair value) | 1.6 | 1.9 |
| = **Goodwill** | **10.0** | **10.3** |

Read it: Boeing paid $8.4B *and* took on a business whose fair-valued liabilities exceeded its assets by ~$1.9B, so goodwill absorbs both — landing at $10.3B, which **exceeds Boeing's total equity.** Allocating >100% of the price to goodwill is rare and a flashing signal.

**Four lessons this adds to the PPA mechanics:**
- **Goodwill = price − identifiable net assets, at the extreme.** When net assets are negative, subtracting a negative *inflates* goodwill above the purchase price. (The $500M-software-co example, inverted.)
- **Fair value cuts both ways — an acquired *liability*.** Spirit was locked into selling fuselages to Boeing at **below-market prices**, so PPA forces a **liability** for the PV of that shortfall — ~$1.5B of "off-market customer contracts." The mirror image of a step-*up*: you mark a money-losing contract *down* to a liability. It's the main reason net assets are negative.
- **The one-year measurement period decides *where* a loss lands.** Inside the window, newly discovered acquired liabilities adjust the allocation and route to **goodwill (balance sheet)** — Boeing's $455M contract-liability increase bumped goodwill $10.0B → $10.3B instead of hitting the P&L as a $455M expense ("relegated to footnotes"). *After* the window closes, further deterioration hits the **income statement** directly. Same economic loss, different statement, by timing.
- **Goodwill > equity is an impairment risk, not a strength.** Goodwill isn't amortized but *is* impairment-tested; this $10.3B is a loaded gun for a future write-down. The tell (WSJ): *if the deal were creating value, management would find **more** value over time, not less* — finding more liabilities signals a coming impairment.

**The business question — "why buy a company with *negative* net assets?"** A *financial* buyer (a PE fund) almost never would. Boeing did it because it wasn't buying assets, it was buying **supply-chain control under duress**: Spirit was its **sole-source** fuselage supplier, ~58% of Spirit's revenue came from Boeing, Spirit was drowning in losses (could have failed and taken Boeing's line down), and after the 2024 door-plug blowout Boeing needed quality control in-house. So Boeing *had* to buy — and "Spirit extracted a large premium" precisely because Boeing had no alternative. Two course lessons in the flesh: the **strategic-vs-financial buyer** distinction (a strategic pays for control/synergy/necessity, not standalone value — like Aon buying USI, Ecolab buying CoolIT), and **negotiation leverage** (Module 2) — a must-keep-alive sole-source supplier holds all the cards. The final irony: Boeing had *spun these very factories off* in 2005 to outsource and cut costs — an expensive, forced reversal of a 20-year financial-engineering bet.

*(Sources: WSJ, "Boeing's $8.4 Billion Deal Is Bleeding Red Ink," J. Weil, Sept 3 2026; Boeing 10-Q filings, Q1/Q2 2026 — consideration $8.389B, goodwill $9,997M → $10,278M, off-market contract liability ~$1.52B. Figures are the company's provisional PPA.)*

---

## 3.4 Deal Structuring: Asset Sales / 338(h)(10) vs Stock Sales

### Part 1 — The two ways to buy (the SPA-vs-APA fork, cashed out)
- **Stock (share) purchase:** buy the *equity* — get the entire legal entity as-is: ALL assets + ALL liabilities (known AND unknown, incl. undisclosed lawsuits). Step into the seller's shoes.
- **Asset purchase:** buy selected *assets* + assume only chosen liabilities. Old entity + everything you didn't pick stays with the seller.

**Buyer generally prefers ASSET deals, for TWO reasons:**
1. **Clean liability shield** — cherry-pick assets, leave unknown lawsuits/environmental/bad contracts behind. (Predictability is a *consequence* of this.)
2. **The STEP-UP (the big one):** record assets at the new purchase price for **TAX** — the PPA fair-value step-up (3.3), now deductible → **amortize/depreciate the higher value against taxable income for years = real recurring cash tax savings.**

**Step-up value example — $800M deal, ~$400M of step-up.** It's a DCF: the step-up creates extra tax deductions → the deductions save cash tax → discount that stream to today.

1. **Extra deductions:** $400M step-up ÷ 15-yr amortization = **~$26.7M/yr** of new tax deductions.
2. **Cash tax saved:** × 25% tax rate = **~$6.7M/yr**, for 15 years.
3. **Discount to today.** These savings are near-certain — they depend on tax law, not on the business performing — so they're discounted at a **low, debt-like rate** (~after-tax cost of debt, 4–5%), *not* the equity rate. PV of a 15-year annuity = annual × [1 − (1 + r)⁻¹⁵] ÷ r:

| Discount rate | PV of ~$6.7M/yr × 15 yr | as % of $800M price |
|---|---|---|
| 0% (undiscounted) | ~$100M | ~13% |
| 4% | ~$74M | ~9% |
| 5% | ~$69M | ~9% |
| 8% | ~$57M | ~7% |

At the appropriate ~4–5% rate, the step-up is worth **~$70–75M in today's dollars — roughly 9% of the purchase price.** That's why buyers fight for it, and why they'll pay to get it (the gross-up below).

| | Stock deal | Asset deal |
|---|---|---|
| What you buy | whole entity (equity) | selected assets |
| Liabilities | all (known+unknown) | only chosen |
| Tax basis | **carries over** (no step-up) | **stepped up** to price |
| Amortize step-up for tax? | **No** | **Yes** (years of cash tax savings) |
| Buyer prefers | | ✅ |

### Part 2 — Why the seller fights back: double taxation + the 338(h)(10) truce
**The asymmetry:**
- Seller sells **STOCK** → taxed **ONCE** (shareholder pays cap-gains on the gain).
- C-corp sells **ASSETS** → taxed **TWICE**: (1) *company-level* corporate tax on the gain (assets worth >> depreciated book — the very step-up the buyer loves *triggers* this), then (2) *shareholder-level* tax when the cash-rich company distributes proceeds to owners.
- **The buyer's step-up and the seller's double tax are two sides of the same coin.**

| Seller's effective tax | Stock sale | Asset sale (C-corp) |
|---|---|---|
| Corporate layer | — | ~21% of gain |
| Shareholder layer | ~20–25% | ~20–25% |
| **Total** | **~20–25%** | **~35–45%** |
→ Often a **10–20 pt** swing in proceeds → why sellers refuse asset deals. Both sides fighting over the same pool of money (buyer saves ~10% via step-up; seller loses ~15% via double tax).

**338(h)(10) election — best of both worlds:** do the deal *legally as a stock sale* (buyer gets the entity, seller avoids asset-by-asset transfer) but *elect to treat it as an ASSET sale for TAX* (buyer gets the step-up). BUT it **triggers the seller's double tax anyway**. Why a seller agrees: **the buyer SHARES the step-up** — if buyer's step-up gain > seller's extra tax cost, buyer **"grosses up" the price** (pays extra to offset the seller's added tax) and BOTH beat a plain stock sale. A tax election that *creates* value; the sides split it.
**Conditions:** requires target to be an **S-corp or a subsidiary of a consolidated group** — NOT a standalone C-corp (cousin: **336(e)** election for some cases). Only works when buyer's benefit > seller's extra tax (depends on how much of the price becomes fast-amortizing intangibles vs slow buildings).

| | Buyer wants | Seller wants | Resolution |
|---|---|---|---|
| Deal form | Asset (step-up + clean liabilities) | Stock (single tax) | **338(h)(10)**: legally stock, taxed as assets |
| Benefit | Step-up shield (~$75M) | Avoid double tax | Buyer grosses up price to share |
| Works when | | | Buyer benefit > seller extra tax; target = S-corp/sub |

**PE relevance:** same $800M → materially different after-tax returns depending on structure; good sponsors model stock vs asset vs 338(h)(10) explicitly. The step-up being fought over = literally the PPA exercise (3.3), weaponized for tax.

---

## 3.5 Impact of Deal Structure on Seller Proceeds, Cash Flow & Sponsor Returns (Module 3 capstone)

**Everything in Module 3 lands on TWO numbers: what the seller nets, and the sponsor's IRR.** Trace one deal (bought at 10× EBITDA):

**Lever 1 — QoE-adjusted EBITDA (3.2) sets the ENTRY PRICE.** Seller marketed $52M adj EBITDA; QoE knocks it to a defensible $50M. At 10×: $520M → **$500M**. **$2M of EBITDA diligence moved price $20M** → why the *E* is fought line by line; the QoE fee pays for itself many times over.

**Lever 2 — NWC peg (3.2) adjusts price at closing.** Peg $40M; actual $36M (seller drained $4M) → price −$4M → **$496M** (and you avoid injecting that $4M in month one).

**Lever 3 — Leverage (3.1) splits the check.** Finance $496M with 5 turns (5 × $50M = $250M debt) at S+475 (~8.4% all-in); equity = **$246M**. Debt does the heavy lifting; equity < half the price.

**Lever 4 — Step-up (3.3/3.4) boosts cash flow.** Negotiate 338(h)(10), step up ~$300M of assets; at 25% ≈ **$5M/yr cash tax savings** — never in EBITDA, but real cash to pay down debt / lift equity return.

**Number 1 — what the SELLER nets:**

| | $M |
|---|---|
| Headline (marketed) | 520 |
| − QoE haircut | (20) |
| − NWC peg shortfall | (4) |
| = Gross proceeds | 496 |
| − Taxes (stock vs 338(h)(10) gross-up) | varies |
| **= Seller pockets** | **≈ 460–475** |
Seller dreamed of $520M, nets ~$465M — every dollar of the gap was a specific Module 3 lever.

**Number 2 — the SPONSOR's IRR:** equity in $246M. 5-yr hold, EBITDA $50M→$70M, exit at 10×: exit EV $700M − remaining debt ~$170M = exit equity **$530M** → MOIC $530/$246 = **2.15× ≈ 17% IRR**.

**CAPSTONE INSIGHT — each lever moves the IRR:**
- Higher QoE number → higher entry price → LOWER IRR (overpaid).
- More leverage → smaller equity check → HIGHER IRR (and risk).
- Step-up's ~$5M/yr tax savings → faster debt paydown → HIGHER exit equity + IRR.
- Tighter NWC peg → protects cash needed to service debt.
**One sentence for all of Module 3:** accounting & structure aren't paperwork — they're **levers on the equity return**; a sponsor who models stock-vs-asset, the QoE bridge, the NWC peg, and the debt package explicitly out-returns one who treats them as afterthoughts.

---

## Deep dive — Zombie funds & the exit drought (real-world anchor, mid-2026)

*Source: WSJ, "Private-Equity Assets Stuck in 'Zombie Funds' Are at a Record High," Mark Maurer, July 21, 2026. Use as the case study for Module 6 (exits) and as a reality check on Module 4/5 hold-period assumptions.*

**What a "zombie fund" is:** a fund limping past its intended ~10-yr life — no longer raising money, no longer making acquisitions, just holding assets the GP can't sell.

**The numbers:**

| Measure | Figure |
|---|---|
| NAV in US PE funds **10+ years old** (end-2025, PitchBook) | **$348.5B — all-time high** |
| vs 2015 / vs 2005 | 3.5× / >100× |
| The wave behind it: **7–9-year-old** funds | **$512.7B**, >2× the 2015 level |
| Unrealized portfolio value (Sept 2025, Preqin) | **$3.91T = 74% of all North American PE assets**, up from $922.8B a decade earlier |

**The cause (= Module 3.1 made concrete):** funds from the mid-to-late 2010s bought at the **2020–21 peak when rates were near zero**; buyers today won't pay peak prices at higher borrowing costs. Benchmark-vs-spread decomposition: a 2021 buyer financed at ~4% all-in vs today ~8.4% (SOFR 3.63% + spread). **Coverage math won't support the old multiple**, so the bid never reaches the seller's mark — and selling below the mark means crystallizing the loss. Dry powder has grown more slowly (fundraising hurdles).

**Connections to earlier lessons:**
- **The J-curve that never completes (1.2):** the harvest period (yrs 5–10) simply never arrived. And the **fee misalignment** is exactly what enrages LPs — the management fee keeps being paid on a fund running its last couple of assets. (Quoted color: an outsourced-manager exec described some as being run by a handful of people and a dog.)
- **TVPI/RVPI skepticism vindicated at industry scale (1.2 metrics + Clearlake vs Silver Lake):** the **74%-unrealized** figure IS the DPI-vs-RVPI problem systemically — three-quarters of stated industry value is GP marks, not cash. "DPI is the new IRR."
- **LP consequences:** capital tied up in aging funds blocks new commitments; the liquidity crunch is worst for **pensions and insurers with payout obligations** → could push institutions and HNW investors to **cut PE allocations** (a demand-side threat to the whole asset class).

**IMPORTANT NUANCE (sharpens 1.5/secondaries):** sponsors say **most continuation vehicles are NOT meant for zombie funds** — secondary buyers largely avoid *impaired* assets. This fits the discount-to-NAV logic: buyers price for a return, and a genuinely broken asset can't be discounted into attractiveness. **Secondaries are a valve for GOOD assets in STUCK funds, not for bad assets.**

**Apply QoE skepticism to the sponsor quotes (3.2):** several firms argue long holds are *deliberate* — "deep value creation." Sometimes true, but structurally identical to the add-back problem: **the party with the incentive supplies the narrative.** The testable version: one firm cited a frozen M&A market plus a stated 3–4 year target hold — a *checkable* claim rather than a vibe. Industry view quoted: expect a "culling of the herd" / "cleansing" — some assets will lose.

**The reverse flywheel — fundraising & the nine-year backlog (2026 update).** The zombie-fund *stock* above has a *flow* behind it: the whole fund lifecycle is jammed, and each stalled stage starves the next.

| Stage | Should be | 2026 reality |
|---|---|---|
| Hold | 3–5 yrs | 6–9+; ~4,000 US portcos held 6+ yrs, ~1,500 held 9+ |
| Exit | sell / IPO | exit proceeds ~−50% Q1→Q2 2026 ($191B → $103B) |
| Distributions (DPI) | cash back to LPs | "the bump in realizations hasn't been enough" |
| Fundraising | LPs recycle into next fund | $86B in Q1 2026 — worst pace since ~2016; 8th straight quarterly decline |

At the current clearing rate, PwC estimates it would take **~9 years** to work through the ~13,500 US PE-backed companies — the zombie phenomenon as a *flow* problem, not just a stock. The causal loop (WSJ): 2022 rate hikes froze dealmaking → GPs couldn't sell at target prices → returned less cash → LPs, short of distributions, committed less → fundraising fell. A flywheel running in reverse, each turn starving the next.

- **DPI, not IRR, is the binding constraint** — reinforces the 74%-unrealized point above. Marks can hold; it's *cash back* that's broken, and LPs fund on cash back. "You can't eat IRR."
- **The SaaSpocalypse = the leverage-thesis trap** (see "Two ways to die from leverage"). ~1,200 of the 13,500 are software, bought in 2020–21 with debt that "assumed breakneck pandemic growth"; AI fears then slashed software multiples. A concentrated, levered thesis that reversed → owners now won't sell at the markdown → stuck. Same disease as TXU, in slow motion, across a whole vintage. *(Balance: the panic ran ahead of the fundamentals — public software incumbents' switching-cost moats largely **held** through 2026, with the real damage landing on seat-based pricing rather than the companies. See the two-sided treatment in 6.2, "moats erode, but test the panic first.")*
- **Fundraising is concentrating** among a shrinking set of large, established managers — consistent with "12 is the new 5": when leverage-driven returns fade, capital flows to those who can show *operational* value creation.

**The release valves (and the honest counterweight):** secondaries / continuation vehicles let LPs cash out while the GP keeps managing the asset (the 1.5 secondaries strategy — a valve for *good* assets, per the nuance above), and the **IPO window is reopening** — 16 PE-backed IPOs raising $10.1B in H1 2026, the most since end-2021 (the same window Jersey Mike's used). Exits are recovering off the 2022–23 bottom, so this is a *cyclical* seizure, not structural death — though Bain frames it as a "5+ year problem" on the scale of the post-2008 workout.

**The other half — bifurcation, exits & priced valves (2026).** The freeze is real, but "PE is dying" is the wrong read: capital is still moving, just *unevenly*. Five signals from mid-2026:

| Signal | What it shows |
|---|---|
| **KKR closes NAX4 — $23B**, its largest-ever NA fund, *into* the worst environment in a decade | **bifurcation** — the giants raise records while small funds starve; the "concentration among large managers" trend with a face |
| **Aon buys USI from KKR for ~$17B** (KKR paid $4.3B in 2017) | **exits still happen** — to a *strategic* buyer; ~4× over a ~9-yr hold. Exits are what un-jam the machine (exit → distribution → next fund) |
| **KKR sells CoolIT for $4.75B — ~15× in ~3 yrs** (bought ~$270M, 2023) | a *structural-thesis* winner (AI liquid-cooling; revenue ~4×, EBITDA ~10×) exited to a strategic (Ecolab) — real **operational** value creation, "12 is the new 5" in the flesh |
| **GenNx360 raises $865M** (beat its target) on an **AI-barbell** thesis | even the *midmarket* can raise with differentiation; continuation vehicles bridged the drought |
| **Cox offers 26% below NAV** for trapped BDC investors | the crunch has a **credit** dimension — gated redemptions, secondary discounts pricing the SaaSpocalypse one balance-sheet layer down |

Three takeaways that balance the doom:
- **Bifurcated, not collapsed.** Scale and differentiation win; the undifferentiated middle is squeezed. KKR raises a record *in the same market* where the aggregate hit a decade low.
- **Self-healing at the margin.** Marquee exits (USI ~4×, CoolIT ~15×) generate the distributions that fund the next raise — the reverse flywheel turning *forward*, led by the best assets and strategic buyers.
- **The valves are priced, not free.** Continuation vehicles (GenNx360) and 26%-of-NAV secondaries (BDCs) are the market *clearing* illiquidity at a cost — the discount-to-NAV logic of 1.5, live.

The honest frame for anyone entering the industry: this is a **reset that rewards operators and the differentiated, not an extinction.** The capital still flows — it just now demands that you can either exit or stand out.

**What a BDC is, and the semi-liquidity trap (the credit side of the crunch).** A **BDC (Business Development Company)** is a US wrapper (a 1980 amendment to the Investment Company Act) for a **private-credit fund**: it pools investor capital and lends to mid-sized, often *sponsor-backed* private companies — the same companies PE buys. "BDC" is the *packaging*; "private credit / direct lending" is the *activity*. There are two kinds, and the distinction is the whole story:

| BDC type | How you get out | The crunch |
|---|---|---|
| **Listed (traded)** | sell shares on an exchange, anytime | not the problem child |
| **Non-traded** (e.g. Blackstone's BCRED) | redeem *back to the fund*, only through periodic **capped** windows | **the trapped-investor story** |

**Who runs them:** the private-credit arms of the big alternative-asset managers — Apollo, Ares, Blue Owl, **HPS** (BlackRock's credit arm), Blackstone. The industry fact hiding here: these firms are no longer "PE firms" but **diversified alt-managers**, and *credit is often their largest engine* (KKR ~$796B total AUM; BCRED alone ~$43B NAV). When you ask "is this just their private-credit arm?" — yes, and that arm frequently dwarfs the buyout business.

**The mechanism — a liquidity mismatch (the Situational lesson, in a wrapper):**
- Assets are **illiquid** (private loans that can't be sold quickly).
- Liabilities were sold as **semi-liquid** (retail/wealth investors told they could redeem periodically).
- Fear hits (AI threatens software borrowers → will the loans repay?) → everyone redeems at once → you can't liquidate a private-loan book on demand.
- So the fund **gates**: the ~5%/quarter cap (BCRED saw 10% *requested*, 5% *allowed*). The gate is a **feature** — it prevents a fire-sale — but to the investor it means *"I asked for my money and can get only a fraction, slowly."*

That gap between "I want out now" and "5% at a time" is the opening **Cox Capital** exploits: immediate cash at **~26% below NAV** to investors who'd rather take ~74 cents today than wait quarters for an uncertain 100. Cox's own logic — *"confidence in the underlying portfolios, less in the exit outcomes"* — says the assets are fine; the *liquidity* is broken, and he's buying the gap. It's the exact illiquidity trade-off that defines PE itself (the J-curve lock-up, Module 1), now seen from the **lender's** side and sold to *retail*: the gate is the illiquidity **saving the fund from a fire-sale while trapping the investor** — "illiquidity saves you from the run and traps you afterward" (the Situational deep dive), verbatim.

**MODELING LESSON for Modules 4–5:** the standard assumptions "**5-year hold**" and "**exit at the entry multiple**" are *assumptions*, and the last four years have punished them. Exit timing and exit multiple are the two most fragile inputs in an LBO model — sensitize both.

---

# 4 — Private Company Analysis, Valuation & LBO Modeling (Pt. 1)

*Builds the analytical base + operating model for a middle-market LBO. Module 5 adds the LBO mechanics. We build an actual .xlsx (Cascade Components) one schedule at a time.*

## 4.1 Private vs Public Company Analysis
The moment the target is PRIVATE (most of what PE buys), five things change and reshape the model:
1. **Data quality is the first diligence problem.** Public = audited, standardized, quarterly SEC filings. Private middle-market = often UNAUDITED, sometimes tax-basis (built to minimize taxes, not reflect economics), non-standardized chart of accounts. You must establish whether the data is trustworthy before analyzing it → why QoE is a bigger deal on private targets (not pre-validated by an auditor/SEC).
2. **Financials are run for the OWNER → you must NORMALIZE.** Founder-owned = optimized around the owner (above-market salary, family on payroll, personal vehicle/real estate, below-market related-party rent). None survives the sale → normalize to a clean standalone new-owner basis = the bidirectional QoE adjustments (Module 3). Public cos are already run for shareholders.
3. **No market price → valuation must be TRIANGULATED.** Public = live observable price (market cap is a fact; a take-private is a *premium* to it). Private = no observable price → estimate from comps + DCF + precedent (the football field). Absence of a price is why the valuation methods matter MORE here.
4. **Illiquidity & control change the value itself.** Private stake illiquid (capital locked years, the J-curve) → illiquidity premium. Control: public buyout = assemble dispersed shareholders + pay a control premium; private = usually 100% control in one negotiated deal with a founder.
5. **Information asymmetry is severe → structure absorbs risk.** Seller knows vastly more; no continuous disclosure → reps & warranties, indemnities, escrows, earnouts (Module 2) are the risk-allocation tools for buying something you can't fully see.
**Throughline:** private-company analysis is analysis under incomplete, non-standardized, owner-biased information → normalization, QoE, and valuation triangulation carry the weight. Public hands you clean data + a price; private makes you *manufacture* both.

**Worked check (owner normalization):** reported "EBITDA" $6M; founder salary $1.5M vs $500K market CEO → **+$1.0M** add-back; son $200K for a $100K job → **+$0.1M**; factory rented from founder $400K *below* market → this is the trap: fixing it to market *raises* the rent expense, so it's a **−$0.4M** add-DOWN. Normalized EBITDA = 6.0 + 1.0 + 0.1 − 0.4 = **$6.7M**. (Most owner adjustments add back, but market-rate corrections can cut both ways.)

**Real-world anchor — Blackstone / Jersey Mike's (WSJ, July 2026).** The owner-normalization exercise above, playing out in a real ~$8B deal. Blackstone bought a majority of the founder-owned sandwich chain (founder Peter Cancro, who built it from one shop in 1975, kept a ~10% rollover stake) and then stripped out exactly the founder-discretionary costs a new owner stops paying:

| Founder-era item | Blackstone's normalization | Maps to |
|---|---|---|
| Discretionary bonuses & donations | cut to **$11M (2025)** from **$192M (2024)** — ~$181M removed | excess owner comp → add-back |
| Family on payroll | nine relatives (wife, sons, daughter, brother) paid; several removed pre-IPO | family-on-payroll → add-back |
| $41M private jet | carved out of the purchase | personal asset → not acquired |
| Leverage | +~$500M debt → $2.1B total; interest **$104M (2025)** vs **$43M (2024)** | leverage & the interest load (1.7) |

Two teaching points. (1) These are the *same* adjustments as the check above, just at scale — normalization isn't academic, it's the first thing a sponsor does. (2) The counterweight: the chain's debt is high vs. franchised peers, and customers publicly accused it of *skimping on portions* post-buyout (the company denies it) — a reminder that cost discipline carries reputational risk if it touches the product. It also pairs as the **mirror image of the zombie-fund anchor** (Module 6): an 18-month buy-to-IPO exit, not stuck capital.

## Deep dive — Owner-comp normalization in the wild: Jersey Mike's (2026)
The 4.1 worked check — founder salary, family on the payroll, a personal asset run through the company — is not a toy example. Here it is at $8 billion, documented in an SEC filing.

**The setup.** Blackstone bought a majority stake in Jersey Mike's (the #2 U.S. sub chain behind Subway) in late 2024 for a reported ~$8B including debt; founder Peter Cancro, who had run it since buying a single Jersey Shore shop in 1975, kept ~10%. Eighteen months later — unusually fast for PE — Blackstone is taking it public on the NYSE (ticker JMKE) at ~$8B, selling up to $1.09B of stock.

**The normalization — the 4.1 lesson, itemized.** A founder-run business carries costs that don't survive a sale. Blackstone stripped them out:

| Owner-era expense | Founder-run | Post-deal | 4.1 category |
|---|---|---|---|
| Corporate private jet | $41M asset | carved out of the purchase | personal asset run through the company |
| Discretionary bonuses & donations | $192M (2024) | $11M (2025) | discretionary / owner-directed spend |
| Family on the payroll | 9 relatives paid (wife, sons, daughter, brother) — individual members drew tens of millions over 2023–25 per the filing | left the payroll pre-IPO | related-party compensation |

Every one of these is an add-back of the kind we practiced: a cost the new owner won't incur, added back to show the business's true standalone earnings. The filing shows the effect — net income rose to $55M (2025) from $5M (2024) on revenue of $724M vs $653M — **even though** the buyout nearly doubled interest expense (to $104M from $43M) after Blackstone layered on ~$500M of new debt (total ~$2.1B).

**Three course threads in one deal:**
- **Owner normalization (4.1):** the jet, the donations, the family payroll — textbook, at scale, in a real S-1.
- **Leverage (1.7):** ~$2.1B of debt; interest $43M → $104M — the amplification/risk edge. Gordon Haskett flags the debt as high versus franchised peers.
- **The exit (Module 1 / the zombie-fund contrast):** an ~18-month hold flipped straight to an IPO is the *opposite* of a zombie fund — Blackstone caught an open IPO window instead of getting stuck.

**The honest nuance.** Not all of the $192M → $11M cut is a clean "add-back" — some was genuine discretionary spend (charitable donations) a founder chose and a financial owner won't. And cost discipline has a perception cost: customers have posted about "scrawnier" sandwiches, which Blackstone denies. That is the discipline effect (1.7) *and its limit* in one image — strip the owner's excess, but cut the product and you damage the brand you are selling.

*(Sources: WSJ, "How Blackstone Put Jersey Mike's on a Fast Track to This Week's IPO," Maurer & Haddon, July 29 2026; Jersey Mike's Subs Form S-1; corroborated by CNBC, Forbes, Bloomberg. Figures are point-in-time, pre-IPO-pricing.)*

## 4.2 Valuation Methodologies for the Private Target
The three lenses and their synthesis were built in depth in 1.8 — here's how they apply once the target is private:

| Method | What it is | Private-company nuance |
|---|---|---|
| Trading comps | peer EV/EBITDA × your EBITDA | no live price of your own → peers carry more weight; size/liquidity discount vs public peers |
| Precedent transactions | multiples actually *paid* in comparable M&A | include a control premium; scarce / stale data in the middle market |
| DCF (intrinsic) | PV of free cash flow + terminal value (1.8) | forecasts rest on normalized, QoE-cleaned numbers (4.1), not audited public filings |
| LBO / walk-away ceiling | max a PE buyer can pay at target return (1.8) | usually the *lowest* — the financial buyer's discipline line |

The output is the **football field** (1.8): overlay the ranges, find the convergence zone. For a private target the absence of a market price is exactly why you triangulate across all four rather than trusting any single one. *(Mechanics, formulas, and worked examples: see 1.8.)*

## 4.3 Middle-Market Case Study: Cascade Components
Designs/manufactures engineered fastening & sealing components for aerospace/defense/industrial OEMs. Founded 1994, family-owned, founder-CEO retiring → sale process. Classic middle-market LBO target (stable niche, real assets, recurring OEM relationships, buy-and-build potential). A **manufacturer on purpose** — real inventory/receivables (working capital matters) + real capex/D&A (meaningful BS + debt schedule), unlike asset-light SaaS.

| $mm | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Revenue | 289.0 | 303.5 | 320.0 |
| Gross profit | 100.0 | 105.2 | 112.0 (35.0%) |
| Adjusted EBITDA | 50.5 | 54.2 | 58.0 (18.1%) |
| Capex | 11.6 | 12.1 | 12.8 (~4%) |

### Setting up the workbook — Cover & Assumptions
File: **Cascade_Components_LBO_Model.xlsx** (download the live workbook: https://simers.github.io/pe/Cascade_Components_LBO_Model.xlsx). Conventions: blue = input, black = formula, green = cross-sheet link, yellow = key assumption; $mm 1 decimal; % stored as fractions; multiples 0.0x.
- **Cover:** company description, color legend, units/conventions, tab guide.
- **Assumptions:** historical financials (FY23–25, with gross profit/margin & EBITDA-margin formulas); operating projection drivers (revenue growth %, gross margin %, SG&A % rev, D&A % rev, capex % rev, tax rate — Y1–Y5); working-capital days (DSO 55 / DIO 85 / DPO 45); transaction assumptions stubbed "TBD" for Module 5 (entry multiple, leverage, cost of debt, exit multiple, hold).
- Next: build the Income Statement tab (historical → projected P&L to EBIT/EBITDA), then Balance Sheet + working capital, then (Module 5) debt schedule, sources & uses, returns.

## 4.4 Defining & Calculating EBITDA — the EBITDA Bridge
Added an **EBITDA Bridge** tab answering "where is the adjustment?": Reported EBITDA (blue input) + tagged add-backs → Adjusted EBITDA (formula). Key point the user surfaced: the add-backs do NOT all live in SG&A — they're scattered (SBC in COGS *and* SG&A; one-offs in their own line, SG&A, or COGS), which is exactly why they're hard to find and why QoE exists. Building EBITDA *bottom-up* (NI + I + T + D&A) is different from *adjusting* EBITDA (reported + SBC + one-offs) — the former reverses lines BELOW EBITDA, the latter adds items scattered across the P&L.
Cascade FY25: Reported 54.0 + add-backs 4.0 (owner-comp 2.5 [SG&A, High]; facility relocation 1.2 [COGS+SG&A, Medium]; transaction/legal 0.3 [SG&A, Medium]; inventory write-down 0 [COGS]) = **Adjusted 58.0** (+7.4% uplift). Each add-back tagged by P&L location + defensibility (Module 3 spectrum).
Model changes: Assumptions "Adjusted EBITDA" is now a **formula** (Gross profit + SG&A), not a hardcoded number; a **tie-out check** row (= Adjusted EBITDA − operating-model EBITDA = 0) guarantees the bridge and the IS can't silently diverge; all three years tie.

## 4.5 Financial Modeling Best Practices
The build embodies a small set of rules that separate a robust model from a fragile one:

| Principle | What it means | Why it matters |
|---|---|---|
| One home per input | every driver is a single labeled assumption cell | change it once, it flows everywhere |
| No hardcodes in formulas | `=D5*(1+Assumptions!B18)`, never `=D5*1.055` | a buried constant is invisible and un-auditable |
| Formulas identical across columns | Y1–Y5 use the same logic | the #1 silent error is one edited cell mid-row |
| Subtotals are sums, never re-keyed | EBITDA, EBIT, NWC computed from the lines above | they can't drift out of agreement |
| Colour-code cells | blue = input, black = formula, green = link | anyone can see what's safe to change |
| Check rows that can't be fudged | e.g. the EBITDA-bridge tie-out = 0 | a broken link announces itself |
| Operating model before financing | revenue → EBIT first; debt / interest later | you can't compute interest before sizing the debt |

These aren't cosmetic — they're what lets someone else (or future-you) trust and change the model without breaking it.

**Driver conventions — what's standard vs. a simplification.** Not every driver is created equal. Some percentage-of-revenue drivers are accepted convention; others are first-pass proxies a diligence team would probe:

| Driver (as used here) | Standard? | Refinement a rigorous model adds |
|---|---|---|
| SG&A as % of revenue | **Yes** — conventional | split fixed (rent, corporate salaries) from variable (commissions, shipping): `fixed base + variable % × revenue`, so operating leverage *emerges* from the fixed base being spread over more sales, rather than being *assumed* by hand-lowering the % each year |
| Gross margin % | Yes | usually fine; refine only if input costs or mix shift materially |
| Depreciation from the **asset base** (rate × beginning PP&E) | **Yes** — the rigorous way | this is already the "good" version (not % of revenue) |
| **Capex as % of revenue** | Common, but the **weakest** | capex is driven by *capacity and the asset base*, not one year's sales, and is **lumpy** (a plant is built in a step, not smoothly). Better: **maintenance capex ≈ depreciation** (replace what wears out) + a separate **growth capex** line tied to the expansion plan; or drive capex off the PP&E base / target utilization |

The tension is visible in our own model: **depreciation** runs off the asset base (rigorous) while **capex** runs off revenue (looser) — yet capex and depreciation are two sides of the same PP&E account. It ties out and is fine for a first pass, but a purist would anchor both to the same logic (split maintenance-vs-growth capex). The lesson: *know which of your drivers are convention and which are simplifications you'd defend or refine* — that judgment is exactly what a QoE team pressure-tests.

## 4.6 Income Statement & Balance Sheet Projections

### Income Statement projection
Added the **Income Statement** tab: historical FY23–25 (linked from Assumptions, green) + projected Y1–Y5 (formulas driven off the Assumptions drivers). Modeling best practices embodied (4.5): every projection references an assumption cell (`=D5*(1+Assumptions!B18)`, never a hardcoded 1.055); formulas identical across all five projection columns; subtotals (Gross profit, EBITDA, EBIT) are sums, not re-keyed. EBITDA (4.4) is the operating output = Gross profit + SG&A (both pre-D&A).
Result: Revenue 320→420, **EBITDA 58.0→81.1**, margin 18.1%→19.3% (from the SG&A operating-leverage assumption), EBIT 47.6→67.2.
**Build order lesson:** the operating model (revenue → EBIT) is built *first*; interest, taxes, and net income can't be computed until the debt is sized, so they're added in Module 5 (5.2) once the debt schedule exists. *(The snapshot above shows the finished tab — the rows below EBIT are those Module 5 additions.)* You can't compute interest before you've sized the debt, which is exactly why the capital structure feeds in later.
Next: Balance Sheet tab (working capital via DSO/DIO/DPO → the cash a growing manufacturer consumes), then Module 5's debt schedule + returns.

### Reading the projection — drivers, margins & the D&A trap
Two questions worked through against the live Income Statement, kept because they expose how the model wires together.

**Q1 — EBITDA margin expands 18.1% → 19.3% over five years, yet there is no "EBITDA margin" assumption. What drives it?**
Not revenue growth. A margin is a *ratio to revenue*, so anything that scales one-for-one with revenue leaves the ratio unchanged — growth lifts the *dollars* of EBITDA, not the *percentage*. The expansion tracks two percentage assumptions:

| Income Statement ($mm) | FY2025 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|---|
| Revenue | 320.0 | 337.6 | 357.9 | 379.3 | 400.2 | 420.2 |
| EBITDA | 58.0 | 61.4 | 66.6 | 72.1 | 76.8 | 81.1 |
| **EBITDA margin %** | **18.1%** | **18.2%** | **18.6%** | **19.0%** | **19.2%** | **19.3%** |
| ↳ SG&A % of revenue *(assumption)* | 16.9% | 16.8% | 16.6% | 16.4% | 16.3% | 16.2% |
| ↳ Gross margin % *(assumption)* | 35.0% | 35.0% | 35.2% | 35.4% | 35.5% | 35.5% |

The margin rises because **SG&A % falls (operating leverage — the main driver)** and gross margin ticks up. *Proof:* hold every % assumption flat and EBITDA still grows, but the margin sits dead flat no matter how high growth is pushed. Growth is the accelerator on the dollars; the percentage assumptions move the margin.

**Q2 — If Year 1 revenue growth goes 5.5% → 10%, which lines change and which don't?**
Almost every projected line is built as a **% *of that revenue***, so nearly all of them move:

| Income Statement line | How it's built | Moves when growth changes? |
|---|---|---|
| Revenue | prior year × (1 + growth %) | **Yes** — the driver |
| Cost of goods sold | −(revenue × (1 − gross margin %)) | **Yes** |
| Gross profit | revenue + COGS | **Yes** |
| SG&A | −(revenue × SG&A %) | **Yes** |
| EBITDA | gross profit + SG&A | **Yes** |
| Depreciation & amort. | −(revenue × D&A %) | **Yes — the trap** |
| EBIT | EBITDA + D&A | **Yes** |
| Gross margin %, SG&A %, D&A %, tax rate | inputs (assumptions) | **No** — they're the rates, not outputs |

Concretely, changing only the Year 1 growth input:

| Year 1 ($mm) | Growth = 5.5% | Growth = 10% |
|---|---|---|
| Revenue | 337.6 | 352.0 |
| Cost of goods sold | (219.4) | (228.8) |
| Gross profit | 118.2 | 123.2 |
| SG&A | (56.7) | (59.1) |
| EBITDA | 61.4 | 64.1 |
| Depreciation & amort. | (11.1) | (11.6) |
| EBIT | 50.3 | 52.4 |
| **EBITDA margin %** | **18.2%** | **18.2%** |

Every dollar line moves — including D&A — yet the **margin is unchanged at 18.2%**, which proves Q1 in one table: growth scales the dollars, but the rates (and therefore the margin) don't move.

**Modeling lesson — why D&A-as-%-of-revenue is a shortcut:** real depreciation comes from the **fixed-asset base** (prior PP&E + capex, depreciated over useful life), so it is driven by the *balance sheet and capex schedule*, not by the current year's sales. A rigorous model computes D&A from a **PP&E roll-forward**; then D&A would *not* jump just because revenue did. The %-of-revenue version is fine for a first pass but is exactly the kind of assumption to flag — and it's why the next build is the **Balance Sheet** (PP&E, capex, and depreciation linked properly, so D&A stops being a revenue-driven plug).


### The Balance Sheet — working capital & PP&E
The Balance Sheet turns two operating drivers into cash consequences and fixes the D&A shortcut.

**Working capital schedule (driven by DSO / DIO / DPO).** AR = DSO/365 × revenue; Inventory = DIO/365 × COGS; AP = DPO/365 × COGS; NWC = AR + Inventory − AP.

*Why revenue for one and COGS for the other two — match each balance to the flow it actually settles against:*

| Line | Days metric | Runs off | Why that base |
|---|---|---|---|
| Accounts receivable | DSO (days sales outstanding) | **revenue** | customers are billed at the *selling price*, so what they owe scales with sales |
| Inventory | DIO (days inventory outstanding) | **COGS** | stock is carried at *cost*, not sale price, so it scales with cost of goods |
| Accounts payable | DPO (days payables outstanding) | **COGS** | you owe suppliers for *inputs* (the cost side), so it also scales with COGS |

The "days" figure just says how long each balance sits there: **balance = (days ÷ 365) × the annual flow.** E.g. 55-day DSO on $320M revenue = 55/365 × 320 = **$48.2M** of receivables (about seven weeks of sales uncollected). Same logic gives 85 days of inventory-at-cost and 45 days of payables-at-cost.

| Cascade ($mm) | FY2025 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|---|
| Accounts receivable (55d) | 48.2 | 50.9 | 53.9 | 57.2 | 60.3 | 63.3 |
| Inventory (85d) | 48.4 | 51.1 | 54.0 | 57.1 | 60.1 | 63.1 |
| Accounts payable (45d) | (25.6) | (27.1) | (28.6) | (30.2) | (31.8) | (33.4) |
| **Net working capital** | **71.0** | **74.9** | **79.3** | **84.0** | **88.6** | **93.0** |
| (Increase)/decrease in NWC — cash | — | (3.9) | (4.4) | (4.7) | (4.6) | (4.4) |

**Growth eats cash:** NWC climbs $71M → $93M, so ~$4M of cash is consumed *every year* just funding the larger receivables + inventory of a growing business — a recurring drain EBITDA ignores. This is the Dayforce lesson, now living in the model.

**PP&E roll-forward (fixes the D&A shortcut).** Beginning + Capex − Depreciation = Ending; Depreciation = rate (12%) × beginning PP&E.

| Cascade ($mm) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Beginning net PP&E | 85.0 | 88.3 | 92.0 | 95.8 | 99.5 |
| + Capital expenditures | 13.5 | 14.3 | 14.8 | 15.2 | 16.0 |
| − Depreciation | (10.2) | (10.6) | (11.0) | (11.5) | (11.9) |
| **Ending net PP&E** | **88.3** | **92.0** | **95.8** | **99.5** | **103.5** |

The Income Statement's D&A now **links to this depreciation** (grows with the asset base, ~$10 → 12M) instead of scaling as a flat % of revenue — exactly the fix flagged in the earlier Q&A: *depreciation is a balance-sheet consequence, not a sales ratio.* (EBITDA is unchanged since D&A sits below it; EBIT is slightly higher.)

**Operating net assets** = NWC + net PP&E = the invested capital, excluding cash / debt / goodwill. The *full* balance sheet (cash, LBO debt, goodwill, equity) is completed in Module 5 with the financing structure.

**What links the three statements — and what's still deferred.** A common question at this stage: *why is depreciation the only line that appears on both the income statement and the balance sheet?* It isn't quite — revenue and COGS are on both too (the balance sheet *pulls* them to size working capital and capex). What makes depreciation stand out is **direction**: it's the only line that flows **balance sheet → income statement** (D&A comes from the PP&E roll-forward), whereas everything else so far flows income statement → balance sheet. It looks lonely only because the model is deliberately incomplete — most of the links that tie the two statements together are exactly the ones we parked for Module 5:

| Connector | Direction | Built yet? |
|---|---|---|
| Revenue, COGS → receivables / inventory / payables / capex | IS → BS | ✅ yes |
| Depreciation (PP&E roll-forward) → D&A | **BS → IS** | ✅ yes |
| Interest expense ← debt balance | BS → IS | ⬜ Module 5 (needs the debt schedule) |
| Net income → retained earnings (equity) | IS → BS (via cash flow) | ⬜ Module 5 |
| Taxes → deferred tax / taxes payable | IS → BS | ⬜ Module 5 |
| Cash balance ← cash flow statement | (IS + BS) → CF → BS | ⬜ Module 5 |

Depreciation genuinely *is* special in three-statement modeling — it's the classic line that touches **all three** at once: an expense on the income statement, a non-cash add-back on the cash flow statement, and the charge that reduces net PP&E on the balance sheet. But it's about to have company: interest can't be computed until the debt schedule sizes the debt (which is why EBIT is the last operating line before the capital structure comes in), and cash is the *plug* from a cash flow statement that starts at net income and adds back D&A, less ΔNWC and capex — both of which we've already built. Module 5 makes those links live.

**Two conventions worth pinning down.**

*Why payables is subtracted (even though the schedule lists it as a positive).* A working-capital schedule lists each account at its natural balance; the *formula* carries the sign. What each item does depends on which side of the balance sheet it lives on:

| Item | Balance-sheet side | Effect on NWC | Intuition |
|---|---|---|---|
| Accounts receivable | Current **asset** | **+** | cash you're owed but haven't collected — your cash is tied up |
| Inventory | Current **asset** | **+** | cash sunk into unsold goods — tied up |
| Accounts payable | Current **liability** | **−** | suppliers financing you — someone else's cash funding your operations |

So on a *formal* balance sheet payables is "added" — to the **liabilities** side. But NWC measures how much of *your own* cash is tied up in operations, and a liability offsets that: receivables and inventory soak up cash (+), payables is free supplier financing (−). Net of the three = the cash the business consumes to operate.

*Why capex here is all PP&E (vs. Dayforce's mostly-software capex).* "Capex" is a category, not one account — any cash spent on a long-lived asset that gets *capitalized* (put on the balance sheet) instead of expensed. It then splits by asset type:

| Capitalized spend | Balance-sheet home | Runs off as | Typical for |
|---|---|---|---|
| Machines, plant, buildings, equipment | **PP&E** (tangible) | **Depreciation** | manufacturers, industrials |
| Capitalized software dev, some R&D | **Intangible assets** | **Amortization** | software / SaaS |

Cascade is a specialty industrial manufacturer, so its capex is overwhelmingly physical → one capex line → PP&E → depreciation. A SaaS business like Dayforce (capex = PP&E $14.3M **+** capitalized software $95.3M) would need a **second roll-forward** — a capitalized-software (intangibles) schedule amortized in parallel — and "capex" would be the sum of both. Same mechanics, different asset type; Cascade simply has only the tangible half.

*Modeling notes:* retired the "D&A % of revenue" assumption; added "PP&E depreciation rate" (12%) and "Opening net PP&E" ($85M); IS D&A ties exactly to BS depreciation.

---

# 5 — Private Company Analysis, Valuation & LBO Modeling (Pt. 2)
*The full LBO: fund the deal (sources & uses), pay the debt down from cash flow, complete the P&L, and measure the return. Everything here is built on the Cascade operating model from Module 4.*

## 5.1 Sources & Uses — funding the deal
A buyout is funded like buying a house: **Uses** = what you pay for (the business + fees); **Sources** = where the money comes from (debt + equity). The two must balance to the penny. Entry: 9.0× × $58.0M LTM EBITDA = **$522.0M** enterprise value, financed at 5.0× leverage.

**Uses of funds — what you pay for:**

| Uses ($mm) | Amount | How |
|---|---|---|
| Purchase enterprise value | 522.0 | 9.0× entry × $58.0M EBITDA |
| Transaction fees | 13.1 | 2.5% of EV (advisory / legal / diligence) |
| Financing fees | 5.8 | 2.0% of new debt (arrangement / OID) |
| **Total uses** | **540.9** | |

**Sources of funds — where the money comes from:**

| Sources ($mm) | Amount | How |
|---|---|---|
| New term debt | 290.0 | 5.0× leverage × $58.0M EBITDA |
| Management rollover | 12.0 | mgmt equity rolled into newco |
| **Sponsor equity (plug)** | **238.9** | the check the PE firm writes |
| **Total sources** | **540.9** | |

Balances exactly (check = 0). Resulting capitalization: **53.6% debt / 46.4% equity.**

**The four ideas that matter here:**
- **Sponsor equity is the *plug*.** Debt is sized first (leverage × EBITDA = a fixed amount lenders will provide); rollover is negotiated; sponsor equity fills whatever gap remains: *Total uses − debt − rollover* = **$238.9M**, the check the fund writes.
- **Fees are real uses.** Transaction fees (advisory/legal/diligence) plus financing fees (arrangement/OID) add ~$18.9M you must actually fund — buyouts aren't priced at the sticker EV alone.
- **Management rollover aligns incentives.** Management (or a founder) reinvests part of their sale proceeds into newco, keeping skin in the game (the rollover lever from Module 2). It also reduces the sponsor's check.
- **Leverage sets the risk dial.** 5.0× = $290M of debt. More leverage → smaller equity check → higher potential return *and* higher risk — the amplification of 1.7, now an input you can turn.

**Three equity numbers — keep them straight.** It's easy to conflate the entry-equity figures, but they answer different questions (and the model uses all three):

| Number | $mm | Question it answers |
|---|---|---|
| Entry business equity | 232.0 | What is the equity *worth* at entry? (EV − debt) — the value-bridge's starting point |
| Sponsor equity check | 238.9 | What does the *PE firm* write? (business equity + fees − rollover) |
| Total equity invested | 250.8 | What did *all* equity holders put in? (sponsor + rollover) — the MOIC denominator |

The sponsor check ($238.9M) exceeds business equity ($232M) by exactly *fees ($18.9M) − rollover ($12M) = $6.9M*: fees push the cheque up, the rollover pulls it down. And the value-creation bridge starts from $232M while MOIC divides by $250.8M — not an inconsistency but the **fee drag** made visible: the business equity roughly 2.35×'s, yet the sponsor's *realized* MOIC is 2.17× because ~$18.9M of fees never became productive equity.

Sources & Uses is the **entry point** of the whole LBO: the equity invested here is exactly what the exit equity gets divided by to produce MOIC and IRR. Everything downstream — the debt schedule, the completed P&L, the returns — builds from this table.

**Check (leverage as a dial):** if we raised leverage from 5.0× to 6.0× (holding the 9.0× entry and the fee rates), what happens to (a) new debt, (b) the sponsor-equity check, and (c) the risk profile? (Compute a and b; describe c in one line.)

## 5.2 Debt Schedule — deleveraging & the completed P&L
Two things finally happen here: interest flows into the income statement to **complete net income**, and free cash flow **sweeps the debt down** year by year.

**The circularity — and how we dodge it.** Interest depends on the debt balance → paydown depends on free cash flow → FCF depends on net income → net income depends on interest. That's a circular reference. The fix: charge interest on the **beginning-of-year** debt balance (last year's ending — already known), which breaks the loop with no iterative calculation.

**The completed income statement** (projected years now run all the way down):

| $mm | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| EBIT | 51.2 | 56.0 | 61.0 | 65.3 | 69.2 |
| Interest expense | (24.6) | (23.6) | (22.2) | (20.4) | (18.3) |
| Pre-tax income | 26.6 | 32.4 | 38.8 | 44.9 | 50.9 |
| Taxes (25%) | (6.6) | (8.1) | (9.7) | (11.2) | (12.7) |
| **Net income** | **19.9** | **24.3** | **29.1** | **33.7** | **38.2** |
| net margin % | 5.9% | 6.8% | 7.7% | 8.4% | 9.1% |

**Cash flow → debt paydown → deleveraging:**

| $mm | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Free cash flow (NI + D&A − ΔNWC − capex) | 12.7 | 16.2 | 20.7 | 25.4 | 29.7 |
| Beginning debt | 290.0 | 277.3 | 261.1 | 240.4 | 215.0 |
| Interest @ 8.5% | 24.6 | 23.6 | 22.2 | 20.4 | 18.3 |
| Debt paydown (sweep) | (12.7) | (16.2) | (20.7) | (25.4) | (29.7) |
| **Ending debt** | **277.3** | **261.1** | **240.4** | **215.0** | **185.3** |
| Net debt / EBITDA | 4.5× | 3.9× | 3.3× | 2.8× | 2.3× |

**Why subtract D&A on the income statement, then add it back here?** It looks like pointless round-tripping, but the two moves do different jobs — one is about **tax**, the other about **cash** — and they only *look* like they cancel.
- **Subtracting D&A on the IS computes the tax bill.** Depreciation is a real tax deduction, so it must come out before taxes are calculated. That $10.2M deduction cuts the tax bill by ~$2.6M (10.2 × 25%) — the depreciation **tax shield** (same mechanism as the interest shield in 1.7).
- **Adding it back in the cash flow corrects for it never being cash.** Depreciation isn't a payment — it's an accounting allocation of capex spent in *earlier* years. Net income fell by $10.2M, but no cash left the bank that year, so we reverse the one non-cash deduction.
- **The "round-trip" isn't one, because taxes are computed in between.** Net income $19.9M + D&A $10.2M = **$30.1M** of operating cash — which is *higher* than the ~$27.6M you'd get by taxing EBITDA directly with no D&A deduction. The ~$2.5M gap is exactly the tax shield you captured by taking the detour.

Equivalently: **cash flow = EBITDA − cash taxes − interest − capex − ΔNWC** — depreciation never appears, because it isn't cash. The income-statement route (subtract D&A → tax → net income → add it back) is just the bookkeeping path to that same number, taken so the *cash taxes* come out right along the way.

**The virtuous cycle (why deleveraging accelerates).** As debt pays down, interest falls → net income rises → free cash flow grows → *more* paydown. FCF more than doubles ($12.7M → $29.7M) over the hold; debt drops **$290M → $185M** (−$104.7M), and leverage falls from **5.0× at entry to 2.3× at exit**. That debt paydown is one of the three engines of LBO equity value — *deleveraging converts enterprise value into equity* (from 1.6): even with a flat exit multiple, the sponsor's slice of the business grows because the lender's slice shrinks.

**Two simplifying conventions (worth stating plainly):**

*1. The 100% cash sweep — where the cash really goes.* First a distinction: **interest is already paid above the free-cash-flow line** — the cash-flow build starts from *net income*, which is already *after* the $24.6M of interest. So the debt is *serviced* out of operating cash; the free cash flow below is what's left to *repay principal*. In this model 100% of that residual sweeps to the loan balance — the cleanest possible rule, but not what a real deal does. The residual actually has other claims:

| Real claim on residual FCF | What a 100% sweep ignores |
|---|---|
| Minimum operating cash | you don't sweep the balance to zero |
| Mandatory amortization | term loans repay a fixed % (e.g. 1%/yr) regardless |
| Partial excess-cash sweep | credit agreements often sweep 50–75%, stepping down as leverage falls |
| Revolver flex | draws/repays for seasonality |
| Bolt-on acquisitions | in a buy-and-build, spare cash funds add-ons (1.5) |
| Dividend recaps | sponsors may pull cash out rather than delever |

So the model sweeps to zero excess every year, with no minimum balance, no mandatory schedule, and no alternative uses — which **overstates how fast debt comes down** and ignores that a sponsor might *choose* to deploy the cash elsewhere. A production model splits mandatory vs. optional repayment and adds a minimum-cash line. It's also a lever in the sensitivities: *how* you use free cash flow is itself a return decision.

*2. Beginning-balance interest* — charging interest on the opening balance slightly overstates it (no credit for mid-year paydown) but keeps the model non-circular.

Next (5.3–5.4): the **exit** — apply the exit multiple to Year-5 EBITDA, subtract the $185.3M of remaining debt to get exit equity, and divide by the $238.9M sponsor check to get **MOIC and IRR** — then stress it with sensitivity tables.

## 5.3 Exit & Returns — MOIC, IRR, and the value bridge
The payoff: sell the business at the exit multiple, pay off the debt still outstanding, and see what the equity turned into.

**The exit (Year 5):**

| $mm | |
|---|---|
| Year-5 EBITDA | 81.1 |
| × Exit multiple | 9.0× |
| = Exit enterprise value | 729.9 |
| − Exit net debt (after 5 yrs of paydown) | (185.3) |
| **= Exit equity** | **544.6** |

**The return:** equity invested at entry = **$250.8M** (sponsor $238.9M + rollover $12M, including ~$18.9M of fees); exit equity = **$544.6M**.
- **MOIC = 544.6 ÷ 250.8 = 2.17×**
- **IRR = 2.17^(1/5) − 1 = 16.8%** (one outflow at entry, one inflow at exit → MOIC annualized over the 5-year hold)

A solid, defensible base case — a touch below the 20–25% IRR "target," precisely *because* we assumed no multiple expansion and only moderate leverage. It's conservative on purpose.

**Where did the money come from? The value-creation bridge (the three levers, 1.6).** Decomposing the gain from entry *business* equity ($232M = EV − debt) to exit equity ($544.6M):

| Lever | Value created | Share |
|---|---|---|
| EBITDA growth (ΔEBITDA × entry multiple) | $207.9M | 67% |
| Multiple expansion (Δmultiple × exit EBITDA) | $0M | 0% |
| Debt paydown (deleveraging) | $104.7M | 33% |
| **Total value created** | **$312.6M** | 100% |

- **Zero from multiple expansion — by design** (exit = entry = 9.0×). So *every dollar* of value came from operations (growing EBITDA) and deleveraging — the "12 is the new 5" reality made concrete: no free lift from rising multiples, so the return has to be *earned*.
- **Deleveraging is a third of the return** on its own — just paying the debt down converts $104.7M of enterprise value into equity, with no operational heroics.
- **Fees are a quiet drag:** the bridge builds to $544.6M on $232M of business equity, but the sponsor actually put in $250.8M (the extra $18.9M = fees), which is why realized MOIC (2.17× on $250.8M) trails the "business" MOIC (2.35× on $232M).

## 5.4 Sensitivity — the returns matrix
A single point estimate is false precision (the DCF lesson). What actually moves the return is the entry and exit multiple:

*MOIC (entry ↓ × exit →):*

| entry \ exit | 8.0× | 8.5× | 9.0× | 9.5× | 10.0× |
|---|---|---|---|---|---|
| 8.0× | 2.42 | 2.63 | 2.85 | 3.06 | 3.27 |
| 8.5× | 2.10 | 2.28 | 2.46 | 2.65 | 2.83 |
| **9.0×** | 1.85 | 2.01 | **2.17** | 2.33 | 2.49 |
| 9.5× | 1.65 | 1.80 | 1.94 | 2.09 | 2.23 |
| 10.0× | 1.49 | 1.62 | 1.76 | 1.89 | 2.02 |

*IRR (entry ↓ × exit →):*

| entry \ exit | 8.0× | 8.5× | 9.0× | 9.5× | 10.0× |
|---|---|---|---|---|---|
| 8.0× | 19.3% | 21.4% | 23.3% | 25.0% | 26.7% |
| 8.5× | 16.0% | 17.9% | 19.8% | 21.5% | 23.1% |
| **9.0×** | 13.1% | 15.0% | **16.8%** | 18.5% | 20.1% |
| 9.5× | 10.6% | 12.4% | 14.2% | 15.8% | 17.4% |
| 10.0× | 8.4% | 10.2% | 11.9% | 13.5% | 15.1% |

**Two lessons jump out of the grid:**
- **Entry multiple matters more than exit.** Moving *down* a row (paying less) lifts the return more than moving *right* a column (selling higher) — because the entry multiple is the **denominator**, and you lock your return in the day you buy. "You make your money on the buy" is the cliché; the grid proves it.
- **The base case (2.17× / 16.8%) sits mid-grid** — reaching the 20%+ LPs want takes either a cheaper entry or genuine multiple expansion, which is exactly the pressure behind the walk-away discipline of 1.8.

This completes the mechanical LBO: operating model → sources & uses → debt schedule → exit → returns, all integrated and tying out. The last piece (5.5) turns these numbers into an **investment recommendation** — would you actually do this deal, and at what price?

## 5.5 Constructing an Investment Recommendation
This is a different skill from everything before it. The model **computes**; the recommendation **judges**. The model answers *"what return do these assumptions produce?"*; the recommendation answers *"should we do this deal, and at what price?"* — which means judging whether the assumptions are realistic, whether the return clears the bar, and whether the downside is survivable.

**Anatomy of an investment-committee (IC) memo** — five sections, five questions:

| Section | The question it answers |
|---|---|
| Thesis | Why is this a good business to own — in 2–3 sentences? |
| Returns | Base / downside / upside — does it clear the hurdle? |
| Value-creation plan | Where does the return come from, *specifically*? |
| Risks & mitigants | What kills this deal, and how do we survive it? |
| Recommendation | Yes / no, at what price, with what conditions? |

**Applied to Cascade:**

*Thesis.* A profitable, steadily growing specialty industrial manufacturer with durable ~18% margins, a clean balance sheet, and a founder retiring — a natural, motivated seller. Recurring demand and available operating leverage (SG&A falling as a % of revenue). The kind of cash-generative, ownable business an LBO is built for.

*Returns (from the sensitivity grid):*

| Scenario | Entry × Exit | MOIC | IRR |
|---|---|---|---|
| Downside | 10.0× / 8.0× | 1.49× | 8.4% |
| **Base** | **9.0× / 9.0×** | **2.17×** | **16.8%** |
| Upside | 8.0× / 10.0× | 3.27× | 26.7% |

*Value-creation plan.* 67% EBITDA growth + 33% deleveraging + **0% multiple expansion** — honest and operational, but it *requires the operating plan to deliver* (≈6% revenue growth, margin expansion via SG&A leverage). No financial-engineering magic; you have to actually run the business better. That is "12 is the new 5" staring back at you.

*Risks & mitigants:*

| Risk | Mitigant |
|---|---|
| Cyclical industrial end-markets | moderate 5.0× leverage that delevers fast (→ 2.3×); covenant headroom |
| Founder departure / key-person | $12M management rollover + retention; recruit proven operators |
| Exit multiple compresses | base assumes *no* expansion; even the 8.0× downside returns capital (1.49×) |
| Margin plan slips | SG&A operating leverage is the swing — diligence the fixed/variable split (4.5) |
| Coverage tightens if rates rise | EBITDA/interest ≈2.5×, cash coverage ≈1.5× — monitor; consider hedging the floating rate |

*The verdict — and the price discipline.* At **9.0×, the base case is 16.8% IRR** — decent, but below the ~20%+ LPs expect, and without much margin for error. The downside still returns capital (1.49×), so this is a *pass on price*, not a *reject on risk*. The disciplined recommendation:
- **Pass at 9.0×.**
- **Pursue at ≤ 8.5×**, where the base case clears ~20% IRR (2.46×) — and lower still if you want cushion.
- That threshold *is* the walk-away ceiling of 1.8: the model tells you the most you can pay to earn your return, and you hold that line in the auction rather than chasing the deal above it.

**What separates a good recommendation from a bad one:**
- **Honest assumptions, not reverse-engineered ones.** The temptation is to nudge growth, margin, or the exit multiple until IRR clears 20%. That is precisely how smart people talk themselves into bad deals. Hold the assumptions honest and let *price* be the variable you solve for.
- **Pre-mortem.** Assume the deal failed — why? (A recession hit the cyclical end-market; the margin plan never materialized; you overpaid at entry.) Then confirm the downside case survives each one.
- **Return *of* capital before return *on* capital.** The downside landing at 1.49× (not below 1.0×) is exactly what makes this a price decision rather than a risk veto.
- **The model disciplines the decision; it doesn't make it.** Its highest use isn't the headline IRR — it's telling you the *price at which the deal works*, so you can hold the line. "You make your money on the buy" is a modeling output, a negotiating anchor, and a recommendation, all at once.

**Worked example — the 9.5× test (what "hold assumptions honest" really means).** Suppose the seller won't move below 9.5×. The base plan there returns only 15.8% (at a 9.5× exit) to 17.4% (at 10.0×) — short of 20%. So can the *operating plan* honestly make up the difference? Flexing the model:

| At 9.5× entry | Exit 9.5× (no expansion) | Exit 10.0× (+0.5× re-rating) |
|---|---|---|
| Base plan — Y5 EBITDA $81M | 15.8% | 17.4% |
| Aggressive (growth +1pt & SG&A → 15.5%) — $88M | 18.6% | **20.2%** |
| Very aggressive (+ 40bps gross margin) — $90M | 19.5% | 21.1% |

The grid *is* the lesson: **at a flat 9.5× exit, no defensible operating plan clears 20%** — even $90M of Year-5 EBITDA (+11% over base) reaches only 19.5%. Clearing 20% needs *two stacked bets* — an operating plan ~10% richer than base **and** a half-turn of multiple expansion (the very lever "12 is the new 5" says not to bank on).

Whether that's a *pass* or a *proceed* turns on one question: are those richer numbers **underwritten or assumed?**
- Revenue +1pt isn't defensible by assertion — the base already *decelerates* (a maturing business); it needs a named driver (a bolt-on, a product with a pipeline, documented pricing power).
- SG&A to 15.5% is *more* operating leverage than base already assumes — plausible only with a concrete cost program you can point to (shared services, automation, a specific headcount plan).
- +40 bps of gross margin needs a real pricing or mix story.

So "seller won't move below 9.5×" is not a reflexive no — it's a **diligence mandate**: *can we underwrite ~$88–90M of exit EBITDA (specific cost-out and growth drivers we'd bet our own capital on) and a credible structural reason the multiple re-rates (e.g. buy-and-build turns Cascade into a larger, more strategic asset)? If both, with evidence — proceed. If either is just a more optimistic cell — pass.* That is the line between price discipline and stubbornness: you'll pay 9.5×, but only for assumptions you've **earned**, not typed.

**Check (the capstone):** rather than cut price, your deal partner proposes rescuing the 9.0× base case by raising leverage from 5.0× to 6.0× — *"more debt, higher IRR, done."* Is that a legitimate fix for a sub-20× return? What does it actually change, and what does it *not* change? (Revisit what leverage does to the return *and* to the risk — and ask whether it addresses the thing that's actually wrong with the deal.)

**Answer — leverage is a claim on the returns, not a source of them.** More debt re-slices the pie between lender and sponsor; it does not make the pie bigger. Only two things enlarge the pie: paying less (price) or growing EBITDA (operations) — and the second is exactly what diligence has to verify. So reaching for debt to rescue a sub-hurdle return treats a *valuation* problem with a *financing* tool.

| Raising 5.0× → 6.0× leverage | Changes | Doesn't change |
|---|---|---|
| the return | smaller equity cheque → higher *base* IRR (a denominator effect, not a better deal) | what the business is *worth* |
| the risk | wider outcome distribution *both ways*; fixed interest rises → coverage 2.35× → ~1.96× (~1.5× on a cash basis) | whether the operating plan is *real* |
| the structure | more of the value promised to lenders | the exit multiple |

Three things follow, and they're the ones to say out loud:
- **Not a substitute for diligence.** The base case is light because of the business's *value* and the *credibility of the plan* — debt touches neither.
- **It concentrates risk on a thinner equity base.** The same swing in enterprise value now lands on a smaller slice (1.7 amplification, pointed the wrong way).
- **Certain cost against hoped-for benefit.** You take a *fixed*, larger interest bill for *hoped-for* operational delivery diligence hasn't confirmed — and when the base case is already the problem, levering to flatter it just deepens a downside that now risks a covenant breach or an equity wipe.

And the market may not even allow it: at ~1.5× cash coverage lenders widen spreads, tighten covenants, or decline — and *easy* leverage on offer is usually a late-cycle signal, not a green light.

*The one nuance (so the lesson isn't "leverage is bad"):* the tell is **order of operations.** Leverage as the *conclusion* of conviction — you've underwritten the cash flows, so you size the equity efficiently — is fine. Leverage as a *substitute* for conviction — the return's light, so add debt — is the trap. The partner is proposing the second. Cut the price or underwrite a bigger, credible plan; debt is neither.

*Module 5 complete: operating model → sources & uses → debt schedule → exit & returns → recommendation. The mechanics and the judgment. Modules 6–8 build on this — deeper value creation, fund-level returns, and the case-interview LBO under time pressure.*

---

# 6 — Thinking Like a Private Equity Professional (Pt. 1)
*From mechanics to judgment. Modules 4–5 built the model; Module 6 builds the **view** behind the assumptions — how PE reasons about industries, moats, and growth, and how a diligence finding becomes a modeling input. This is the answer to the 9.5× question: how you *earn* a growth assumption instead of typing it.*

## 6.1 Understanding Industries and TAMs
**Start with the industry, not the company — the market is the ceiling.** A company can only become as large as the market allows, so PE evaluates the *picture* (industry) before the *frame* (company):
- A great operator in a *shrinking* market fights the current for the whole hold.
- A mediocre operator in a *growing* market gets carried by it.
- The industry sets the realistic range for the **revenue-growth assumption** that drives the entire model (recall 5.5: revenue growth is the input everything else flows from).

**TAM / SAM / SOM — the three nested markets.** Sizing "the market" means being precise about *which* market:

| Layer | What it is | The discipline |
|---|---|---|
| **TAM** — Total Addressable Market | total demand if you served 100% of every segment, everywhere | the theoretical ceiling; usually irrelevantly large |
| **SAM** — Serviceable Addressable Market | the slice your product line + geography actually serve today | narrows TAM to what you *could* sell |
| **SOM** — Serviceable Obtainable Market | the slice you can realistically *win* given competition & capacity | **your revenue can never exceed this** |

The trap is quoting TAM ("it's a $50B market!") to imply opportunity. What bounds the model is **SOM and its growth** — the realistic ceiling on the revenue line.

**Top-down vs bottom-up sizing — the credibility test:**

| Approach | How you build it | Verdict |
|---|---|---|
| Top-down | start with a big industry figure, take a % ("1% of $50B = $500M") | **weak** — assumes share with no mechanism; a classic red flag |
| Bottom-up | # of customers × units each × price, grown by real drivers | **defensible** — ties to things you can diligence |

This is the "underwritten, not assumed" rule (5.5) applied to the *top line*. "We'll get 1% of a huge market" is the reverse-engineering trap; "there are N plants, each replaces X components a year at $Y, and the installed base is growing Z%" is a claim diligence can test. Bottom-up is how you *earn* the growth number.

**Structural vs cyclical growth — the distinction that prevents overpaying.**
- **Structural (secular):** a durable demand tailwind — electrification driving grid components, aging demographics driving healthcare. Survives a recession.
- **Cyclical:** rides the economic cycle — construction, autos, semiconductors. A "growing" cyclical market may just be *mid-cycle*.
- Mistaking a cyclical peak for structural growth is exactly how buyers overpay at the top — **TXU** read a natural-gas-price *cycle* as a floor (Module 1). The diligence question is always: *is this tailwind durable, or are we buying the peak?*

**How it becomes a modeling assumption.** The industry view converts directly into the revenue-growth line:

> revenue growth ≈ (market/SOM growth) + (share change from the value-creation plan)

For Cascade we assumed ~5–6% growth. Module 6 asks whether that's defensible: if the served market grows ~3–4% structurally and the plan credibly adds ~1–2 points of share (new products, share gains, price), 5–6% is *earned*. If the market is flat and you've penciled 6%, you're assuming share you haven't justified — the 9.5× trap again.

**The PE-specific angle.** PE doesn't need a *huge* TAM — it needs a market big enough to grow into over the hold, with **defensible** share (that's 6.2, moats). A niche market with a durable barrier beats a giant market anyone can enter. And **buy-and-build works precisely in *fragmented* markets** (many small players to roll up — 1.5): fragmentation is itself a market-structure read.

**Check (6.1):** a founder pitches you: *"The global industrial-sensor market is $80B and growing 8% a year; we'll capture 2% within five years — that's $1.6B of revenue."* Name what's wrong with this as an underwriting basis, and list the three questions you'd ask to turn it into a defensible, bottom-up revenue build.

**Answer.** The pitch is **top-down and untestable**: it starts from a huge number ($80B) and asserts a share (2%) with *no mechanism* connecting the two — nothing about who buys, why they'd switch, or whether the company can even produce that much. It's a wish in the costume of an estimate. Two deeper flaws: (1) 2% is taken against the **TAM**, but revenue lives in **SOM** — if the served slice is really ~$3B (industrial pressure sensors, North America, oil & gas), 2% of the *right* denominator is a different, far more credible number; and (2) "getting *to* 2%" is itself a **share-gain** assumption that needs its own mechanism (someone has to lose). The fix is to rebuild bottom-up and pressure-test both the demand ceiling and the supply ceiling:

| # | Question | What it tests |
|---|---|---|
| 1 | $80B of *what* — and what's your **served** market (SAM), not the global TAM? | resets the denominator to reality |
| 2 | Build it bottom-up: how many target customers, buying how many units, at what price? | replaces the asserted % with a checkable build |
| 3 | Where does the **share gain** come from — who loses, and why would they switch? | forces a real competitive mechanism (→ 6.2, moats) |
| 4 | Is the 8% **structural or cyclical**, and can you build the **capacity** to serve $1.6B? | tests the tailwind's durability *and* the supply-side ceiling |

Two rules to carry forward: **always reset TAM → SAM → SOM before believing a share number**, and treat **"getting to X% share" as an assumption that needs a mechanism**, not a given — which is exactly why the next lesson is moats.

## 6.2 Barriers to Entry & Competitive Advantages
This is the answer to question 3 from 6.1 — *where does the share gain come from, and why would anyone let you keep it?* A market can be large and growing, but if anyone can enter, your share and your margins get competed away. The **moat** is what makes the SOM *defensible*, not merely winnable.

**A moat protects two different things:**
- **Share** — can a rival or new entrant take your customers?
- **Margin** — even if they can't take customers, can competition force your prices down (or costs up) until the profit is gone?

This is why moats drive the model: the revenue-growth line (6.1) *and* the gross-margin / SG&A lines (Module 4) only hold if something stops competitors eroding them. **No moat → margins mean-revert toward the cost of capital**, and a penciled 18% EBITDA margin quietly bleeds to the industry floor over the hold. The moat is the reason the margin assumption survives.

**Barrier vs advantage — related but not the same (you want both):**

| | What it does | Question it answers |
|---|---|---|
| **Barrier to entry** | keeps *new* competitors out | "why won't three startups copy this?" |
| **Competitive advantage** | beats the rivals *already* here | "why do you win against today's incumbents?" |

**The durable moats (Porter, updated).** The test for each: *does it get **stronger** as the company grows and time passes?* A real moat widens; a fake one is a temporary head start that erodes.

| Moat | Mechanism | Example |
|---|---|---|
| **Switching costs** | ripping you out is costly/risky, so customers stay | software wired into workflows; a bank's core system |
| **Network effects** | each user makes the product more valuable to others | marketplaces; payment networks (Visa) |
| **Cost advantage** | you produce cheaper — scale, process, input access | low-cost manufacturer; best ore body |
| **Intangibles** | brand, patents, regulatory licenses | pharma patents; a trusted rating-agency brand |
| **Efficient scale** | the market profitably supports only one or two players | a regional pipeline; a rural cement plant |

**"Moat or nice-to-have?" — the diligence filter.** Founders call everything a moat; these tests separate them, and all are checkable in the data room (6.3):
- **Replication test:** could a competitor with $50M and 18 months copy it? If yes, it's a *lead*, not a moat (most "technology advantages" fail here).
- **Pricing-power test (best single evidence):** has the company raised prices without losing customers? Sustained pricing power *is* a moat showing up in the numbers.
- **Churn/retention test:** do customers stay? High retention + net revenue retention >100% is switching costs made visible.
- **Margin-stability test:** have gross margins held or risen through years of competition, or slowly bled? Bleeding margins = a leaking moat.

A moat isn't a story the founder tells — it's a pattern in the evidence.

**Moat → model.** The finding converts straight into assumptions:

| Diligence finding | Model consequence |
|---|---|
| Strong moat (pricing power, high retention) | hold or *expand* margins; growth is defensible → base case stands |
| Weak / no moat | fade margins toward the industry floor and haircut growth — model the erosion |

For **Cascade**, the honest question: *what's the moat?* Plausibly switching costs (components engineered into a customer's spec → costly, risky requalification) and niche cost/scale. If diligence confirms them — decade-long customers, spec'd-in products, stable-to-rising gross margins — the ~18% margins and the expansion we penciled are earned. If it's really a commodity parts-maker, that expansion is fiction and the model should fade margins instead. **The moat is the difference between the base case and wishful thinking.**

**The moat PE *builds*, not just buys.** Buy-and-build (1.5) manufactures a scale/cost moat none of the small add-ons had alone — a rolled-up regional services company gains route density, purchasing power, and a brand no single location could afford. Fragmented market (6.1) + a *latent* scale advantage is the classic PE setup: the moat doesn't exist yet, and building it *is* the value-creation plan.

**The dark side — and the discipline: moats erode, but test the panic first.** A moat is a snapshot, not a guarantee — *and* a falling stock is not proof the moat broke. The 2026 **SaaSpocalypse** is the case study in both directions. The fear: AI writes code cheaply, so expensive off-the-shelf software (Salesforce, Workday, ServiceNow…) gets replaced by AI-concocted versions. The market priced near-extinction — software shed ~**$2 trillion** of market cap over ~12 months (Salesforce −30%, Workday −33%, some names −70%+). Then the incumbents' moat *held*, and why maps straight onto this lesson:

| Why the moat held | The moat it is |
|---|---|
| Most software work is *maintaining/updating/integrating*, not greenfield code (where AI excels) | the threat hit the wrong activity |
| Deep integration into customers' tangled IT stacks — self-integrating AI code is a hard job the customer would own | **switching costs** |
| Inertia/habits — even Sam Altman said disruption came slower than expected: "people keep buying from the same company" | switching costs as behavior |
| Buyers are operators, not engineers ("a world of difference between building vs operating") | the moat is in *operating* |

Salesforce then reported revenue +~11% with Agentforce ARR crossing ~$1.5B (+240% YoY) and jumped **+22% on earnings day**; AI became a tailwind the incumbents monetize (embedding agents, partnering with AI providers) rather than only a threat.

**But don't over-correct — find the real erosion vector.** The honest read is *bifurcation*: the genuine threat is **"seat compression"** (AI agents cut headcount → fewer seats → the *seat-based pricing model* is at risk even where the company survives — Atlassian, Workday, DocuSign, MongoDB cited). So AI is hitting the **business model** (seat-based → usage/outcome pricing) more than the **companies**. The lesson: *"is there a moat?"* is never enough — ask *"is it widening or eroding, **what specifically could breach it**, and is today's price panic or structural?"* Here the switching-cost moat held; the pricing model is the part actually eroding. (It's also a 6.5 point: "software" isn't one trade — platform-moated vs. seat-based behave oppositely; the blend "software is dying" hid that — and the panic drove Salesforce to ~16× forward earnings vs. a ~43× 10-yr average, a possible mispricing for whoever tested the thesis instead of trading the headline.)

**Check (6.2):** you're diligencing Cascade. Management claims two moats: *(a)* "our components are engineered into customers' products, so switching means re-testing and re-certifying — customers never leave," and *(b)* "we have the best engineering team in the industry." For each: real moat or nice-to-have, which test would you run, and what data-room evidence would confirm or kill it?

**Answer.**

*(a) Engineered-in → real moat (switching costs).* Right test: **churn/retention**, evidenced by cohort retention in the data room. But retention alone can be a *trap* — high retention is also consistent with lazy, un-competed customers or contracts about to expire, so you must check *why* they stay. The switching-cost thesis predicts specific corroboration: **customer tenure in decades**, **products in the customer's own spec/BOM** (pull the engineering docs, not management's word), **long requalification timelines** (confirm on customer reference calls), and — the clinching tell — **pricing power** (if switching is truly costly, Cascade can raise prices modestly without losing volume). Run churn *and* pricing-power together; they're conclusive. *Kills it:* a major customer that recently switched, short contracts up for rebid, or gross margins slipping despite the "stickiness."

*(b) Best engineering team → nice-to-have, not a moat.* Fails the **replication test** (a rival with capital can hire or poach talent) and — deeper — **it isn't an asset you own; it walks out the door every night.** A moat must be structural (in the product, the relationship, the cost base), not resident in people who can leave. The upgrade: a great team can be the *engine that builds* a moat — if that talent is what gets products spec'd into customer designs, the team is the *cause* and the switching cost is the *moat*. Diligence consequence: flag **key-person risk** (retention packages, non-competes) precisely *because* it isn't structural.

*Two rules to carry forward:* **retention needs a reason** ("they stay" is an observation; "they stay because re-speccing costs 18 months" is a moat — get from the *what* to the *why*, and corroborate with the customer, not the seller); and **locate the durable asset** — ask "is this structural and owned, or copied with money / walks out the door?" Team, first-mover, hot product → not durable; spec'd-in position, network, licensed scale → structural.

## 6.3 The Data Room Loop and Working with Management Data
Every "here's the evidence I'd pull" from 6.1–6.2 points here: the data that verifies a moat or a growth story is prepared by the **seller**. This lesson is how a PE team actually runs diligence — and how much to trust what it's handed.

**What a data room is, and the fact that governs it.** A data room (VDR — virtual data room) is a secure repository where the seller posts diligence documents: financials, contracts, customer data, org charts, legal files, the QoE. The governing fact: **it is assembled, curated, and controlled by the seller.** Everything in it was *chosen* to be there — which makes it *incomplete by construction*. Your job is to work the gap between what's shown and what's true.

**The data-room *loop* — iterative, not a one-shot dump:**

| Step | What happens |
|---|---|
| 1. Request | submit an initial document request list (the "DRL") |
| 2. Receive | seller posts (some of) it |
| 3. Analyze | you read it — and it *generates new questions* |
| 4. Follow-up | you request the adjacent things it revealed (and omitted) |
| → repeat | each round narrows toward the real risks |

The important findings come from **rounds 2–3**, not round 1. Round 1 is what the seller *wanted* to show; the follow-ups chase what their curation left out. Treating the DRL as one-and-done misses the point.

**Read the gap — the dog that didn't bark.** The most valuable skill is noticing what's *missing*:
- revenue by customer but not *margin* by customer → maybe the big customers are the unprofitable ones
- *aggregate* retention but not *cohort* retention → maybe recent cohorts churn worse (moat eroding, 6.2)
- *this* year's pricing but not the *history* → maybe there's no pricing power
- QoE covers FY23–25 but owner-comp normalization only shows FY25 → why not the earlier years?

Every gap is a question: *"you've shown me X; please also provide the adjacent Y."* The missing Y is the risk.

**Management data is a starting point, not a fact — the QoE connection.** Numbers management hands you are *their representation*, prepared by people paid to sell at the highest price. Not cynicism — the structure of the transaction.

| Management gives you… | You treat it as… | Because… |
|---|---|---|
| "Adjusted EBITDA of $58M" | a claim to verify (that's what QoE is for) | add-backs may be aggressive (4.4 bridge scrutiny) |
| "The pipeline is $200M" | unweighted optimism | not probability-weighted; ask stage/conversion history |
| A management projection | the *seller's* case, not yours | you build your *own* model (M4–5) from diligenced drivers |
| "Churn is low" | an assertion needing cohort data | aggregates hide the trend (6.2) |

The habit: **management data = what they claim; diligence = what's true; the gap = your risk (and your leverage).**

**Triangulate — verify against sources the seller doesn't control:** customer reference calls (best check on a "sticky customer" claim); third-party market data (sanity-check the TAM story, 6.1); public comps / channel checks; the QoE and auditors (but sell-side QoE is itself a starting point — buy-side QoE exists for this reason).

**Fight the deal team's own optimism.** The pressure isn't only from the seller — the *buy-side* team, months in and wanting to close, reads ambiguous data charitably (the reverse-engineering trap of 5.5, applied to diligence). The antidote is disconfirming questions: not "what supports the thesis?" but "**what would have to be true for this to be a disaster, and does the data rule it out?**"

**Connection to the model.** The loop is the machinery that *produces* the assumptions. Every blue input — growth (6.1), margins (6.2), DSO/DIO/DPO, capex — should trace to a diligenced fact. When 5.5 said "underwritten, not assumed," **this loop is the underwriting.** The model is only as honest as the diligence behind its inputs.

**Check (6.3).** Cascade's data room has posted: revenue by year, aggregate retention (94%), the sell-side QoE, and a projection showing growth *accelerating* 5% → 8%. For each: a follow-up cut to request, and what a bad answer reveals. Plus one outside-the-room check.

**Answer.**

| Item posted | Follow-up to request | What a bad answer reveals |
|---|---|---|
| Revenue by year | revenue **and gross margin by customer**, + revenue retention by customer | **concentration × margin**: top 3 = ~45% of revenue *and* the lowest-margin accounts → growth is being "bought" with unprofitable volume, and losing one breaks the model |
| Aggregate retention 94% | **cohort** retention by vintage | recent (2024–25) cohorts churn far worse than the blended 94% → the moat is eroding *now* (6.2) |
| Sell-side QoE | the **detail behind each add-back** (buy-side QoE) | "one-time" items that recur every year → true EBITDA ~$52M not $58M; at 9× that's ~$54M of price on air |
| Projection accelerating 5% → 8% | the **mechanism**: product ship-dates/pipeline, price increases already in contracts; conversion history | no mechanism — acceleration *against gravity* (big bases decelerate) is just the assumption that makes the seller's price work → discount it, build your own |

*Outside-the-room check:* **customer reference calls** — a customer *volunteering* that switching is painful confirms the switching-cost moat from a source the seller doesn't control. Discipline: the seller hands you their *happiest* references, so ask them *disconfirming* questions ("what would make you switch?") and try to reach a *former* or off-list customer — the reference they *didn't* pick is the most informative call.

*The strategic point:* each gap is **leverage, not just risk**. "Your 94% is really 85% in recent cohorts, and $6M of adjustments recur, so we're underwriting $52M — which is why our price is 8.5×, not 9.5×." Diligence findings are exactly how you justify the 5.5 price discipline *to the seller*.

## 6.4 The Operating Model & Drivers of Value
The hinge of the course: where the diligence *judgment* of 6.1–6.3 becomes the *driver cells* of the model from Modules 4–5. "Underwritten, not assumed" finally meets the blue input cells.

**Operating model vs LBO model.** The **operating model** projects the *business* — revenue → costs → EBITDA → cash flow — *before* financing. The **LBO model** wraps it in a capital structure (debt, equity, returns). 6.4 is about the engine: it's where your *view of the business* lives, and the LBO layer just monetizes it. Get the engine wrong and no financing cleverness saves you (5.5 — debt is a claim on returns, not a source).

**Driver-based, not line-item — the core idea:**

| Approach | How revenue reaches Year 3 | Verdict |
|---|---|---|
| Line-item (output-based) | "revenue grows 6%" — type the rate | an assumption with no mechanism; can't diligence, stress, or defend it |
| Driver-based (input-based) | revenue = customers × units × price, each grown by its own driver | every number traces to something verifiable, sensitizable, defensible |

This is 6.1's top-down-vs-bottom-up, generalized to the *whole* model. A driver-based model never says "margins expand to 20%"; it says margins expand *because* SG&A is part-fixed and revenue grows. **Push every assumption down to the lowest level you can diligence, and let the summary numbers emerge.**

**The driver tree — decompose until you hit something diligenceable:**
- Revenue → **volume × price** (never a single growth %). Volume → new (pipeline × win-rate) + retained (churn/cohorts, 6.3) + expansion (upsell). Price → list × realization, grown by pricing power (6.2).
- COGS → unit cost × volume (input costs, labor, freight).
- SG&A → **fixed base + variable %** (the 4.5 split — where operating leverage *emerges*).
- Capex → maintenance (≈ depreciation) + growth (tied to the capacity the volume plan needs).

Stop where the next level is noise, not signal (revenue = volume × price is worth splitting; per-SKU-per-region for 50 products is false precision). **Judgment is knowing where the meaningful drivers stop.**

**Drivers *of value* — which ones move the return.** Sensitize each driver (the 5.4 discipline, applied to operating inputs) to find the two or three the return actually depends on:

| Value lever | Driver behind it | Where it appeared |
|---|---|---|
| Revenue growth | volume (share × market) + price | 6.1, 6.2 |
| Margin expansion | SG&A operating leverage; GM mix; procurement | 4.5, "12 is the new 5" |
| Capital efficiency | working-capital release (DSO/DIO/DPO); capex discipline | 4.6, 4.5 |
| Multiple / deleveraging | (financing — 5.2–5.4) | the LBO layer, not the operating model |

The first three are *operational* — what Module 7 executes and what "12 is the new 5" says you must now earn. A good operating model **exposes** these as explicit, sensitizable inputs.

**Separate inputs from outputs — the classic modeling sin.**
- **Inputs (blue):** drivers you assume — volume, price, the SG&A split, WC days. Diligence underwrites these.
- **Outputs (black):** everything computed from them — EBITDA, margins, FCF, returns. **Never type an output.**

If you're *typing* a margin or EBITDA number, stop — it's an output masquerading as an input, i.e. a smuggled assumption you can't defend (the 4.5 color convention, now with its *reason*: it's the visible line between your diligenced view and the model's math).

**Cascade — the diligence-to-driver map (the module's payoff):**

| Diligence finding (6.1–6.3) | Becomes this driver |
|---|---|
| Served market ~3–4% + plan adds ~1–2 pts share | revenue growth ~5–6% (blue) |
| Switching-cost moat (pricing power, retention) | gross margin holds/expands; growth defensible |
| SG&A ~60% fixed (verified in the data room) | the SG&A % decline driving margin expansion |
| Cohort retention healthy | the volume-retention piece of the revenue build |
| Maintenance capex ≈ depreciation + growth per capacity | the capex % line |

If a finding *fails* (say cohort retention deteriorating), you don't lower a number — you change the *driver* (churn rises → volume fades → margins compress). The driver structure lets diligence flow cleanly in instead of being fudged into one growth rate.

**Check (6.4).** A junior hands you a Cascade model where **EBITDA margin is a blue input**, typed 18.1% → 19.3%. What's wrong *structurally* (the design, not the numbers)? Rebuild it in words, and name the diligence finding needed to defend the margin path.

**Answer.** The margin is a **computed output**, so a blue margin cell is an assumption masquerading as a fact — the junior *asserted* the expansion instead of deriving it. Rebuild:

- **Blue inputs:** revenue (volume × price), **gross-margin %**, and **SG&A = fixed base + variable %**.
- **The margin emerges (never typed):** GP = revenue × GM%; SG&A = fixed + variable% × revenue; EBITDA = GP − SG&A; **EBITDA margin = EBITDA ÷ revenue** (black).

It expands *on its own* because revenue grows while the **fixed portion of SG&A doesn't** — fixed cost spreads over a bigger base. **Operating leverage isn't an assumption; it's a consequence of the fixed/variable split.** In the junior's file 18.1→19.3 is asserted; here it *falls out* — and is defensible because you can point to the diligenced split that produces it.

*Two findings defend the path* (one per half of the margin): **the moat** (pricing power / switching costs → stable-to-rising **gross margin**) and **the fixed/variable SG&A split** (→ operating leverage). Bidirectional: confirm the moat → margin holds/expands honestly; fail it (commodity, no pricing power, GM bleeding) → change the *driver* to gross-margin compression and let a flat-or-falling EBITDA margin flow through. *One-line version:* wrong because it's an output; rebuild with revenue, GM%, and fixed-plus-variable SG&A as inputs, let EBITDA margin compute itself — it expands as fixed SG&A spreads over growing revenue — defensible only if diligence confirms both the moat and the cost-structure split.

## 6.5 Business Segmentation & Revenue Builds
The finale of Module 6, and where 6.4's "revenue = volume × price, decomposed" becomes a concrete build. It turns a single blended growth rate into a defensible, diligenceable projection.

**The problem it solves: one blended rate hides everything that matters.** A company "growing 6%" might be one segment growing 20% and another shrinking 5% — opposite implications for value. Segmentation breaks the business into parts that **grow, earn, and risk differently**, then builds each up separately.

**What a blend destroys:**

| A blend hides… | Why it's dangerous |
|---|---|
| **Mix** (fast + slow segments averaged) | can't tell durable growth (good segment compounding) from decay (good segment shrinking as a %) |
| **Margin differences** | growth in a *low*-margin segment flatters revenue but hurts EBITDA margin — the blend disguises it |
| **Risk** | a "stable 6%" may be a safe segment + an AI-threatened one; the blend hides the landmine (the SaaSpocalypse inside "software revenue") |

**How to segment — cut along whichever axis makes segments behave differently:**

| Axis | Segments look like | Use when |
|---|---|---|
| Product / service line | new machines vs spare parts vs service | offerings have different economics |
| Customer type | enterprise vs SMB; OEM vs aftermarket | buyers behave differently (churn, price) |
| Geography | NA vs Europe vs Asia | markets grow/price differently |
| Channel | direct vs distributor vs online | go-to-market differs in margin/growth |
| **Recurring vs one-time** | subscriptions/contracts vs transactional | **often the most important cut** — recurring is worth more |

Test for a good split: *would you underwrite each segment with a **different** growth and margin assumption?* If two segments get the same assumptions → over-split (false precision). If one hides two businesses → under-split (hidden risk). Same "decompose until the next level is noise" judgment as 6.4.

**The revenue build — bottom-up, per segment**, then summed:

> Total revenue = Σ (each segment's volume × price), each grown by *its own* driver

The classic **layer cake** for a segment with a customer base:

| Layer (this year's revenue) | Driver |
|---|---|
| **Retained** (existing customers) | last year's base × (1 − churn) — cohort retention (6.3) |
| **+ Expansion** | upsell / price increases — pricing power (6.2) |
| **+ New** | new logos × avg deal size (pipeline × win-rate) |
| **= Segment revenue** | the sum |

Every layer traces to a data-room fact (churn from cohorts, expansion from pricing history, new from pipeline) — a structure you can diligence, sensitize, and defend, not a number you asserted.

**Two live examples (from the 2026 articles):**
- **GenNx360's "AI barbell"** — segmentation at the *portfolio* level, cut by a **risk axis**: AI "picks-and-shovels" (data-center cooling, aerospace/defense — *benefit* from AI) vs AI-resistant everyday services (commercial painting — *shielded*). The "risk" row turned into a thesis.
- **CoolIT** — "data-center infrastructure isn't one trade — it's power, land, fiber, cooling, water." KKR bought the **cooling** sub-segment specifically (sharpest tailwind, most defensible moat) → a ~15× instead of an index return. Segmenting the *market* is how they found it.

**Cascade — what segmentation reveals.** Split the single revenue line into **new equipment vs aftermarket parts & service**:

| Segment | Behavior | Model consequence |
|---|---|---|
| New equipment | cyclical, lower-margin, lumpy (tied to customer capex) | the *cyclical* risk of 6.1 lives here — sensitize hard |
| Aftermarket (parts + service) | recurring, high-margin, sticky (installed base needs parts) | where the **moat** (6.2) and the margin actually live |

For an industrial manufacturer the **aftermarket is usually the crown jewel** — recurring, high-margin, defensible — and the value thesis often hinges on *growing the aftermarket mix*. A blended "18% margin, 6% growth" hides that entirely. **Segmentation is how you find out which business you're actually buying.**

**Check (6.5).** Cascade "grew 6%." Diligence splits it: **new equipment** (60% of revenue, grew 9%) and **aftermarket** (40%, grew 1.5%). (i) The concern hiding in the blend? (ii) What to know about each segment's margins, and why mix shift matters for the EBITDA-margin assumption? (iii) One outside-the-room check?

**Answer.**

*(i) The blend hides that the crown jewel is stalling while the cyclical, low-margin segment carries the growth.* Decompose it: new equipment 60% × 9% = **5.4 pts**; aftermarket 40% × 1.5% = **0.6 pts** — so **~90% of the "6%" comes from the cyclical, low-margin business**, and the high-margin recurring segment is essentially flat (1.5% ≈ inflation → no real volume growth). Worse, new-equipment demand is likely near a *cyclical peak*, so that 5.4 pts can reverse: a peak-cyclical number flattering a decaying core.

*(ii) You'd want each segment's gross margin, then run the mix forward.* The mix is **shifting toward the low-margin segment** (equipment growing → bigger share; aftermarket shrinking as a %). So even if each segment's own margin holds flat, the **blended margin *falls* from mix alone.** That's backwards from the base case's assumed 18.1% → 19.3% expansion: this trend predicts **compression** unless a structural force (SG&A leverage, or reviving aftermarket growth) overwhelms it. *Margins can't expand cyclically — they must expand structurally* — which is exactly why mix shift matters. (Margin is an *output* of the segment mix, 6.4, and the segments say it should compress.)

*(iii) Customer reference calls — but diagnosing **why aftermarket is flat**,* since three answers point opposite ways: (a) "we've switched to cheaper third-party parts" → **the moat is leaking** (6.2), terminal, kills the margin thesis; (b) "our equipment is still new, we haven't needed parts yet" → a **lagged tailwind** (today's equipment → tomorrow's parts), bullish; (c) "Cascade never sold us service contracts" → a **commercial gap** PE can fix (attach-rate upside) → the value-creation plan writes itself.

*The strategic reframe:* once segmented, Cascade isn't "a manufacturer growing 6% at 18%" — it's **"a stalling high-margin aftermarket annuity attached to a cyclical, low-margin equipment business near its peak."** That flips the value thesis (grow the *aftermarket mix*, not the whole), the model (split the lines, let margin *emerge*), and the price (≈90% of growth is cyclical and may reverse — the 5.5 discipline, with a reason). **When a segmentation shows the mix shifting toward the worse business, the burden on any margin-expansion assumption flips from "why wouldn't it?" to "what structural force overcomes the adverse mix?" — name it with evidence, or fade the margin.**

---

# Sources & References

*Real figures in this handbook were verified against public sources during course preparation (mostly via web search of primary disclosures and financial press). **Point-in-time data drifts** — fund marks, interest rates, and market sizes change; verify against primary sources before relying on them. Worked examples labeled "illustrative" (including the entire **Cascade Components** case and the round-number LBO/DCF examples) are hypothetical teaching constructs — not real companies, transactions, or projections.*

**Fund performance & returns.** Clearlake and Silver Lake fund-level multiples and IRRs (DPI / RVPI / TVPI, since-inception IRR), and the trough-vintage examples (Arsenal, Tiger Global 2022 funds): CalPERS Private Equity Program fund-performance disclosures, as of September 30, 2025.

**Secondaries & market data.** Ardian ASF IX (~$30B), 2025 secondaries volume (~$226B), the NYC pension ~$5B sale to Blackstone, and buyer AUM figures (Lexington, Coller, HarbourVest, Blackstone Strategic Partners): firm announcements and secondary-market press, 2025.

**Emerging markets.** India PE/VC commitments (~$78B since 2020; >⅓ of new Asian PE capital) and the "best EM" ranking: Preqin investor surveys (2024/2025) and PwC commentary.

**Industry backdrop & the value-creation era.** Bain & Company, *Global Private Equity Report* (2026) — the "12 is the new 5" framing (a typical 2010s buyout needed ~5% annual EBITDA growth to reach a 2.5× MOIC over five years; ~10–12% is required today, with cheap debt and multiple expansion gone), plus fundraising and deal-value context. Corroborated by Bain press materials and PE trade press.

**PE liquidity crunch — fundraising & the exit backlog (Module 1 deep-dive).** WSJ, "Private-Equity Fundraising Falls to Slowest Pace in a Decade," Chris Cumming, Apr 3, 2026 ($86B raised in Q1 2026, worst pace since ~2016; 2025 ≈ $423B global; the "reset" digesting 2020–21 vintages), and WSJ, "Private-Equity Firms Are Sitting on a Nine-Year Backlog," Mark Maurer, Jul 7, 2026 (PwC/PitchBook: ~9 years to clear ~13,500 US portcos; ~1,500 held 9+ yrs; the SaaSpocalypse; 16 PE-backed IPOs / $10.1B in H1 2026). Corroborated by PitchBook Q1/Q2 2026 fundraising reports and PwC analysis.

**PE resilience & bifurcation — the other half of the crunch (Module 1 deep-dive).** WSJ: "KKR Closes Record $23 Billion North America Private-Equity Fund" (N. Miller, Apr 2, 2026; NAX4, largest NA-only fund ever; predecessor funds 23% gross / 19% net IRR, 2.1× / 1.8× MOIC); "Aon Nears Roughly $17 Billion Deal for Insurance Brokerage USI" (L. Thomas & M. Maurer, Aug 30, 2026; KKR bought USI for $4.3B in 2017 — a strategic exit); "Midmarket Firm GenNx360 Raises $865 Million Fund for AI-Fueled Transformation" (M. Armental, Aug 27, 2026; AI-barbell thesis; Precision Aviation exit ~2.5× / 48% IRR; continuation vehicles); and "Private Credit's Chills Draw Bargain Hunters Offering Cash to Trapped Investors" (I. Taylor, Aug 24, 2026; Cox Capital ~26%-of-NAV BDC offers; gated redemptions; nonaccruals 4.69%). KKR CoolIT sale to Ecolab ($4.75B, ~15×) corroborated by BusinessWire/Ecolab, Mar 2026.

**SaaSpocalypse — the contrarian read (Module 6.2 moat-test).** WSJ, "AI Is Disrupting Software Companies — but Not as Fast as Many Feared," Asa Fitch, Sept 8, 2026 (incumbents' switching-cost/integration moats held; Salesforce +22% on earnings with Agentforce ARR ~$1.5B / +240%; the real vector is "seat compression" of the seat-based pricing model, not company extinction; Salesforce ~16× forward P/E vs ~43× 10-yr avg). Corroborated by the ~$2T 2026 software drawdown data and Salesforce/ServiceNow/Workday Q2–Q3 2026 results.

**Leveraged finance.** SOFR (3.63%, mid-July 2026): Federal Reserve Bank of New York (publishes SOFR daily). Private credit vs. broadly-syndicated market sizes (~$1.5–2T each; ~$3T by 2028 forecast), CLO issuance ($43.1B), spread levels (median S+475; S+350 examples), JPMorgan's ~$50B direct-lending expansion, and jumbo unitranche deals (Ares/Ardonagh ~$3.3B, Foundation Risk Partners ~$2.2B, KKR Credit ~$1.1B): industry data providers and financial press, 2025–2026.

**Company transactions.** Hilton (Blackstone, ~$26B, 2007; ~3× / ~16% IRR over ~11 yrs), TXU (~$45B, 2007; 2014 bankruptcy), RJR Nabisco (~$25B, 1988): contemporaneous financial press and company disclosures. **Electronic Arts** take-private (~$55B, Sept 2025 — the **largest LBO ever**, eclipsing TXU): PIF, Silver Lake & Affinity Partners; ~$36B equity + $20B JPMorgan debt; $210/share, 25% premium — WSJ, "Electronic Arts Goes Private for $55 Billion in Largest LBO Ever," Miller & Thomas, Sept 29 2025.

**PPA / goodwill — real extreme case (Module 3.3 deep-dive).** WSJ, "Boeing's $8.4 Billion Deal Is Bleeding Red Ink," Jonathan Weil, Sept 3, 2026, and Boeing Form 10-Q (Q1/Q2 2026): the Spirit AeroSystems acquisition — consideration ~$8.39B, goodwill $9,997M → $10,278M (exceeding the purchase price because identifiable net assets were negative), ~$1.52B "off-market customer contracts" liability, and the one-year measurement-period true-up routing losses to goodwill rather than the income statement. Thoma Bravo / Dayforce take-private (~$12.3B, $70.00/share): company press releases and SEC filings. Verint/Calabrio (~$2B, $20.50/share), PROS/Conga (~$1.4B, $23.25/share), Boeing Digital Aviation Solutions / Thoma Bravo ($10.55B), ADIA co-investment in Dayforce, Platinum Equity/Aventiv, and Vista/Cloud Software Group continuation vehicle (~$5.6B): company announcements and financial press, verified via web search.

**Company financials.** Dayforce FY2024 income statement, EBITDA/Adjusted-EBITDA reconciliation, cash-flow and capex detail: Dayforce reported FY2024 results (company filings). WeWork "Community Adjusted EBITDA" (2017 net loss $(933.5)M → $233.1M "profit"): The We Company Form S-1 (2019) and contemporaneous press.

**Zombie funds (real-world anchor).** WSJ, "Private-Equity Assets Stuck in 'Zombie Funds' Are at a Record High," Mark Maurer, July 21, 2026 — including the figures that article attributes to **PitchBook** ($348.5B in funds ≥10 years old; $512.7B in 7–9-year funds) and **Preqin** ($3.91T unrealized value; 74% of North American PE assets).

**Owner-comp normalization case (Module 4 deep-dive).** WSJ, "How Blackstone Put Jersey Mike's on a Fast Track to This Week's IPO," Mark Maurer & Heather Haddon, July 29, 2026, plus Jersey Mike's Subs **Form S-1** — the corporate jet ($41M), discretionary bonuses/donations ($192M → $11M), family payroll, debt (~$2.1B; interest $43M → $104M), and IPO terms (~$8B valuation, up to $1.09B raise, NYSE: JMKE). Corroborated by CNBC, Forbes, and Bloomberg (July 2026).

**Leverage risk — hedge-fund vs LBO (Module 1 deep-dive).** WSJ, "His Wedding Guests Were Arriving—Just as His $45 Billion Fund Was Falling Apart," Berber Jin, Peter Rudegeair, Gregory Zuckerman & Anissa Gardizy, July 31, 2026 (Situational Awareness: ~4x leverage, margin calls, forced block sale to Citadel, ~$5B Anthropic stake retained) — corroborated by CNBC, FT, Bloomberg. **TXU / Energy Future Holdings** (2007 buyout → 2014 Chapter 11; KKR / TPG / Goldman; ~$45B, ~$40B debt; ~$8B sponsor equity wiped; Berkshire ~$873M bond loss): Harvard Business School case and contemporaneous financial press.

**Owner-comp normalization & fast exit (real-world anchor).** WSJ, "How Blackstone Put Jersey Mike's on a Fast Track to This Week's IPO," Mark Maurer and Heather Haddon, July 29, 2026 — figures per the company's SEC IPO filing as reported: ~$6B majority purchase (~$8B including debt), founder ~10% rollover; discretionary bonuses & donations cut to $11M (2025) from $192M (2024); ~$500M added debt bringing total to $2.1B; interest expense $104M (2025) vs $43M (2024); ~$8B IPO valuation, up to $1.09B of shares sold.

**Quotations.** Warren Buffett on stock-based compensation ("If compensation isn't an expense, what is it?…") is widely reported and paraphrased here.

**Frameworks & mechanics.** Standard PE concepts — fund structure and waterfalls, LBO returns math, DCF and comparable-company valuation, Quality of Earnings, purchase-price allocation, working-capital pegs, and the 338(h)(10) election — are established industry practice drawn from standard corporate-finance and deal references; no single source, and none should be read as legal or tax advice.
