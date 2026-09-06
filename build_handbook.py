#!/usr/bin/env python3
"""
build_handbook.py  —  Regenerate the Private Equity Course Handbook (HTML + PDF).

WHAT IT DOES
  1. Reads pe_course_notes.md (the living course notes).
  2. Inserts the rebuilt SVG diagrams after their lesson headings.
  3. Converts Markdown -> styled, print-ready HTML  ->  pe_course_handbook.html
  4. Renders that HTML to  pe_course_handbook.pdf  via headless Chromium (Playwright).

HOW TO RUN
  cd /mnt/user-data/outputs && python3 build_handbook.py

HOW TO EXTEND (Module 4 and beyond)
  * Add a diagram:  put a new entry in FIG  ->  'key': (caption, svg_string)
                    - use the class names below so it inherits the print palette:
                      .c-teal / .c-amber / .c-purple / .c-coral / .c-gray on a <g>,
                      text classes .th (title) / .ts (small), lines .arr / .leader.
                    - do NOT use var(--...) refs; use hex directly.
  * Show it:        add the lesson's EXACT notes heading to PLACE  ->  ['key', ...]
                    (run once; the script prints any PLACE heading it could not find,
                     which usually means the heading text drifted — fix the key.)
  * New modules just work:  '# MODULE 4 ...' H1s in the notes automatically start a
     new page and pick up the styling. Only diagrams need the FIG/PLACE additions.

REQUIREMENTS (all preinstalled in this environment): python-markdown, playwright (+chromium).
"""

import pathlib
import base64
import markdown

NOTES = "pe_course_notes.md"
OUT_HTML = "pe_course_handbook.html"
OUT_PDF = "pe_course_handbook.pdf"

# ============================================================================
# DIAGRAMS  —  key: (caption, svg).  Add new ones at the bottom of this dict.
# ============================================================================
FIG = {}

FIG['gp_lp'] = ('Private equity fund structure', '''<svg viewBox="0 0 680 420" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<g class="c-teal"><rect x="120" y="40" width="300" height="56" rx="8"/><text class="th" x="270" y="64" text-anchor="middle">Limited partners (LPs)</text><text class="ts" x="270" y="82" text-anchor="middle">Pensions, endowments, funds</text></g>
<line x1="270" y1="96" x2="270" y2="168" class="arr" marker-end="url(#a1)"/><text class="ts" x="285" y="134">~95% capital</text>
<g class="c-purple"><rect x="120" y="170" width="300" height="56" rx="8"/><text class="th" x="270" y="194" text-anchor="middle">The fund</text><text class="ts" x="270" y="212" text-anchor="middle">A limited partnership</text></g>
<g class="c-coral"><rect x="450" y="170" width="180" height="56" rx="8"/><text class="th" x="540" y="194" text-anchor="middle">GP / the firm</text><text class="ts" x="540" y="212" text-anchor="middle">Runs &amp; invests ~2%</text></g>
<line x1="450" y1="198" x2="422" y2="198" class="arr" marker-end="url(#a1)"/>
<line x1="270" y1="226" x2="158" y2="318" class="arr" marker-end="url(#a1)"/><line x1="270" y1="226" x2="340" y2="318" class="arr" marker-end="url(#a1)"/><line x1="270" y1="226" x2="522" y2="318" class="arr" marker-end="url(#a1)"/><text class="ts" x="210" y="262">buys equity</text>
<g class="c-gray"><rect x="80" y="320" width="150" height="48" rx="8"/><text class="th" x="155" y="344" text-anchor="middle">Company A</text></g>
<g class="c-gray"><rect x="265" y="320" width="150" height="48" rx="8"/><text class="th" x="340" y="344" text-anchor="middle">Company B</text></g>
<g class="c-gray"><rect x="450" y="320" width="150" height="48" rx="8"/><text class="th" x="525" y="344" text-anchor="middle">Company C</text></g>
<text class="ts" x="340" y="392" text-anchor="middle">Portfolio companies — profits flow back up the same path</text></svg>''')

FIG['jcurve'] = ('The J-curve, with real Clearlake funds', '''<svg viewBox="0 0 680 400" xmlns="http://www.w3.org/2000/svg">
<text class="ts" x="92" y="44">Cumulative cash returned to LPs</text>
<line x1="92" y1="60" x2="92" y2="330" stroke="#D8D7D2" stroke-width="1"/><line x1="92" y1="330" x2="624" y2="330" stroke="#D8D7D2" stroke-width="1"/>
<line x1="92" y1="205" x2="624" y2="205" class="leader"/><text class="ts" x="110" y="197">break-even — invested capital fully returned</text>
<path d="M92 205 C150 275, 195 300, 235 300 C320 300, 370 258, 405 205 C460 122, 545 96, 612 88" fill="none" stroke="#888780" stroke-width="2"/>
<circle cx="235" cy="300" r="5" fill="#D85A30"/><text class="ts" x="248" y="306">Clearlake VII · 2022 · trough</text>
<circle cx="405" cy="205" r="5" fill="#BA7517"/><text class="ts" x="352" y="186">Clearlake V · 2018</text>
<circle cx="612" cy="88" r="5" fill="#1D9E75"/><text class="ts" x="600" y="80" text-anchor="end">Clearlake III · 2012</text>
<text class="ts" x="358" y="352" text-anchor="middle">Years since the fund's first investment &#8594;</text></svg>''')

