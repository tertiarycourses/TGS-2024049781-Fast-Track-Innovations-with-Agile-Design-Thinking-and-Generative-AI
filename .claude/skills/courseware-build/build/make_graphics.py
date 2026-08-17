#!/usr/bin/env python3
"""
Generate the course's diagram assets (matplotlib, Arial, white background,
Tertiary house palette) into .claude/skills/courseware-build/assets/img/.

These are the visual backbone of the deck: the Double Diamond, the three-mindset
overlap, dual-track agile, the 5-stage DT loop, the GenAI overlay, the cake
release model, feedback loops and the metrics quadrant.

Run:  python3 make_graphics.py
"""
import os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle, FancyBboxPatch, Polygon, Wedge
from matplotlib.lines import Line2D

plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.sans-serif"] = ["Arial", "Helvetica", "DejaVu Sans"]

BLUE   = "#1F6FEB"
TEAL   = "#10B981"
VIOLET = "#7C3AED"
AMBER  = "#F59E0B"
RED    = "#DC2626"
INK    = "#161B26"
GREY   = "#5B6372"
LIGHT  = "#F5F8FC"
LINE   = "#D7E0EA"

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(os.path.dirname(HERE), "assets", "img")
os.makedirs(OUT, exist_ok=True)


def _save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  wrote", name)
    return p


def _ax(w=12, h=6.2):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")
    ax.axis("off")
    return fig, ax


def _box(ax, x, y, w, h, label, sub="", color=BLUE, fill=None, fs=13, subfs=10.5, r=0.04):
    fill = fill if fill else "white"
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle=f"round,pad=0.01,rounding_size={r}",
                 linewidth=2, edgecolor=color, facecolor=fill, zorder=2))
    ty = y + h / 2 + (0.11 if sub else 0)
    ax.text(x + w / 2, ty, label, ha="center", va="center",
            fontsize=fs, fontweight="bold", color=color, zorder=3)
    if sub:
        ax.text(x + w / 2, y + h / 2 - 0.15, sub, ha="center", va="center",
                fontsize=subfs, color=GREY, zorder=3, wrap=True)


def _arrow(ax, x1, y1, x2, y2, color=GREY, lw=2.0, style="-|>", ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                 mutation_scale=18, linewidth=lw, color=color,
                 linestyle=ls, zorder=1, shrinkA=2, shrinkB=2))


# ------------------------------------------------------------------ 1. Double Diamond
def double_diamond():
    fig, ax = _ax(12.6, 5.6)
    ax.set_xlim(0, 12.6); ax.set_ylim(0, 5.6)

    def diamond(cx, half_w, cy, half_h, color, alpha=0.13):
        pts = [(cx - half_w, cy), (cx, cy + half_h), (cx + half_w, cy), (cx, cy - half_h)]
        ax.add_patch(Polygon(pts, closed=True, facecolor=color, alpha=alpha,
                             edgecolor=color, linewidth=2.2, zorder=1))

    cy, hh = 3.05, 1.5
    diamond(3.0, 2.55, cy, hh, BLUE)
    diamond(8.6, 2.55, cy, hh, TEAL)

    ax.text(3.0, 5.05, "PROBLEM SPACE", ha="center", fontsize=12.5,
            fontweight="bold", color=BLUE)
    ax.text(8.6, 5.05, "SOLUTION SPACE", ha="center", fontsize=12.5,
            fontweight="bold", color=TEAL)

    for x, t, c in [(1.55, "Discover", BLUE), (4.45, "Define", BLUE),
                    (7.15, "Develop", TEAL), (10.05, "Deliver", TEAL)]:
        ax.text(x, cy + 0.02, t, ha="center", va="center", fontsize=13.5,
                fontweight="bold", color=c)

    ax.text(3.0, 1.15, "Diverge  →  Converge", ha="center", fontsize=10.5, color=GREY, style="italic")
    ax.text(8.6, 1.15, "Diverge  →  Converge", ha="center", fontsize=10.5, color=GREY, style="italic")

    ax.text(3.0, 0.52, "Are we solving\nthe RIGHT PROBLEM?", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color=INK)
    ax.text(8.6, 0.52, "Are we building\nthe RIGHT SOLUTION?", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color=INK)

    _arrow(ax, 0.35, cy, 0.5, cy, color=GREY)
    ax.text(0.18, cy + 0.42, "Brief", fontsize=10, color=GREY, ha="center")
    _arrow(ax, 11.2, cy, 11.9, cy, color=VIOLET, lw=2.4)
    ax.text(12.0, cy + 0.45, "AGILE\nDELIVERY", fontsize=10.5, color=VIOLET,
            ha="center", va="center", fontweight="bold")
    ax.text(12.0, cy - 0.5, "Are we building\nit RIGHT?", fontsize=9.2, color=GREY, ha="center", va="center")
    return _save(fig, "double-diamond.png")


