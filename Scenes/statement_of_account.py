from manim import *

# ─── Palette ───────────────────────────────────────────
BG      = "#0D1B2A"
GOLD    = "#FFD166"
TEAL    = "#06D6A0"
PINK    = "#EF476F"
BLUE    = "#118AB2"
LAVENDER= "#B388FF"
WHITE   = "#F0F4F8"
GRAY    = "#6B7C93"
GREEN_C = "#69F0AE"
RED_C   = "#FF5252"
ORANGE  = "#FF9F1C"

def fmt(n):
    return f"K{n:,.0f}"

# ─── Transactions ──────────────────────────────────────
TRANSACTIONS = [
    ("June 1",  "Balance b/f",              "—",        150_000,  0,        150_000),
    ("June 4",  "Invoice – Goods sold",     "INV-001",  320_000,  0,        470_000),
    ("June 8",  "Credit Note – Returns",    "CN-001",   0,        40_000,   430_000),
    ("June 12", "Cash Received",            "—",        0,        200_000,  230_000),
    ("June 18", "Invoice – Goods sold",     "INV-002",  180_000,  0,        410_000),
    ("June 22", "Discount Allowed",         "—",        0,        20_000,   390_000),
    ("June 27", "Cash Received",            "—",        0,        150_000,  240_000),
]

FINAL_BALANCE = 240_000

EXPLANATIONS = [
    ("June 1",  "Opening balance",
     "Banda Stores owed K150,000\nfrom the previous month.",
     ORANGE, "+"),
    ("June 4",  "Credit sale K320,000",
     "Chilimba sold goods on credit.\nDebit Banda = balance increases.",
     BLUE,   "+"),
    ("June 8",  "Returns K40,000",
     "Banda returned goods.\nA Credit Note reduces the balance.",
     PINK,   "−"),
    ("June 12", "Cash receipt K200,000",
     "Banda paid K200,000 in cash.\nBalance decreases.",
     GREEN_C,"−"),
    ("June 18", "Credit sale K180,000",
     "Another credit sale.\nBalance increases again.",
     BLUE,   "+"),
    ("June 22", "Discount K20,000",
     "Chilimba allowed a settlement\ndiscount — reduces balance.",
     LAVENDER,"−"),
    ("June 27", "Cash receipt K150,000",
     "Final cash payment.\nBalance falls to K240,000.",
     GREEN_C,"−"),
]


# ══════════════════════════════════════════════════════
# SCENE 1 – Title
# ══════════════════════════════════════════════════════
class TitleScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        top = Text("STATEMENT OF ACCOUNT", font_size=52,
                   color=GOLD, weight=BOLD)
        mid = Text("Chilimba Traders  →  Banda Stores",
                   font_size=24, color=TEAL)
        mid.next_to(top, DOWN, buff=0.3)
        line = Line(LEFT*4.5, RIGHT*4.5, color=TEAL, stroke_width=2)
        line.next_to(mid, DOWN, buff=0.25)
        bot = Text("June 2025  |  Business Studies", font_size=18, color=GRAY)
        bot.next_to(line, DOWN, buff=0.25)

        self.play(Write(top, run_time=1.4))
        self.play(FadeIn(mid, shift=UP*0.3), Create(line))
        self.play(FadeIn(bot))
        self.wait(2)
        self.play(FadeOut(VGroup(top, mid, line, bot)))