FIG['spectrum'] = ('The private-capital risk / return spectrum', '''<svg viewBox="0 0 680 240" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text class="th" x="340" y="26" text-anchor="middle">The private-capital risk / return spectrum</text>
<g class="c-teal"><rect x="46" y="50" width="88" height="62" rx="8"/><text class="th" x="90" y="74" text-anchor="middle">Credit</text><text class="ts" x="90" y="94" text-anchor="middle">lending</text></g>
<g class="c-amber"><rect x="146" y="50" width="88" height="62" rx="8"/><text class="th" x="190" y="74" text-anchor="middle">Infra</text><text class="ts" x="190" y="94" text-anchor="middle">long-life</text></g>
<g class="c-amber"><rect x="246" y="50" width="88" height="62" rx="8"/><text class="th" x="290" y="74" text-anchor="middle">Real estate</text><text class="ts" x="290" y="94" text-anchor="middle">property</text></g>
<g class="c-purple"><rect x="346" y="50" width="88" height="62" rx="8"/><text class="th" x="390" y="74" text-anchor="middle">Buyout</text><text class="ts" x="390" y="94" text-anchor="middle">leveraged</text></g>
<g class="c-purple"><rect x="446" y="50" width="88" height="62" rx="8"/><text class="th" x="490" y="74" text-anchor="middle">Growth</text><text class="ts" x="490" y="94" text-anchor="middle">scaling</text></g>
<g class="c-purple"><rect x="546" y="50" width="88" height="62" rx="8"/><text class="th" x="590" y="74" text-anchor="middle">Venture</text><text class="ts" x="590" y="94" text-anchor="middle">startups</text></g>
<line x1="46" y1="134" x2="634" y2="134" class="arr" marker-end="url(#a2)"/>
<text class="ts" x="46" y="150">lower risk &amp; return · paid first (debt)</text><text class="ts" x="634" y="150" text-anchor="end">higher risk &amp; return · paid last (equity)</text>
<g class="c-gray"><rect x="46" y="176" width="588" height="48" rx="8"/><text class="th" x="340" y="196" text-anchor="middle">Hedge funds — the structural outlier</text><text class="ts" x="340" y="214" text-anchor="middle">liquid · public markets · open-ended (no 10-year drawdown)</text></g></svg>''')

FIG['buildup'] = ('Buy-and-build: the multiple-arbitrage engine', '''<svg viewBox="0 0 680 270" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text class="th" x="340" y="26" text-anchor="middle">Buy-and-build: the multiple-arbitrage engine</text>
<g class="c-purple"><rect x="40" y="55" width="200" height="64" rx="8"/><text class="th" x="140" y="74" text-anchor="middle">Platform company</text><text class="ts" x="140" y="92" text-anchor="middle">$20M EBITDA &#215; 8&#215;</text><text class="ts" x="140" y="108" text-anchor="middle">= $160M EV</text></g>
<g class="c-teal"><rect x="40" y="145" width="200" height="64" rx="8"/><text class="th" x="140" y="164" text-anchor="middle">+ 5 bolt-on add-ons</text><text class="ts" x="140" y="182" text-anchor="middle">$15M EBITDA &#215; 5&#215;</text><text class="ts" x="140" y="198" text-anchor="middle">= $75M cost</text></g>
<line x1="240" y1="87" x2="428" y2="120" class="arr" marker-end="url(#a3)"/><line x1="240" y1="177" x2="428" y2="144" class="arr" marker-end="url(#a3)"/><text class="ts" x="334" y="104" text-anchor="middle">5&#215; &#8594; 10&#215;</text>
<g class="c-amber"><rect x="430" y="100" width="210" height="64" rx="8"/><text class="th" x="535" y="119" text-anchor="middle">Combined at exit</text><text class="ts" x="535" y="137" text-anchor="middle">$35M EBITDA &#215; 10&#215;</text><text class="ts" x="535" y="153" text-anchor="middle">= $350M EV</text></g>
<text class="th" x="340" y="228" text-anchor="middle">Exit $350M &#8722; cost $235M &#8776; $115M created</text>
<text class="ts" x="340" y="248" text-anchor="middle">&#8230;before any organic growth or debt paydown — purely from the re-rating</text></svg>''')

FIG['lbo_bridge'] = ('LBO value bridge (illustrative)', '''<svg viewBox="0 0 680 368" xmlns="http://www.w3.org/2000/svg">
<text class="th" x="340" y="26" text-anchor="middle">LBO value bridge (illustrative)</text>
<g class="c-teal"><rect x="70" y="214" width="90" height="86" rx="4"/></g><text class="th" x="115" y="206" text-anchor="middle">$500M</text>
<line x1="160" y1="214" x2="210" y2="214" class="leader"/>
<g class="c-amber"><rect x="210" y="129" width="90" height="85" rx="4"/><text class="th" x="255" y="171" text-anchor="middle">+$500M</text></g>
<line x1="300" y1="129" x2="350" y2="129" class="leader"/>
<g class="c-purple"><rect x="350" y="94" width="90" height="35" rx="4"/><text class="ts" x="395" y="111" text-anchor="middle">+$200M</text></g>
<line x1="440" y1="94" x2="490" y2="94" class="leader"/>
<g class="c-teal"><rect x="490" y="94" width="90" height="206" rx="4"/></g><text class="th" x="535" y="86" text-anchor="middle">$1,200M</text>
<line x1="60" y1="300" x2="600" y2="300" stroke="#D8D7D2" stroke-width="1"/>
<text class="th" x="115" y="314" text-anchor="middle">Entry</text><text class="ts" x="115" y="329" text-anchor="middle">equity</text>
<text class="th" x="255" y="314" text-anchor="middle">EBITDA</text><text class="ts" x="255" y="329" text-anchor="middle">growth</text>
<text class="th" x="395" y="314" text-anchor="middle">Debt</text><text class="ts" x="395" y="329" text-anchor="middle">paydown</text>
<text class="th" x="535" y="314" text-anchor="middle">Exit</text><text class="ts" x="535" y="329" text-anchor="middle">equity</text>
<text class="ts" x="340" y="354" text-anchor="middle">MOIC 2.4&#215; · IRR &#8776;19% over 5 yrs · exit multiple held flat at 10&#215;</text></svg>''')