# ------------------------------------------------------------------ 2. Three mindsets overlap
def three_mindsets():
    fig, ax = _ax(11.2, 6.4)
    ax.set_xlim(0, 11.2); ax.set_ylim(0, 6.4)
    r = 1.95
    centres = {"DESIGN THINKING": (4.2, 4.05, BLUE),
               "LEAN": (7.0, 4.05, TEAL),
               "AGILE": (5.6, 2.05, VIOLET)}
    for name, (cx, cy, col) in centres.items():
        ax.add_patch(Circle((cx, cy), r, facecolor=col, alpha=0.16,
                            edgecolor=col, linewidth=2.4, zorder=1))
    ax.text(3.05, 5.35, "DESIGN\nTHINKING", ha="center", va="center",
            fontsize=13, fontweight="bold", color=BLUE, zorder=4)
    ax.text(8.15, 5.35, "LEAN", ha="center", va="center",
            fontsize=13, fontweight="bold", color=TEAL, zorder=4)
    ax.text(5.6, 0.92, "AGILE", ha="center", va="center",
            fontsize=13, fontweight="bold", color=VIOLET, zorder=4)

    ax.text(3.05, 4.75, "explore & solve\nthe right problem", ha="center", va="center",
            fontsize=9.6, color=GREY, zorder=4)
    ax.text(8.15, 4.75, "test beliefs,\nlearn the right outcome", ha="center", va="center",
            fontsize=9.6, color=GREY, zorder=4)
    ax.text(5.6, 1.42, "adapt to change\nas we build", ha="center", va="center",
            fontsize=9.6, color=GREY, zorder=4)

    ax.text(5.6, 3.42, "INNOVATION\nTHAT SHIPS", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color=INK, zorder=5)
    ax.text(5.6, 0.18, "Three mindsets, one team — it is not 'or', it is 'and'.",
            ha="center", fontsize=10.5, color=GREY, style="italic")
    return _save(fig, "three-mindsets.png")


# ------------------------------------------------------------------ 3. Design Thinking 5 stages
def dt_five_stages():
    fig, ax = _ax(12.6, 4.5)
    ax.set_xlim(0, 12.6); ax.set_ylim(0, 4.5)
    stages = [("1", "EMPATHISE", "Understand the\nuser's world", BLUE),
              ("2", "DEFINE", "Frame the\nreal problem", VIOLET),
              ("3", "IDEATE", "Generate many\noptions", AMBER),
              ("4", "PROTOTYPE", "Build to think,\ncheap and fast", TEAL),
              ("5", "TEST", "Learn from\nreal users", RED)]
    w, gap, y = 2.15, 0.42, 1.62
    x = 0.28
    for num, title, sub, col in stages:
        _box(ax, x, y, w, 1.55, "", "", color=col, fill=LIGHT)
        ax.add_patch(Circle((x + w / 2, y + 1.18), 0.235, facecolor=col,
                            edgecolor="none", zorder=4))
        ax.text(x + w / 2, y + 1.18, num, ha="center", va="center",
                fontsize=11.5, fontweight="bold", color="white", zorder=5)
        ax.text(x + w / 2, y + 0.74, title, ha="center", va="center",
                fontsize=12, fontweight="bold", color=col, zorder=5)
        ax.text(x + w / 2, y + 0.33, sub, ha="center", va="center",
                fontsize=9.4, color=GREY, zorder=5)
        if x + w + gap < 12.4:
            _arrow(ax, x + w + 0.06, y + 0.78, x + w + gap - 0.06, y + 0.78, color=LINE, lw=2.6)
        x += w + gap

    ax.annotate("", xy=(1.35, 1.42), xytext=(11.3, 1.42),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.6,
                                connectionstyle="arc3,rad=0.28", linestyle="--"))
    ax.text(6.3, 0.38, "Iterate — the loop is non-linear; any test can send you back to empathise.",
            ha="center", fontsize=10.4, color=GREY, style="italic")
    ax.text(6.3, 3.92, "THE FIVE STAGES OF DESIGN THINKING", ha="center",
            fontsize=12.5, fontweight="bold", color=INK)
    return _save(fig, "dt-five-stages.png")


