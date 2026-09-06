# Private Equity Course — Full Conversation Transcript

> A faithful reconstruction of our session, formatted as a dialogue. Companion to `pe_course_notes.md` (the polished lesson content) and `pe_course_progress.md` (the checklist). This file captures the *conversation* — every question, answer, correction, and tangent — including the interactive Q&A that isn't in the notes. Diagrams shown as inline widgets are described in brackets.

---

**You:** *(uploaded the 8-module PE course syllabus)* This will be a long running conversation. Looking to learn about Private Equity. Can you help with providing me lessons along the lines of this course?

**Instructor:** Agreed to be your instructor and teach it as a real course — one lesson at a time, plain language, anchored to concrete examples and numbers, connecting each new idea to prior ones, and actually building the math in the modeling modules. Then delivered:

### Module 1, Lesson 1 — History & Evolution of Private Equity
Core definition to anchor the whole asset class: **PE firms raise money from outside investors to buy private companies, improve them over years, and sell them for more.** The eras:
- **Origins (1940s–70s):** ARD (1946, Georges Doriot) — its ~$70k investment in Digital Equipment Corp (1957) grew to hundreds of millions, proving the model and seeding VC.
- **1980s LBO boom:** KKR (1976); leverage as the return engine; Milken's junk bonds as fuel; RJR Nabisco (1988, ~$25B, *Barbarians at the Gate*) — the era that gave PE its reputation.
- **1990s–2000s institutionalization:** Drexel collapse (1990); Blackstone/Carlyle/Apollo; pensions & endowments allocating; mega-deals returned then froze in 2008.
- **2010s–today:** firms went public ("alternative asset managers"); cheap money → dry powder explosion; post-2022 higher rates reshaped the math.
Throughline: buy private companies + use leverage + hold to improve. 1980s gave leverage + reputation; 90s–2000s gave discipline + scale; 2010s made it mainstream.

Then asked, via tappable options, how to calibrate: depth, pace, and format extras.

---

**You:** Depth: "This is perfect." Pace: "One lesson per turn." Extras: Visual diagrams + Practice questions/quizzes + A running progress tracker file.

**Instructor:** Set up the progress tracker file, then taught:

### Module 1, Lesson 2 — Fund Structure, Management & the GP/LP Relationship
- The fund = a **limited partnership**. **GP** (the firm) runs it, makes all decisions, commits 1–5% of its own capital ("skin in the game"). **LPs** (pensions, endowments, sovereign funds, insurers, funds-of-funds, family offices) supply 95%+, are passive, liability limited to their commitment.
- "The firm" = management company (collects the fee) + GP entity (collects carry).
- **Commitments vs. calls:** LPs *commit*, then the GP *calls* capital (drawdowns) over a ~5-yr investment period; ~10-yr fund life (investment period yrs 1–5, harvest yrs 5–10).
- **"2 and 20":** ~2% management fee (steady, paid regardless of performance) + 20% carried interest (profit share, the alignment driver).
- **Distribution waterfall:** (1) return of capital → (2) preferred return / hurdle (~8%) → (3) GP catch-up → (4) 80/20 split.
- **The J-curve:** early negative returns (fees, no exits yet) then positive as companies sell.

[Diagram: GP/LP fund structure — LPs commit ~95% capital into the Fund (a limited partnership), the GP/firm runs it and commits ~2%, the fund buys equity in portfolio companies A/B/C, and profits flow back up the same path.]

**Practice questions:** (1) term for the LP's remaining obligation + fund phase; (2) walk the waterfall on a $500M fund returning $900M; (3) how the management fee creates misalignment and what counteracts it.

---

**You:** (1) dry powder, not sure about life cycle phases; (2) return of capital → preferred return → GP catch-up → 80/20 split; (3) GPs earn fees regardless, carried interest is the alignment mechanism.

**Instructor:** Graded: (1) half-right — the precise term is **uncalled/unfunded commitment** (dry powder is the aggregate); taught the two life-cycle phases (investment vs. harvest); the tell (capital still being called) = **investment period**. (2) Correct ordering; emphasized the *why* — the waterfall *subordinates* GP carry to LPs being made whole first; the 8% hurdle is annualized. (3) Correct; added the sharper misalignment (fee on *committed* capital tempts ever-larger funds) and that alignment = carry **plus** the GP commitment.

---

**You:** Can you give an example or two of the J-curve using real funds if possible?