FIG['debt_stack'] = ('The LBO debt stack (capital structure)', '''<svg viewBox="0 0 680 320" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="dwn" viewBox="0 0 10 10" refX="5" refY="8" markerWidth="6" markerHeight="6" orient="auto"><path d="M1 2L5 8L9 2" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text class="th" x="340" y="26" text-anchor="middle">The LBO debt stack (capital structure)</text>
<line x1="150" y1="52" x2="150" y2="292" stroke="#888780" stroke-width="1.5" marker-end="url(#dwn)"/>
<text class="ts" x="140" y="58" text-anchor="end">paid first</text><text class="ts" x="140" y="72" text-anchor="end">· secured ·</text><text class="ts" x="140" y="270" text-anchor="end">paid last</text><text class="ts" x="140" y="284" text-anchor="end">· first loss ·</text>
<line x1="510" y1="52" x2="510" y2="292" stroke="#888780" stroke-width="1.5" marker-end="url(#dwn)"/>
<text class="ts" x="520" y="58">lower cost</text><text class="ts" x="520" y="284">higher cost</text>
<g class="c-teal"><rect x="180" y="50" width="300" height="42" rx="4"/><text class="th" x="330" y="64" text-anchor="middle">Senior secured (1st lien)</text><text class="ts" x="330" y="80" text-anchor="middle">revolver + term loan B</text></g>
<g class="c-teal"><rect x="180" y="100" width="300" height="42" rx="4"/><text class="th" x="330" y="121" text-anchor="middle">Second lien</text></g>
<g class="c-amber"><rect x="180" y="150" width="300" height="42" rx="4"/><text class="th" x="330" y="171" text-anchor="middle">Senior unsecured / high-yield</text></g>
<g class="c-amber"><rect x="180" y="200" width="300" height="42" rx="4"/><text class="th" x="330" y="214" text-anchor="middle">Subordinated / mezzanine</text><text class="ts" x="330" y="230" text-anchor="middle">PIK · warrants</text></g>
<g class="c-purple"><rect x="180" y="250" width="300" height="42" rx="4"/><text class="th" x="330" y="264" text-anchor="middle">Equity (sponsor)</text><text class="ts" x="330" y="280" text-anchor="middle">first loss · uncapped upside</text></g></svg>''')

FIG['ebitda'] = ('Building EBITDA from net income', '''<svg viewBox="0 0 680 325" xmlns="http://www.w3.org/2000/svg">
<text class="th" x="340" y="24" text-anchor="middle">EBITDA = net income + the four things it adds back</text>
<g class="c-teal"><rect x="180" y="186" width="130" height="104" stroke-width="1"/><text class="th" x="245" y="238" text-anchor="middle">Net income</text></g><text class="ts" x="325" y="238">$45M — what's left after everything</text>
<g class="c-amber"><rect x="180" y="152" width="130" height="34" stroke-width="1"/></g><text class="ts" x="245" y="169" text-anchor="middle">+ Taxes</text><text class="ts" x="325" y="169">+$15M  (the "T")</text>
<g class="c-amber"><rect x="180" y="106" width="130" height="46" stroke-width="1"/></g><text class="ts" x="245" y="129" text-anchor="middle">+ Interest</text><text class="ts" x="325" y="129">+$20M  (the "I")</text>
<g class="c-amber"><rect x="180" y="60" width="130" height="46" stroke-width="1"/></g><text class="ts" x="245" y="83" text-anchor="middle">+ Deprec. &amp; amort.</text><text class="ts" x="325" y="83">+$20M  (the "D" &amp; "A")</text>
<line x1="170" y1="60" x2="170" y2="290" stroke="#888780" stroke-width="1"/><text class="th" x="245" y="48" text-anchor="middle">= EBITDA $100M</text>
<text class="ts" x="340" y="308" text-anchor="middle">Strips out financing (I), taxes (T) &amp; non-cash charges (D, A) to show core operating profit</text></svg>''')

FIG['dcf_comp'] = ('Valuing a company by comparable multiples', '''<svg viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg">
<text class="th" x="245" y="24" text-anchor="middle">Comparable EV/EBITDA multiples</text>
<line x1="70" y1="250" x2="470" y2="250" stroke="#D8D7D2" stroke-width="1"/>
<g class="c-teal"><rect x="90" y="128" width="60" height="122"/></g><text class="ts" x="120" y="120" text-anchor="middle">9.0&#215;</text><text class="ts" x="120" y="264" text-anchor="middle">Comp A</text>
<g class="c-teal"><rect x="190" y="114" width="60" height="136"/></g><text class="ts" x="220" y="106" text-anchor="middle">10.0&#215;</text><text class="ts" x="220" y="264" text-anchor="middle">Comp B</text>
<g class="c-teal"><rect x="290" y="101" width="60" height="149"/></g><text class="ts" x="320" y="93" text-anchor="middle">11.0&#215;</text><text class="ts" x="320" y="264" text-anchor="middle">Comp C</text>
<g class="c-teal"><rect x="390" y="87" width="60" height="163"/></g><text class="ts" x="420" y="79" text-anchor="middle">12.0&#215;</text><text class="ts" x="420" y="264" text-anchor="middle">Comp D</text>
<line x1="70" y1="107" x2="470" y2="107" class="leader"/><text class="ts" x="76" y="99">median 10.5&#215;</text>
<g class="c-amber"><rect x="500" y="90" width="160" height="120" rx="8"/><text class="th" x="580" y="112" text-anchor="middle">Apply to target</text><text class="ts" x="580" y="134" text-anchor="middle">$100M EBITDA &#215; 10.5&#215;</text><text class="th" x="580" y="154" text-anchor="middle">= $1,050M EV</text><text class="ts" x="580" y="176" text-anchor="middle">&#8722; $200M net debt</text><text class="th" x="580" y="196" text-anchor="middle">= $850M equity</text></g></svg>''')