# ------------------------------------------------------------------ 4. Dual-track agile
def dual_track():
    fig, ax = _ax(12.4, 5.4)
    ax.set_xlim(0, 12.4); ax.set_ylim(0, 5.4)

    ax.add_patch(FancyBboxPatch((0.3, 3.05), 11.8, 1.85,
                 boxstyle="round,pad=0.02,rounding_size=0.06",
                 facecolor=BLUE, alpha=0.07, edgecolor=BLUE, linewidth=2))
    ax.add_patch(FancyBboxPatch((0.3, 0.62), 11.8, 1.85,
                 boxstyle="round,pad=0.02,rounding_size=0.06",
                 facecolor=VIOLET, alpha=0.07, edgecolor=VIOLET, linewidth=2))

    ax.text(0.62, 4.62, "DISCOVERY TRACK", fontsize=12.5, fontweight="bold", color=BLUE)
    ax.text(0.62, 4.30, "fast learning & validation  ·  should we build this, and what exactly?",
            fontsize=9.8, color=GREY)
    ax.text(0.62, 2.18, "DELIVERY TRACK", fontsize=12.5, fontweight="bold", color=VIOLET)
    ax.text(0.62, 1.86, "predictability & quality  ·  how do we build this well?",
            fontsize=9.8, color=GREY)

    dx = [("Interview", 1.9), ("Prototype", 3.85), ("Test", 5.8), ("Kill / keep", 7.75), ("Validated item", 9.9)]
    for label, x in dx:
        ax.add_patch(Circle((x, 3.62), 0.30, facecolor="white", edgecolor=BLUE, linewidth=2, zorder=3))
        ax.add_patch(Polygon([(x, 3.775), (x + 0.145, 3.62), (x, 3.465), (x - 0.145, 3.62)],
                             closed=True, facecolor=BLUE, edgecolor="none", zorder=4))
        ax.text(x, 3.12, label, ha="center", fontsize=9.3, color=INK, zorder=4)
    for i in range(len(dx) - 1):
        _arrow(ax, dx[i][1] + 0.32, 3.62, dx[i + 1][1] - 0.32, 3.62, color=BLUE, lw=1.6)

    for i, x in enumerate([2.4, 4.9, 7.4, 9.9]):
        _box(ax, x - 1.0, 0.82, 2.0, 0.78, f"Sprint {i+1}", "", color=VIOLET, fill="white", fs=11.5)
    for i, x in enumerate([2.4, 4.9, 7.4]):
        _arrow(ax, x + 1.02, 1.21, x + 1.48, 1.21, color=VIOLET, lw=1.8)

    for x in [5.8, 7.75, 9.9]:
        _arrow(ax, x, 3.30, x - 0.35, 1.68, color=TEAL, lw=1.9, ls=(0, (4, 2)))
    ax.text(11.55, 2.62, "validated\nbacklog items", fontsize=9.4, color=TEAL,
            ha="center", va="center", fontweight="bold")

    ax.text(6.2, 0.18, "One team, two tracks, running simultaneously — discovery feeds delivery, never a handoff.",
            ha="center", fontsize=10.4, color=GREY, style="italic")
    return _save(fig, "dual-track-agile.png")


