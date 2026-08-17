#!/usr/bin/env python3
"""
Build the activities/ folder — ONE FOLDER PER ACTIVITY, each containing the
activity brief as Markdown AND as PDF.

    activities/
      README.md                                  index of all 12 activities
      activity-01-airbnb-method-alone/
          activity-01-airbnb-method-alone.md
          activity-01-airbnb-method-alone.pdf
      activity-02-.../
      ...

Each brief carries: the real-world case, the workplace scenario, what you will
produce, the DETAILED step-by-step instructions, the discussion questions, the
completion check and the trainer debrief.

Markdown → HTML → PDF via LibreOffice (soffice), which is already required by the
rest of the courseware pipeline.

Run:  python3 build_activities.py
"""
import os, re, sys, subprocess, shutil

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4
ACT = DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4


def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO = _find_repo(HERE)
OUTDIR = os.path.join(REPO, "activities")
TOPIC_BY_NUM = {t["num"]: t for t in C.TOPICS}
SOFFICE = os.environ.get("SOFFICE", "soffice")

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 10.5pt; color: #161B26; line-height: 1.45; }
h1 { font-size: 18pt; color: #161B26; margin: 0 0 3mm 0; }
h2 { font-size: 13pt; color: #1F6FEB; margin: 5mm 0 2mm 0; }
h3 { font-size: 11.5pt; color: #10B981; margin: 3.5mm 0 1.5mm 0; }
p  { margin: 0 0 2.5mm 0; }
ul, ol { margin: 0 0 3mm 0; padding-left: 7mm; }
li { margin-bottom: 1.8mm; }
.tools { color: #5B6372; }
.footer { font-size: 8.5pt; color: #5B6372; margin-top: 5mm; }
table { border-collapse: collapse; width: 100%; margin: 0 0 3.5mm 0; }
td, th { border: 1px solid #D7E0EA; padding: 2.2mm 3mm; font-size: 10pt; vertical-align: top; }
th { background: #1F6FEB; color: #FFFFFF; font-weight: bold; }
td.k { background: #F5F8FC; font-weight: bold; width: 26%; color: #1F6FEB; }
table.box td { border: none; padding: 3mm 4mm; }
table.case td { background: #F5F8FC; border-left: 4px solid #7C3AED; }
table.scen td { background: #FFFFFF; border: 1.5px solid #10B981; border-left: 4px solid #10B981; }
table.chk  td { background: #FFF8E8; border-left: 4px solid #F59E0B; }
table.deb  td { background: #F5F8FC; border-left: 4px solid #10B981; }
table.rule td { border-bottom: 3px solid #1F6FEB; padding: 0; }
code { font-family: Consolas, monospace; font-size: 9.5pt; color: #0B3060; }
"""



def slug(text, maxwords=5):
    t = re.sub(r"[^a-zA-Z0-9\s-]", "", text.lower())
    words = [w for w in t.split() if w not in
             ("the", "a", "an", "and", "or", "of", "for", "with", "to", "in", "on", "at", "why", "how")]
    return "-".join(words[:maxwords])


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build_md(a):
    tp = TOPIC_BY_NUM[a["topic"]]
    L = []
    L.append(f"# Activity {a['num']} — {a['title']}")
    L.append("")
    L.append(f"**Course:** {C.TITLE}  ")
    L.append(f"**WSQ Course Code:** {C.COURSE_CODE}  ")
    L.append(f"**Topic {tp['code']}:** {tp['title']}  ")
    L.append(f"**Duration:** {a.get('duration', 45)} minutes  ")
    L.append(f"**Group size:** 3–5 participants  ")
    L.append(f"**Tools:** {a['services']}")
    L.append("")
    L.append("## Learning Outcome Addressed")
    L.append("")
    L.append(a["objective"])
    L.append("")
    L.append("## The Real Case")
    L.append("")
    L.append(a["case"])
    L.append("")
    L.append("## Your Scenario")
    L.append("")
    L.append(a["scenario"])
    L.append("")
    L.append("## What You Will Do")
    L.append("")
    L.append(a["desc"])
    L.append("")
    L.append("## What You Will Produce")
    L.append("")
    L.append(a["build"])
    L.append("")
    L.append("## Step-by-Step Instructions")
    L.append("")
    for i, (instr, cmd) in enumerate(a["steps"], 1):
        L.append(f"{i}. {instr}")
        if cmd:
            L.append("")
            L.append(f"   `{cmd}`")
            L.append("")
    L.append("")
    L.append("## Discussion Questions")
    L.append("")
    for i, q in enumerate(a["discussion"], 1):
        L.append(f"{i}. {q}")
    L.append("")
    L.append("## How You Know You Are Done")
    L.append("")
    L.append(a["test"])
    L.append("")
    L.append("## Debrief — What the Room Should Conclude")
    L.append("")
    L.append(a["debrief"])
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"*{C.ORG} ({C.UEN.replace('UEN: ', 'UEN ')}) · {C.COURSE_CODE} · "
             f"Version {C.VERSION} · {C.VERSION_DATE}*")
    L.append("")
    return "\n".join(L)


def _boxtbl(cls, inner):
    """Single-cell table — LibreOffice renders this as ONE unbroken shaded block,
    unlike a CSS-bordered div which it breaks per line."""
    return f"<table class='box {cls}'><tr><td>{inner}</td></tr></table>"


def build_html(a):
    tp = TOPIC_BY_NUM[a["topic"]]
    H = ["<html><head><meta charset='utf-8'><style>", CSS, "</style></head><body>"]
    H.append(f"<h1>Activity {a['num']} — {esc(a['title'])}</h1>")
    H.append("<table class='box rule'><tr><td></td></tr></table>")

    # metadata as a proper 2-column table (no justification stretching)
    H.append("<table>")
    H.append(f"<tr><td class='k'>Course</td><td>{esc(C.TITLE)}</td></tr>")
    H.append(f"<tr><td class='k'>WSQ Course Code</td><td>{C.COURSE_CODE}</td></tr>")
    H.append(f"<tr><td class='k'>Topic</td><td>Topic {tp['code']}: {esc(tp['title'])}</td></tr>")
    H.append(f"<tr><td class='k'>Duration</td><td>{a.get('duration', 45)} minutes &nbsp;·&nbsp; "
             f"Group size: 3–5 participants</td></tr>")
    H.append(f"<tr><td class='k'>Tools</td><td class='tools'>{esc(a['services'])}</td></tr>")
    H.append("</table>")

    H.append("<h2>Learning Outcome Addressed</h2>")
    H.append(f"<p>{esc(a['objective'])}</p>")

    H.append("<h2>The Real Case</h2>")
    H.append(_boxtbl("case", esc(a["case"])))

    H.append("<h2>Your Scenario</h2>")
    H.append(_boxtbl("scen", esc(a["scenario"])))

    H.append("<h2>What You Will Do</h2>")
    H.append(f"<p>{esc(a['desc'])}</p>")
    H.append("<h3>What you will produce</h3>")
    H.append(f"<p>{esc(a['build'])}</p>")

    H.append("<h2>Step-by-Step Instructions</h2><ol>")
    for instr, cmd in a["steps"]:
        item = esc(instr)
        if cmd:
            item += f"<br><code>{esc(cmd)}</code>"
        H.append(f"<li>{item}</li>")
    H.append("</ol>")

    H.append("<h2>Discussion Questions</h2><ol>")
    for q in a["discussion"]:
        H.append(f"<li>{esc(q)}</li>")
    H.append("</ol>")

    H.append("<h2>How You Know You Are Done</h2>")
    H.append(_boxtbl("chk", esc(a["test"])))

    H.append("<h2>Debrief — What the Room Should Conclude</h2>")
    H.append(_boxtbl("deb", esc(a["debrief"])))

    H.append(f"<div class='footer'>{esc(C.ORG)} ({C.UEN.replace('UEN: ', 'UEN ')}) · "
             f"{C.COURSE_CODE} · Version {C.VERSION} · {C.VERSION_DATE}</div>")
    H.append("</body></html>")
    return "\n".join(H)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    made = []
    for a in ACT:
        name = f"activity-{a['num']:02d}-{slug(a['title'])}"
        folder = os.path.join(OUTDIR, name)
        os.makedirs(folder, exist_ok=True)

        md_path = os.path.join(folder, name + ".md")
        with open(md_path, "w") as f:
            f.write(build_md(a))

        html_path = os.path.join(folder, name + ".html")
        with open(html_path, "w") as f:
            f.write(build_html(a))

        subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf",
                        "--outdir", folder, html_path],
                       capture_output=True, timeout=180)
        os.remove(html_path)
        pdf_path = os.path.join(folder, name + ".pdf")
        ok = os.path.exists(pdf_path)
        made.append((a, name, ok))
        print(f"  {'OK ' if ok else 'PDF FAILED'}  {name}")

    # ---------------- index ----------------
    idx = [f"# Activities — {C.TITLE}", "",
           f"**WSQ Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**", "",
           "Twelve real-world case-study activities. Each activity has its own folder containing the "
           "brief as Markdown and as a print-ready PDF.", "",
           "Each brief carries: the documented real-world case, the workplace scenario your group "
           "works on, the detailed step-by-step instructions, the discussion questions, the "
           "completion check and the trainer debrief.", "",
           "## Course Ed-Tools", "",
           "| Tool | URL | Used in |", "|---|---|---|"]
    dt = [a["num"] for a in ACT if "Design Thinking Studio" in a["services"]]
    pd = [a["num"] for a in ACT if "Padlet" in a["services"]]
    idx.append(f"| Design Thinking Studio | https://alfredang.github.io/designthinking/ | "
               f"Activities {', '.join(str(n) for n in dt)} |")
    idx.append(f"| Padlet Classroom Board | https://alfredang.github.io/padlet/ | "
               f"Activities {', '.join(str(n) for n in pd)} |")
    idx += ["", "## The Activities", "",
            "| # | Activity | Topic | Duration | Real-world case | Brief |",
            "|---|---|---|---|---|---|"]
    for a, name, ok in made:
        tp = TOPIC_BY_NUM[a["topic"]]
        case_name = a["case"].split(".")[0][:52]
        idx.append(f"| {a['num']} | {a['title']} | Topic {tp['code']} | "
                   f"{a.get('duration', 45)} min | {case_name}… | "
                   f"[MD]({name}/{name}.md) · [PDF]({name}/{name}.pdf) |")
    idx += ["", "## By Topic", ""]
    for t in C.TOPICS:
        acts = [x for x in ACT if x["topic"] == t["num"]]
        idx.append(f"**Topic {t['code']} — {t['title']}**  ")
        for a in acts:
            idx.append(f"- Activity {a['num']}: {a['title']} ({a.get('duration', 45)} min)")
        idx.append("")
    idx += ["---", "",
            f"*{C.ORG} ({C.UEN.replace('UEN: ', 'UEN ')}) · {C.COURSE_CODE} · "
            f"Version {C.VERSION} · {C.VERSION_DATE}*", ""]
    with open(os.path.join(OUTDIR, "README.md"), "w") as f:
        f.write("\n".join(idx))

    okc = sum(1 for _, _, ok in made if ok)
    print(f"\nBuilt {len(made)} activity folders in {OUTDIR}")
    print(f"PDFs generated: {okc}/{len(made)}")
    print("Index: activities/README.md")


if __name__ == "__main__":
    main()
