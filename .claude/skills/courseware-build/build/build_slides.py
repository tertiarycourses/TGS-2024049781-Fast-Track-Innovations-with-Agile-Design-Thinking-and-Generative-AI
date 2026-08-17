#!/usr/bin/env python3
"""
Build the WSQ Master Trainer slide deck for TGS-2024049781
"Fast-Track Innovations with Agile Design Thinking and Generative AI (GenAI)".

All-white Tertiary Infotech house style. Content is driven entirely by
course_data.py + data_domainN.py so the deck stays 100% aligned with the LP, LG
and the activities/ folder.

House rules honoured here:
  * Visual components only — no bullet walls (tile_grid / img_points / img_full /
    compare_table / process_map / cards3 / case_slide / discussion_slide).
  * Admin block: TRAQOM digital attendance, About the Trainer x2 (General
    template + named trainer), ground rules, lesson plan, learning outcomes,
    briefing BEFORE assessment, assessment, assessment flow, LMS.
  * Assessment admin repeated at the END: Assessment -> Assessment Flow ->
    Digital Attendance -> Thank You.
  * NO step-by-step procedure slides — per the course brief the detailed steps
    live ONLY in the Learner Guide. The deck carries the case, the scenario,
    the discussion questions and the debrief.

Run:  python3 build_slides.py
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# The shared house engine: palette, slide primitives and every visual component.
from engine_helpers import *          # noqa: F401,F403
from engine_helpers import (
    C, ACTIVITIES, REPO, prs, PAGE,
    BLUE, TEAL, AMBER, INK, GREY, LIGHT, WHITE, LINE, VIOLET,
    cover, section, content, two_col, cards3, big_statement, tile_grid, flow_h,
    process_map, decision_map, compare_table, trainer_slide, brk,
    img_points, img_full, case_slide, discussion_slide, debrief_slide,
    edtool_slide, _transition,
)

ACT = {a["num"]: a for a in ACTIVITIES}


# ============================================================ COVER
cover()


# ============================================================ ADMIN
section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "")

tile_grid("Digital Attendance (Mandatory)", [
    ("Three times a day", "Take the AM, PM and Assessment digital attendance — mandatory for every WSQ-funded course."),
    ("Trainer shows the QR", "The trainer or administrator displays the digital attendance QR code from the SSG portal."),
    ("Scan and submit", "Scan the QR code with your mobile phone camera and submit your attendance."),
    ("75% minimum", "A minimum of 75% attendance is required to be eligible for assessment and funding.")],
    kicker="TRAQOM · SSG DIGITAL ATTENDANCE", cols=2, size=15)

trainer_slide("YOUR TRAINER · GENERAL", "Your Trainer",
    "General Trainer template —\nto be completed by the trainer",
    [("Name", ""), ("Title / Designation", ""), ("Qualifications", ""),
     ("Areas of expertise", ""), ("Training & industry experience", ""), ("Contact", "")],
    initials="?", accent=GREY)

trainer_slide("YOUR TRAINER", C.TRAINER,
    "Principal Trainer\nTertiary Infotech Academy Pte Ltd",
    [("Role", "Principal Trainer, Tertiary Infotech Academy Pte Ltd"),
     ("Expertise", "Design thinking, agile innovation, generative AI and applied data science."),
     ("Delivers", "WSQ courses on innovation, design thinking, agile practice and generative AI."),
     ("Founder", "Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
    initials="AA", accent=BLUE)

content("Let's Know Each Other", [
    "Your name, organisation and role.",
    "A product, service or process you are responsible for improving.",
    "Your experience with design thinking, agile or generative AI tools (if any).",
    "One innovation that is currently stuck — we will come back to it on Day 2."],
    kicker="ICE-BREAKER")

tile_grid("Ground Rules", [
    "Set your mobile phone to silent mode.",
    "Participate actively — no question is too small.",
    "Mutual respect: agree to disagree.",
    "One conversation at a time.",
    "Be punctual; return from breaks on time.",
    "75% attendance is required."],
    kicker="HOUSEKEEPING", cols=2, size=15)

tile_grid("Download Your Course Material", [
    ("1 · Go to the LMS portal", "Open https://lms-tms.tertiaryinfotech.com in your browser."),
    ("2 · Log in", "Sign in with the account e-mail you used to register for this course."),
    ("3 · Open this course", "Select 'Fast-Track Innovations with Agile Design Thinking and Generative AI (GenAI)'."),
    ("4 · Download", "Download the Trainer Slides, Learner Guide and Lesson Plan (PDF)."),
    ("5 · Get the activity briefs", "Download the activity PDFs — each carries the case, questions and debrief."),
    ("6 · Keep them open", "You may use these materials during the open-book assessment.")],
    kicker="LMS / TMS  ·  lms-tms.tertiaryinfotech.com", cols=2, size=14)

tile_grid("Skills Framework Alignment", [
    ("TSC Title", C.TSC_TITLE),
    ("TSC Code", C.TSC_CODE),
    ("A1 / A2", "Integrate design thinking into processes; develop strategies to proliferate it across the organisation."),
    ("A3 / A5", "Synthesise information from stakeholders; engage them to uncover motivations and behaviours."),
    ("A4 / A6", "Drive new strategies for products and services; cultivate design thinking to foster innovation."),
    ("A7 · K1–K5", "Lead design thinking projects; trends, innovation management, growth drivers, resources, PM tools.")],
    kicker="SKILLS FRAMEWORK  ·  TSC", cols=2, size=13.5, accent=VIOLET)

two_col("Lesson Plan — 2 Days, 8 hours/day", [
    (f"Day 1 — {C.DAY_THEMES[1]}", 0),
    ("Digital Attendance (AM) · Introductions · Learning Outcomes", 1),
    ("Topic 1: Foundations of DT, Agile and GenAI (Activities 1–3)", 1),
    ("Lunch Break · Digital Attendance (PM)", 1),
    ("Topic 2: Problem Framing and Ideation (Activities 4–6)", 1),
    ("End of Day 1", 1)],
    [(f"Day 2 — {C.DAY_THEMES[2]}", 0),
     ("Digital Attendance (AM)", 1),
     ("Topic 3: Agile Development and AI (Activities 7–9)", 1),
     ("Lunch Break · Digital Attendance (PM)", 1),
     ("Topic 4: Scaling and Sustaining Innovations (Activities 10–12)", 1),
     ("Revision · TRAQOM Survey · Digital Attendance (Assessment)", 1),
     ("Final Assessment (WA + Case Study)", 1)],
    kicker="SCHEDULE", lhead="Day 1", rhead="Day 2")

tile_grid("Learning Outcomes", [
    ("LO1 · Integrate DT + Agile + GenAI", "Integrate design thinking methodologies and agile principles to drive organisational innovation using generative AI."),
    ("LO2 · Synthesise stakeholder inputs", "Synthesise stakeholder inputs to uncover end-user needs for successful innovation."),
    ("LO3 · Lead design thinking projects", "Lead design thinking projects using project management tools and techniques to enhance organisational performance."),
    ("LO4 · Develop agile DT strategies", "Develop strategies for agile design thinking to enhance product and service innovation.")],
    kicker="WHAT YOU'LL ACHIEVE", cols=2, size=14)

tile_grid("Course Outline", [
    ("Topic 1 — Foundations of Design Thinking, Agile and Generative AI",
     "Mindsets and methodologies · product development through DT and Agile · how GenAI enhances both · latest trends."),
    ("Topic 2 — Problem Framing and Ideation",
     "Defining the problem · persona mapping and empathy with GenAI · ideation techniques · AI-driven prototyping."),
    ("Topic 3 — Agile Development and AI for Rapid Solution Delivery",
     "Agile frameworks · converting ideas into features, stories and tasks with GenAI · faster sprints · scaling across teams."),
    ("Topic 4 — Scaling and Sustaining Innovations",
     "Scaling DT and AI across the organisation · stakeholder buy-in · resource management with AI · metrics and KPIs.")],
    kicker="FOUR TOPICS  ·  12 CASE-STUDY ACTIVITIES", cols=1, size=14)

# --- the two ed-tools used throughout the course
edtool_slide("Your Collaboration Tool — Design Thinking Studio",
    "Design Thinking Studio", "https://alfredang.github.io/designthinking/",
    "A shared five-stage design thinking workspace. The whole class works in one live workspace, "
    "posting notes into the Empathize, Define, Ideate, Prototype and Test stages — including a "
    "four-quadrant Empathy Map, How Might We questions with voting, a brainstorming board with "
    "Crazy 8s, and a full prototype and test plan section.",
    ["The trainer clicks Create New Workspace and shares the code or QR.",
     "Click Join Workspace, enter the code, then enter your display name.",
     "Use the stage stepper to move through Empathize → Define → Ideate → Prototype → Test.",
     "Click Add note in any section — give it a Title, Description and optional Category."],
    kicker="ED-TOOL 1 · USED IN ACTIVITIES 4, 5, 6, 9, 11")

edtool_slide("Your Classroom Board — Padlet",
    "Padlet Classroom Board", "https://alfredang.github.io/padlet/",
    "An online classroom board for posting group output, comparing it across groups, and voting. "
    "Posts can carry text, images, links, YouTube videos or PDFs, and can be liked and commented on. "
    "The board is organised into sections and sub-sections, and can be sorted by newest, oldest or "
    "most liked so the strongest thinking rises to the top.",
    ["The trainer creates a classroom and shares the classroom code.",
     "Join the classroom and enter your display name.",
     "Use + to Add post into the section for the current activity.",
     "Like the strongest posts from other groups and comment on their reasoning."],
    kicker="ED-TOOL 2 · USED IN ACTIVITIES 1, 2, 3, 7, 8, 10, 12", accent=VIOLET)

tile_grid("Briefing for Assessment", [
    ("Do · Clear your desk", "Place phones and other materials under the table or on the floor."),
    ("Don't · No recording", "No photos or recording of assessment scripts."),
    ("Don't · No discussion", "Work individually — no discussion during the assessment."),
    ("Do · Black or blue pen", "Use a black or blue pen for hard-copy assessments."),
    ("Don't · No correction fluid", "No liquid paper or correction tape may be used."),
    ("Do · Stop on time", "Scripts are collected when time is up.")],
    kicker="BEFORE YOU START", cols=2, size=14, accent=AMBER)

tile_grid("Assessment", [
    ("Written Assessment (WA)", "Short-Answer Questions (SAQ) · 1 hour · open book. Tests the underpinning knowledge taught in the slides."),
    ("Case Study (CS)", "A scenario-based innovation case · 1 hour · open book. Tests applied judgement across all four topics."),
    ("Open book", "You may use the course slides, the Learner Guide, your activity briefs and approved materials only."),
    ("Eligibility", "A minimum of 75% attendance is required to be eligible for assessment and funding."),
    ("Result", "You are assessed as Competent (C) or Not Yet Competent (NYC) on each instrument."),
    ("Appeals", "An appeal process is available if you wish to contest an assessment outcome.")],
    kicker="FINAL ASSESSMENT", cols=2, size=14)

process_map("Assessment Flow", [
    ("TRAQOM survey", "Scan the QR code on the LMS"),
    ("Digital attendance", "Scan the SSG assessment QR"),
    ("Sit WA then CS", "Open book · 1 hour each"),
    ("Submit on the LMS", "Upload your completed answers"),
    ("Sign the record", "Sign the Assessment Summary Record")],
    kicker="ON ASSESSMENT DAY", color=BLUE,
    synthesis=("REMEMBER", "All five steps are mandatory for WSQ funding — missing the digital attendance or the TRAQOM survey can invalidate your claim."))

tile_grid("Criteria for Funding", [
    ("Attendance", "A minimum attendance rate of 75%, based on the SSG Digital Attendance record."),
    ("Assessment", "Complete both assessment components and be assessed as 'Competent'."),
    ("Digital attendance", "Scan the SSG QR code for AM, PM and Assessment on every training day."),
    ("TRAQOM survey", "Complete the mandatory TRAQOM course feedback survey on the LMS.")],
    kicker="WSQ FUNDING", cols=2, size=15, accent=AMBER)


# ============================================================ TOPIC 1
T = C.TOPICS[0]
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])

big_statement("Your first idea is almost never your best idea.",
    "Design Thinking is the discipline of resisting the first plausible answer long enough to find a better one.",
    "TOPIC 01 · WHY THIS MATTERS", color=BLUE)

img_full("The Three Mindsets of Innovation", "three-mindsets.png",
    kicker="DESIGN THINKING · LEAN · AGILE",
    caption="Design Thinking = explore and solve the RIGHT PROBLEM · Lean = test beliefs to find the RIGHT OUTCOME · Agile = adapt to change and BUILD IT RIGHT.")

compare_table("Design Thinking vs Lean vs Agile",
    ["", "Design Thinking", "Lean Startup", "Agile"],
    [["Primary focus", "Understanding users deeply", "Validating ideas efficiently", "Iterative delivery and adaptation"],
     ["The question it answers", "How should we think about this problem?", "How do we validate this solution efficiently?", "How do we build, scale and improve it?"],
     ["Origin", "Human-centred design practice", "Toyota lean manufacturing", "A counterpoint to Waterfall"],
     ["Core move", "Reframe the problem through empathy", "Build an MVP, let the customer decide value", "Ship increments in short sprints"],
     ["Timeframe", "Flexible — one day to one month", "Rapid, minimal validation cycles", "Sprint-based, continuous"],
     ["Fails when", "It never reaches delivery", "It validates a problem nobody has", "It builds the wrong thing efficiently"]],
    kicker="THE COMPARISON THAT ANCHORS THE COURSE", accent=BLUE,
    note="It is not 'Lean or Agile?' — it is 'and'. All three are mindsets, not processes.")

img_points("The Double Diamond", "double-diamond.png", [
    ("Diamond 1 · Problem space", "Diverge to understand the user, then converge on a clear problem statement."),
    ("Diamond 2 · Solution space", "Diverge to generate many solutions, then converge on the one worth building."),
    ("Then Agile delivers", "Sprints answer the third question: building it right?"),
    ("The discipline", "Never converge before you diverge. The first diamond is the one teams skip.")],
    kicker="THE CORE DIAGRAM OF THE COURSE")

img_full("The Five Stages of Design Thinking", "dt-five-stages.png",
    kicker="EMPATHISE · DEFINE · IDEATE · PROTOTYPE · TEST",
    caption="The stages overlap and repeat continuously — this is a loop you re-enter, not a waterfall you complete once.", accent=TEAL)

tile_grid("What Design Thinking Actually Is", [
    ("A solution-based approach", "It tackles problems that are ill-defined or unknown by understanding the human needs involved."),
    ("Human-centred reframing", "It re-frames the problem in human terms before any solution is proposed."),
    ("Volume then judgement", "It creates many ideas in structured ideation, then converges deliberately."),
    ("Hands-on by default", "It adopts a build-to-think approach through prototyping and testing with real users.")],
    kicker="DEFINITION", cols=2, size=14)

tile_grid("The Abilities That Make a Designer", [
    ("Dealing with ambiguity", "Staying productive when the problem itself is still unclear — the defining skill of the discipline."),
    ("Empathetic learning", "Understanding a user's world from inside their experience, not from a survey summary."),
    ("Synthesis", "Turning a mass of qualitative evidence into a small number of insights you can design against."),
    ("Experimentation", "Treating every belief as testable, and designing the cheapest test that could disprove it.")],
    kicker="CARISSA CARTER · STANFORD d.school", cols=2, size=14, accent=VIOLET)

tile_grid("Wicked Problems — Why Framing Comes First", [
    ("Coined in 1973", "Horst Rittel and Melvin Webber, UC Berkeley professors of design and urban planning."),
    ("Hard to even define", "Abstract challenges with multiple interconnected layers — poverty, climate change, public health."),
    ("No single right answer", "They have no fixed endpoint and no single correct solution, only better and worse responses."),
    ("Tame problems differ", "A tame problem has a knowable answer; reaching for a tame method on a wicked problem is the classic error.")],
    kicker="RITTEL & WEBBER, 1973", cols=2, size=14, accent=AMBER)

img_full("Where Generative AI Accelerates the Loop", "genai-overlay.png",
    kicker="THE GENAI OVERLAY",
    caption="AI acts as an amplifier of good design thinking discipline — never a substitute for it.", accent=VIOLET)

compare_table("What GenAI Does Well — and Where It Fails",
    ["Stage", "GenAI genuinely accelerates", "What must stay human"],
    [["Empathise", "Synthesising interview transcripts and field notes at speed", "Being in the room; noticing what is not said"],
     ["Define", "Generating and stress-testing candidate reframes", "Choosing which problem the organisation will own"],
     ["Ideate", "Multiplying idea volume and range on demand", "Recognising the idea that fits this context"],
     ["Prototype", "Drafting copy, flows, screens and edge cases", "Deciding what is cheap enough to learn from"],
     ["Test", "Clustering feedback and drafting scripts", "Watching a real user hesitate, and asking why"]],
    kicker="THE PRACTICAL DIVISION OF LABOUR", accent=TEAL,
    note="A language model produces the statistically likely, not the locally true. Use it to diverge; validate before you converge.")

tile_grid("Latest Trends in Innovation", [
    ("AI-assisted discovery", "Research synthesis that took a team weeks now takes hours — the bottleneck moves to judgement."),
    ("Continuous discovery", "Discovery is no longer a phase before delivery; it runs permanently alongside it."),
    ("Cross-functional trios", "A product manager, designer and engineer own discovery together rather than passing artefacts."),
    ("Evidence over opinion", "Decisions increasingly demand a named assumption and the test that would disprove it."),
    ("Responsible AI", "Provenance, bias and governance become part of the innovation process, not a legal afterthought."),
    ("Outcome over output", "Organisations shift from counting features shipped to measuring the customer value created.")],
    kicker="WHERE THE PRACTICE IS GOING", cols=2, size=14)


# ============================================================ helper: an activity block
def activity_block(num, accent=VIOLET):
    """Case → discussion questions → debrief. NO step slides (they live in the LG)."""
    a = ACT[num]
    case_slide(f"ACTIVITY {a['num']}  ·  {a.get('duration','45')} MIN", a["title"],
               a["case"], a["scenario"],
               kicker=f"TOPIC {a['topic']:02d} · REAL-WORLD CASE STUDY", accent=accent)
    discussion_slide(f"Activity {a['num']} — Discussion Questions", a["discussion"],
                     kicker=f"ACTIVITY {a['num']} · WORK IN GROUPS OF 3–5",
                     duration=f"{a.get('duration','45')} MIN")
    tile_grid(f"Activity {a['num']} — What You Produce", [
        ("Your task", a["desc"]),
        ("You will produce", a["build"]),
        ("Tools", a["services"]),
        ("Done when", a["test"])],
        kicker=f"ACTIVITY {a['num']} · BRIEF", cols=1, size=13.5, accent=TEAL)
    debrief_slide(f"Activity {a['num']} — Debrief", a["debrief"],
                  kicker=f"ACTIVITY {a['num']} · TRAINER DEBRIEF")


activity_block(1, accent=BLUE)
activity_block(2, accent=VIOLET)
activity_block(3, accent=TEAL)

content("Recap — Topic 1", [
    "Design Thinking finds the right problem; Lean validates the right solution; Agile builds it right.",
    "The Double Diamond alternates divergence and convergence across the problem and solution spaces.",
    "The five stages are a loop you re-enter, not a sequence you complete.",
    "Wicked problems have no single correct answer — which is exactly why framing precedes solving.",
    "GenAI compresses synthesis and multiplies ideas, but empathy and judgement remain human work."],
    kicker="TOPIC RECAP", size=16)

brk("Lunch Break", "1 hour")


# ============================================================ TOPIC 2
T = C.TOPICS[1]
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])

big_statement("A problem well framed is a problem half solved.",
    "The reframe is the highest-leverage move in design thinking — and the first thing teams skip under deadline pressure.",
    "TOPIC 02 · WHY THIS MATTERS", color=VIOLET)

img_full("The Problem-Assumption Model", "problem-assumption.png",
    kicker="SCHNEIDER & O'REILLY",
    caption="The bridge from Design Thinking into Lean validation — four questions that turn a belief into a test.", accent=VIOLET)

tile_grid("Framing the Design Challenge", [
    ("1 · Write the challenge", "One short, memorable sentence stating the problem you want to solve."),
    ("2 · Make it a question", "Convert it into a 'How Might We' question that invites many answers."),
    ("3 · Define the impact", "State the change you want to see if you succeed."),
    ("4 · Explore solutions", "Sketch possible directions — without committing to any of them yet."),
    ("5 · Name the constraints", "Write the context and constraints that surround the question."),
    ("6 · Revisit the question", "Expect to rewrite the HMW as you learn — the first version is rarely right.")],
    kicker="SIX STEPS TO A DESIGN CHALLENGE", cols=2, size=13.5)

decision_map("Is Your 'How Might We' at the Right Altitude?",
    "Read your HMW question aloud. Can you immediately name only ONE obvious solution?",
    ("YES — it is too NARROW", "The solution is hiding inside the question. Widen it: ask what the user is really trying to achieve."),
    ("NO — can you name ANY concrete answer?", "If you cannot picture a single concrete answer, it is too BROAD. Narrow it to a specific user in a specific moment."),
    kicker="THE ALTITUDE TEST", color=VIOLET,
    note="A workable HMW invites many different answers, and you can imagine testing each one.")

compare_table("Problem Statement vs Point of View vs How Might We",
    ["", "What it is", "Example"],
    [["Problem statement", "A neutral description of what is wrong", "Elderly patients miss their screening appointments."],
     ["Point of View (POV)", "[User] needs [need] because [insight]", "Mdm Tan needs to feel safe asking questions because she fears being judged for not understanding."],
     ["How Might We (HMW)", "An invitation to generate solutions", "How might we make a first screening feel safe rather than exposing?"],
     ["The failure mode", "Jumping straight to a solution disguised as a problem", "'We need an SMS reminder system.' — that is an answer, not a problem."]],
    kicker="THREE ARTEFACTS, THREE JOBS", accent=BLUE,
    note="The POV is where research becomes designable. Skip it and the HMW floats free of evidence.")

img_points("The Empathy Map", "empathy-map.png", [
    ("Says and Does are observable", "You can watch and record these directly — evidence."),
    ("Thinks and Feels are inferred", "You are interpreting — label as inference, not fact."),
    ("Pains and Gains at the base", "Obstacles faced, and what success looks like to them."),
    ("Look for the contradiction", "The gap between what users say and do is where the insight lives.")],
    kicker="EMPATHISE · THE CORE TOOL", accent=TEAL)

tile_grid("Building Useful Personas", [
    ("Start with 3–5", "Enough to show meaningful variation, few enough to hold in the team's head."),
    ("Ground every claim", "Each goal, pain and behaviour should trace to something a real person said or did."),
    ("Include the awkward one", "The user who does not fit the happy path is usually where the design breaks."),
    ("Keep them comparable", "Consistent layout and one shared metric across personas so you can compare them."),
    ("Label AI-generated content", "An AI persona is a hypothesis. Mark it as unvalidated until evidence confirms it."),
    ("Retire them honestly", "A persona contradicted by evidence must be changed, not defended.")],
    kicker="PERSONA MAPPING", cols=2, size=13.5, accent=BLUE)

tile_grid("Ideation Techniques", [
    ("Brainstorming", "Group generation under explicit rules: defer judgement, go for volume, build on others' ideas."),
    ("Brainwriting", "Silent written generation first — it prevents the loudest voice from anchoring the room."),
    ("Crazy 8s", "Eight rapid variations in eight minutes; speed defeats the internal critic."),
    ("Worst Possible Idea", "Deliberately generate terrible ideas to break the fear of contributing."),
    ("SCAMPER", "Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, Reverse."),
    ("AI amplification", "Generate manually first, then use GenAI to extend — never the reverse, or it anchors the room.")],
    kicker="DIVERGE BEFORE YOU CONVERGE", cols=2, size=13.5, accent=AMBER)

big_statement("Separate the generation of ideas from the evaluation of ideas.",
    "Judging while generating kills the unusual ideas first — and the unusual idea is the one you came for.",
    "THE ONE RULE OF IDEATION", color=AMBER)

tile_grid("Prototyping — Build to Think", [
    ("Buy information cheaply", "A prototype's job is to purchase learning at the lowest possible price."),
    ("Low fidelity invites honesty", "A rough sketch gets real objections; a polished mockup gets polite notes on the font."),
    ("Wizard of Oz", "Fake the mechanism with a human behind the curtain — learn the behaviour before building anything."),
    ("Storyboard the experience", "Draw the scenario as a strip so the team can role-play and feel where it breaks."),
    ("Write the falsification test", "State in advance what result would prove the concept wrong — or it is a demo, not a test."),
    ("GenAI drafts the content", "Screen copy, flows, edge cases and interview scripts in minutes — you still run the test.")],
    kicker="PROTOTYPE · TEST", cols=2, size=13.5, accent=TEAL)

activity_block(4, accent=BLUE)
activity_block(5, accent=AMBER)
activity_block(6, accent=TEAL)

content("Recap — Topic 2", [
    "Framing turns a technical brief into a human one — and that reframe is where the leverage is.",
    "A POV statement ([user] needs [need] because [insight]) makes research designable.",
    "A How Might We question must be neither so narrow it hides the answer nor so broad it invites none.",
    "Empathy maps expose the gap between what users say and what they do.",
    "Diverge with volume, converge with judgement — and never let AI anchor the room first.",
    "A prototype exists to be proven wrong cheaply, not to look finished."],
    kicker="TOPIC RECAP", size=16)

big_statement("End of Day 1.",
    "Tomorrow: how the validated problem becomes a backlog, a sprint, and an innovation the organisation can sustain.",
    "DAY 1 CLOSE", color=BLUE)


# ============================================================ TOPIC 3
T = C.TOPICS[2]
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])

big_statement("The most expensive way to test your idea is to build production-quality software.",
    "Jeff Patton — the sentence that justifies every prototype, every discovery cycle and every killed idea.",
    "TOPIC 03 · WHY THIS MATTERS", color=VIOLET)

compare_table("Being Agile vs Doing Agile",
    ["", "Doing Agile (the rituals)", "Being Agile (the mindset)"],
    [["Stand-up", "A status report to the manager", "The team re-plans its own day"],
     ["Backlog", "A queue of requirements handed down", "A living, validated set of bets"],
     ["Sprint review", "A demo performed for stakeholders", "A genuine request for disconfirming feedback"],
     ["Retrospective", "A meeting that produces a tidy list", "The team says the uncomfortable thing and changes something"],
     ["Change request", "A disruption to be resisted", "New information to be welcomed and evaluated"],
     ["Velocity", "A productivity target imposed on the team", "A planning input owned by the team"]],
    kicker="THE DISTINCTION THAT DECIDES OUTCOMES", accent=VIOLET,
    note="Practices without principles are a short-lived Band-Aid; principles without practices are a fruitless exercise in philosophy.")

img_full("The Scrum Loop", "scrum-loop.png",
    kicker="AGILE FRAMEWORKS FOR INNOVATION PROJECTS",
    caption="Scrum delivers the highest value in the shortest time through transparency, inspection and adaptation.", accent=TEAL)

tile_grid("The Scrum Team — Three Accountabilities", [
    ("Product Owner", "Owns the product vision and the backlog; the final decision-maker on priority. Owns the WHAT."),
    ("Scrum Master", "Enables the process, removes impediments, protects the team's focus, coaches the practice."),
    ("Developers", "The cross-functional group who build the increment. Self-organising; they own the HOW."),
    ("Team size", "Small enough to stay coordinated — typically around seven people, plus or minus two."),
    ("Cross-functional", "The team contains every skill needed to produce a done increment without external handoff."),
    ("Self-managing", "The team decides how the work gets done; nobody outside it assigns tasks to individuals.")],
    kicker="WHO DOES WHAT", cols=2, size=13.5)

img_full("Dual-Track Agile — Discovery and Delivery Together", "dual-track-agile.png",
    kicker="THE OPERATING MODEL OF MODERN PRODUCT TEAMS",
    caption="Discovery asks 'should we build this?'; delivery asks 'how do we build it well?' — one team, two tracks, running at once.", accent=BLUE)

tile_grid("Four Myths About Dual-Track", [
    ("'Discovery comes first, then delivery'", "No — both run continuously and simultaneously within the same team."),
    ("'Everything flows discovery → delivery'", "No — most ideas are changed or killed during discovery. That is the point."),
    ("'They are separate teams'", "No — a trio may lead discovery, but the whole team participates in it."),
    ("'Discovery ends at launch'", "No — keep measuring and learning after you ship; that is when reality arrives.")],
    kicker="JEFF PATTON · CORRECTING THE RECORD", cols=2, size=13.5, accent=AMBER)

big_statement("Beware the mini-waterfall inside your sprint.",
    "PM writes requirements → hands to a designer → hands to the delivery team. Each handoff looks like collaboration and is actually a queue.",
    "MARTY CAGAN · THE COMMON ANTI-PATTERN", color=AMBER)

compare_table("From Idea to Task — the Decomposition Ladder",
    ["Level", "What it is", "Example"],
    [["Epic", "A large body of work spanning many sprints", "Self-service health screening"],
     ["Feature", "A coherent capability within an epic", "Appointment booking without a call centre"],
     ["Hill", "An outcome statement: as a [who], I want [what], so that [wow]", "As a first-time patient, I can book a screening in under 3 minutes, so that I never need to phone."],
     ["User story", "A small unit of value: as a [user], I want [goal], so that [reason]", "As a patient, I want to see the next three available slots so that I can choose quickly."],
     ["Task", "The work needed to deliver the story", "Build the slot-availability API endpoint."]],
    kicker="CONVERTING IDEAS INTO AGILE ARTEFACTS", accent=BLUE,
    note="A Hill states the outcome and the 'wow'; a user story states the function. Teach both — they do different jobs.")

tile_grid("User Stories — the Three C's", [
    ("Card", "The story is written small, on a card. Its size is a deliberate constraint on scope."),
    ("Conversation", "The card is a promise to have a conversation — the detail lives in the discussion, not the text."),
    ("Confirmation", "Acceptance criteria define how you will know it is done. Testable, not restated."),
    ("The common failure", "Acceptance criteria that merely repeat the story. If it cannot fail a test, it is not a criterion.")],
    kicker="RON JEFFRIES · THE 3 C's", cols=2, size=13.5, accent=TEAL)

img_full("Release Prioritisation — The Three-Cake Model", "cake-releases.png",
    kicker="IBM DESIGN THINKING",
    caption="Every release must be a whole cake at its own scale. A slice of an unfinished wedding cake is not a smaller product — it is a broken one.", accent=VIOLET)

tile_grid("Agile Estimation — Story Points", [
    ("Size, not duration", "Points measure relative complexity and effort, not hours. Duration is derived later from velocity."),
    ("Relative, not absolute", "Humans compare well and predict poorly — 'this is twice that' beats 'this takes six hours'."),
    ("A constrained scale", "Fibonacci-like values (1, 2, 3, 5, 8, 13) force meaningful distinctions between sizes."),
    ("Additive", "Points can be summed across stories; time-based estimates cannot be summed honestly."),
    ("Velocity from done work", "Only fully 'done, done' stories count. Partial credit destroys the signal."),
    ("Planning Poker", "Estimate privately, reveal together, discuss the outliers — that discussion is the real value.")],
    kicker="ESTIMATION THAT SURVIVES CONTACT", cols=2, size=13.5)

tile_grid("GenAI Across the Sprint", [
    ("Backlog drafting", "Generate candidate stories and acceptance criteria from a Hill in seconds — then cut what is unvalidated."),
    ("Backlog grooming", "Flag duplicates and related items across a large backlog faster than a human scan."),
    ("Test data", "Generate realistic edge-case data sets for testing without exposing real customer records."),
    ("Retro synthesis", "Cluster retrospective themes across many notes — after the team has spoken, never instead of it."),
    ("Sprint reporting", "Draft the summary so the Scrum Master spends the time on impediments, not formatting."),
    ("Where it must not run", "Prioritisation, the disruption decision, and the retrospective conversation itself.")],
    kicker="FASTER ITERATIONS WITHOUT LOSING THE DECISION", cols=2, size=13.5, accent=VIOLET)

activity_block(7, accent=BLUE)
activity_block(8, accent=VIOLET)
activity_block(9, accent=TEAL)

content("Recap — Topic 3", [
    "Being Agile is a mindset; doing Agile is the ceremonies — organisations need both to work.",
    "Scrum's three accountabilities separate the what (PO), the enablement (SM) and the how (Developers).",
    "Dual-track agile runs discovery and delivery simultaneously in one team, feeding a validated backlog.",
    "Ideas decompose Epic → Feature → Hill → Story → Task; Hills carry the outcome, stories carry the function.",
    "Story points measure relative size, and velocity counts only fully completed work.",
    "GenAI drafts, clusters and summarises — the team still owns every decision."],
    kicker="TOPIC RECAP", size=16)

brk("Lunch Break", "1 hour")


# ============================================================ TOPIC 4
T = C.TOPICS[3]
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])

big_statement("Training 400 people produces 400 people who know the vocabulary.",
    "Scaling innovation is not a training problem — it is a question of what gets measured, who may decide, and what leaders visibly do.",
    "TOPIC 04 · WHY THIS MATTERS", color=TEAL)

tile_grid("Three Levers That Actually Scale Innovation", [
    ("Purpose, alignment and autonomy", "Be stubborn on the vision and flexible on the details. Teams need a clear outcome and the authority to pursue it."),
    ("Measure things that matter", "Structure metrics around the decisions you intend to make. A metric that cannot change a decision is decoration."),
    ("Decide from learning", "Define beliefs so they can be tested, choose the most important thing to learn, then design the experiment that delivers it.")],
    kicker="THE OPERATING SYSTEM, NOT THE TRAINING CALENDAR", cols=1, size=14)

tile_grid("Four Principles for a Culture That Sustains It", [
    ("People over process", "Assemble people around a shared mission rather than around a reporting structure."),
    ("Creativity and innovation", "Build exploration time into the workflow and permit smart risk-taking."),
    ("Iteration and adaptation", "Replace year-long plans with low-fidelity versions tested in real conditions."),
    ("Multi-disciplinary autonomous teams", "Cross-functional teams with genuine local decision authority beat hierarchies.")],
    kicker="STEVE PERKINS · THE DESIGN GYM", cols=2, size=14, accent=VIOLET)

tile_grid("Engaging Stakeholders and Creating Buy-In", [
    ("Start small and visible", "Choose a low-risk, high-value opportunity; one credible win buys more permission than any deck."),
    ("Bring evidence, not opinion", "Show the user quote, the test result and the assumption you falsified."),
    ("Name the metric in advance", "Agree what would count as success before you run the pilot, not after."),
    ("Involve the sceptic early", "The person most likely to block it is the most valuable participant in the discovery."),
    ("Leaders participate, not sponsor", "A leader who sits in a user interview changes the organisation's behaviour more than a memo."),
    ("Make the risk explicit", "State what you will stop doing if the evidence goes against you — it earns credibility.")],
    kicker="BUY-IN FOR AI-DRIVEN INNOVATION", cols=2, size=13.5, accent=AMBER)

tile_grid("Resource Management in Innovation Projects", [
    ("Fund learning, not plans", "Release budget in stages tied to validated learning rather than in one annual block."),
    ("Protect discovery capacity", "If discovery is unstaffed, delivery will build whatever is loudest."),
    ("Use AI to free expert time", "Automate synthesis and drafting so scarce expertise goes to judgement work."),
    ("Track the cost of being wrong", "The relevant number is not what a test costs, but what building the wrong thing costs."),
    ("Govern AI use", "Record provenance, check for bias, and keep an audit trail for AI-assisted decisions."),
    ("Kill work deliberately", "Stopping a weak initiative releases the scarcest resource you have — your best people.")],
    kicker="RESOURCES · GOVERNANCE", cols=2, size=13.5, accent=BLUE)

tile_grid("Sensemaking — Turning Ambiguity into Action", [
    ("Signals arrive incomplete", "Real innovation decisions are made on conflicting, partial and contested evidence."),
    ("Build a shared narrative", "Sensemaking produces a story the organisation can act on together, not a data dump."),
    ("Name the disconfirming signal", "The evidence that contradicts your narrative is the most valuable input in the room."),
    ("AI helps, then misleads", "GenAI clusters signals well and manufactures a confident narrative even when the evidence is thin.")],
    kicker="SENSEMAKING", cols=2, size=13.5, accent=VIOLET)

img_full("Feedback Loops — Reinforcing and Balancing", "feedback-loops.png",
    kicker="SYSTEMS THINKING",
    caption="Systemic failure is a reinforcing loop with no effective balancing counterpart — no individual decision has to be irrational.", accent=AMBER)

tile_grid("The Five Ideas of Systems Thinking", [
    ("Interconnectedness", "Shift from linear cause-and-effect to circular thinking — everything is part of a wider system."),
    ("Synthesis", "Combine elements to see the whole; analysis alone dissects and loses the behaviour."),
    ("Emergence", "System behaviour arises from interaction and cannot be predicted from the parts alone."),
    ("Feedback loops", "Reinforcing loops amplify; balancing loops stabilise. Find which one you are standing in."),
    ("Causality", "Understand how a change in one variable actually propagates to an outcome."),
    ("Systems mapping", "Draw elements and their interconnections to find the leverage point worth intervening at.")],
    kicker="SEEING THE WHOLE", cols=2, size=13.5, accent=TEAL)

compare_table("Systems Thinking vs Design Thinking",
    ["", "Design Thinking", "Systems Thinking"],
    [["Starting point", "A human need", "A pattern of behaviour over time"],
     ["Unit of attention", "The user and their experience", "The structure that produces the outcome"],
     ["Asks", "What does this person need?", "Why does this system keep producing this result?"],
     ["Typical output", "A validated solution concept", "A leverage point and an intervention"],
     ["Blind spot", "Can optimise one user while harming the system", "Can map elegantly and never ship anything"],
     ["Used together", "Design the intervention with empathy", "Place it where the system will actually respond"]],
    kicker="TWO LENSES, ONE PROBLEM", accent=BLUE,
    note="Use systems thinking to choose where to intervene; use design thinking to design the intervention itself.")

img_full("The Innovation Metric Test", "metrics-quadrant.png",
    kicker="METRICS AND KPIs",
    caption="If a movement in the number would change no decision, the number is decoration — and it will not survive a budget review.", accent=VIOLET)

img_points("Three Validations, Three Different Tests", "three-validations.png", [
    ("Problem validation", "Evidence the problem exists and matters to enough people."),
    ("Solution validation", "Evidence your solution actually solves it for them."),
    ("Demand validation", "Evidence they will adopt, switch to, or pay for it."),
    ("The common error", "Presenting solution evidence as if it proved demand — how products launch to silence.")],
    kicker="DO NOT CONFLATE THESE", accent=TEAL)

tile_grid("A Balanced Innovation Scorecard", [
    ("Customer value", "Time saved, effort removed, task success rate, or a genuine satisfaction signal."),
    ("Business value", "Revenue, cost avoided, retention, or cycle time — expressed in money where honest."),
    ("Societal value", "Access, inclusion, safety or environmental effect — the value not captured in the price."),
    ("A leading indicator", "Something that moves early enough to still change a decision this quarter."),
    ("The decision test", "For every metric, write the decision that would change if it moved. No decision, no metric."),
    ("Beware vanity metrics", "Ideas submitted, workshops run and people trained always rise and prove nothing.")],
    kicker="WHAT TO PUT ON THE BOARD SLIDE", cols=2, size=13.5, accent=AMBER)

activity_block(10, accent=BLUE)
activity_block(11, accent=AMBER)
activity_block(12, accent=VIOLET)

content("Recap — Topic 4", [
    "Scaling changes the operating system: what is measured, who decides, and what leaders actually do.",
    "Buy-in is earned with a small visible win and evidence, not with a persuasive deck.",
    "Sensemaking builds a shared narrative from conflicting signals — and AI can manufacture false confidence.",
    "Systems thinking finds the leverage point; design thinking designs the intervention that goes there.",
    "Every metric must have a decision attached to it, or it is decoration.",
    "Problem, solution and demand validation are three separate tests — never present one as another."],
    kicker="TOPIC RECAP", size=16)


# ============================================================ CLOSE
section("WRAP-UP", "Course Summary & Next Steps", "")

tile_grid("What You Achieved", [
    ("LO1 · Integrated DT, Agile and GenAI", "You positioned design thinking, lean and agile against each other and placed GenAI correctly inside the loop."),
    ("LO2 · Synthesised stakeholder inputs", "You built empathy maps, POV statements and How Might We questions from real case evidence."),
    ("LO3 · Led design thinking projects", "You ran dual-track discovery, converted Hills into a sized backlog and managed a sprint disruption."),
    ("LO4 · Developed agile DT strategies", "You built a scaling plan, mapped systemic risk and designed a metric set that changes decisions.")],
    kicker="LEARNING OUTCOMES", cols=2, size=13.5)

tile_grid("Take This Back to Work on Monday", [
    ("Reframe one brief", "Take one current requirement and rewrite it as a POV and a How Might We question."),
    ("Run one cheap test", "Pick your riskiest assumption and design the cheapest test that could disprove it."),
    ("Audit one metric", "Apply the decision test to your team's favourite number. Be honest about the result."),
    ("Start one discovery track", "Give one team two hours a week of protected discovery time and see what changes."),
    ("Label your AI output", "Mark every AI-generated persona or insight as unvalidated until evidence confirms it."),
    ("Find one balancing loop", "Identify a reinforcing loop in your organisation that has no counterweight — and propose one.")],
    kicker="NEXT STEPS", cols=2, size=13.5, accent=TEAL)

tile_grid("Continue Your Learning", [
    ("Design Thinking Studio", "https://alfredang.github.io/designthinking/ — keep using the workspace with your own team."),
    ("Padlet Classroom Board", "https://alfredang.github.io/padlet/ — run your own retrospectives and idea boards."),
    ("Thoughtworks on DT, Lean and Agile", "Jonny Schneider on how the three mindsets work together."),
    ("Marty Cagan & Jeff Patton", "Dual-track agile, continuous discovery and the product trio."),
    ("Rittel & Webber (1973)", "The original paper on wicked problems and why framing precedes solving."),
    ("Tertiary Infotech course catalogue", "www.tertiarycourses.com.sg — further WSQ courses in AI and innovation.")],
    kicker="GO DEEPER", cols=2, size=13.5)

content("Support", [
    "If you have any enquiries during or after the class, you can contact us below.",
    "Email: enquiry@tertiaryinfotech.com",
    "Tel: +65 6100 0613",
    "Website: www.tertiarycourses.com.sg",
    "LMS / TMS: https://lms-tms.tertiaryinfotech.com"],
    kicker="WE'RE HERE TO HELP")

# --- mandatory assessment admin block, repeated at the END
tile_grid("Assessment", [
    ("Written Assessment (SAQ)", "1 hour · open book · short-answer questions on the underpinning knowledge."),
    ("Case Study (CS)", "1 hour · open book · a scenario-based innovation case across all four topics."),
    ("Digital attendance", "Remember to take the Assessment digital attendance (TRAQOM) before you start."),
    ("Submit on the LMS", "Upload your completed answers at https://lms-tms.tertiaryinfotech.com/")],
    kicker="WRAP-UP", cols=2, size=15)

process_map("Assessment Flow", [
    ("TRAQOM survey", "Scan the QR code on the LMS"),
    ("Digital attendance", "Scan the SSG assessment QR"),
    ("Sit WA then CS", "Open book · 1 hour each"),
    ("Submit on the LMS", "Upload your completed answers"),
    ("Sign the record", "Sign the Assessment Summary Record")],
    kicker="ON ASSESSMENT DAY", color=BLUE,
    synthesis=("REMEMBER", "All five steps are mandatory for WSQ funding — missing the digital attendance or the TRAQOM survey can invalidate your claim."))

tile_grid("Digital Attendance (Mandatory)", [
    ("Three times a day", "Take the AM, PM and Assessment digital attendance — mandatory for every WSQ-funded course."),
    ("Trainer shows the QR", "The trainer or administrator displays the digital attendance QR code from the SSG portal."),
    ("Scan and submit", "Scan the QR code with your mobile phone camera and submit your attendance."),
    ("75% minimum", "A minimum of 75% attendance is required to be eligible for assessment and funding.")],
    kicker="TRAQOM · SSG DIGITAL ATTENDANCE", cols=2, size=15)

big_statement("Thank You!",
    "You can now frame the right problem, validate it cheaply, deliver it with agile discipline, and scale it without losing the evidence.",
    "END OF COURSE", color=TEAL)


# ============================================================ motion pass
DIVIDER_KEYS = ("COURSE ADMINISTRATION", "WRAP-UP", "DAY 1 CLOSE",
                "TOPIC 01 · WHY", "TOPIC 02 · WHY", "TOPIC 03 · WHY", "TOPIC 04 · WHY",
                "END OF COURSE", "THE ONE RULE OF IDEATION",
                "MARTY CAGAN · THE COMMON ANTI-PATTERN")
for s in prs.slides:
    joined = " ".join(sh.text_frame.text for sh in s.shapes if sh.has_text_frame)
    is_div = any(k in joined for k in DIVIDER_KEYS) or \
             any((t["title"] in joined and f"TOPIC {t['code']}" in joined) for t in C.TOPICS)
    _transition(s, "push" if is_div else "fade", speed="med" if is_div else "fast")

OUT = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
prs.save(OUT)
print(f"Saved {OUT}  ({len(prs.slides._sldIdLst)} slides)")