# ------------------------------------------------------------------ 5. GenAI overlay on the DT loop
def genai_overlay():
    fig, ax = _ax(12.6, 5.4)
    ax.set_xlim(0, 12.6); ax.set_ylim(0, 5.4)
    stages = [("EMPATHISE", "Synthesise interview\ntranscripts & notes", BLUE),
              ("DEFINE", "Generate & stress-test\nproblem reframes", VIOLET),
              ("IDEATE", "Multiply ideas,\nanalogical prompting", AMBER),
              ("PROTOTYPE", "Draft copy, flows\nand mock screens", TEAL),
              ("TEST", "Cluster feedback,\ndraft test scripts", RED)]
    w, gap = 2.15, 0.42
    x = 0.28
    for title, ai, col in stages:
        _box(ax, x, 3.15, w, 1.05, title, "", color=col, fill="white", fs=12)
        ax.add_patch(FancyBboxPatch((x, 1.28), w, 1.42,
                     boxstyle="round,pad=0.01,rounding_size=0.04",
                     facecolor=col, alpha=0.10, edgecolor=col, linewidth=1.6))
        ax.text(x + w / 2, 1.99, ai, ha="center", va="center", fontsize=9.3, color=INK)
        _arrow(ax, x + w / 2, 3.10, x + w / 2, 2.76, color=col, lw=1.8)
        x += w + gap

    ax.text(6.3, 4.92, "WHERE GENERATIVE AI ACCELERATES THE LOOP", ha="center",
            fontsize=12.5, fontweight="bold", color=INK)
    ax.text(6.3, 4.52, "AI amplifies the discipline — it does not replace the judgement.",
            ha="center", fontsize=10.2, color=GREY, style="italic")
    ax.add_patch(FancyBboxPatch((0.28, 0.28), 11.84, 0.72,
                 boxstyle="round,pad=0.01,rounding_size=0.05",
                 facecolor=AMBER, alpha=0.13, edgecolor=AMBER, linewidth=1.8))
    ax.text(6.2, 0.64, "HUMAN STAYS ACCOUNTABLE:  empathy, ethical judgement, the decision to proceed, and validation against real users.",
            ha="center", va="center", fontsize=10.3, fontweight="bold", color=INK)
    return _save(fig, "genai-overlay.png")


# ------------------------------------------------------------------ 6. Cupcake / birthday / wedding
def cake_releases():
    fig, ax = _ax(11.6, 5.2)
    ax.set_xlim(0, 11.6); ax.set_ylim(0, 5.2)
    specs = [("CUPCAKE", "Release 1", "Complete and satisfying\nat small scale", TEAL, 1.05, 1.5),
             ("BIRTHDAY CAKE", "Release 2", "Broader value,\nmore users served", BLUE, 1.75, 3.9),
             ("WEDDING CAKE", "Release 3", "The full realised\nvision at scale", VIOLET, 2.5, 7.1)]
    for name, rel, sub, col, h, cx in specs:
        base_w = 1.05 + h * 0.42
        layers = 1 if name == "CUPCAKE" else (2 if "BIRTHDAY" in name else 3)
        for li in range(layers):
            lw_ = base_w * (1 - li * 0.22)
            lh = h / layers * 0.86
            ly = 1.12 + li * (h / layers)
            ax.add_patch(FancyBboxPatch((cx - lw_ / 2, ly), lw_, lh,
                         boxstyle="round,pad=0.01,rounding_size=0.05",
                         facecolor=col, alpha=0.20 + li * 0.14,
                         edgecolor=col, linewidth=2, zorder=2))
        ax.text(cx, 0.82, name, ha="center", fontsize=12, fontweight="bold", color=col)
        ax.text(cx, 0.50, rel, ha="center", fontsize=10, color=INK, fontweight="bold")
        ax.text(cx, 0.14, sub, ha="center", fontsize=9.2, color=GREY)

    for x1, x2 in [(2.15, 2.75), (5.35, 5.95)]:
        _arrow(ax, x1, 2.0, x2, 2.0, color=GREY, lw=2.0)

    ax.text(9.9, 3.5, "Every release is\na WHOLE cake —\nnot a slice of an\nunfinished one.",
            ha="center", va="center", fontsize=11, color=INK, fontweight="bold")
    ax.add_patch(FancyBboxPatch((8.55, 2.55), 2.7, 1.95,
                 boxstyle="round,pad=0.02,rounding_size=0.06",
                 facecolor=AMBER, alpha=0.12, edgecolor=AMBER, linewidth=1.8, zorder=1))
    ax.text(5.8, 4.85, "RELEASE PRIORITISATION — THE THREE-CAKE MODEL", ha="center",
            fontsize=12.5, fontweight="bold", color=INK)
    return _save(fig, "cake-releases.png")


