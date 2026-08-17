# Fast-Track Innovations with Agile Design Thinking and Generative AI (GenAI)

**WSQ Course Code: TGS-2024049781** · 2 days (16 training hours + 2 hours assessment)
Conducted by **Tertiary Infotech Academy Pte Ltd** (UEN 201200696W)

[![Course](https://img.shields.io/badge/WSQ-TGS--2024049781-1F6FEB)](https://www.tertiarycourses.com.sg/wsq-fast-track-innovations-with-agile-design-thinking-and-generative-ai-genai.html)
[![Duration](https://img.shields.io/badge/Duration-2%20days%20%C2%B7%2016h-10B981)](#lesson-plan)
[![Activities](https://img.shields.io/badge/Activities-12%20case%20studies-7C3AED)](#activities)
[![SkillsFuture](https://img.shields.io/badge/SkillsFuture-Funded-F59E0B)](https://courses.myskillsfuture.gov.sg/courses/TGS-2024049781)

This repository holds the complete courseware for the WSQ course *Fast-Track Innovations with
Agile Design Thinking and Generative AI (GenAI)* — the trainer slide deck, the Lesson Plan, the
Learner Guide and twelve real-world case-study activities.

---

## What this course teaches

The course sits at the intersection of three disciplines that are routinely confused with one
another, and adds generative AI as an accelerant rather than a replacement:

| Discipline | The question it answers | Its job |
|---|---|---|
| **Design Thinking** | How should we think about this problem? | Find the **right problem** |
| **Lean** | How do we validate this efficiently? | Validate the **right solution** |
| **Agile** | How do we build, scale and improve it? | **Build it right** |
| **Generative AI** | Where can we compress the loop? | Amplify the discipline — never replace the judgement |

It is not "Lean *or* Agile" — it is "and".

## Learning outcomes

- **LO1** — Integrate design thinking methodologies and agile principles to drive organisational innovation using generative AI.
- **LO2** — Synthesise stakeholder inputs to uncover end-user needs for successful innovation.
- **LO3** — Lead design thinking projects using project management tools and techniques to enhance organisational performance.
- **LO4** — Develop strategies for agile design thinking to enhance product and service innovation.

**Skills Framework alignment:** Design Thinking Practice (`ICT-ACE-5014-1.1`) — abilities A1–A7, knowledge K1–K5.

---

## Course outline

### Topic 1 — Foundations of Design Thinking, Agile, and Generative AI
The three mindsets and the question each answers · the Double Diamond · the five stages of design
thinking · wicked problems (Rittel & Webber, 1973) · where generative AI accelerates the loop and
where it must not be trusted · latest trends in innovation.

### Topic 2 — Problem Framing and Ideation
Framing the design challenge · the Problem-Assumption Model (Schneider & O'Reilly) · problem
statement vs Point of View vs How Might We · the altitude test · empathy maps · persona mapping
with GenAI · ideation techniques · prototyping and falsifiable test plans.

### Topic 3 — Agile Development and AI for Rapid Solution Delivery
Being agile vs doing agile · the Scrum loop and its three accountabilities · dual-track agile and
the mini-waterfall anti-pattern · Epic → Feature → Hill → Story → Task · the three C's · the
three-cake release model · story points and velocity · GenAI across the sprint.

### Topic 4 — Scaling and Sustaining Innovations
The three levers that scale innovation · culture and the four principles · stakeholder buy-in ·
resource management with AI · sensemaking · systems thinking and feedback loops · the innovation
metric test · problem vs solution vs demand validation.

---

## Activities

Twelve activities, each built on a **documented real-world case**, each in its own folder with a
Markdown brief and a print-ready PDF. Every brief carries the case, a workplace scenario, detailed
step-by-step instructions, five discussion questions and a trainer debrief.

| # | Activity | Topic | Real-world case |
|---|---|---|---|
| 1 | [Airbnb — Diagnosing Why a Method Alone Does Not Save a Business](activities/activity-01-airbnb-diagnosing-method-alone-does/) | 1 | Airbnb, 2009 — the photography insight |
| 2 | [Netflix vs Blockbuster — Innovation as an Operating System](activities/activity-02-netflix-vs-blockbuster-innovation-as/) | 1 | Blockbuster declines Netflix, 2000 |
| 3 | [Positioning GenAI in the Innovation Loop](activities/activity-03-positioning-genai-innovation-loop-where/) | 1 | AI personas that were plausible and wrong |
| 4 | [GE Adventure Series — Reframing the Problem](activities/activity-04-ge-adventure-series-reframing-problem/) | 2 | GE Healthcare paediatric MRI |
| 5 | [IDEO Shopping Cart — Volume, Then Judgement](activities/activity-05-ideo-shopping-cart-volume-then/) | 2 | IDEO on ABC Nightline, 1999 |
| 6 | [Rapid Prototyping with AI](activities/activity-06-rapid-prototyping-ai-from-concept/) | 2 | A Wizard-of-Oz clinic kiosk test |
| 7 | [Spotify — Reading a Scaling Model Honestly](activities/activity-07-spotify-reading-scaling-model-honestly/) | 3 | Squads, Tribes, Chapters and Guilds |
| 8 | [From Hills to Backlog with GenAI](activities/activity-08-from-hills-backlog-converting-ideas/) | 3 | IBM Design Thinking workshops |
| 9 | [Running Dual-Track Agile — A Sprint Simulation](activities/activity-09-running-dual-track-agile-sprint-simulation/) | 3 | Cagan's "mini-waterfalls inside Scrum" |
| 10 | [DBS Bank — Scaling Innovation Across 25,000 People](activities/activity-10-dbs-bank-scaling-innovation-across/) | 4 | "Make Banking Joyful" |
| 11 | [Boeing 737 MAX — Systems Thinking](activities/activity-11-boeing-737-max-systems-thinking/) | 4 | Local optimisation, systemic failure |
| 12 | [Innovation Metrics — KPIs That Change a Decision](activities/activity-12-innovation-metrics-designing-kpis-that/) | 4 | Two programmes, one budget review |

### Classroom ed-tools

| Tool | Link | Used in |
|---|---|---|
| **Design Thinking Studio** — a shared 5-stage workspace (Empathize · Define · Ideate · Prototype · Test) | https://alfredang.github.io/designthinking/ | Activities 4, 5, 6, 9, 11 |
| **Padlet Classroom Board** — an online board for posting, comparing and voting on group output | https://alfredang.github.io/padlet/ | Activities 1, 2, 3, 7, 8, 10, 12 |

---

## Repository contents

```
courseware/     Trainer slide deck (PPTX + PDF), Lesson Plan (DOCX + PDF), Learner Guide (DOCX + PDF)
activities/     12 activity folders, each with a Markdown brief and a PDF
LG-*.md         The Learner Guide as Markdown (mirrors the DOCX exactly)
.claude/        The single-source build pipeline (see below)
```

The assessment papers and answer keys are **trainer-only** and are deliberately not published here.

## Building the courseware

Every artifact is generated from one content module, so the deck, Lesson Plan, Learner Guide and
activity briefs can never drift apart.

```
.claude/skills/courseware-build/build/
  course_data.py        metadata, learning outcomes, topics, day themes, assessment
  data_domain1..4.py    the 12 activities — case, scenario, steps, questions, debrief
  make_graphics.py      generates the 12 diagrams used across the deck and guide
  build_slides.py       → courseware/<title>-v4.0.pptx
  build_lesson_plan.py  → courseware/LP-<title>.docx
  build_learner_guide.py→ LG-<title>.md + courseware/LG-<title>.docx
  build_activities.py   → activities/activity-NN-*/ (Markdown + PDF)
  build_assessment.py   → assessment/ (trainer-only, not committed)
```

Regenerate everything:

```bash
cd .claude/skills/courseware-build/build
python3 make_graphics.py
python3 build_slides.py
python3 build_lesson_plan.py
python3 build_learner_guide.py
python3 build_activities.py
```

Requires `python-pptx`, `python-docx`, `matplotlib`, `Pillow` and LibreOffice (`soffice`) for PDF rendering.

---

## Course information

| | |
|---|---|
| **Duration** | 2 days · 16 training hours · 2 hours assessment |
| **Timing** | 9:30 am – 6:30 pm (1-hour lunch; tea breaks within training time) |
| **Assessment** | Written Assessment (SAQ, 0.5 h) + Case Study (1 h) — both open book |
| **Prerequisites** | 3 GCE 'O' Level passes including English or WPL Level 5; 1 year working experience; basic computer literacy |
| **Funding** | WSQ 50–70%, SkillsFuture Credit, SFEC, UTAP, PSEA |
| **Certification** | Certificate of Achievement + SSG Statement of Achievement (75% attendance + Competent) |

**Course page:** https://www.tertiarycourses.com.sg/wsq-fast-track-innovations-with-agile-design-thinking-and-generative-ai-genai.html
**MySkillsFuture:** https://courses.myskillsfuture.gov.sg/courses/TGS-2024049781

---

## Further reading

The course content draws on: Jonny Schneider (Thoughtworks) on how Design Thinking, Lean and Agile
work together; Adaptovate on the Design Thinking–Agile relationship; BMC on the three-way
comparison; Burba (2016, *PM Network* 30(10)) on agile by design; UX Magazine on the Double Diamond
and Design Sprints; Steve Perkins (The Design Gym) on culture; PremierAgile on problem finding vs
problem solving; Startup Frontier on the IBM two-day workshop; Rittel & Webber (1973) on wicked
problems; Sy (2007), Patton and Cagan on dual-track agile; Liedtka (UVA Darden) on design thinking
research; and Hubbard on measurement.

---

© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W). All rights reserved.
www.tertiarycourses.com.sg · enquiry@tertiaryinfotech.com · +65 6100 0613