# ══════════════════════════════════════════════════════
# SCENE 2 – What is a Statement of Account?
# ══════════════════════════════════════════════════════
class ConceptScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("What is a Statement of Account?",
                     font_size=30, color=GOLD, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(Write(title))

        bullets = [
            ("📄", "A document sent by a SELLER to a BUYER",           TEAL),
            ("📋", "Summarises all transactions in a given period",      WHITE),
            ("➕", "Debits = amounts the buyer OWES (invoices)",         BLUE),
            ("➖", "Credits = amounts deducted (returns, discounts, cash)", PINK),
            ("💰", "Closing balance = amount still owed at period end",  GOLD),
        ]

        for i, (icon, text, col) in enumerate(bullets):
            ico = Text(icon, font_size=22)
            txt = Text(text, font_size=19, color=col)
            row = VGroup(ico, txt).arrange(RIGHT, buff=0.25)
            row.move_to([0, 2.0 - i*0.7, 0])
            box = SurroundingRectangle(row, color=col, buff=0.12,
                                       corner_radius=0.08, stroke_width=0.8)
            self.play(FadeIn(VGroup(row, box), shift=RIGHT*0.3, run_time=0.5))
            self.wait(0.4)

        self.wait(1.5)
        self.play(FadeOut(*self.mobjects))


# ══════════════════════════════════════════════════════
# SCENE 3 – Transaction-by-transaction explanation
# ══════════════════════════════════════════════════════
class TransactionScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        header = Text("Step 1 – Understanding Each Transaction",
                      font_size=26, color=GOLD, weight=BOLD).to_edge(UP, buff=0.3)
        self.play(Write(header))

        running = 0
        for date, short, detail, col, sign in EXPLANATIONS:
            # amount from TRANSACTIONS table
            row = next(r for r in TRANSACTIONS if r[0] == date)
            amt = row[3] if row[3] else row[4]

            date_txt   = Text(date,  font_size=24, color=col, weight=BOLD)
            short_txt  = Text(short, font_size=20, color=WHITE)
            detail_txt = Text(detail, font_size=16, color=GRAY)
            sign_txt   = Text(f"{sign} {fmt(amt)}", font_size=22,
                              color=GREEN_C if sign == "+" else RED_C, weight=BOLD)

            if sign == "+":
                running += amt
            else:
                running -= amt

            bal_txt = Text(f"Running Balance: {fmt(running)}",
                           font_size=18, color=GOLD)

            date_txt.move_to(UP*2.0)
            short_txt.next_to(date_txt, DOWN, buff=0.15)
            detail_txt.next_to(short_txt, DOWN, buff=0.15)
            sign_txt.next_to(detail_txt, DOWN, buff=0.25)
            bal_txt.next_to(sign_txt, DOWN, buff=0.2)

            box = SurroundingRectangle(sign_txt, color=col, buff=0.1,
                                       corner_radius=0.08)
            grp = VGroup(date_txt, short_txt, detail_txt,
                         sign_txt, box, bal_txt)

            self.play(FadeIn(grp, shift=UP*0.3, run_time=0.6))
            self.wait(1.4)
            self.play(FadeOut(grp, run_time=0.35))

        self.play(FadeOut(header))


# ══════════════════════════════════════════════════════
# SCENE 4 – Full Statement of Account table
# ══════════════════════════════════════════════════════
class StatementScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Step 2 – Statement of Account",
                     font_size=26, color=GOLD, weight=BOLD).to_edge(UP, buff=0.28)
        self.play(Write(title))

        # ── Sender / Receiver block ──────────────────────
        sender = VGroup(
            Text("FROM: Chilimba Traders", font_size=14, color=TEAL),
            Text("P.O. Box 456, Blantyre, Malawi", font_size=12, color=GRAY),
        ).arrange(DOWN, aligned_edge=LEFT)
        receiver = VGroup(
            Text("TO: Banda Stores", font_size=14, color=PINK),
            Text("P.O. Box 789, Zomba", font_size=12, color=GRAY),
        ).arrange(DOWN, aligned_edge=LEFT)
        sender.to_corner(UL, buff=0.5).shift(DOWN*0.7)
        receiver.to_corner(UR, buff=0.5).shift(DOWN*0.7)
        date_hdr = Text("Statement Date: 30 June 2025",
                        font_size=13, color=LAVENDER).to_edge(LEFT, buff=0.5).shift(DOWN*0.05+ UP*0.7)
        self.play(FadeIn(VGroup(sender, receiver, date_hdr)))

        # ── Column headers ────────────────────────────────
        TOP_Y = 1.85
        COL   = [-4.6, -1.0, 1.1, 2.8, 4.6]  # Date, Details, Debit, Credit, Balance
        hdrs  = ["Date", "Details / Ref", "Debit (K)", "Credit (K)", "Balance (K)"]
        hdr_cols = [GOLD, GOLD, BLUE, PINK, TEAL]

        hdr_grp = VGroup()
        for txt, cx, col in zip(hdrs, COL, hdr_cols):
            t = Text(txt, font_size=14, color=col, weight=BOLD).move_to([cx, TOP_Y, 0])
            hdr_grp.add(t)
        self.play(FadeIn(hdr_grp))

        sep1 = Line(LEFT*5.8, RIGHT*5.8, stroke_width=0.8, color=GRAY)
        sep1.move_to([0, TOP_Y - 0.28, 0])
        self.play(Create(sep1))

        # ── Data rows ─────────────────────────────────────
        row_h = 0.44
        all_rows = VGroup()
        for i, (date, detail, ref, dr, cr, bal) in enumerate(TRANSACTIONS):
            y = TOP_Y - 0.55 - i * row_h
            ref_str  = f"{detail}" + (f"  [{ref}]" if ref != "—" else "")
            dr_str   = fmt(dr) if dr else "—"
            cr_str   = fmt(cr) if cr else "—"
            bal_str  = fmt(bal)

            dr_col  = BLUE   if dr else GRAY
            cr_col  = PINK   if cr else GRAY
            bal_col = GREEN_C if bal > 0 else WHITE

            cells = [
                Text(date,    font_size=13, color=WHITE),
                Text(ref_str, font_size=12, color=WHITE),
                Text(dr_str,  font_size=13, color=dr_col),
                Text(cr_str,  font_size=13, color=cr_col),
                Text(bal_str, font_size=13, color=bal_col, weight=BOLD),
            ]
            row_vg = VGroup()
            for cell, cx in zip(cells, COL):
                cell.move_to([cx, y, 0])
                row_vg.add(cell)

            all_rows.add(row_vg)
            self.play(FadeIn(row_vg, shift=RIGHT*0.2, run_time=0.4))

        # ── Total / Closing line ───────────────────────────
        bot_y = TOP_Y - 0.55 - len(TRANSACTIONS)*row_h
        sep2  = Line(LEFT*5.8, RIGHT*5.8, stroke_width=0.8, color=GRAY).move_to([0, bot_y, 0])
        self.play(Create(sep2))

        closing_lbl = Text("AMOUNT DUE:", font_size=15, color=GOLD, weight=BOLD).move_to([COL[2], bot_y-0.38, 0])
        closing_val = Text(fmt(FINAL_BALANCE), font_size=15, color=TEAL, weight=BOLD).move_to([COL[4], bot_y-0.38, 0])
        self.play(FadeIn(VGroup(closing_lbl, closing_val)))

        self.wait(2.8)
        self.play(FadeOut(*self.mobjects))