# ------------------------------------------------------------------ 7. Feedback loops
def feedback_loops():
    fig, ax = _ax(11.6, 4.9)
    ax.set_xlim(0, 11.6); ax.set_ylim(0, 4.9)

    def loop(cx, title, col, nodes, sign):
        ax.text(cx, 4.42, title, ha="center", fontsize=12.5, fontweight="bold", color=col)
        r = 1.32
        cy = 2.25
        for i, n in enumerate(nodes):
            a = math.pi / 2 - i * (2 * math.pi / len(nodes))
            x, y = cx + r * math.cos(a), cy + r * math.sin(a)
            ax.add_patch(FancyBboxPatch((x - 0.82, y - 0.28), 1.64, 0.56,
                         boxstyle="round,pad=0.01,rounding_size=0.06",
                         facecolor="white", edgecolor=col, linewidth=1.8, zorder=3))
            ax.text(x, y, n, ha="center", va="center", fontsize=9.4, color=INK, zorder=4)
        for i in range(len(nodes)):
            a1 = math.pi / 2 - i * (2 * math.pi / len(nodes))
            a2 = math.pi / 2 - (i + 1) * (2 * math.pi / len(nodes))
            x1, y1 = cx + r * 0.99 * math.cos(a1), cy + r * 0.99 * math.sin(a1)
            x2, y2 = cx + r * 0.99 * math.cos(a2), cy + r * 0.99 * math.sin(a2)
            ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                         mutation_scale=15, linewidth=1.9, color=col,
                         connectionstyle="arc3,rad=-0.30", zorder=2,
                         shrinkA=26, shrinkB=26))
        ax.add_patch(Circle((cx, cy), 0.42, facecolor=col, alpha=0.14,
                            edgecolor=col, linewidth=1.6, zorder=2))
        ax.text(cx, cy, sign, ha="center", va="center", fontsize=17,
                fontweight="bold", color=col, zorder=4)

    loop(3.0, "REINFORCING LOOP", RED,
         ["Ship faster", "Skip validation", "Rework grows", "More pressure"], "R")
    loop(8.6, "BALANCING LOOP", TEAL,
         ["Ship faster", "Quality gate", "Defects caught", "Pace corrected"], "B")

    ax.text(5.8, 0.24, "A reinforcing loop amplifies; a balancing loop stabilises. Systemic failure is a reinforcing loop with no balancing counterpart.",
            ha="center", fontsize=10.3, color=GREY, style="italic")
    return _save(fig, "feedback-loops.png")


# ------------------------------------------------------------------ 8. Metrics quadrant
def metrics_quadrant():
    fig, ax = _ax(10.8, 5.6)
    ax.set_xlim(0, 10.8); ax.set_ylim(0, 5.6)
    ax.add_patch(Rectangle((1.5, 0.9), 7.8, 3.9, facecolor="white",
                           edgecolor=LINE, linewidth=1.6))
    ax.plot([5.4, 5.4], [0.9, 4.8], color=LINE, lw=1.4)
    ax.plot([1.5, 9.3], [2.85, 2.85], color=LINE, lw=1.4)

    quads = [(3.45, 3.85, "VANITY", "Rises reliably,\nchanges nothing", RED),
             (7.35, 3.85, "DECISION-GRADE", "Moves → a decision\nchanges", TEAL),
             (3.45, 1.85, "NOISE", "Neither actionable\nnor meaningful", GREY),
             (7.35, 1.85, "LAGGING TRUTH", "Real but too late\nto steer", AMBER)]
    for x, y, t, s, c in quads:
        ax.text(x, y + 0.32, t, ha="center", fontsize=12, fontweight="bold", color=c)
        ax.text(x, y - 0.22, s, ha="center", fontsize=9.6, color=GREY)

    ax.text(5.4, 0.42, "DOES IT CHANGE A DECISION?  →", ha="center",
            fontsize=10.6, fontweight="bold", color=INK)
    ax.text(0.95, 2.85, "IS IT TIMELY?  →", rotation=90, ha="center", va="center",
            fontsize=10.6, fontweight="bold", color=INK)
    ax.text(5.4, 5.22, "THE INNOVATION METRIC TEST", ha="center",
            fontsize=12.5, fontweight="bold", color=INK)
    ax.text(5.4, 4.93, "\"If a measurement matters at all, it must have some conceivable effect on decisions and behaviour.\" — Hubbard",
            ha="center", fontsize=9.6, color=GREY, style="italic")
    return _save(fig, "metrics-quadrant.png")


