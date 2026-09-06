#!/usr/bin/env python3
"""
build_model.py — Cascade Components LBO model (PE Course Modules 4-5).

Builds the workbook one section at a time. This is v1: Cover + Assumptions.
Later turns add: Income Statement, Balance Sheet, Cash Flow, Debt Schedule,
Sources & Uses, and Returns — each as its own tab, referencing Assumptions.

Conventions (per the xlsx skill's financial-model guidance):
  * BLUE text  = hardcoded input / assumption      (editable levers)
  * BLACK text = formula / calculation
  * GREEN text = link from another sheet
  * YELLOW fill= key assumption the user sets
  * $ in millions, one decimal ; percentages stored as FRACTIONS ; multiples 0.0x
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.properties import PageSetupProperties

# ---- styling helpers --------------------------------------------------------
FONT = "Arial"
BLUE = "0000FF"     # inputs
GREEN = "008000"    # cross-sheet links
BLACK = "000000"
WHITE = "FFFFFF"
TEAL = "1D6F5C"     # header band
LGRAY = "EFEFEF"    # section band

CUR = '$#,##0.0;($#,##0.0);"-"'          # $mm, 1 decimal
CUR0 = '$#,##0;($#,##0);"-"'
PCT = '0.0%;(0.0%);"-"'
MULT = '0.0"x"'
MULT2 = '0.00"x"'   # two-decimal multiple, for MOIC (2.17x vs 2.28x must be distinguishable)
DAYS = '0'
NUM = '#,##0.0;(#,##0.0);"-"'

thin = Side(style="thin", color="D0D0D0")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)


def style(cell, *, bold=False, size=10, color=BLACK, italic=False,
          fill=None, align=None, fmt=None, border=False, wrap=False):
    cell.font = Font(name=FONT, bold=bold, size=size, color=color, italic=italic)
    if fill:
        cell.fill = PatternFill("solid", fgColor=fill)
    if align:
        cell.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
    else:
        cell.alignment = Alignment(vertical="center", wrap_text=wrap)
    if fmt:
        cell.number_format = fmt
    if border:
        cell.border = BORDER
    return cell


def section(ws, row, text, span=7):
    """A shaded section header spanning `span` columns."""
    for c in range(1, span + 1):
        style(ws.cell(row=row, column=c), fill=LGRAY, bold=True, size=10)
    ws.cell(row=row, column=1).value = text


wb = Workbook()

# ============================================================================
# COVER
# ============================================================================
cv = wb.active
cv.title = "Cover"
cv.sheet_view.showGridLines = False
for col, w in {"A": 2.5, "B": 26, "C": 22, "D": 22, "E": 22, "F": 20, "G": 4}.items():
    cv.column_dimensions[col].width = w

style(cv.cell(row=2, column=2, value="Cascade Components Corp."), bold=True, size=20, color=TEAL)
style(cv.cell(row=3, column=2, value="LBO Operating Model  —  Middle-Market Case Study"), size=12, italic=True)
style(cv.cell(row=4, column=2, value="Private Equity Course · Modules 4–5 · built one schedule at a time"), size=9, italic=True, color="808080")

desc = ("Cascade Components designs and manufactures engineered fastening and sealing "
        "components for aerospace, defense, and industrial OEMs. Founded 1994; family-owned; "
        "the founder-CEO is retiring and running a sale process. A classic middle-market LBO "
        "target: a stable niche business with real assets, recurring OEM relationships, and "
        "room for a buy-and-build roll-up.")
cv.merge_cells("B6:F9")
style(cv.cell(row=6, column=2, value=desc), size=10, wrap=True, align="left")
cv.cell(row=6, column=2).alignment = Alignment(vertical="top", wrap_text=True)

# Legend
style(cv.cell(row=11, column=2, value="How to read this model"), bold=True, size=11, color=TEAL)
legend = [
    (BLUE, "Blue text", "Hardcoded input / assumption — the levers you edit"),
    (BLACK, "Black text", "Formula / calculation — do not overwrite"),
    (GREEN, "Green text", "Link pulled from another sheet"),
    (None, "Yellow fill", "Key assumption to set (also blue text)"),
]
r = 12
for color, label, meaning in legend:
    cell = cv.cell(row=r, column=2, value="■  " + label)
    if color:
        style(cell, bold=True, color=color, size=10)
    else:
        style(cell, bold=True, size=10)
        cv.cell(row=r, column=2).fill = PatternFill("solid", fgColor="FFFF00")
    style(cv.cell(row=r, column=3, value=meaning), size=10)
    cv.merge_cells(start_row=r, start_column=3, end_row=r, end_column=6)
    r += 1

style(cv.cell(row=r + 1, column=2, value="Units & conventions"), bold=True, size=11, color=TEAL)
notes = [
    "All figures in $ millions unless noted; one decimal place.",
    "Percentages are stored as fractions (0.181 renders 18.1%).",
    "Valuation multiples shown as 0.0x. Years are text labels.",
    "Illustrative case study — figures are realistic but not a real company.",
]
for i, n in enumerate(notes):
    style(cv.cell(row=r + 2 + i, column=2, value="•  " + n), size=10)
    cv.merge_cells(start_row=r + 2 + i, start_column=2, end_row=r + 2 + i, end_column=6)

# Tab guide
gr = r + 2 + len(notes) + 2
style(cv.cell(row=gr, column=2, value="Tabs"), bold=True, size=11, color=TEAL)
tabs = [
    ("Cover", "This page — company, legend, conventions"),
    ("Assumptions", "All operating & transaction drivers (Module 4–5)"),
    ("EBITDA Bridge", "Reported → Adjusted EBITDA reconciliation (Module 3/4)"),
    ("Income Statement", "Historical + projected P&L → EBITDA/EBIT (Module 4)"),
    ("Balance Sheet", "Working capital (DSO/DIO/DPO) + PP&E roll-forward (Module 4)"),
    ("Sources & Uses", "How the deal is funded at close (Module 5)"),
    ("Debt Schedule", "Cash-flow sweep + debt roll-forward; interest → P&L (Module 5)"),
    ("Returns", "Exit value, MOIC / IRR, value bridge & sensitivities (Module 5)"),
]
for i, (t, d) in enumerate(tabs):
    style(cv.cell(row=gr + 1 + i, column=2, value=t), bold=True, size=10)
    style(cv.cell(row=gr + 1 + i, column=3, value=d), size=10)
    cv.merge_cells(start_row=gr + 1 + i, start_column=3, end_row=gr + 1 + i, end_column=6)

# Provenance / credits
cr = gr + 1 + len(tabs) + 2
style(cv.cell(row=cr, column=2,
      value="Course structure follows the Wharton Online & Wall Street Prep PE Certificate syllabus. "
            "Independent study aid generated by Claude (Anthropic); directed and reviewed by "
            "Simer Sawhney, Co-founder, Voatz Inc. Educational use only — not investment advice; "
            "illustrative figures.  v1.0 · August 2026"),
      italic=True, size=8, color="808080")
cv.merge_cells(start_row=cr, start_column=2, end_row=cr + 2, end_column=6)
cv.cell(row=cr, column=2).alignment = Alignment(vertical="top", wrap_text=True)

# ============================================================================
# ASSUMPTIONS
# ============================================================================
aw = wb.create_sheet("Assumptions")
aw.sheet_view.showGridLines = False
widths = {"A": 34, "B": 12, "C": 12, "D": 12, "E": 12, "F": 12, "G": 12, "H": 30}
for col, w in widths.items():
    aw.column_dimensions[col].width = w

# Title band
aw.merge_cells("A1:H1")
style(aw.cell(row=1, column=1, value="Cascade Components — Model Assumptions"),
      bold=True, size=14, color=WHITE, fill=TEAL, align="left")
aw.row_dimensions[1].height = 22

# ---- Historical financials --------------------------------------------------
section(aw, 3, "HISTORICAL FINANCIALS  ($mm)", span=8)
hdr = ["", "FY2023", "FY2024", "FY2025", "", "", "", "Notes / source"]
for j, h in enumerate(hdr, start=1):
    style(aw.cell(row=4, column=j, value=h), bold=True, align="center" if 1 < j < 5 else "left")

hist = [
    # label, 2023, 2024, 2025, note
    ("Revenue", 289.0, 303.5, 320.0, "Company financials (illustrative)"),
    ("  Cost of goods sold", -189.0, -198.3, -208.0, "≈ 65% of revenue"),
    ("Gross profit", None, None, None, "Revenue − COGS (formula)"),
    ("  Gross margin %", None, None, None, "Gross profit ÷ Revenue"),
    ("  SG&A (excl. D&A)", -49.5, -51.0, -54.0, "operating overhead"),
    ("Adjusted EBITDA", 50.5, 54.2, 58.0, "Gross profit + SG&A; reconciled on EBITDA Bridge tab"),
    ("  EBITDA margin %", None, None, None, "EBITDA ÷ Revenue"),
    ("Depreciation & amort.", 9.5, 9.9, 10.4, "≈ 3.3% of revenue"),
    ("Capital expenditures", 11.6, 12.1, 12.8, "≈ 4% of revenue"),
]
row = 5
first_hist_row = row
for label, v23, v24, v25, note in hist:
    is_calc = v23 is None
    indent = label.startswith("  ")
    style(aw.cell(row=row, column=1, value=label), bold=not indent and not is_calc,
          italic=is_calc and indent, size=10)
    if label.strip() in ("Gross profit", "Adjusted EBITDA"):
        style(aw.cell(row=row, column=1), bold=True)
    if is_calc:
        # formulas per column
        for col in (2, 3, 4):
            L = get_column_letter(col)
            if label.strip() == "Gross profit":
                f = f"={L}5+{L}6"           # revenue + COGS(neg)
                fmt = CUR
            elif label.strip() == "Gross margin %":
                f = f"={L}7/{L}5"
                fmt = PCT
            elif label.strip() == "EBITDA margin %":
                f = f"={L}10/{L}5"
                fmt = PCT
            style(aw.cell(row=row, column=col, value=f), fmt=fmt, align="center")
    elif label.strip() == "Adjusted EBITDA":
        for col in (2, 3, 4):
            L = get_column_letter(col)
            style(aw.cell(row=row, column=col, value=f"={L}7+{L}9"), fmt=CUR, align="center", bold=True)
    else:
        for col, val in zip((2, 3, 4), (v23, v24, v25)):
            style(aw.cell(row=row, column=col, value=val), color=BLUE, fmt=CUR, align="center")
    style(aw.cell(row=row, column=8, value=note), italic=True, size=9, color="808080")
    row += 1

# growth line
style(aw.cell(row=row, column=1, value="  Revenue growth %"), italic=True, size=10)
style(aw.cell(row=row, column=3, value="=C5/B5-1"), fmt=PCT, align="center")
style(aw.cell(row=row, column=4, value="=D5/C5-1"), fmt=PCT, align="center")
row += 2

# ---- Operating assumptions (projection) ------------------------------------
op_start = row
section(aw, row, "OPERATING ASSUMPTIONS  (projection drivers)", span=8)
row += 1
yhdr = ["", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "", "Basis"]
for j, h in enumerate(yhdr, start=1):
    style(aw.cell(row=row, column=j, value=h), bold=True, align="center" if 1 < j < 7 else "left")
row += 1

op = [
    ("Revenue growth %",        [0.055, 0.060, 0.060, 0.055, 0.050], PCT, "organic; buy-and-build adds later"),
    ("Gross margin %",          [0.350, 0.352, 0.354, 0.355, 0.355], PCT, "modest mix/scale improvement"),
    ("SG&A % of revenue",       [0.168, 0.166, 0.164, 0.163, 0.162], PCT, "operating leverage as it scales"),
    ("PP&E depreciation rate",   [0.120, 0.120, 0.120, 0.120, 0.120], PCT, "straight-line on net PP&E (~8-yr life)"),
    ("Capex % of revenue",      [0.040, 0.040, 0.039, 0.038, 0.038], PCT, "maintenance + modest growth"),
    ("Tax rate",                [0.250, 0.250, 0.250, 0.250, 0.250], PCT, "blended federal + state"),
]
key_rows = []
for label, vals, fmt, basis in op:
    style(aw.cell(row=row, column=1, value=label), size=10)
    for k, val in enumerate(vals):
        style(aw.cell(row=row, column=2 + k, value=val), color=BLUE, fmt=fmt, align="center",
              fill="FFFF00" if label == "Revenue growth %" else None)
    style(aw.cell(row=row, column=8, value=basis), italic=True, size=9, color="808080")
    key_rows.append((label, row))
    row += 1

row += 1
# working capital days + PP&E base
section(aw, row, "WORKING CAPITAL & PP&E ASSUMPTIONS", span=8)
row += 1
for j, h in enumerate(["", "Value", "", "", "", "", "", "Drives"], start=1):
    style(aw.cell(row=row, column=j, value=h), bold=True, align="center" if j == 2 else "left")
row += 1
wc = [
    ("DSO — days sales outstanding", 55, DAYS, "accounts receivable"),
    ("DIO — days inventory outstanding", 85, DAYS, "inventory (manufacturer -> high)"),
    ("DPO — days payables outstanding", 45, DAYS, "accounts payable"),
    ("Opening net PP&E, end-FY2025 ($mm)", 85.0, CUR, "PP&E roll-forward base"),
]
for label, val, fmt, drives in wc:
    style(aw.cell(row=row, column=1, value=label), size=10)
    style(aw.cell(row=row, column=2, value=val), color=BLUE, fmt=fmt, align="center")
    style(aw.cell(row=row, column=8, value=drives), italic=True, size=9, color="808080")
    row += 1

row += 1
# ---- Transaction assumptions (Module 5) ------------------------------------
section(aw, row, "TRANSACTION ASSUMPTIONS  (entry structure)", span=8)
row += 1
txn = [
    ("Entry EV / LTM EBITDA multiple", 9.0, MULT, "purchase-price multiple"),
    ("Net debt / EBITDA (leverage)", 5.0, MULT, "turns of new debt at close"),
    ("Blended cost of debt", 0.085, PCT, "≈ SOFR 3.6% + ~490 bps blended"),
    ("Exit EV / EBITDA multiple", 9.0, MULT, "exit = entry (no multiple expansion assumed)"),
    ("Hold period (years)", 5, '0', "years to exit"),
    ("Transaction fees (% of EV)", 0.025, PCT, "advisory / legal / diligence"),
    ("Financing fees (% of new debt)", 0.020, PCT, "arrangement / OID"),
    ("Management rollover ($mm)", 12.0, CUR, "mgmt equity rolled into newco"),
]
for label, val, fmt, note in txn:
    style(aw.cell(row=row, column=1, value=label), size=10)
    c = aw.cell(row=row, column=2, value=val)
    style(c, color=BLUE, align="center", fmt=fmt, fill="FFFF00")
    style(aw.cell(row=row, column=8, value=note), italic=True, size=9, color="808080")
    row += 1

# freeze panes under the title
aw.freeze_panes = "A2"

# ============================================================================
# EBITDA BRIDGE  (reported -> adjusted; ties to the operating model)
# ============================================================================
bw = wb.create_sheet("EBITDA Bridge", 2)   # index 2: Cover, Assumptions, Bridge, IS
bw.sheet_view.showGridLines = False
bw.column_dimensions["A"].width = 34
for col in "BCD":
    bw.column_dimensions[col].width = 11
bw.column_dimensions["E"].width = 18
bw.column_dimensions["F"].width = 28

bw.merge_cells("A1:F1")
style(bw.cell(row=1, column=1, value="Cascade Components — EBITDA Bridge  ($mm)"),
      bold=True, size=14, color=WHITE, fill=TEAL, align="left")
bw.row_dimensions[1].height = 22
style(bw.cell(row=2, column=1,
      value="Reported \u2192 Adjusted EBITDA. Each add-back is tagged by where it sits on the P&L and how defensible it is (Module 3 spectrum)."),
      italic=True, size=9, color="808080")
bw.merge_cells("A2:F2")

bhdr = ["$mm", "FY2023", "FY2024", "FY2025", "Where on P&L", "Defensibility"]
for j, h in enumerate(bhdr, start=1):
    style(bw.cell(row=4, column=j, value=h), bold=True, align="center" if 1 < j < 5 else "left", border=True)

# Reported EBITDA (blue inputs — diligence facts from the company's actuals)
style(bw.cell(row=5, column=1, value="Reported EBITDA"), bold=True)
for col, val in zip("BCD", (47.5, 51.0, 54.0)):
    bw[f"{col}5"] = val
    style(bw[f"{col}5"], color=BLUE, fmt=CUR, align="right")

# Add-backs (blue inputs), each with P&L location + defensibility tag
addbacks = [
    ("  Owner-comp normalization",        (1.8, 2.0, 2.5), "SG&A",         "High \u2014 clean, quantifiable"),
    ("  Facility relocation (one-time)",  (0.0, 0.0, 1.2), "COGS + SG&A",  "Medium \u2014 verify truly one-time"),
    ("  Transaction & legal (non-recur.)",(0.8, 0.7, 0.3), "SG&A",         "Medium \u2014 confirm non-operating"),
    ("  Inventory write-down (non-recur.)",(0.4, 0.5, 0.0),"COGS",         "Medium \u2014 check whether it recurs"),
]
r = 6
for label, vals, loc, defens in addbacks:
    style(bw.cell(row=r, column=1, value=label), size=10)
    for col, val in zip("BCD", vals):
        bw[f"{col}{r}"] = val
        style(bw[f"{col}{r}"], color=BLUE, fmt=CUR, align="right")
    style(bw.cell(row=r, column=5, value=loc), size=9, italic=True, align="left")
    style(bw.cell(row=r, column=6, value=defens), size=9, italic=True, align="left")
    r += 1

# Total add-backs (formula)
style(bw.cell(row=10, column=1, value="Total add-backs"), bold=True)
for col in "BCD":
    bw[f"{col}10"] = f"=SUM({col}6:{col}9)"
    style(bw[f"{col}10"], fmt=CUR, align="right", bold=True)
    bw[f"{col}10"].border = Border(top=Side(style="thin", color="B0B0B0"))

# Adjusted EBITDA (formula = reported + add-backs)
style(bw.cell(row=11, column=1, value="Adjusted EBITDA"), bold=True)
for col in "BCD":
    bw[f"{col}11"] = f"={col}5+{col}10"
    style(bw[f"{col}11"], fmt=CUR, align="right", bold=True)
    bw[f"{col}11"].border = Border(top=Side(style="thin", color="808080"),
                                   bottom=Side(style="double", color="808080"))

# Margin + uplift
style(bw.cell(row=12, column=1, value="  Adjusted EBITDA margin %"), italic=True)
style(bw.cell(row=13, column=1, value="  Uplift over reported %"), italic=True)
for col in "BCD":
    bw[f"{col}12"] = f"={col}11/Assumptions!{col}5"
    style(bw[f"{col}12"], fmt=PCT, align="right")
    bw[f"{col}13"] = f"={col}11/{col}5-1"
    style(bw[f"{col}13"], fmt=PCT, align="right")

# Tie-out check vs the operating model's EBITDA (Assumptions row 10 = GP + SG&A)
style(bw.cell(row=15, column=1, value="Check: Adjusted EBITDA \u2212 operating model"), bold=True)
for col in "BCD":
    bw[f"{col}15"] = f"={col}11-Assumptions!{col}10"
    style(bw[f"{col}15"], fmt=CUR, align="right", bold=True)
style(bw.cell(row=15, column=5, value="zero confirms the tie \u2713"), size=9, italic=True, color="008000")
bw.merge_cells("E15:F15")

# Defensibility legend
style(bw.cell(row=17, column=1, value="Defensibility (Module 3): High add-backs survive diligence; Medium ones need support; "
      "serial \u2018one-offs\u2019 and run-rate/pro-forma items are where buyers push back hardest."),
      italic=True, size=9, color="808080")
bw.merge_cells("A17:F18")
bw.cell(row=17, column=1).alignment = Alignment(vertical="top", wrap_text=True)

bw.freeze_panes = "B5"

# ============================================================================
# INCOME STATEMENT  (historical linked from Assumptions; projections = formulas)
# ============================================================================
iw = wb.create_sheet("Income Statement")
iw.sheet_view.showGridLines = False
iw.column_dimensions["A"].width = 30
for col in "BCDEFGHI":
    iw.column_dimensions[col].width = 11

iw.merge_cells("A1:I1")
style(iw.cell(row=1, column=1, value="Cascade Components — Income Statement  ($mm)"),
      bold=True, size=14, color=WHITE, fill=TEAL, align="left")
iw.row_dimensions[1].height = 22

# period banners
iw.merge_cells("B3:D3"); style(iw.cell(row=3, column=2, value="Actual"), bold=True, italic=True, align="center", fill=LGRAY)
iw.merge_cells("E3:I3"); style(iw.cell(row=3, column=5, value="Projected"), bold=True, italic=True, align="center", fill=LGRAY)

# column headers
col_hdr = ["$mm", "FY2023", "FY2024", "FY2025", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
for j, h in enumerate(col_hdr, start=1):
    style(iw.cell(row=4, column=j, value=h), bold=True, align="center" if j > 1 else "left", border=True)

# IS projected column -> Assumptions column (Y1..Y5 live in Assumptions B..F)
proj = {"E": "B", "F": "C", "G": "D", "H": "E", "I": "F"}
_BSCOL = {"E": "C", "F": "D", "G": "E", "H": "F", "I": "G"}  # IS proj col -> Balance Sheet year col
proj_cols = list(proj.keys())
hist_cols = ["B", "C", "D"]
# Assumptions row references (from the layout above)
A_REV, A_COGS, A_SGA, A_DA = 5, 6, 9, 12
A_GROW, A_GM, A_SGAPCT, A_DAPCT, A_TAX = 18, 19, 20, 21, 23

labels = [
    (5, "Revenue", True), (6, "  growth %", False), (7, "  Cost of goods sold", False),
    (8, "Gross profit", True), (9, "  gross margin %", False), (10, "  SG&A (excl. D&A)", False),
    (11, "EBITDA", True), (12, "  EBITDA margin %", False), (13, "  Depreciation & amort.", False),
    (14, "EBIT", True), (15, "  EBIT margin %", False),
    (16, "  Interest expense", False), (17, "Pre-tax income", True),
    (18, "  Taxes", False), (19, "Net income", True), (20, "  net margin %", False),
]
for r, lab, bold in labels:
    style(iw.cell(row=r, column=1, value=lab), bold=bold)

# ---- HISTORICAL columns: link to Assumptions (green for direct links)
for hc in hist_cols:
    iw[f"{hc}5"] = f"=Assumptions!{hc}{A_REV}"
    iw[f"{hc}7"] = f"=Assumptions!{hc}{A_COGS}"
    iw[f"{hc}8"] = f"={hc}5+{hc}7"
    iw[f"{hc}9"] = f"={hc}8/{hc}5"
    iw[f"{hc}10"] = f"=Assumptions!{hc}{A_SGA}"
    iw[f"{hc}11"] = f"={hc}8+{hc}10"
    iw[f"{hc}12"] = f"={hc}11/{hc}5"
    iw[f"{hc}13"] = f"=-Assumptions!{hc}{A_DA}"
    iw[f"{hc}14"] = f"={hc}11+{hc}13"
    iw[f"{hc}15"] = f"={hc}14/{hc}5"
iw["C6"] = "=C5/B5-1"
iw["D6"] = "=D5/C5-1"

# ---- PROJECTED columns: formulas off Assumptions drivers
prev = "D"  # FY2025 is the base for Year 1
for pc in proj_cols:
    ac = proj[pc]
    iw[f"{pc}5"] = f"={prev}5*(1+Assumptions!{ac}{A_GROW})"
    iw[f"{pc}6"] = f"={pc}5/{prev}5-1"
    iw[f"{pc}7"] = f"=-({pc}5*(1-Assumptions!{ac}{A_GM}))"
    iw[f"{pc}8"] = f"={pc}5+{pc}7"
    iw[f"{pc}9"] = f"={pc}8/{pc}5"
    iw[f"{pc}10"] = f"=-({pc}5*Assumptions!{ac}{A_SGAPCT})"
    iw[f"{pc}11"] = f"={pc}8+{pc}10"
    iw[f"{pc}12"] = f"={pc}11/{pc}5"
    iw[f"{pc}13"] = f"=-'Balance Sheet'!{_BSCOL[pc]}15"          # D&A = depreciation from PP&E roll-forward
    iw[f"{pc}14"] = f"={pc}11+{pc}13"
    iw[f"{pc}15"] = f"={pc}14/{pc}5"
    iw[f"{pc}16"] = f"=-'Debt Schedule'!{_BSCOL[pc]}14"         # interest (DS positive → IS negative)
    iw[f"{pc}17"] = f"={pc}14+{pc}16"                           # pre-tax income
    iw[f"{pc}18"] = f"=-MAX({pc}17,0)*Assumptions!{ac}{A_TAX}"  # taxes (no benefit on losses)
    iw[f"{pc}19"] = f"={pc}17+{pc}18"                           # net income
    iw[f"{pc}20"] = f"={pc}19/{pc}5"                            # net margin %
    prev = pc

# ---- number formats & colors across the grid
for r, lab, bold in labels:
    is_pct = r in (6, 9, 12, 15, 20)
    for col in "BCDEFGHI":
        cell = iw[f"{col}{r}"]
        if cell.value is None:
            continue
        green_link = (col in hist_cols) and (r in (5, 7, 10, 13))
        style(cell, fmt=(PCT if is_pct else CUR),
              color=GREEN if green_link else BLACK, bold=bold, align="right")

# subtotal top-borders
for r in (8, 11, 14, 17, 19):
    for col in "BCDEFGHI":
        iw[f"{col}{r}"].border = Border(top=Side(style="thin", color="B0B0B0"))

# memo
style(iw.cell(row=22, column=1,
      value="Interest, taxes & net income (projected years) come from the Debt Schedule; historical periods pre-date the LBO capital structure."),
      italic=True, size=9, color="808080")
iw.merge_cells("A22:I22")
style(iw.cell(row=23, column=1,
      value="Convention: interest is charged on the beginning-of-year debt balance — the standard way to avoid a circular reference."),
      italic=True, size=9, color="808080")
iw.merge_cells("A23:I23")

iw.freeze_panes = "B5"

# ============================================================================
# BALANCE SHEET  (working capital schedule + PP&E roll-forward + net assets)
# ============================================================================
bs = wb.create_sheet("Balance Sheet")
bs.sheet_view.showGridLines = False
bs.column_dimensions["A"].width = 32
for col in "BCDEFG":
    bs.column_dimensions[col].width = 11
bs.column_dimensions["H"].width = 30

bs.merge_cells("A1:G1")
style(bs.cell(row=1, column=1, value="Cascade Components — Balance Sheet & Working Capital  ($mm)"),
      bold=True, size=14, color=WHITE, fill=TEAL, align="left")
bs.row_dimensions[1].height = 22
style(bs.cell(row=2, column=1,
      value="Operating (asset-side) balance sheet. Cash, debt, goodwill & equity are completed in Module 5 with the LBO financing."),
      italic=True, size=9, color="808080")
bs.merge_cells("A2:H2")

# column headers: FY2025 base + Year 1-5
bhdr = ["$mm", "FY2025", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
for j, h in enumerate(bhdr, start=1):
    style(bs.cell(row=5, column=j, value=h), bold=True, align="center" if j > 1 else "left", border=True)
style(bs.cell(row=4, column=1, value="WORKING CAPITAL SCHEDULE  (driven by DSO / DIO / DPO)"),
      bold=True, fill=LGRAY)
for c in range(2, 8):
    style(bs.cell(row=4, column=c), fill=LGRAY)

# column mapping: BS col -> Income Statement col (revenue row 5, COGS row 7)
BS_ALL = ["B", "C", "D", "E", "F", "G"]
IS_ALL = ["D", "E", "F", "G", "H", "I"]
A_YR = {"C": "B", "D": "C", "E": "D", "F": "E", "G": "F"}  # BS year col -> Assumptions col (Y1..Y5)

# labels
wc_labels = [
    (6, "  Accounts receivable  (DSO)"),
    (7, "  Inventory  (DIO)"),
    (8, "  Accounts payable  (DPO)"),
    (9, "Net working capital"),
    (10, "  (Increase)/decrease in NWC — cash"),
]
for r, lab in wc_labels:
    style(bs.cell(row=r, column=1, value=lab), bold=(r == 9))

for bcol, icol in zip(BS_ALL, IS_ALL):
    bs[f"{bcol}6"] = f"=Assumptions!$B$27/365*'Income Statement'!{icol}5"
    bs[f"{bcol}7"] = f"=Assumptions!$B$28/365*(-'Income Statement'!{icol}7)"
    bs[f"{bcol}8"] = f"=Assumptions!$B$29/365*(-'Income Statement'!{icol}7)"
    bs[f"{bcol}9"] = f"={bcol}6+{bcol}7-{bcol}8"
# change in NWC (cash impact): only Y1..Y5; negative = cash consumed as NWC grows
for i in range(1, len(BS_ALL)):
    cur, prev = BS_ALL[i], BS_ALL[i - 1]
    bs[f"{cur}10"] = f"=-({cur}9-{prev}9)"

# PP&E roll-forward
style(bs.cell(row=12, column=1, value="PP&E ROLL-FORWARD  (D&A now comes from the asset base)"),
      bold=True, fill=LGRAY)
for c in range(2, 8):
    style(bs.cell(row=12, column=c), fill=LGRAY)
ppe_labels = [
    (13, "  Beginning net PP&E"),
    (14, "  + Capital expenditures"),
    (15, "  − Depreciation"),
    (16, "Ending net PP&E"),
]
for r, lab in ppe_labels:
    style(bs.cell(row=r, column=1, value=lab), bold=(r == 16))
# FY2025 base: show opening PP&E as the ending balance for continuity
bs["B16"] = "=Assumptions!$B$30"
for bcol in ["C", "D", "E", "F", "G"]:
    acol, icol = A_YR[bcol], IS_ALL[BS_ALL.index(bcol)]
    # beginning = prior year ending (Y1 begin = opening PP&E)
    if bcol == "C":
        bs[f"{bcol}13"] = "=Assumptions!$B$30"
    else:
        prev = BS_ALL[BS_ALL.index(bcol) - 1]
        bs[f"{bcol}13"] = f"={prev}16"
    bs[f"{bcol}14"] = f"=Assumptions!{acol}22*'Income Statement'!{icol}5"   # capex % x revenue
    bs[f"{bcol}15"] = f"=Assumptions!{acol}21*{bcol}13"                     # deprec rate x beginning
    bs[f"{bcol}16"] = f"={bcol}13+{bcol}14-{bcol}15"

# Operating net assets (invested capital, ex cash/debt)
style(bs.cell(row=18, column=1, value="OPERATING NET ASSETS  (invested capital, excl. cash / debt / goodwill)"),
      bold=True, fill=LGRAY)
for c in range(2, 8):
    style(bs.cell(row=18, column=c), fill=LGRAY)
na_labels = [(19, "  Net working capital"), (20, "  Net PP&E"), (21, "Operating net assets")]
for r, lab in na_labels:
    style(bs.cell(row=r, column=1, value=lab), bold=(r == 21))
for bcol in BS_ALL:
    bs[f"{bcol}19"] = f"={bcol}9"
    bs[f"{bcol}20"] = f"={bcol}16"
    bs[f"{bcol}21"] = f"={bcol}19+{bcol}20"

# number formats + colors
for r in [6, 7, 8, 9, 10, 13, 14, 15, 16, 19, 20, 21]:
    for bcol in BS_ALL:
        c = bs[f"{bcol}{r}"]
        if c.value is None:
            continue
        style(c, fmt=CUR, align="right", bold=(r in (9, 16, 21)))
# subtotal top-borders
for r in (9, 16, 21):
    for bcol in BS_ALL:
        bs[f"{bcol}{r}"].border = Border(top=Side(style="thin", color="B0B0B0"))

# notes
style(bs.cell(row=23, column=1,
      value="Growth eats cash: NWC rises every year, so the \"(Increase)/decrease in NWC\" line is a recurring cash outflow (row 10)."),
      italic=True, size=9, color="808080")
bs.merge_cells("A23:H23")
style(bs.cell(row=24, column=1,
      value="D&A fix: Income-Statement depreciation now links to row 15 (rate × beginning PP&E) — no longer a % of revenue."),
      italic=True, size=9, color="808080")
bs.merge_cells("A24:H24")

bs.freeze_panes = "B5"

# ============================================================================
# SOURCES & USES  (how the deal is funded at close)
# ============================================================================
su = wb.create_sheet("Sources & Uses")
su.sheet_view.showGridLines = False
su.column_dimensions["A"].width = 34
su.column_dimensions["B"].width = 13
su.column_dimensions["C"].width = 30

su.merge_cells("A1:C1")
style(su.cell(row=1, column=1, value="Cascade Components — Sources & Uses  ($mm)"),
      bold=True, size=14, color=WHITE, fill=TEAL, align="left")
su.row_dimensions[1].height = 22
style(su.cell(row=2, column=1,
      value="How the purchase is funded at close. Uses = what you pay for; Sources = where the money comes from. They must balance."),
      italic=True, size=9, color="808080")
su.merge_cells("A2:C2")

# Assumptions references
EB = "Assumptions!$D$10"      # LTM Adjusted EBITDA (FY2025)
ENTRY = "Assumptions!$B$33"; LEV = "Assumptions!$B$34"
TXNF = "Assumptions!$B$38"; FINF = "Assumptions!$B$39"; ROLL = "Assumptions!$B$40"

def su_row(r, label, formula=None, fmt=CUR, bold=False, fill=None, note=None, blue=False):
    style(su.cell(row=r, column=1, value=label), bold=bold, size=10)
    if formula is not None:
        c = su.cell(row=r, column=2, value=formula)
        style(c, fmt=fmt, align="right", bold=bold, color=BLUE if blue else BLACK)
        if fill:
            c.fill = PatternFill("solid", fgColor=fill)
    if note:
        style(su.cell(row=r, column=3, value=note), italic=True, size=9, color="808080")

# Entry memo
style(su.cell(row=4, column=1, value="ENTRY"), bold=True, fill=LGRAY)
style(su.cell(row=4, column=2), fill=LGRAY); style(su.cell(row=4, column=3), fill=LGRAY)
su_row(5, "  LTM Adjusted EBITDA", f"={EB}", note="from EBITDA Bridge (FY2025)")
su_row(6, "  Entry EV / EBITDA multiple", f"={ENTRY}", fmt=MULT, note="purchase-price multiple")
su_row(7, "Entry enterprise value", "=B6*B5", bold=True, note="multiple × EBITDA")

# Uses
style(su.cell(row=9, column=1, value="USES OF FUNDS"), bold=True, fill=LGRAY)
style(su.cell(row=9, column=2), fill=LGRAY); style(su.cell(row=9, column=3), fill=LGRAY)
su_row(10, "  Purchase enterprise value", "=B7", note="buy the business (cash-free, debt-free)")
su_row(11, "  Transaction fees", f"={TXNF}*B7", note="advisory / legal / diligence")
su_row(12, "  Financing fees", f"={FINF}*({LEV}*{EB})", note="arrangement / OID on new debt")
su_row(13, "Total uses", "=SUM(B10:B12)", bold=True)
su.cell(row=13, column=2).border = Border(top=Side(style="thin", color="808080"))

# Sources
style(su.cell(row=15, column=1, value="SOURCES OF FUNDS"), bold=True, fill=LGRAY)
style(su.cell(row=15, column=2), fill=LGRAY); style(su.cell(row=15, column=3), fill=LGRAY)
su_row(16, "  New term debt", f"={LEV}*{EB}", note="leverage × EBITDA (5.0×)")
su_row(17, "  Management rollover", f"={ROLL}", note="mgmt equity rolled into newco")
su_row(18, "  Sponsor equity (plug)", "=B13-B16-B17", note="the check the PE firm writes")
su_row(19, "Total sources", "=SUM(B16:B18)", bold=True)
su.cell(row=19, column=2).border = Border(top=Side(style="thin", color="808080"))

# Check
su_row(21, "Check: sources − uses", "=B19-B13", bold=True, note="must be 0")
style(su.cell(row=21, column=3, value="0 confirms it balances ✓"), italic=True, size=9, color="008000")

# Capitalization memo
style(su.cell(row=23, column=1, value="CAPITALIZATION"), bold=True, fill=LGRAY)
style(su.cell(row=23, column=2), fill=LGRAY); style(su.cell(row=23, column=3), fill=LGRAY)
su_row(24, "  Total capitalization", "=B13")
su_row(25, "  Debt % of total", "=B16/B13", fmt=PCT)
su_row(26, "  Equity % of total", "=(B17+B18)/B13", fmt=PCT)
su_row(27, "  Sponsor equity check", "=B18", bold=True, note="business equity 232.0 + fees − rollover")
style(su.cell(row=29, column=1,
      value="Reconciles to Returns: sponsor check 238.9 = business equity 232.0 (EV − debt) + fees 18.9 − rollover 12.0."),
      italic=True, size=9, color="808080")
su.merge_cells("A29:C30")
su.cell(row=29, column=1).alignment = Alignment(vertical="top", wrap_text=True)

su.freeze_panes = "A3"

# ============================================================================
# DEBT SCHEDULE  (cash-flow available for paydown + debt roll-forward)
# ============================================================================
ds = wb.create_sheet("Debt Schedule")
ds.sheet_view.showGridLines = False
ds.column_dimensions["A"].width = 34
for col in "BCDEFG":
    ds.column_dimensions[col].width = 11
ds.column_dimensions["H"].width = 26

ds.merge_cells("A1:G1")
style(ds.cell(row=1, column=1, value="Cascade Components — Debt Schedule  ($mm)"),
      bold=True, size=14, color=WHITE, fill=TEAL, align="left")
ds.row_dimensions[1].height = 22
style(ds.cell(row=2, column=1,
      value="Free cash flow sweeps the debt down each year; interest (on the beginning balance) feeds the income statement."),
      italic=True, size=9, color="808080")
ds.merge_cells("A2:H2")

dhdr = ["$mm", "At close", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
for j, h in enumerate(dhdr, start=1):
    style(ds.cell(row=4, column=j, value=h), bold=True, align="center" if j > 1 else "left", border=True)

DS_YEAR = ["C", "D", "E", "F", "G"]
IS_YEAR = ["E", "F", "G", "H", "I"]   # Income Statement projected cols
BS_YEAR = ["C", "D", "E", "F", "G"]   # Balance Sheet year cols (same letters as DS)

# ---- Cash flow available for debt paydown
style(ds.cell(row=5, column=1, value="CASH FLOW AVAILABLE FOR DEBT PAYDOWN"), bold=True, fill=LGRAY)
for c in range(2, 8):
    style(ds.cell(row=5, column=c), fill=LGRAY)
cf_labels = [(6, "  Net income"), (7, "  + Depreciation & amort."),
             (8, "  − (Increase)/decrease in NWC"), (9, "  − Capital expenditures"),
             (10, "Free cash flow (pre-paydown)")]
for r, lab in cf_labels:
    style(ds.cell(row=r, column=1, value=lab), bold=(r == 10))
for dcol, iscol, bscol in zip(DS_YEAR, IS_YEAR, BS_YEAR):
    ds[f"{dcol}6"] = f"='Income Statement'!{iscol}19"
    ds[f"{dcol}7"] = f"='Balance Sheet'!{bscol}15"        # add back depreciation (positive)
    ds[f"{dcol}8"] = f"='Balance Sheet'!{bscol}10"        # NWC cash impact (already signed)
    ds[f"{dcol}9"] = f"=-'Balance Sheet'!{bscol}14"       # capex (cash out)
    ds[f"{dcol}10"] = f"=SUM({dcol}6:{dcol}9)"

# ---- Debt roll-forward
style(ds.cell(row=12, column=1, value="DEBT ROLL-FORWARD"), bold=True, fill=LGRAY)
for c in range(2, 8):
    style(ds.cell(row=12, column=c), fill=LGRAY)
db_labels = [(13, "  Beginning debt"), (14, "  Interest expense (@ 8.5%)"),
             (15, "  (−) Debt paydown — cash sweep"), (16, "Ending debt"),
             (17, "  Memo: net debt / EBITDA")]
for r, lab in db_labels:
    style(ds.cell(row=r, column=1, value=lab), bold=(r == 16))

# At-close ending balance = new debt from Sources & Uses
ds["B16"] = "='Sources & Uses'!B16"
prev = "B"
for dcol, iscol in zip(DS_YEAR, IS_YEAR):
    ds[f"{dcol}13"] = f"={prev}16"                                  # beginning = prior ending
    ds[f"{dcol}14"] = f"={dcol}13*Assumptions!$B$35"               # interest on beginning balance
    ds[f"{dcol}15"] = f"=-MIN(MAX({dcol}10,0),{dcol}13)"           # sweep, capped at balance
    ds[f"{dcol}16"] = f"={dcol}13+{dcol}15"                        # ending = beginning − paydown
    ds[f"{dcol}17"] = f"={dcol}16/'Income Statement'!{iscol}11"    # leverage memo
    prev = dcol

# formats
for r in (6, 7, 8, 9, 10, 13, 14, 15, 16):
    for col in "BCDEFG":
        c = ds[f"{col}{r}"]
        if c.value is not None:
            style(c, fmt=CUR, align="right", bold=(r in (10, 16)))
for col in "CDEFG":
    style(ds[f"{col}17"], fmt=MULT, align="right", color="808080")
for r in (10, 16):
    for col in "BCDEFG":
        ds[f"{col}{r}"].border = Border(top=Side(style="thin", color="B0B0B0"))

style(ds.cell(row=19, column=1,
      value="100% cash sweep assumed (all free cash flow pays down debt). Interest is charged on the beginning-of-year balance to keep the model non-circular."),
      italic=True, size=9, color="808080")
ds.merge_cells("A19:H20")
ds.cell(row=19, column=1).alignment = Alignment(vertical="top", wrap_text=True)

ds.freeze_panes = "B5"

# ============================================================================
# RETURNS  (exit value, MOIC/IRR, value-creation bridge, sensitivities)
# ============================================================================
rt = wb.create_sheet("Returns")
rt.sheet_view.showGridLines = False
rt.column_dimensions["A"].width = 32
for col in "BCDEFG":
    rt.column_dimensions[col].width = 12

rt.merge_cells("A1:G1")
style(rt.cell(row=1, column=1, value="Cascade Components — Returns  ($mm)"),
      bold=True, size=14, color=WHITE, fill=TEAL, align="left")
rt.row_dimensions[1].height = 22
style(rt.cell(row=2, column=1,
      value="Exit equity ÷ equity invested = MOIC; annualized = IRR. The bridge attributes the gain to the three value levers (1.6)."),
      italic=True, size=9, color="808080")
rt.merge_cells("A2:G2")

def rrow(r, label, formula=None, fmt=CUR, bold=False, note=None, indent=False):
    style(rt.cell(row=r, column=1, value=("  " + label) if indent else label), bold=bold, size=10)
    if formula is not None:
        style(rt.cell(row=r, column=2, value=formula), fmt=fmt, align="right", bold=bold)
    if note:
        style(rt.cell(row=r, column=3, value=note), italic=True, size=9, color="808080")

def sect(r, text):
    style(rt.cell(row=r, column=1, value=text), bold=True, fill=LGRAY)
    for c in range(2, 8):
        style(rt.cell(row=r, column=c), fill=LGRAY)

# Refs
SU_EV="'Sources & Uses'!B7"; SU_DEBT="'Sources & Uses'!B16"
SU_TXN="'Sources & Uses'!B11"; SU_FIN="'Sources & Uses'!B12"
Y5E="'Income Statement'!I11"; EXITD="'Debt Schedule'!G16"
EBIT0="Assumptions!D10"; ENTRYM="Assumptions!B33"; EXITM="Assumptions!B36"; HOLD="Assumptions!B37"

sect(4, "ENTRY")
rrow(5, "Entry enterprise value", f"={SU_EV}", indent=True)
rrow(6, "Less: new debt", f"=-{SU_DEBT}", indent=True)
rrow(7, "Entry equity (business)", "=B5+B6", bold=True, note="EV − debt (not the sponsor check: that adds fees, nets rollover)")
rrow(8, "Plus: fees funded by equity", f"={SU_TXN}+{SU_FIN}", indent=True, note="transaction + financing")
rrow(9, "Total equity invested", "=B7+B8", bold=True, note="sponsor + rollover")

sect(11, "EXIT  (Year 5)")
rrow(12, "Year-5 EBITDA", f"={Y5E}", indent=True)
rrow(13, "Exit EV / EBITDA multiple", f"={EXITM}", fmt=MULT, indent=True, note="exit = entry (no expansion)")
rrow(14, "Exit enterprise value", "=B12*B13", bold=True)
rrow(15, "Less: exit net debt", f"=-{EXITD}", indent=True, note="after 5 yrs of paydown")
rrow(16, "Exit equity", "=B14+B15", bold=True)

sect(18, "RETURNS")
rrow(19, "MOIC", "=B16/B9", fmt=MULT2, bold=True, note="exit equity ÷ TOTAL equity invested (B16 ÷ B9 = 544.6 ÷ 250.8)")
rrow(20, "IRR (5-yr)", f"=B19^(1/{HOLD})-1", fmt=PCT, bold=True, note="MOIC annualized over the hold")

sect(22, "VALUE-CREATION BRIDGE  (the three levers, 1.6)")
rrow(24, "Entry equity (business, EV − debt)", "=B7")
rrow(25, "+ EBITDA growth", f"=({Y5E}-{EBIT0})*{ENTRYM}", indent=True, note="ΔEBITDA × entry multiple")
rrow(26, "+ Multiple expansion", f"=({EXITM}-{ENTRYM})*{Y5E}", indent=True, note="Δmultiple × exit EBITDA")
rrow(27, "+ Debt paydown (deleveraging)", f"={SU_DEBT}-{EXITD}", indent=True, note="debt repaid over the hold")
rrow(28, "Exit equity (sum of bridge)", "=SUM(B24:B27)", bold=True)
rrow(29, "check vs exit equity", "=B28-B16", note="0 confirms the bridge ties")
# % share of value created (col D)
style(rt.cell(row=24, column=4, value="% of gain"), italic=True, size=8, color="808080", align="right")
for r in (25, 26, 27):
    style(rt.cell(row=r, column=4, value=f"=B{r}/(B28-B24)"), fmt=PCT, align="right", size=9, color="808080")

# ---- Sensitivity: MOIC (entry multiple × exit multiple) ----
AX = [8.0, 8.5, 9.0, 9.5, 10.0]
sect(31, "SENSITIVITY — MOIC  (entry multiple ↓  ×  exit multiple →)")
style(rt.cell(row=32, column=1, value="entry \\ exit"), bold=True, italic=True, align="right", size=9)
for j, xm in enumerate(AX):
    style(rt.cell(row=32, column=2 + j, value=xm), color=BLUE, fmt=MULT, align="center", bold=True)
for i, em in enumerate(AX):
    r = 33 + i
    style(rt.cell(row=r, column=1, value=em), color=BLUE, fmt=MULT, align="right", bold=True)
    for j in range(len(AX)):
        col = get_column_letter(2 + j)
        # numerator: exit equity at exit mult in col header row 32; denominator: entry equity at entry mult in col A
        num = f"({Y5E}*{col}$32-{EXITD})"
        den = f"($A{r}*{EBIT0}*(1+Assumptions!$B$38)+Assumptions!$B$39*{SU_DEBT}-{SU_DEBT})"
        style(rt.cell(row=r, column=2 + j, value=f"={num}/{den}"), fmt=MULT2, align="center")
# highlight base case (entry 9.0 = row 35, exit 9.0 = col D)
rt["D35"].fill = PatternFill("solid", fgColor="FFF2CC")

# ---- Sensitivity: IRR (references the MOIC grid) ----
sect(40, "SENSITIVITY — IRR  (entry multiple ↓  ×  exit multiple →)")
style(rt.cell(row=41, column=1, value="entry \\ exit"), bold=True, italic=True, align="right", size=9)
for j, xm in enumerate(AX):
    style(rt.cell(row=41, column=2 + j, value=xm), color=BLUE, fmt=MULT, align="center", bold=True)
for i, em in enumerate(AX):
    r = 42 + i
    style(rt.cell(row=r, column=1, value=em), color=BLUE, fmt=MULT, align="right", bold=True)
    for j in range(len(AX)):
        col = get_column_letter(2 + j)
        moic_cell = f"{col}{33 + i}"
        style(rt.cell(row=r, column=2 + j, value=f"={moic_cell}^(1/{HOLD})-1"), fmt=PCT, align="center")
rt["D44"].fill = PatternFill("solid", fgColor="FFF2CC")

style(rt.cell(row=48, column=1,
      value="Base case (entry 9.0× / exit 9.0×) highlighted. MOIC = exit equity ÷ total equity invested ($250.8M — sponsor + rollover, incl. fees), the same denominator as the headline. Exit debt is held constant across the grid — the paydown path depends on operations, not the purchase multiple."),
      italic=True, size=9, color="808080")
rt.merge_cells("A48:G49")
rt.cell(row=48, column=1).alignment = Alignment(vertical="top", wrap_text=True)

rt.freeze_panes = "B3"

# ---- print setup: each sheet fits cleanly on one landscape page -------------
for ws in wb.worksheets:
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.page_margins.left = ws.page_margins.right = 0.3
    ws.page_margins.top = ws.page_margins.bottom = 0.4

wb.save("Cascade_Components_LBO_Model.xlsx")
print("workbook written")