**Instructor:** Flagged the honest constraint (fund-level cash flows are mostly private), then used **CalPERS public pension disclosures** (as of 9/30/2025) with a "space-for-time" trick — same manager's funds at different ages:
- **Clearlake:** VII (2022) ~0.00× DPI / 4.1% IRR / 1.11× TVPI → V (2018) 1.39× DPI / 32.3% / 1.96× → III (2012) 2.86× DPI / 40.7% / 2.88×. That progression *is* the J-curve.
- **Silver Lake:** VI (2021) 0.22× / 9.1% → V (2018) 0.62× / 11.6% → IV (2013) 1.81× / 20.9%.
- **The trough, live:** 2022 funds underwater on paper (Arsenal VI −3.6%, Tiger Global's 2022 fund −5.9%) — normal, not failure; at year 3 you can't distinguish trough from underperformance, which is *why* LPs don't judge young funds.
[Diagram: the J-curve — cumulative cash to LPs dips below break-even early then climbs, with Clearlake VII in the trough, V past break-even, III high on the curve.]
Tied back: hundreds of staggered-vintage funds let mature ones offset young troughs → CalPERS's blended ~11.3% since-inception IRR.

---

**You:** Can you expand a bit on DPI and IRR? — terms that haven't been introduced.

**Instructor:** Two families of return metrics:
- **Multiples (ignore time):** DPI = cash returned ÷ paid-in (realized, in-hand); RVPI = unrealized value ÷ paid-in (paper marks); TVPI = DPI + RVPI = total value ÷ paid-in; MOIC = deal-level cousin.
[Diagram: TVPI anatomy — Clearlake V's 1.96× TVPI split into DPI 1.39× (cash) + RVPI 0.57× (still held), with a "paid-in 1.0× / money-back" line.]
- **IRR (all about time):** the annualized rate setting NPV to zero. Timing-sensitive: $100→$200 in 3 yrs ≈ 26% IRR vs 7 yrs ≈ 10%.
- "DPI is the new IRR"; IRR can be flattered by subscription lines. Where they'll reappear: 1.6 (hurdle = IRR threshold), 5/8 (computed by hand).

---

**You:** So in your Clearlake III vs Silver Lake IV example, IRR alone would be misleading because DPI for both is ~3x?

**Instructor:** Not quite — corrected the premise. The ~2.8–2.9× figures were **TVPI**, not DPI. Actual DPIs differ a lot: Clearlake III 2.86× vs Silver Lake IV 1.81×. So IRR and DPI *agree* Clearlake delivered more (more cash, faster); the number that makes them look like twins is **TVPI**, propped up by Silver Lake's 0.97× of unrealized RVPI. So TVPI is the misleading one here, not IRR.
[Diagram: same TVPI (~2.8×), very different cash split — Clearlake III nearly all realized (DPI 2.86×), Silver Lake IV only 1.81× cash + 0.97× paper.]
Caveats: Silver Lake's book is still open (unrealized could rise or be marked down); and the instinct to distrust one number was right — just the direction was backwards. Read all three: TVPI (paper), DPI (pocket), IRR (speed).

---

**You:** next

**Instructor:** ### Module 1, Lesson 3 — PE Within the Alternatives Ecosystem
**Alternatives** = everything beyond the public-stock/bond "60/40." LPs use them for the illiquidity premium, diversification, and access to the private economy. Two organizing axes:
- **Life-cycle (equity continuum):** Venture (startups, minority, no debt, power-law) → Growth (scaling, proven model) → Buyout/LBO (mature, control, leverage = the "PE" this course means). Terminology trap: broad "PE" = all three; colloquial "PE" = buyout.
- **Capital structure:** Private credit / direct lending sits *above* equity (paid first, contractual interest, lower risk) — often the debt in a buyout. Real assets = real estate + infrastructure (stable, long-life, lower risk/return).
[Diagram: risk/return spectrum — Credit → Infra → Real estate → Buyout → Growth → Venture (lower→higher risk; paid first/debt → paid last/equity); Hedge funds flagged as the structural outlier: liquid, public, open-ended, no capital calls/J-curve/DPI.]
LPs set a strategic asset allocation; key constraint = the **illiquidity budget**. Mega-firms now span the whole map → "alternative asset managers."
**Practice Qs:** (1) lender vs equity in the same company; (2) why hedge funds use open-ended structures; (3) minority stake in an unprofitable startup with no debt — is it "PE"?

---

**You:** (1) direct lending sits higher, buyout has higher expected return because former's risk is lower; (2) liquid public securities with active strategies; (3) venture fits better; buyout involves controlling stake and leverage.

**Instructor:** Q2 fully correct, Q1 and Q3 mostly right but skated past the *why*. (1) Added the mechanism: **return is the price of risk** — the lender accepts a capped return for getting paid first; equity is the residual claimant, last in line but with uncapped upside; "safer" and "lower return" are the same fact twice. (2) Sharpened the causal chain: liquid assets → frequent valuation → investors can come and go → open-ended fits. (3) Correct — it's **venture** (minority + unprofitable + no debt); buyout needs a cash-flowing engine to lever and build around.

---

**You:** next

**Instructor:** *(Searched current data first.)* ### Module 1, Lesson 4 — The Current State of PE in Emerging Markets
EM weakens nearly every developed-market assumption:
1. **Leverage often unavailable** (shallow debt markets) → EM PE = minority growth equity, returns from growth not engineering.
2. **Currency risk — the defining hazard:** LP measures in USD, company earns local; depreciation erodes $ returns (2× local × 0.5 FX ≈ 1.0× USD). Hence preference for hard-currency/export revenue.
3. **Exits harder/slower** (shallow IPO markets) → #1 investor concern; more trade sales (+60% YoY APAC), secondaries, continuation funds; longer holds.
4. **Political/regulatory/rule-of-law risk** (capital controls, expropriation; China's govt funds even pushing "guaranteed returns").
5. **Weaker data quality.** 6. **Family/founder-owned targets** reluctant to cede control.
[Diagram: sources of return, DM buyout (earnings growth + multiple expansion + leverage) vs EM PE (almost all earnings growth, currency as a wildcard drag).]
Bull case = growth/demographics; **India** the standout (most-cited best EM in Preqin 2024/25, >⅓ of new Asian PE capital, $78B since 2020). Headline = rotation away from China. Global backdrop: fundraising down 3rd straight year (~$480B), "12 is the new 5."
**Practice Qs:** (1) 2.5× local growth × 40% depreciation → $ return; (2) why EM PE is minority growth equity (two reasons); (3) does a higher hurdle rate fix EM risk?

---

**You:** (1) $ return is 1×, USD-linked means no currency hedging worry; (2) debt isn't there at scale/price/maturity; companies are family/founder-owned, unwilling to cede control; (3) not sure.

**Instructor:** Q2 fully correct. Q1: fixed the arithmetic — a 40% depreciation = ×0.60, so 2.5 × 0.60 = **1.5×** (not 1×; the 1× came from the earlier example); two-thirds of a great result evaporates into FX — which is why USD-linked revenue is a "free" hedge. Q3 (the keystone): **no** — a hurdle rate *prices* risk (an IRR threshold for sharing upside) but doesn't *control* it. It can't recover capital a currency collapse destroyed or beat capital controls. Real mitigation = FX hedging, hard-currency revenue, treaty-jurisdiction structuring, political-risk insurance (MIGA/DFC), staged capital, pre-arranged exits. A too-high hurdle can even *misalign* incentives (a GP zeroed out swings for the fences).

---

**You:** next

**Instructor:** ### Module 1, Lesson 5 — Common Investment Strategies
Organized by maturity, health, transaction type, and whether you even buy an operating company. Buyout playbooks:
1. **Buy-and-build (platform + add-ons)** — the dominant modern strategy; engine = **multiple arbitrage** (buy small firms at low multiples, re-rate at scale).
[Diagram: platform $20M EBITDA @ 8× ($160M) + five add-ons $15M EBITDA @ 5× ($75M) → combined $35M EBITDA exits @ 10× = $350M EV → ~$115M created purely from the re-rating, before any organic growth.]
2. **Carve-out** — buy a non-core division; challenge = disentanglement → TSA.
3. **Take-private** — buy + delist a public company.
4. **Turnaround/distressed** — fix broken/over-levered companies; distressed-for-control buys the debt cheap and converts to equity.
5. **Secondaries** — buy existing fund stakes (LP-led / GP-led continuation funds); buying a mature fund skips the J-curve trough.
6. **Co-investment & fund-of-funds.**
Cross-cutting: three value-creation levers = financial engineering / multiple arbitrage / operational improvement — the industry shifted decisively toward operational.
**Practice Qs:** (1) buy-and-build math (platform $40M@9× + $12M add-ons@6×, exit 11×); (2) why a 7-yr-old secondary fund has a different J-curve; (3) match strategies to four situations.

---

**You:** (1) $432M entry, $572M exit, $140M created, all without organic growth; (2) you're buying marked-up, near-sale assets so cash comes back faster / J-curve is shallower; (3) (a) take-private (b) carve-out (c) turnaround (d) buy-and-build.

**Instructor:** Q1 and Q2 perfect (decomposed the $140M: platform re-rate $80M + add-on re-rate $60M; added that secondaries often transact at a discount to NAV). Q3: a/b/c correct; **(d) is venture, not buy-and-build** — buy-and-build requires a *profitable, cash-generative platform* to lever and roll acquisitions into; an unprofitable startup has no EBITDA, so "startup + unprofitable" = the earliest, riskiest end of the maturity spectrum.

---

**You:** Can you give concrete, recent examples of PE firms for each category (1) Buy and build (2) Carve-out (3) Take private (4) Turnaround (5) Secondaries (6) Co-investment. Focus on tech where possible.

**Instructor:** *(Searched and verified each.)* Noted Thoma Bravo appears three times because a few firms dominate tech buyouts:
1. **Buy-and-build — Thoma Bravo** (coined "buy and build"; 565+ software deals): bought PROS Holdings (~$1.4B) folding its B2B unit into Conga; agreed to buy Verint (~$2B) to combine with Calabrio.
2. **Carve-out — Thoma Bravo / Boeing Digital Aviation Solutions** (Jeppesen, ForeFlight, AerData, OzRunways) $10.55B → standalone "Jeppesen ForeFlight," financed with ~$4B of direct lending.
3. **Take-private — Thoma Bravo / Dayforce** $12.3B, $70/share, 32% premium.
4. **Turnaround/distressed — Platinum Equity / Aventiv** debt-for-equity recap (Apr 2025); Cerberus as the archetype.
5. **Secondaries (GP-led) — Vista / Cloud Software Group** record $5.6B continuation vehicle.
6. **Co-investment — Abu Dhabi Investment Authority alongside Thoma Bravo in Dayforce** (a "significant minority investment"); Golub (400+ co-investments, $1.7B+).
Noted the Dayforce deal is *both* a take-private and a co-investment — labels describe facets, not exclusive boxes.

---

**You:** Yes, deeper into 5 Secondaries. Who is buying into mature funds? More examples.

**Instructor:** Clarified the distinction I'd muddied: **LP-led** (an investor sells its stake — this creates the "skip the trough" dynamic) vs **GP-led** (continuation vehicles — my earlier examples).
[Diagram: LP-led (selling LP → secondary buyer → steps into a mature fund) vs GP-led (GP moves a star asset into a continuation vehicle; existing LPs roll or cash out).]
**Who buys:** Ardian, Lexington (~$55B), Coller (~$35B), HarbourVest (~$115B), Blackstone Strategic Partners (>$100B), Apollo S3, KKR, GCM Grosvenor, StepStone. Ardian just raised **$30B for ASF IX — the largest secondaries fund ever** (backers include CalSTRS, PA SERS, NYC ERS, ADIA $4B). Marquee LP-led deal: **NYC's five pensions sold ~$5B to Blackstone** (May 2025, likely the largest ever — 125+ funds, 74 managers, 95%+ acquired), motivated by "strategic realignment," not distress. 2025 secondaries volume hit a record ~$226B. Broadening buyer base: private wealth (22% of Ardian's fund), Canadian pensions on both sides. Confirmed the lesson: Ardian's own pitch says "no J-curve"; buyers also avoid blind-pool risk and buy at a discount to NAV. LP-led is actually the *larger* share of the market.

---

**You:** You've used the term discount to NAV a few times without explaining it. Please explain clearly with examples. Why do LP-led stakes transact at a discount?

**Instructor:** **NAV** = the GP's reported estimate of holdings' value — an *appraisal, not a market price*, marked quarterly and stale. **Discount to NAV** = price ÷ reported NAV; a $10M stake bought for $8M = a 20% discount ("80 cents on the dollar").
[Diagram: pricing spectrum as % of NAV — ~80% deep discount, ~90% typical LP-led, ~99% single-asset CVs (near par), ~106% trophy premium; NAV = 100% = the GP's mark.]
**Why the discount:** (1) liquidity isn't free (the buyer provides an early exit); (2) NAV is the GP's estimate → buyers demand a margin of safety; (3) the buyer inherits unfunded commitments; (4) remaining fees + time; (5) diligence/friction cost; (6) it's how the buyer manufactures its return. It ranges by quality/market and can flip to a premium. Nuance: accounting lets a buyer re-mark up to NAV immediately → "NAV squeezing," a paper gain that flatters early returns — and part of why secondaries dampen the J-curve.

---

**You:** Can you keep appending everything we have in the conversation and future lessons to a doc? Separate docs per lesson is fine too.

**Instructor:** Set up a **two-file system**: `pe_course_progress.md` (checklist + quick summary) and `pe_course_notes.md` (full content of every lesson + deep-dive), and committed to appending future lessons automatically. Populated the notes doc with everything through 1.5 + the deep-dives.

---

**You:** ok, please continue to use real work examples and double check what you are generating to ensure it is real, not made up.

**Instructor:** Agreed — illustrative math labeled as illustrative, real figures verified by search. *(Verified Hilton first.)* ### Module 1, Lesson 6 — LBO Analysis, Hurdle Rates and Returns
The engine: buy with a thin equity slice + lots of debt; three levers grow the equity (Equity = EV − Net Debt): **EBITDA growth, debt paydown, multiple change.**
Illustrative: $100M EBITDA @ 10× = $1,000M EV, financed $500M debt + $500M equity; 5-yr hold → EBITDA $150M, debt $500→$300M, exit 10× → exit equity $1,200M = **2.4× MOIC / ~19% IRR**.
[Diagram: value bridge — entry equity $500M + $500M (EBITDA growth) + $200M (debt paydown) → exit equity $1,200M, exit multiple flat.]
Gave the MOIC↔IRR↔time table (2×: 26/15/10% over 3/5/7 yrs; 3×: 44/25/17%); exit-multiple sensitivity; leverage amplification (70/30 → 3.3×/27%). Hurdle = an IRR threshold.
**Real anchor — Blackstone × Hilton (2007–18):** $26B (~$20.5B debt + $5.6B equity), held through the crisis, asset-light franchising + new CEO, ~$14B profit, ~3× MOIC, ~16% IRR over ~11 yrs — the most profitable LBO ever (great multiple + long hold = modest IRR; survival was the strategy). Counter: **TXU** (~$45B, 2007, largest LBO ever) → 2014 bankruptcy, ~−100%.
**Practice Qs:** (1) $80M EBITDA @ 9×, 60% debt, 5-yr hold; (2) decompose the levers; (3) why Hilton's smaller multiple gave a higher IRR than the illustrative deal — wait, the reverse.

---

**You:** (1) Entry equity 720M, exit EV 990M, exit equity 510M, MOIC 1.275, IRR ~5%; (2) EBITDA growth 270M, debt paydown 120M, multiple 120M; (3) 3× was over 11 yrs (~10.5% but 16% due to tranched IPO distributions), 2.4× over 5 yrs.

**Instructor:** Q3 correct; Q2 two-thirds right; **Q1 had a root error that cascaded.** "Entry equity = 80×9 = 720M" is the entry *enterprise value*. Since **EV = Debt + Equity** and debt is 60%, equity is the other 40%: debt $432M, equity **$288M**. Then exit debt $432 − $120 = $312M; exit equity $990 − $312 = **$678M**; MOIC **2.35×**; hold is **5 yrs** (not 11) → **~19% IRR**, not 1.275×/5%. The whole miss = treating the purchase price as the equity check. Q2 fix: multiple change = **$0** (exited at the same 9×), so the bridge is $288M + $270M + $120M + $0 = $678M. Named it the single most common beginner error: confusing the price of the company with the size of your check.

---

**You:** For the error in problem 1, when you said 60% debt, I assumed a 600M/400M split — it was not clear it was 60% of entry value. Also, can you check the course notes to ensure all facts/real examples are real, not made up. This is critical.

**Instructor:** Conceded the ambiguity — "60% debt" conventionally means 60% of enterprise value, but I should have said it explicitly (and noted debt + equity must sum to EV, so a $600/$400 split implies a $1,000M EV, which flags the inconsistency). Then **audited the notes:** re-verified the two least-certain items against SEC filings / press releases — **Verint** ($2B EV, $20.50/share, combining with Calabrio) ✓ and **PROS Holdings** (~$1.4B, $23.25/share, B2B into Conga) ✓, both confirmed and enriched. Everything else was either well-established history or searched-and-cited. Tightened three things anyway: credited ARD's co-founders precisely; added a "point-in-time snapshot" caveat to the CalPERS figures; enriched the PROS/Verint entry. Conclusion: nothing fabricated.

---

**You:** next

**Instructor:** *(Verified current leverage levels.)* ### Module 1, Lesson 7 — Leverage as a Tool for Value Creation *(first pass)*
Taught "turns of EBITDA," the current market (~11.7× entry multiples, leverage down to 4–5× from 6–7×, ~9–11% debt cost, equity up to 45–55%), the **debt stack** (senior secured 1st lien → 2nd lien → high-yield → mezzanine → equity), constraints (max leverage, interest coverage, min equity), covenants (maintenance vs incurrence, cov-lite), why leverage creates value (amplification, tax shield, discipline, deleveraging), and the risks (fixed interest, floating rates, refinancing). Anchored to the Verint ~$2.7B leveraged loan.
[Diagram: the debt stack, paid-first/cheapest at top → paid-last/most-expensive at bottom.]
Included an illustrative rate-vs-leverage table and practice Qs.

---

**You:** (1) 5 turns, 60/(300×0.08)=2.5 — wait, this is later. *(Answering 1.7 Q1)* Entry equity via 60% debt...

**Instructor:** *(Note: user then flagged the lesson pace.)*

---

**You:** I think this lesson moved way too fast. Can we start with basics? EBITDA. Also explain 6.5 turns more fully.

**Instructor:** Slowed all the way down. Taught **EBITDA from scratch:** Earnings Before Interest, Taxes, Depreciation & Amortization — you add those four back to isolate core operating profit. Built it from a clean income statement (Revenue $400M − COGS $250M = GP $150M − SG&A $50M = EBITDA $100M − D&A $20M = EBIT $80M − interest $20M = pretax $60M − tax $15M = NI $45M).
[Diagram: EBITDA built bottom-up — Net income $45M + Taxes $15M + Interest $20M + D&A $20M = EBITDA $100M.]
Why PE cares: proxy for cash to service debt, apples-to-apples comparison, the unit of measurement. Honest caveat: EBITDA ≠ cash (ignores capex, working capital). Then rebuilt **turns & coverage** slowly — and **corrected my own arithmetic**: 6.5 turns of a $100M-EBITDA company is **$650M, not $715M** (I'd multiplied by 110). Clean 4-scenario table showing how doubling rates (5%→10%) turns a healthy 6.5-turn structure (3.1× coverage) into a too-thin one (1.5×), forcing leverage down. Fixed it in the notes.

---

**You:** 5 turns, 60/(300×0.08)=2.5, yes, redo lesson 1.7 at this slower pace.

**Instructor:** Confirmed the gut-check (5 turns; 2.5× coverage), then rebuilt 1.7 in four slow parts:

**Part 1 — the core idea (amplification).** Home analogy: a $500k house all-cash rises to $600k = +20%; with $100k down + $400k mortgage = +100%; if it falls to $400k, all-cash −20% but mortgaged −100% (wiped). The loan is fixed and repaid first, so all the swing hits your equity. Company version: $1,000M @ 60% debt, value → $1,200M gives +50% on equity (vs +20% all-equity); → $700M gives −75%. **Amplification factor = 1 ÷ (equity as % of price).**
[Table: debt fixed at $600M across scenarios; equity absorbs the whole swing.]

---

**You:** 200/300=0.667, amplification=1/0.3

**Instructor:** Both correct — 66.7% return, 3.33× amplification; more debt (60%→70%) raised amplification (2.5×→3.33×) in both directions.

**Part 2 — the debt stack.** Why layered: different lenders, different risk appetites → slicing raises *more* total debt. Ordered by **seniority** (the same waterfall idea). Built a real $600M: senior secured 1st-lien $400M @ ~8.5% → 2nd lien $150M @ ~12% → mezzanine $50M @ ~14% → equity $400M. Showed a $500M liquidation: senior 100%, 2nd lien 67%, mezz 0%, equity 0% — the recovery gradient *is* why lower layers charge more.

---

**You:** Senior: 400M, Second: 30M, Mezz: 0, Equity: 0

**Instructor:** Exactly right (a $430M liquidation). Pulled out the psychology: the 2nd lien lost 80% while the senior lost nothing — same failure, different rung — which is *why* each lower layer charges more.

**Part 3 — the other benefits.** (1) **Interest tax shield:** interest is tax-deductible; annual saving = interest × tax rate (e.g., $60M interest × 25% = $15M/yr real cash). (2) **Discipline effect:** heavy debt forces lean, cash-focused management (Jensen). Plus deleveraging. So three benefits: amplification, tax shield, discipline.

---

**You:** 16.8M

**Instructor:** Correct — $80M interest × 21% = $16.8M/yr tax shield.

**Part 4 — limits & risks.** Core danger: interest is fixed, performance isn't. Coverage fragility (a 30% EBITDA dip drops coverage from 1.67× to 1.17×, vaporizing 75% of the cash cushion). Covenants (maintenance vs incurrence; cov-lite). Floating-rate exposure (SOFR spike 2022–23). Refinancing/maturity walls. Real bookend: Hilton (survived) vs TXU (bankrupt). Then rewrote the entire 1.7 notes section as this cleaner Part 1–4 version.

---

**You:** 5 turns, 60/(300×0.08)... *(gut check on new EBITDA/coverage)*: $60M EBITDA, $300M debt @ 8% → 5 turns, coverage 2.5×.

**Instructor:** Both spot on.

---

**You:** 1.8

**Instructor:** ### Module 1, Lesson 8 — Introduction to Valuation Methods
**Part 1 — Comparables & Multiples.** Two philosophies: relative (comps) vs intrinsic (DCF). A **multiple** = value ÷ a metric; workhorse = **EV/EBITDA**. Crucial distinction: **Enterprise Value** (whole business, all capital providers) vs **Equity Value** (EV − net debt); match pre-interest metrics (EBITDA, revenue) to EV, post-interest (net income) to equity/price (P/E). **Trading comps** vs **transaction/precedent comps** (which run higher due to the control premium). Process: pick comps → find multiples → median → × your metric → implied EV → − net debt = equity.
[Diagram: four comps at 9/10/11/12× (median 10.5×) applied to $100M EBITDA → $1,050M EV − $200M net debt = $850M equity.]
Pros: fast, market-grounded. Cons: garbage-in/out; inherits market sentiment.

---

**You:** (a) 50×8=400M (b) 400-80=320M

**Instructor:** Both right — median 8×, $400M EV, $320M equity.

**Part 2 (step 1) — the DCF engine: time value of money.** Future cash is worth less than present cash. **PV = Future ÷ (1+r)ⁿ** (discounting). $100 at 10%: 1yr $90.9, 2yr $82.6, 3yr $75.1, 5yr $62.1.
[Diagram: $100 shrinking by year received, at 10%.]
The discount rate r = opportunity cost + risk (higher risk → higher r → worth less); for a company, r = WACC.

---

**You:** 165.3

**Instructor:** Correct — $200 ÷ 1.21 = $165.3.

**Part 2 (step 2) — building the full DCF.** (A) project free cash flow (FCF = cash after taxes + reinvestment [capex + working capital] — the things EBITDA ignores); (B) discount each year; (C) terminal value (perpetuity growth: final FCF × (1+g) ÷ (r−g), then discount back); (D) sum = EV; (E) − net debt = equity. Worked it: FCF $100→140M, r 10%, g 2%, net debt $200M → PV of FCFs $448M + PV of terminal value $1,108M = **EV $1,556M** − $200M = **$1,356M equity**.
[Diagram: EV composition — $448M (5-yr FCF, 29%) + $1,108M (terminal value, 71%).]
Terminal value = 71% of the answer = the DCF's key weakness (huge sensitivity). Pros: fundamentals-based. Cons: "torture the assumptions."

---

**You:** 100M

**Instructor:** Close — each cash flow individually PVs to $100M ($110/1.1 and $121/1.21), but a DCF *sums* all flows → **$200M**. The whole principle is adding up every discounted flow.

**Part 3 — the football field & the LBO angle.** Each method gives a *range*; plot them side by side and find the convergence zone.
[Diagram: football field — trading comps $900–1,150M, precedent $1,050–1,300M, DCF $1,050–1,350M, LBO $850–1,100M; overlap ~$1.05–1.1B.]
The **LBO analysis** asks a different question — "what's the max a PE buyer can *pay* and still hit its target return?" — run the model backwards, solve for entry price. It sets the walk-away ceiling and usually sits lowest (financial buyers need a return; strategics can pay for synergies). Ties together EBITDA, leverage, MOIC/IRR, exit multiple. **→ Module 1 complete.**

---

**You:** Before we do that, I went back to calculate IRR with your exit-multiple sensitivity example... *(worked through several scenarios and concluded)* your claim of 8× → 1.8× MOIC; 10× → 2.4×; 12× → 3.0× is not correct, because I don't know how you finance a $1200M EV with $500M debt/$500M equity.

**Instructor:** Confirmed the arithmetic was flawless but **my numbers were actually correct** — I'd under-explained one hidden assumption. An **exit-multiple sensitivity holds the ENTRY fixed:** you already bought at 10× for $1,000M, putting in $500M equity — that's done. The 8× and 12× are what a future buyer pays *you* when you *sell*, not new purchase prices — so there's no financing puzzle (at exit you're the seller, receiving cash). With equity fixed at $500M and exit debt $300M: 8× → equity $900M → 1.8×; 10× → $1,200M → 2.4×; 12× → $1,500M → 3.0×. And the beautiful part: your own experiment (buying *and* selling at the same multiple) proved that the multiple washes out — multiple change only helps when exit ≠ entry (the 1.5 arbitrage point). Fixed the wording in the notes.

---

**You:** Can you provide a breakdown of Revenue − COGS = gross profit, etc., for a typical enterprise software firm — for example Dayforce. What comprised their COGS and SG&A, and how much? A real example would help.

**Instructor:** *(Pulled Dayforce's real FY2024 income statement.)* Gave the full statement (Revenue $1,760.0M; total cost of revenue $947.9M; gross profit $812.1M; S&M $342.0M, G&A $366.0M; operating profit $104.1M; net income $18.1M). **COGS composition:** recurring $352.7M (cloud/support), professional services $291.0M (implementation consultants), product development/R&D $223.8M, D&A $80.4M — flagging that Dayforce unusually buries R&D + D&A in COGS, making headline gross margin look like 46% when the true SaaS "cloud recurring gross margin" is 78.9%. **SG&A:** S&M + G&A. Then showed **where the clean chain breaks** (gross profit − SG&A = EBIT not EBITDA; EBITDA isn't a line — reconstruct it: NI + int + tax + total D&A $209.8M = $288.0M).
[Diagram: bridge — $18M net income → +interest/tax → +D&A → EBITDA $288M → +SBC → +one-offs → Adjusted EBITDA $501.5M.]
The chasm: GAAP net income $18.1M (1% margin) vs Adjusted EBITDA $501.5M (28.5%), the gap almost all D&A + SBC. Reality check: capex $109.6M, FCF only $171.5M. LBO tie-in: TB's ~$12.3B ≈ 7× revenue / ~25× adjusted EBITDA. Logged as a deep-dive.

---

**You:** Adjusted EBITDA 501.5 − 109.6 capex − 45.3 interest − 56.4 taxes = 290.2, but you said FCF is 171.5 — where did the remaining 118.7M go?

**Instructor:** Great catch — "Adjusted EBITDA − capex − interest − tax" is *not* FCF because it ignores working capital. The ~$118.7M ≈ **$106M of working capital** + ~$12.7M other timing. The WC drag: growing receivables −$48.0M, deferred sales commissions paid upfront −$43.9M (a SaaS hallmark), a cash earnout payment −$20.9M. Lesson: working capital is a hidden, *recurring* cash drain for growing companies; FCF captures it, adjusted EBITDA doesn't. Logged.

---

**You:** (1) You added accrual interest ($40.6) and tax ($19.5) to build EBITDA but subtracted cash interest ($45.3) and cash tax ($56.4) for FCF — why? (2) Is there a breakdown of the $109.6M capex?

**Instructor:** (1) **EBITDA is an accrual metric** (un-does the income statement) → uses accrual interest/tax; **FCF is a cash metric** → uses cash actually paid. They differ because accrual ≠ cash — and the tax gap is the big one: **book tax expense $19.5M vs cash tax paid $56.4M**, driven by a $34.1M non-cash *deferred tax benefit*. "Tax expense" ≠ "taxes paid." (2) Capex = PP&E $14.3M (13%) + **software & technology $95.3M (87%) = capitalized software development** — engineering recorded as an asset, not expensed, then amortized (feeding D&A). Total tech investment ≈ $223.8M expensed + $95.3M capitalized ≈ $319M; the split is an accounting judgment and a QoE red-flag. Logged both.

---

**You:** Please make sure this entire Dayforce example is part of the notes as it is very instructive.

**Instructor:** Confirmed it was all captured, then **consolidated the three fragments into one polished nine-section deep-dive** in the notes (the statement → COGS → SG&A → where the chain breaks → the $18M→$501M chasm → Adj EBITDA→FCF reconciliation → capex breakdown → accrual vs cash → LBO/QoE payoff + six takeaways).

---

**You:** Can you explain why SBC and one-offs are added to get adjusted EBITDA? What do one-offs typically contain? How large can they get?

**Instructor:** *(Verified Dayforce's add-back detail and WeWork's filing.)* Unifying logic: every add-back argues a cost shouldn't count against sustainable earnings, passing a non-cash / non-recurring / non-operating test — but the *seller writes the definition*. **SBC:** non-cash (the case for), but a real cost via dilution and utterly recurring (the case against; Buffett's line). PE wrinkle: the public RSU program genuinely goes away in a take-private, replaced by a MIP. **One-offs:** the multiple effect ($10M one-off × 10× = $100M of value); Dayforce's list (restructuring, severance, pension termination, FX, earnout fair-value); the danger zone = pro-forma "run-rate synergies." **How large:** Dayforce's $213.5M of add-backs = a 74% uplift (SBC alone 54%); the legendary extreme = **WeWork's "Community Adjusted EBITDA"** turning a $(933)M loss into $233M "profit" by adding back marketing and G&A. Gave the defensibility spectrum. Punchline: every $1 of add-back × the multiple = purchase price, which is why buyers pay Big-4 to interrogate each one → Quality of Earnings. Logged as a deep-dive.

---

**You:** go ahead *(start Module 2)*

**Instructor:** ### Module 2, Lesson 2.1 — Anatomy of the Deal Process
**Part 1 — the stages.** A deal is a **funnel** (narrows the field + deepens commitment). Origination: auction (intermediated) vs proprietary (off-market). Stages: sourcing → teaser + NDA → Round 1 (CIM → IOI) → Round 2 (management presentations → LOI + exclusivity) → confirmatory diligence + financing + SPA negotiation → signing → closing → post-close. Key pattern: commitment escalates from non-binding (teaser, IOI, LOI) to binding (SPA); cheap steps first, expensive steps last.
[Diagram: six-stage timeline, non-binding → binding, field narrows from many bidders to one.]
**Practice:** order NDA/CIM/IOI/LOI/SPA and name the first binding commitment.

---

**You:** NDA, CIM, IOI, LOI, SPA

**Instructor:** Correct order; the **SPA is the first (and only) binding commitment to buy.**

**Part 2 — workstreams & responsibilities.** Diligence runs many workstreams *in parallel* (commercial, financial/QoE, legal, tax, operational, financing), all feeding the model + investment thesis to **confirm or kill** it.
[Diagram: six parallel workstreams → deal team model + IC memo → Investment Committee.]
Roles: Associate (builds the model), VP/Principal (quarterback), Partner/MD (sources, negotiates, faces the IC); the **IC** approves at key gates. Third parties get lesson 2.4.

---

**You:** (a) Associate (b) Partner (c) the accounting firm

**Instructor:** All three correct (model / negotiation + IC / Quality-of-Earnings).

### Lesson 2.2 — Deal Documents
Each document solves a trust-and-commitment problem. **Part 1 (pre-binding):** Teaser (anonymous, attract buyers) → NDA (unlock info; non-solicit + standstill) → CIM (the *sales document* — read projections as claims to test) → IOI (non-binding price range) → LOI (specific price + binding exclusivity) → IC memo (internal case).
**Practice:** (1) posture toward CIM projections + why; (2) which part of an LOI binds.

---

**You:** (1) CIM is a sales document, every business looks wonderful but it's claims to be tested; skepticism because the bank's pay depends on a high price. (2) Price is non-binding, exclusivity is; buyer gets sole access, seller gets the buyer's commitment to spend real diligence money.

**Instructor:** Both excellent and complete.

**Part 2 (binding + closing).** The **SPA** — five components: (1) price + adjustment (EV agreed, equity value trued-up for net debt & working capital at closing; locked box vs completion accounts); (2) reps & warranties (statements of fact); (3) covenants (behavior; interim "ordinary course"); (4) conditions to closing (regulatory, no MAC, reps hold); (5) indemnification (caps/baskets; R&W insurance). SPA vs APA flag. Then financing docs (commitment letter → credit agreement), the TSA (carve-outs), and funds flow (the closing money map = Sources & Uses made real).
[Diagram: signing → the gap (conditions must be met) → closing (funds flow, transfer).]
**Practice:** (1) EV $500M, closing net debt $120M, WC $10M below target → equity to seller; (2) rep vs covenant.

---

**You:** (1) $370M (2) *(defined reps as statements of fact and covenants as promises about behavior)*

**Instructor:** Both right; crystallized: a rep is a statement of *fact*; a covenant is a promise about *future behavior*. Break a rep = you were misled; break a covenant = a promise was broken.

### Lesson 2.3 — Key Terms and Points of Negotiation
Master frame: every term is a buyer-vs-seller tug-of-war; the headline price is only one lever. **Part 1 (price):** headline multiple (+ which EBITDA); form of consideration (earnout bridges a valuation gap; rollover aligns incentives); the price mechanism / working-capital peg (the hidden price fight — without a peg the seller can "starve" the business).
[Diagram: $500M EV − net debt − WC = $370M equity, then − rollover − escrow − earnout = $250M cash the seller pockets at close.]
**Practice:** which tool bridges a $60M valuation gap?

---

**You:** Earnout — part of the price contingent on hitting future targets.

**Instructor:** Exactly — it lets each side "be right," deferring the argument to reality. **Part 2 (risk):** reps scope (broad vs narrow, qualifiers); the indemnification package (cap, basket/deductible, survival, escrow); R&W insurance; and deal certainty (MAC clause, financing out, reverse break fee, and the certainty-vs-price tradeoff).
[Diagram: indemnification zones — below the $5M basket the buyer bears it; between basket and the $50M cap it's recoverable (escrow-funded); above the cap the buyer bears it.]
**Practice:** claims of $3M / $40M / $70M against a $5M true-deductible basket and $50M cap.

---

**You:** (a) 0 because of $5M deductible (b) $40m (c) $50M

**Instructor:** (a) $0 ✓ and (c) $50M ✓ (cap binds); **(b) should be $35M** — a *true deductible* subtracts $5M from every recoverable claim ($40M − $5M). Your $40M is correct for a *tipping basket* (recover from dollar one) — a real alternative, which is why the basket type gets negotiated.

### Lesson 2.4 — The Role of Third Parties
A lean PE team *rents* expertise for three reasons: expertise it lacks, capacity, and independent credibility. The cast (mapping to the workstreams): investment bank, lawyers, accountants (QoE + tax), consultants (commercial DD), lenders, specialists.
[Diagram: lean PE deal team at center surrounded by its advisors.]
Sell-side/buy-side mirror; advisors are expensive → engaged heavily only after exclusivity. **→ Module 2 complete.**

---

**You:** *(after a brief detour re-confirming the Dayforce material was fully in the notes, which the Instructor consolidated)* go ahead *(start Module 3)*

**Instructor:** ### Module 3, Lesson 3.1 — Leveraged Finance, Private Credit & Capital Structures
**Part 1 — the two markets.** The core distinction: **originate-to-distribute** (Broadly Syndicated Loans — a bank arranges then sells to hundreds of CLOs/funds; the loan trades) vs **originate-to-hold** (Private Credit / Direct Lending — a fund lends and keeps it; one lender, no trading). Everything (price, speed, certainty, flexibility, workout) flows from that. Private credit costs ~100–150 bps more but offers certainty of close, speed, flexibility for messy stories, and one-phone-call workouts. **Unitranche** collapses the stack into one loan at one blended rate. Current state (verified): direct lending now matches BSL at $1.5–2T, forecast $3T by 2028; both markets grew (not zero-sum); traffic runs both ways; the markets are converging (JPMorgan's $50B direct-lending push).
**Practice:** which market for a $400M carve-out with messy financials, needing certainty and speed?

---

**You:** Direct lender — will underwrite messy financials CLOs won't touch; BSL is slower and subject to change if the bank can't sell. Also: explain "SOFR plus 4.75%" and "BSL spreads tightened to their lowest since 2008."

**Instructor:** Both reasons spot on. **Part 2 — how a loan is priced.** Rate = benchmark + spread. **SOFR** (Secured Overnight Financing Rate, ~3.63% as of July 2026) = the risk-free benchmark set by Fed policy, *nobody negotiates it*, replaced LIBOR. **Spread** = the credit premium, negotiated, fixed for life, quoted in basis points. "S+475" = SOFR + 4.75% → all-in ~8.38%. Only the spread is fixed; **SOFR floats**, so a Fed hike auto-raises your rate (the 1.7 floating-rate risk, exact mechanism). SOFR floor + OID explained. **"Spreads tightened to lowest since 2008"** = the credit premium shrank to its most borrower-friendly level in ~17 years — driven by supply/demand (record CLO formation + shrinking LBO supply → lenders compete on price), *not* credit quality. Key insight: the all-in rate has two independently-moving parts — "spreads lowest since 2008" doesn't mean debt is cheap, because SOFR is still 3.63% (~8.4% all-in vs ~4% in 2021). Always ask: benchmark story or spread story?

---

**You:** (1) 7.63%, 45.78M (2) 1% SOFR floor → S+400 = 5% (3) 57.78M, coverage 2.62× → 2.076×

**Instructor:** All three perfect — including the floor logic. Highlighted: in (3), coverage fell 2.62× → 2.08× (a 20% deterioration) with EBITDA unchanged — the 2022–23 squeeze in miniature.

### Lesson 3.2 — Quality of Earnings & Net Working Capital
**Part 1 — QoE.** Not an audit (compliance) — it asks "how much of this EBITDA is real, sustainable, repeatable?" Central output = the EBITDA bridge (reported → adjusted → pro-forma). **Key insight: QoE is bidirectional** — buy-side hunts *negative* adjustments sellers never volunteer (understated owner salary, missing standalone costs, one-time benefits left in, deferred maintenance, revenue pulled forward). Signature technique: "proof of cash." Sell-side QoE exists but is seller-paid.
**Practice:** a $20M-EBITDA business — adjust for founder salary, one-time legal, non-repeating order, serial "restructuring."

---

**You:** (a) −400k (b) +1.5M (c) −2M (d) −1M; 10× × −1.9 = −19M

**Instructor:** All four directional calls correct; adjusted EBITDA $18.1M → price $200M becomes $181M (~10% found). Pulled out that 3 of 4 moved *down* (the typical shape), and (d) is *removing the seller's add-back*, not removing a cost.

**Part 2 — Net Working Capital.** NWC = (Receivables + Inventory) − Payables — cash *permanently trapped* running the business. Killer property: **NWC grows with the business** (growth eats cash — you discovered this on Dayforce). Why PE cares: it's a real cash outflow in the model, and it's the **peg** in the deal (a trailing-12-month "normal"; actual above → price up, below → price down; every dollar of the peg is a dollar of price). The nastiest fight: "is that debt or working capital?" (accrued bonuses, deferred revenue, unpaid capex, earnouts — reclassifying as debt-like cuts the price).
**Practice:** peg $25M, actual $19M (seller drained receivables/inventory).

---

**You:** (1) price increases by 6M (2) reducing WC to overstate free cash flow / understate risk (3) less cash to service debt, so they overpaid

**Instructor:** Q3 right, Q2 close; **Q1 backwards — the price goes DOWN by $6M.** The business arrives $6M short of the fuel it needs, so the buyer (who'll inject that cash) pays less. Analogy: buying a car that should come with a full tank — if the seller siphons the gas, you pay less. Rule: actual below target → price down; above → up. On Q2, the sharper point: the seller converts WC into cash and keeps it (cash-free/debt-free), and the peg doesn't *prevent* it — it makes it *pointless* (strip $6M, price drops $6M, seller nets zero).

---

**You:** price up by 6M, because that's 6M above the normal the business needs; the buyer does not need to inject their own cash

**Instructor:** Exactly right — and the second half: the seller *funded* that extra $6M, so reimbursing them is paying for an asset you're receiving. Direction locked: short of the peg → price down; over → up.

---

**Instructor:** ### Lesson 3.3 — Purchase Price Allocation
**Part 1.** PPA answers "what did I actually buy?" The rule that changes everything: you record acquired assets at **fair value, not the seller's book value** (purchase accounting). Three steps: total price → value every identifiable asset/liability at fair value → the leftover is **goodwill** (the plug). Key asymmetry: **internally developed** intangibles (brand, customer relationships) can't be capitalized, but **acquired** ones must be — so PPA *creates* assets that were invisible on the seller's books. Worked example ($500M for a company with $50M book net assets → $320M of created intangibles + $130M goodwill). Identifiable intangibles amortize (finite lives); goodwill isn't amortized (tested for impairment).
**Practice:** $300M manufacturer — compute goodwill; which assets amortize; is $0 vs $25M trade name a contradiction?

---

**You:** (1) 300-250 = 50M (2) customer relationships, trade name, technology amortize, not goodwill (3) seller can't capitalize their own trade name, buyer must record it at fair value — it's what they're paying for.

**Instructor:** All correct; the #3 asymmetry is one of accounting's most counterintuitive points. Surfaced where the $120M tangible net assets came from (a $40M fair-value step-up over $80M book equity).

**Part 2 — closing the Dayforce loop.** Every identifiable intangible amortizes → new D&A that didn't exist before the deal (the $300M manufacturer creates ~$13.7M/yr). **This is the Dayforce puzzle solved:** Ceridian/Dayforce grew by acquisition, each acquisition ran through PPA creating customer-relationship/technology intangibles, whose amortization is the bulk of the ~$129M "scattered through G&A" that crushed net income to $18M — *precisely why* the market values these on EBITDA. Deep truth: acquired-intangible amortization makes serial acquirers' GAAP earnings look terrible even when healthy (the strongest legitimate case for EBITDA). PE kicker: a brand-new PPA happens on *your* LBO, resetting intangibles at your premium price.
**Practice:** $800M deal — goodwill; intangible amortization; EBIT vs why the PE owner ignores it.

---

**You:** (1) 800-650 = 150M (2) CR $25M/yr, Tech $20M/yr (3) 120 − (40+25+20) = 35M; a new PPA happens on every acquisition creating a bigger intangible/goodwill stack.

**Instructor:** All correct. Sharpened the punchline: $120M EBITDA but only $35M EBIT — a third — almost entirely non-cash acquired-intangible amortization; debt is serviced from *cash*, far closer to $120M. That $85M wedge is the same one that made Dayforce look barely profitable.

### Lesson 3.4 — Asset vs Stock Sales & 338(h)(10)
**Part 1.** Two ways to buy: **stock** (buy the equity — get all assets *and* all liabilities, known and unknown) vs **asset** (buy selected assets + chosen liabilities; leave the rest behind). Buyer prefers asset deals for two reasons: (1) clean liability shield; (2) the **step-up** — record assets at the higher purchase price for *tax*, then amortize/depreciate for years of real cash tax savings (worth 10%+ of price).
**Practice:** step-up $400M over 15yr at 25% — deduction, saving; two reasons; why the seller might refuse.

---

**You:** (1) 400/15 = 26.7M, 6.7M/yr (2) more predictable + PPA step-up tax savings (3) buyer cherry-picks so seller keeps the bad stuff.

**Instructor:** Q1 perfect. Refined Q2: the first reason is specifically the **liability shield** (predictability is a consequence). Q3 has a piece, but the *main* reason is **double taxation** →

**Part 2.** A stock sale is taxed **once** (shareholder cap-gains). A C-corp asset sale is taxed **twice** — corporate tax on the gain (the very step-up the buyer loves *triggers* it), then shareholder tax on the distribution — often a 10–20 point swing in proceeds. So the buyer's benefit and the seller's cost are two sides of the same coin. **The 338(h)(10) election:** do the deal *legally as stock* but *taxed as an asset sale* (buyer gets the step-up). It triggers the seller's double tax anyway — so the buyer **grosses up the price** to share the step-up value, and both beat a plain stock sale *when the buyer's benefit exceeds the seller's extra tax*. Requires an S-corp or consolidated subsidiary (cousin: 336(e)).
**Practice:** buyer step-up worth $70M, seller's extra tax $45M.

---

**You:** (1) Yes — buyer's step-up exceeds the seller's extra tax, so gross up (2) covers the seller's extra tax while leaving a gain for the buyer (3) Yes — a $30M step-up doesn't cover the seller's extra tax.

**Instructor:** Q1 and Q3 correct; put numbers on Q2: **the gross-up range is $45M–$70M** (seller needs ≥$45M, buyer affords ≤$70M) → **$25M of surplus** the election *creates*, to be split. Q3: with a $30M benefit vs $45M cost there's no overlap (−$15M surplus) → done as a plain stock sale, step-up left on the table.

### Lesson 3.5 — Structure → Seller Proceeds & Sponsor Returns *(Module 3 capstone)*
Traced one deal: QoE-adjusted EBITDA sets the entry price ($52M marketed → $50M defensible → $20M of price); the NWC peg adjusts at closing (−$4M); leverage splits the check ($250M debt + $246M equity); the step-up boosts cash flow (~$5M/yr). Landed on the two numbers: the **seller nets** ~$465M (dreamed of $520M — every dollar of the gap a specific lever), and the **sponsor's IRR** (~2.15× / ~17%). Capstone insight: each lever moves the IRR. **→ Module 3 complete.**
**Practice:** a full capstone case ($60M marketed EBITDA @ 10×).

---

**You:** (1) 52M, 520M (2) 514M (3) 260M debt + 260M equity (4) QoE, 8×10 = 80M

**Instructor:** Q1, Q2, Q4 correct; **Q3 equity is $254M, not $260M** — equity is the *plug* off the *final* $514M price ($514 − $260 debt), so the $6M NWC haircut comes straight out of the equity check. Nice insight: since debt is fixed, every dollar off the price is a dollar less equity → nudges IRR up.

---

**You:** module 4 and build model in a spreadsheet — I'm trying to connect Google Drive via connector but can't, can you check why?

**Instructor:** Noted we don't need Drive to build the model (I can create the .xlsx here and give a download link). On the connector: I can't inspect your account state directly, but pulled the official troubleshooting. *(Then you set that aside.)*

---

**You:** Never mind, can we add the entire conversation into a running doc — I'd like to read the whole conversation, in addition to the notes.

**Instructor:** Built this transcript (`pe_course_transcript.md`) — a faithful reconstruction of the full dialogue, since the raw transcript wasn't mounted.

---

*End of transcript through the start of Module 4. Future turns will be appended here as the conversation continues.*

---

**You:** *(shared a WSJ article)* I think this article is apropos — "Private-Equity Assets Stuck in 'Zombie Funds' Are at a Record High" (July 21, 2026).

**Instructor:** Agreed — it's the exit drought quantified. The scale: NAV in US funds 10+ years old hit an all-time high of **$348.5B** (3.5× 2015, >100× 2005), with **$512.7B** more in the 7–9-year bucket behind it, and **$3.91T = 74%** of North American PE assets sitting unrealized. Mapped it onto prior lessons: it's **the J-curve that never completes** (the harvest period never arrived — and the fee misalignment from 1.2 is exactly what enrages LPs); it's **TVPI/RVPI skepticism vindicated at industry scale** (74% unrealized = GP marks, not cash — the same instinct that flagged Silver Lake IV); and the cause is **pure Module 3.1** — funds bought at the 2020–21 near-zero-rate peak can't clear today's bid because coverage math at ~8.4% all-in won't support 2021 multiples, and selling below the mark crystallizes the loss. Two refinements: (1) **continuation vehicles are mostly NOT for zombie funds** — secondary buyers avoid impaired assets, so secondaries are a valve for *good* assets in *stuck* funds; (2) apply **QoE skepticism to the sponsor quotes** ("we hold longer for deep value creation") — the party with the incentive supplies the narrative; the testable version cites a frozen M&A market and a stated 3–4 year target hold. Logged as the real-world anchor for Module 6 and as a warning that "5-year hold, exit at entry multiple" are the two most fragile inputs in an LBO model.