# ------------------------------------------------------------------ 9. Problem-Assumption model
def problem_assumption():
    fig, ax = _ax(11.8, 4.4)
    ax.set_xlim(0, 11.8); ax.set_ylim(0, 4.4)
    items = [("1", "What's the\nPROBLEM?", BLUE),
             ("2", "How might we\nSOLVE it?", VIOLET),
             ("3", "What ASSUMPTIONS\nhave we made?", AMBER),
             ("4", "How will we TEST\nthose assumptions?", TEAL)]
    w, gap, x, y = 2.55, 0.42, 0.35, 1.15
    for num, label, col in items:
        ax.add_patch(FancyBboxPatch((x, y), w, 1.85,
                     boxstyle="round,pad=0.01,rounding_size=0.06",
                     facecolor=LIGHT, edgecolor=col, linewidth=2.2, zorder=2))
        ax.add_patch(Rectangle((x, y), 0.10, 1.85, facecolor=col, edgecolor="none", zorder=3))
        ax.add_patch(Circle((x + 0.52, y + 1.42), 0.245, facecolor=col, edgecolor="none", zorder=4))
        ax.text(x + 0.52, y + 1.42, num, ha="center", va="center",
                fontsize=12, fontweight="bold", color="white", zorder=5)
        ax.text(x + w / 2 + 0.10, y + 0.66, label, ha="center", va="center",
                fontsize=11.4, fontweight="bold", color=INK, zorder=5)
        if x + w + gap < 11.6:
            _arrow(ax, x + w + 0.05, y + 0.92, x + w + gap - 0.05, y + 0.92, color=LINE, lw=2.4)
        x += w + gap

    ax.text(5.9, 3.72, "THE PROBLEM-ASSUMPTION MODEL", ha="center",
            fontsize=12.8, fontweight="bold", color=INK)
    ax.text(5.9, 3.38, "Schneider & O'Reilly — the bridge from Design Thinking into Lean validation",
            ha="center", fontsize=10.2, color=GREY, style="italic")
    ax.text(5.9, 0.42, "Every assumption you cannot test is a risk you have chosen not to see.",
            ha="center", fontsize=10.5, color=GREY, style="italic")
    return _save(fig, "problem-assumption.png")


# ------------------------------------------------------------------ 10. Three validations
def three_validations():
    fig, ax = _ax(11.4, 4.6)
    ax.set_xlim(0, 11.4); ax.set_ylim(0, 4.6)
    items = [("PROBLEM\nVALIDATION", "Does this problem\ngenuinely exist\nand matter?", BLUE),
             ("SOLUTION\nVALIDATION", "Does this solution\nactually solve it\nfor those people?", TEAL),
             ("DEMAND\nVALIDATION", "Will enough people\nadopt it — or\npay for it?", VIOLET)]
    w, gap, x, y = 3.35, 0.55, 0.55, 0.95
    for title, sub, col in items:
        ax.add_patch(FancyBboxPatch((x, y), w, 2.35,
                     boxstyle="round,pad=0.02,rounding_size=0.07",
                     facecolor=col, alpha=0.09, edgecolor=col, linewidth=2.2, zorder=2))
        ax.text(x + w / 2, y + 1.78, title, ha="center", va="center",
                fontsize=12.2, fontweight="bold", color=col, zorder=4)
        ax.text(x + w / 2, y + 0.86, sub, ha="center", va="center",
                fontsize=10.2, color=INK, zorder=4)
        x += w + gap

    ax.text(5.7, 4.16, "THREE SEPARATE CONCERNS — THREE DIFFERENT TESTS", ha="center",
            fontsize=12.6, fontweight="bold", color=INK)
    ax.text(5.7, 0.42, "A good prototype test proves the solution works. It says nothing about how many people have the problem.",
            ha="center", fontsize=10.4, color=GREY, style="italic")
    return _save(fig, "three-validations.png")