FIG['dayforce'] = ('$18M net income becomes $501M "Adjusted EBITDA" (Dayforce FY2024)', '''<svg viewBox="0 0 680 330" xmlns="http://www.w3.org/2000/svg">
<text class="th" x="340" y="22" text-anchor="middle">$18M net income &#8594; $501M "Adjusted EBITDA" (Dayforce, FY2024)</text>
<g class="c-teal"><rect x="74" y="282" width="64" height="8"/></g><text class="ts" x="106" y="274" text-anchor="middle">$18</text><text class="ts" x="106" y="305" text-anchor="middle">Net</text><text class="ts" x="106" y="318" text-anchor="middle">income</text>
<g class="c-amber"><rect x="152" y="255" width="64" height="27"/></g><text class="ts" x="184" y="247" text-anchor="middle">+$60</text><text class="ts" x="184" y="305" text-anchor="middle">+ int</text><text class="ts" x="184" y="318" text-anchor="middle">&amp; tax</text>
<g class="c-amber"><rect x="230" y="160" width="64" height="95"/></g><text class="ts" x="262" y="152" text-anchor="middle">+$210</text><text class="ts" x="262" y="311" text-anchor="middle">+ D&amp;A</text>
<g class="c-teal"><rect x="308" y="160" width="64" height="130"/></g><text class="th" x="340" y="152" text-anchor="middle">$288</text><text class="ts" x="340" y="311" text-anchor="middle">EBITDA</text>
<g class="c-amber"><rect x="386" y="89" width="64" height="71"/></g><text class="ts" x="418" y="81" text-anchor="middle">+$157</text><text class="ts" x="418" y="311" text-anchor="middle">+ SBC</text>
<g class="c-amber"><rect x="464" y="63" width="64" height="26"/></g><text class="ts" x="496" y="55" text-anchor="middle">+$57</text><text class="ts" x="496" y="305" text-anchor="middle">+ one-</text><text class="ts" x="496" y="318" text-anchor="middle">offs</text>
<g class="c-teal"><rect x="542" y="63" width="64" height="227"/></g><text class="th" x="574" y="55" text-anchor="middle">$501</text><text class="ts" x="574" y="305" text-anchor="middle">Adj.</text><text class="ts" x="574" y="318" text-anchor="middle">EBITDA</text></svg>''')

FIG['deal_stages'] = ('The buyout deal process — sourcing to close', '''<svg viewBox="0 0 680 230" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="ff" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text class="th" x="340" y="22" text-anchor="middle">The buyout deal process — sourcing to close</text>
<g class="c-teal"><rect x="40" y="46" width="90" height="56" rx="6"/><text class="th" x="85" y="66" text-anchor="middle">Sourcing</text><text class="ts" x="85" y="86" text-anchor="middle">find the deal</text></g>
<g class="c-teal"><rect x="142" y="46" width="90" height="56" rx="6"/><text class="th" x="187" y="66" text-anchor="middle">Teaser + NDA</text><text class="ts" x="187" y="86" text-anchor="middle">get access</text></g>
<g class="c-amber"><rect x="244" y="46" width="90" height="56" rx="6"/><text class="th" x="289" y="66" text-anchor="middle">Round 1</text><text class="ts" x="289" y="86" text-anchor="middle">CIM &#8594; IOI</text></g>
<g class="c-amber"><rect x="346" y="46" width="90" height="56" rx="6"/><text class="th" x="391" y="66" text-anchor="middle">Round 2</text><text class="ts" x="391" y="86" text-anchor="middle">mgmt &#8594; LOI</text></g>
<g class="c-purple"><rect x="448" y="46" width="90" height="56" rx="6"/><text class="th" x="493" y="66" text-anchor="middle">Diligence</text><text class="ts" x="493" y="86" text-anchor="middle">+ SPA</text></g>
<g class="c-purple"><rect x="550" y="46" width="90" height="56" rx="6"/><text class="th" x="595" y="66" text-anchor="middle">Sign &#8594; Close</text><text class="ts" x="595" y="86" text-anchor="middle">funds flow</text></g>
<line x1="130" y1="74" x2="142" y2="74" class="arr" marker-end="url(#ff)"/><line x1="232" y1="74" x2="244" y2="74" class="arr" marker-end="url(#ff)"/><line x1="334" y1="74" x2="346" y2="74" class="arr" marker-end="url(#ff)"/><line x1="436" y1="74" x2="448" y2="74" class="arr" marker-end="url(#ff)"/><line x1="538" y1="74" x2="550" y2="74" class="arr" marker-end="url(#ff)"/>
<line x1="40" y1="140" x2="640" y2="140" class="arr" marker-end="url(#ff)"/>
<text class="ts" x="40" y="128">non-binding (teaser, IOI, LOI)</text><text class="ts" x="640" y="128" text-anchor="end">binding (SPA)</text><text class="ts" x="40" y="158">escalating commitment &#8594;</text>
<text class="ts" x="340" y="188" text-anchor="middle">The field narrows at each gate: many interested bidders &#8594; one buyer</text></svg>''')