# ══════════════════════════════════════════════════════
# SCENE 5 – Balance verification waterfall
# ══════════════════════════════════════════════════════
class VerificationScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Step 3 – Balance Verification",
                     font_size=28, color=GOLD, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(Write(title))

        steps = [
            ("Opening balance",          "+", 150_000, 150_000),
            ("+ Invoice (4 Jun)",         "+", 320_000, 470_000),
            ("− Returns (8 Jun)",          "−",  40_000, 430_000),
            ("− Cash receipt (12 Jun)",    "−", 200_000, 230_000),
            ("+ Invoice (18 Jun)",         "+", 180_000, 410_000),
            ("− Discount (22 Jun)",        "−",  20_000, 390_000),
            ("− Cash receipt (27 Jun)",    "−", 150_000, 240_000),
        ]

        prev_y = 2.2
        prev_mob = None
        for label, sign, amt, running in steps:
            color = GREEN_C if sign == "+" else RED_C
            lbl  = Text(label, font_size=17, color=WHITE)
            op   = Text(f"{sign} {fmt(amt)}", font_size=17,
                        color=color, weight=BOLD)
            eq   = Text(f"= {fmt(running)}", font_size=17,
                        color=GOLD, weight=BOLD)
            row  = VGroup(lbl, op, eq).arrange(RIGHT, buff=0.4)
            row.move_to([0, prev_y, 0])
            prev_y -= 0.58

            arrow = None
            if prev_mob is not None:
                arrow = Arrow(prev_mob.get_bottom(), row.get_top(),
                              buff=0.05, color=GRAY,
                              stroke_width=1.5, max_tip_length_to_length_ratio=0.15)
                self.play(Create(arrow, run_time=0.25))

            self.play(FadeIn(row, run_time=0.5))
            prev_mob = row

        # Highlight closing balance
        close_box = SurroundingRectangle(prev_mob, color=TEAL,
                                          buff=0.12, corner_radius=0.1,
                                          stroke_width=2)
        close_txt = Text("Closing Balance  =  K240,000  ✓",
                         font_size=20, color=TEAL, weight=BOLD)
        close_txt.next_to(prev_mob, DOWN, buff=0.45)
        self.play(Create(close_box), Write(close_txt))
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects))


# ══════════════════════════════════════════════════════
# SCENE 6 – Summary
# ══════════════════════════════════════════════════════
class SummaryScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = Text("Solution Summary", font_size=36,
                     color=GOLD, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(Write(title))

        points = [
            ("1.", "Opening balance:  K150,000  (amount owed from May)",    ORANGE),
            ("2.", "Total Debits (invoices):  K320,000 + K180,000 = K500,000",  BLUE),
            ("3.", "Total Credits (returns + cash + discount):  K410,000",   PINK),
            ("4.", "Net closing balance:  K150k + K500k − K410k = K240,000", TEAL),
            ("5.", "Statement sent to BUYER (Banda Stores) by SELLER",       LAVENDER),
            ("6.", "Purpose: remind buyer of amount due & transaction history", WHITE),
        ]

        for i, (num, text, col) in enumerate(points):
            n   = Text(num,  font_size=18, color=col, weight=BOLD)
            t   = Text(text, font_size=16, color=WHITE)
            row = VGroup(n, t).arrange(RIGHT, buff=0.22)
            row.move_to([0, 2.1 - i*0.62, 0])
            box = SurroundingRectangle(row, color=col, buff=0.1,
                                       corner_radius=0.08, stroke_width=0.7)
            self.play(FadeIn(VGroup(row, box), shift=LEFT*0.3, run_time=0.45))
            self.wait(0.3)

        self.wait(2)

        end     = Text("END", font_size=64, color=GOLD, weight=BOLD)
        end_sub = Text("Chilimba Traders  |  Statement of Account  |  June 2025",
                       font_size=17, color=GRAY)
        end_sub.next_to(end, DOWN, buff=0.25)
        self.play(FadeOut(*self.mobjects),
                  FadeIn(VGroup(end, end_sub)))
        self.wait(2.5)


# ══════════════════════════════════════════════════════
# MASTER SCENE
# ══════════════════════════════════════════════════════
class StatementOfAccountSolution(Scene):
    def construct(self):
        for S in [TitleScene, ConceptScene, TransactionScene,
                  StatementScene, VerificationScene, SummaryScene]:
            S.construct(self)