# ------------------------------------------------------------------ 11. Empathy map
def empathy_map():
    fig, ax = _ax(9.8, 5.6)
    ax.set_xlim(0, 9.8); ax.set_ylim(0, 5.6)
    cx, cy = 4.9, 3.05
    quads = [("SAYS", 2.55, 4.05, BLUE), ("THINKS", 7.25, 4.05, VIOLET),
             ("DOES", 2.55, 2.05, TEAL), ("FEELS", 7.25, 2.05, AMBER)]
    ax.add_patch(Rectangle((0.5, 1.05), 8.8, 4.0, facecolor="white",
                           edgecolor=LINE, linewidth=1.8))
    ax.plot([cx, cx], [1.05, 5.05], color=LINE, lw=1.6)
    ax.plot([0.5, 9.3], [3.05, 3.05], color=LINE, lw=1.6)
    for t, x, y, c in quads:
        ax.text(x, y + 0.42, t, ha="center", fontsize=13, fontweight="bold", color=c)
    ax.text(2.55, 3.62, "Quotes — what they\nsay out loud", ha="center", fontsize=9.4, color=GREY)
    ax.text(7.25, 3.62, "Beliefs they don't\nsay out loud", ha="center", fontsize=9.4, color=GREY)
    ax.text(2.55, 1.62, "Observable\nbehaviour", ha="center", fontsize=9.4, color=GREY)
    ax.text(7.25, 1.62, "Emotional\nstate", ha="center", fontsize=9.4, color=GREY)
    ax.add_patch(Circle((cx, cy), 0.62, facecolor="white", edgecolor=INK, linewidth=2, zorder=4))
    ax.text(cx, cy, "USER", ha="center", va="center", fontsize=11.5,
            fontweight="bold", color=INK, zorder=5)
    ax.text(4.9, 5.35, "THE EMPATHY MAP", ha="center", fontsize=12.8,
            fontweight="bold", color=INK)
    ax.text(4.9, 0.58, "PAINS — obstacles and frustrations          GAINS — what success looks like to them",
            ha="center", fontsize=10.2, color=GREY, fontweight="bold")
    ax.text(4.9, 0.20, "Look for the contradiction between what they SAY and what they DO — that gap is the insight.",
            ha="center", fontsize=9.8, color=GREY, style="italic")
    return _save(fig, "empathy-map.png")


# ------------------------------------------------------------------ 12. Scrum loop
def scrum_loop():
    fig, ax = _ax(12.2, 4.8)
    ax.set_xlim(0, 12.2); ax.set_ylim(0, 4.8)
    _box(ax, 0.35, 2.05, 2.1, 1.25, "Product\nBacklog", "", color=BLUE, fill=LIGHT, fs=11.5)
    _box(ax, 3.05, 2.05, 2.1, 1.25, "Sprint\nPlanning", "", color=VIOLET, fill=LIGHT, fs=11.5)
    ax.add_patch(FancyBboxPatch((5.75, 1.55), 3.3, 2.25,
                 boxstyle="round,pad=0.02,rounding_size=0.07",
                 facecolor=TEAL, alpha=0.10, edgecolor=TEAL, linewidth=2.2))
    ax.text(7.4, 3.44, "SPRINT  (1–4 weeks)", ha="center", fontsize=11.5,
            fontweight="bold", color=TEAL)
    ax.text(7.4, 2.92, "Daily Scrum — 15 min", ha="center", fontsize=10, color=INK)
    ax.text(7.4, 2.52, "Build the increment", ha="center", fontsize=10, color=INK)
    ax.text(7.4, 2.12, "Inspect & adapt daily", ha="center", fontsize=10, color=INK)
    _box(ax, 9.65, 2.05, 2.2, 1.25, "Increment\n+ Review", "", color=AMBER, fill=LIGHT, fs=11.5)

    for x1, x2 in [(2.47, 3.03), (5.17, 5.73), (9.07, 9.63)]:
        _arrow(ax, x1, 2.68, x2, 2.68, color=GREY, lw=2.0)
    ax.annotate("", xy=(1.4, 1.98), xytext=(10.75, 1.98),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.8,
                                connectionstyle="arc3,rad=0.22", linestyle="--"))
    ax.text(6.1, 0.72, "Retrospective feeds the next sprint — inspect and adapt",
            ha="center", fontsize=10.2, color=GREY, style="italic")
    ax.text(6.1, 4.35, "THE SCRUM LOOP", ha="center", fontsize=12.8,
            fontweight="bold", color=INK)
    return _save(fig, "scrum-loop.png")


if __name__ == "__main__":
    print("Generating course graphics →", OUT)
    double_diamond(); three_mindsets(); dt_five_stages(); dual_track()
    genai_overlay(); cake_releases(); feedback_loops(); metrics_quadrant()
    problem_assumption(); three_validations(); empathy_map(); scrum_loop()
    print("Done.")