FIG['ev_cash'] = ('Headline price is not the cash the seller pockets', '''<svg viewBox="0 0 680 330" xmlns="http://www.w3.org/2000/svg">
<text class="th" x="340" y="22" text-anchor="middle">Headline price &#8800; cash the seller pockets</text>
<g class="c-teal"><rect x="70" y="60" width="64" height="230"/></g><text class="th" x="102" y="52" text-anchor="middle">$500M</text><text class="ts" x="102" y="304" text-anchor="middle">EV</text>
<g class="c-coral"><rect x="148" y="60" width="64" height="55"/></g><text class="ts" x="180" y="303" text-anchor="middle">&#8722; net debt</text><text class="ts" x="180" y="317" text-anchor="middle">$120M</text>
<g class="c-coral"><rect x="226" y="115" width="64" height="5"/></g><text class="ts" x="258" y="303" text-anchor="middle">&#8722; WC</text><text class="ts" x="258" y="317" text-anchor="middle">$10M</text>
<line x1="290" y1="120" x2="304" y2="120" class="leader"/><text class="ts" x="330" y="112">&#8592; equity value $370M</text>
<g class="c-coral"><rect x="304" y="120" width="64" height="23"/></g><text class="ts" x="336" y="303" text-anchor="middle">&#8722; roll-</text><text class="ts" x="336" y="317" text-anchor="middle">over $50</text>
<g class="c-coral"><rect x="382" y="143" width="64" height="14"/></g><text class="ts" x="414" y="303" text-anchor="middle">&#8722; escrow</text><text class="ts" x="414" y="317" text-anchor="middle">$30</text>
<g class="c-coral"><rect x="460" y="157" width="64" height="18"/></g><text class="ts" x="492" y="303" text-anchor="middle">&#8722; earnout</text><text class="ts" x="492" y="317" text-anchor="middle">$40</text>
<g class="c-teal"><rect x="538" y="175" width="64" height="115"/></g><text class="th" x="570" y="167" text-anchor="middle">$250M</text><text class="ts" x="570" y="303" text-anchor="middle">cash now</text></svg>''')

# ---- Module 4+ diagrams go here (same format) --------------------------------

FIG['walkaway'] = ('The LBO walk-away ceiling: run the model backward', '''<svg viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="wa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text class="th" x="340" y="24" text-anchor="middle">Forward asks the price; backward asks the ceiling</text>
<text class="ts" x="180" y="52" text-anchor="middle" font-weight="bold">FORWARD (normal)</text>
<text class="ts" x="500" y="52" text-anchor="middle" font-weight="bold">BACKWARD (solve for ceiling)</text>
<line x1="340" y1="44" x2="340" y2="284" class="leader"/>
<g class="c-gray"><rect x="70" y="66" width="220" height="30" rx="4"/><text class="ts" x="180" y="85" text-anchor="middle">Start: entry price (known)</text></g>
<line x1="180" y1="96" x2="180" y2="116" class="arr" marker-end="url(#wa)"/>
<g class="c-gray"><rect x="70" y="118" width="220" height="30" rx="4"/><text class="ts" x="180" y="137" text-anchor="middle">less debt = equity check</text></g>
<line x1="180" y1="148" x2="180" y2="168" class="arr" marker-end="url(#wa)"/>
<g class="c-teal"><rect x="70" y="170" width="220" height="30" rx="4"/><text class="ts" x="180" y="189" text-anchor="middle">&#8594; compute the MOIC (output)</text></g>
<g class="c-amber"><rect x="390" y="66" width="220" height="30" rx="4"/><text class="ts" x="500" y="85" text-anchor="middle">Fix required MOIC (input)</text></g>
<line x1="500" y1="96" x2="500" y2="116" class="arr" marker-end="url(#wa)"/>
<g class="c-amber"><rect x="390" y="118" width="220" height="30" rx="4"/><text class="ts" x="500" y="132" text-anchor="middle">exit equity &#247; MOIC</text><text class="ts" x="500" y="144" text-anchor="middle">= max equity check</text></g>
<line x1="500" y1="148" x2="500" y2="168" class="arr" marker-end="url(#wa)"/>
<g class="c-amber"><rect x="390" y="170" width="220" height="30" rx="4"/><text class="ts" x="500" y="184" text-anchor="middle">+ debt raised</text><text class="ts" x="500" y="196" text-anchor="middle">= max price (output)</text></g>
<g class="c-coral"><rect x="390" y="212" width="220" height="34" rx="4"/><text class="th" x="500" y="233" text-anchor="middle">= the walk-away ceiling</text></g>
<text class="ts" x="340" y="276" text-anchor="middle">Base case: exit equity $1,000M &#247; 2.5&#215; = $400M max equity + $500M debt = $900M ceiling (9.0&#215;)</text></svg>''')

# FIG['debt_schedule'] = ('The debt paydown schedule', '''<svg ...>...</svg>''')
# FIG['returns_bridge'] = ('MOIC / IRR returns attribution', '''<svg ...>...</svg>''')

# ============================================================================
# PLACEMENT  —  EXACT notes heading  ->  [figure keys in order].
# (If a heading here isn't found, the script warns you so you can fix the text.)
# ============================================================================
PLACE = {
    '## 1.2 Fund Structure, Management & the GP/LP Relationship': ['gp_lp'],
    '## Deep dive — The J-curve with real funds': ['jcurve'],
    '## 1.3 PE Within the Alternatives Ecosystem': ['spectrum'],
    '## 1.5 Common Investment Strategies': ['buildup'],
    '## 1.6 LBO Analysis, Hurdle Rates and Returns': ['lbo_bridge'],
    '## 1.7 Leverage as a Tool for Value Creation': ['debt_stack'],
    '## Deep dive — EBITDA basics (foundation)': ['ebitda'],
    '## 1.8 Introduction to Valuation Methods (DCF, Comparables & Multiples)': ['dcf_comp'],
    '### Method 3 (synthesis) — the football field & the LBO angle': ['walkaway'],
    '## Deep dive — Reading a real software income statement (Dayforce, FY2024)': ['dayforce'],
    '## 2.1 Anatomy of the Deal Process: Stages, Workstreams & Responsibilities': ['deal_stages'],
    '## 2.3 Key Terms and Points of Negotiation': ['ev_cash'],
    # Module 4+ example:
    # '## 4.1 Building the Operating Model': ['sources_uses'],
}

# ---- raster snapshots (PNG) embedded as base64 after a heading ----
# heading -> list of (caption, png filename). Files that don't exist are skipped.
IMG_PLACE = {
    '### Income Statement projection': [
        ('Income Statement tab — historical (green links) flowing into the 5-year projection',
         'snap_income_statement.png')],
    '## 4.4 Defining & Calculating EBITDA — the EBITDA Bridge': [
        ('EBITDA Bridge tab — reported → adjusted, each add-back tagged; check row ties to 0',
         'snap_ebitda_bridge.png')],
    '### The Balance Sheet — working capital & PP&E': [
        ('Balance Sheet tab — working-capital schedule (DSO/DIO/DPO) + PP&E roll-forward feeding D&A',
         'snap_balance_sheet.png')],
    '## 5.1 Sources & Uses — funding the deal': [
        ('Sources & Uses tab — entry EV, fees, new debt, rollover, and the sponsor-equity plug (balances to 0)',
         'snap_sources_uses.png')],
    '## 5.2 Debt Schedule — deleveraging & the completed P&L': [
        ('Debt Schedule tab — free-cash-flow sweep pays debt $290M → $185M; interest feeds the income statement',
         'snap_debt_schedule.png')],
    '## 5.3 Exit & Returns — MOIC, IRR, and the value bridge': [
        ('Returns tab — exit equity, MOIC 2.17× / IRR 16.8%, the value-creation bridge, and entry×exit sensitivities',
         'snap_returns.png')],
}

# ============================================================================
# STYLING
# ============================================================================
CSS = '''
@page { size: Letter; margin: 16mm 15mm 18mm 15mm; }
* { box-sizing: border-box; }
body { font-family:'DejaVu Sans', sans-serif; font-size:10pt; line-height:1.5; color:#232320; }
h1 { font-size:20pt; color:#2E7D63; border-bottom:2px solid #2E7D63; padding-bottom:6px; margin:0 0 14px; break-before:page; }
h2 { font-size:14pt; color:#233; margin:22px 0 6px; border-bottom:1px solid #D8D7D2; padding-bottom:3px; break-after:avoid; }
h3 { font-size:11.5pt; color:#3F2E7E; margin:16px 0 4px; break-after:avoid; }
p { margin:6px 0; }
strong { color:#111; }
ul,ol { margin:6px 0 6px 18px; padding:0; }
li { margin:3px 0; }
table { border-collapse:collapse; width:100%; margin:10px 0; font-size:9pt; break-inside:avoid; }
th,td { border:1px solid #D8D7D2; padding:5px 8px; text-align:left; vertical-align:top; }
th { background:#F0F6F3; color:#233; }
tr:nth-child(even) td { background:#FAFAF8; }
blockquote { border-left:3px solid #1D9E75; margin:8px 0; padding:4px 12px; background:#F4FAF7; color:#333; font-size:9.5pt; }
code { font-family:'DejaVu Sans Mono', monospace; background:#F2F2EF; padding:1px 4px; border-radius:3px; font-size:9pt; }
hr { border:none; border-top:1px solid #E4E3DE; margin:16px 0; }
figure.fig { break-inside:avoid; margin:14px auto; padding:10px; border:1px solid #E4E3DE; border-radius:8px; background:#FCFCFB; text-align:center; }
figure.fig svg { width:100%; height:auto; max-width:620px; }
figure.snap { break-inside:avoid; margin:14px auto; padding:8px; border:1px solid #E4E3DE; border-radius:8px; background:#FFFFFF; text-align:center; }
figure.snap img { width:100%; height:auto; max-width:660px; }
figcaption { font-size:8.5pt; color:#6A6A66; font-style:italic; margin-top:4px; }
svg text { font-family:'DejaVu Sans', sans-serif; }
text.th, .th { font-weight:600; font-size:13px; }
text.ts, .ts { font-size:11px; }
.c-teal rect{fill:#E3F4EF;stroke:#1D9E75;} .c-teal text{fill:#0F5C45;}
.c-amber rect{fill:#FBF0DC;stroke:#BA7517;} .c-amber text{fill:#7A4D0E;}
.c-purple rect{fill:#EDE7FB;stroke:#7C5CD6;} .c-purple text{fill:#3F2E7E;}
.c-coral rect{fill:#FBE6DE;stroke:#D85A30;} .c-coral text{fill:#8A3417;}
.c-gray rect{fill:#EEEEEC;stroke:#B8B7B2;} .c-gray text{fill:#4A4A46;}
.leader{stroke:#C4C3BE;stroke-dasharray:4 3;fill:none;} .arr{stroke:#8A8984;fill:none;stroke-width:1.5;}
.cover { text-align:center; padding-top:120px; break-after:page; }
.cover h1 { font-size:32pt; border:none; color:#2E7D63; break-before:avoid; }
.cover p { font-size:12pt; color:#555; }
.cover .sub { font-size:14pt; color:#333; margin-top:8px; }
.toc-title { font-size:20pt; color:#2E7D63; border-bottom:2px solid #2E7D63; padding-bottom:6px; margin:0 0 14px; break-before:page; }
.toc-row { display:flex; align-items:baseline; font-size:10pt; margin:2.5px 0; }
.toc-row.l1 { font-weight:bold; margin-top:9px; color:#233; font-size:10.5pt; }
.toc-row.l2 { margin-left:16px; font-weight:normal; color:#333; }
.toc-row .t { flex:0 1 auto; }
.toc-row .dots { flex:1 1 auto; border-bottom:1px dotted #C9C8C3; margin:0 5px; position:relative; top:-3px; }
.toc-row .pg { flex:0 0 auto; color:#666; font-variant-numeric:tabular-nums; }
'''

COVER = '''<div class="cover">
<h1>Private Equity</h1>
<p class="sub">A Course Handbook — with diagrams</p>
<p>The PE asset class &amp; investment framework &#183; the deal process &#183; leverage, accounting diligence &amp; deal structuring &#183; and beyond</p>
<p style="margin-top:40px; font-size:10pt;">Grounded in real examples: Hilton &#183; Dayforce &#183; Thoma Bravo &#183; Verint &#183; CalPERS disclosures &#183; the secondaries market</p>
<div style="margin-top:90px; font-size:8.5pt; color:#777; line-height:1.5; max-width:560px; margin-left:auto; margin-right:auto; text-align:left; border-top:1px solid #ccc; padding-top:14px;">
<b>Provenance &amp; credits.</b> Course structure follows the syllabus of the Wharton&nbsp;Online &amp; Wall&nbsp;Street&nbsp;Prep Private&nbsp;Equity Certificate Program. This handbook is an <b>independent study aid</b>: all explanations, worked examples, the Cascade&nbsp;Components case, and commentary were <b>generated by Claude (Anthropic)</b> as an interactive tutor, and are not affiliated with, endorsed by, or reproduced from that program. Directed and reviewed by <b>Simer&nbsp;Sawhney</b>, Co-founder, Voatz&nbsp;Inc.<br><br>
Educational use only &#8212; not investment advice. Deal figures for Cascade&nbsp;Components are illustrative; all cited third-party facts should be verified against their original sources.<br><br>
<span style="color:#999;">v1.0 &#183; August&nbsp;2026 &#183; a living document</span>
</div>
</div>'''


def delatex(s):
    """Convert any LaTeX math that sneaks into the notes into readable plain text.

    The handbook has no MathJax, so raw LaTeX would print literally (e.g.
    '\\frac{\\text{Price}}{\\text{NAV}}'). This renders it as 'Price / NAV'.
    Keeps math readable without needing a math renderer in the PDF pipeline.
    """
    import re
    # 1) \text{...}, \mathrm{...} etc -> their contents (MUST run first so the
    #    \frac and \underbrace handlers below see brace-free arguments)
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\\(?:text|mathrm|mathbf|mathit)\{([^{}]*)\}', r'\1', s)
    # 2) \underbrace{a}_{b} -> a (b)
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\\underbrace\{([^{}]*)\}_\{([^{}]*)\}', r'\1 (\2)', s)
    # 3) \frac{a}{b} -> (a / b)   [inner-most first, so nested fractions resolve]
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', r'(\1 / \2)', s)
    # common symbols
    for a, b in [(r'\times', '×'), (r'\div', '÷'), (r'\approx', '≈'),
                 (r'\le', '≤'), (r'\ge', '≥'), (r'\neq', '≠'), (r'\pm', '±'),
                 (r'\cdot', '·'), (r'\rightarrow', '→'), (r'\to', '→'),
                 (r'\qquad', '   ·   '), (r'\quad', '  '), (r'\,', ' '), (r'\%', '%')]:
        s = s.replace(a, b)
    s = s.replace('\\\\', ' ')
    # display/inline delimiters: bold the display formulas so they stand out
    s = re.sub(r'\$\$\s*(.*?)\s*\$\$', r'**\1**', s, flags=re.S)
    s = re.sub(r'(?<!\w)\$([^$\n]+)\$(?!\w)', r'\1', s)
    # any stragglers: drop leftover control sequences and stray braces
    s = re.sub(r'\\[a-zA-Z]+', '', s)
    s = s.replace('{', '').replace('}', '')
    return s


def fix_tables(md_text):
    """Ensure every markdown table has a blank line before its header row.

    python-markdown's table extension silently fails to parse a table that sits
    flush against the preceding text, leaving raw '|---|---|' in the output.
    Idempotent: only inserts a blank line where one is missing.
    """
    import re
    sep = re.compile(r'^\s*\|(?:\s*:?-+:?\s*\|)+\s*$')  # a full delimiter row
    lines = md_text.split('\n')
    out = []
    for i, ln in enumerate(lines):
        nxt = lines[i + 1] if i + 1 < len(lines) else ''
        is_header = ('|' in ln) and sep.match(nxt)
        if is_header and out and out[-1].strip() != '':
            out.append('')
        out.append(ln)
    return '\n'.join(out)


def build():
    md = pathlib.Path(NOTES).read_text()
    start = md.find('## 1.1 History')
    if start == -1:
        raise SystemExit("Could not find '## 1.1 History' in the notes — check NOTES path.")
    md = md[start:]
    md = ('# 1 — The PE Asset Class & Investment Framework\n\n'
          '<div style="color:#FFFFFF;font-size:5px">\u00A7BODYSTART\u00A7</div>\n\n' + md)
    md = delatex(md)  # render any LaTeX as plain text (no MathJax in the PDF)
    md = fix_tables(md)  # guarantee tables parse (blank line before each header)

    # insert figures after their headings; track which placements matched
    matched = set()
    out = []
    for ln in md.split('\n'):
        out.append(ln)
        key = ln.strip()
        if key in PLACE:
            matched.add(key)
            for fk in PLACE[key]:
                cap, svg = FIG[fk]
                out.append(f'\n\n<figure class="fig">{svg}<figcaption>{cap}</figcaption></figure>\n\n')
        if key in IMG_PLACE:
            for cap, fn in IMG_PLACE[key]:
                fp = pathlib.Path(fn)
                if fp.exists():
                    b64 = base64.b64encode(fp.read_bytes()).decode()
                    out.append(
                        f'\n\n<figure class="snap"><img src="data:image/png;base64,{b64}"/>'
                        f'<figcaption>{cap}</figcaption></figure>\n\n')
                else:
                    print(f"  (snapshot missing, skipped: {fn})")
    md2 = '\n'.join(out)

    unmatched = [h for h in PLACE if h not in matched]
    if unmatched:
        print("WARNING — these PLACE headings were not found in the notes (fix the text):")
        for h in unmatched:
            print("   ", h)

    body = markdown.markdown(md2, extensions=['tables', 'attr_list', 'sane_lists'])

    # collect headings (level 1 = module, level 2 = lesson/section) for the TOC
    headings = []
    for ln in md2.split('\n'):
        if ln.startswith('## '):
            headings.append((2, _clean_title(ln[3:])))
        elif ln.startswith('# '):
            headings.append((1, _clean_title(ln[2:])))

    placed = sum(len(PLACE[h]) for h in matched)
    print(f"content built ({len(body):,} bytes; {placed} figures placed; {len(headings)} headings)")
    return headings, body


import re as _re


def _clean_title(s):
    s = _re.sub(r'\*\*|\*|`|_', '', s)
    return _re.sub(r'\s+', ' ', s).strip()


def _esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


SENTINEL = '\u00A7BODYSTART\u00A7'


def build_toc_html(entries):
    """entries: list of (level, title, page-or-None)."""
    rows = ['<h1 class="toc-title">Contents</h1>']
    for level, title, page in entries:
        pg = '' if page is None else str(page)
        rows.append(
            f'<div class="toc-row l{level}"><span class="t">{_esc(title)}</span>'
            f'<span class="dots"></span><span class="pg">{pg}</span></div>')
    return '<section class="toc">' + '\n'.join(rows) + '</section>'


def assemble(body_html, toc_html):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body>{COVER}{toc_html}{body_html}</body></html>')


def render_html(html_str):
    pathlib.Path(OUT_HTML).write_text(html_str)
    from playwright.sync_api import sync_playwright
    uri = pathlib.Path(OUT_HTML).resolve().as_uri()
    footer = ('<div style="width:100%;font-size:8px;color:#999;text-align:center;'
              'padding-top:2px;"><span class="pageNumber"></span> / '
              '<span class="totalPages"></span></div>')
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(uri, wait_until='load')
        pg.wait_for_timeout(1000)
        pg.pdf(path=OUT_PDF, format='Letter', print_background=True,
               display_header_footer=True, header_template='<div></div>', footer_template=footer,
               margin={'top': '16mm', 'bottom': '16mm', 'left': '15mm', 'right': '15mm'})
        b.close()


def _norm(s):
    return _re.sub(r'\s+', ' ', s).strip().casefold()


def heading_pages(pdf_path, titles):
    """Return 1-based page numbers for each title, searching only the body
    (pages after the sentinel that marks the end of the TOC).

    Matching is space-INSENSITIVE: pypdf sometimes injects spaces between
    glyphs of a large/wrapped heading (e.g. 'exceeds' -> 'e x c e e d s'),
    which would defeat a plain substring search. Stripping all whitespace
    from both the page text and the key makes the match robust to that and
    to line-wraps."""
    from pypdf import PdfReader
    pages = [(_norm(p.extract_text() or '')) for p in PdfReader(pdf_path).pages]
    pages_ns = [p.replace(' ', '') for p in pages]
    body_start = 0
    for i, t in enumerate(pages):
        if _norm(SENTINEL) in t:
            body_start = i          # sentinel sits with the first body heading
            break
    out = []
    for title in titles:
        key = _norm(title).replace(' ', '')[:24]
        found = None
        for i in range(body_start, len(pages)):
            if key and key in pages_ns[i]:
                found = i + 1
                break
        out.append(found)
    return out


def render_pdf():
    headings, body = build()
    titles = [t for _, t in headings]
    entries = [(lvl, t, None) for lvl, t in headings]
    prev = None
    for iteration in range(5):
        render_html(assemble(body, build_toc_html(entries)))
        pages = heading_pages(OUT_PDF, titles)
        if pages == prev:
            break
        entries = [(lvl, t, pg) for (lvl, t), pg in zip(headings, pages)]
        prev = pages
    from pypdf import PdfReader
    n = len(PdfReader(OUT_PDF).pages)
    missing = sum(1 for p in pages if p is None)
    note = f" ({missing} headings unresolved)" if missing else ""
    print(f"PDF written  -> {OUT_PDF}  ({n} pages; TOC converged in {iteration+1} pass(es){note})")


if __name__ == '__main__':
    render_pdf()
