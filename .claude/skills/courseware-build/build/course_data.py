"""
SINGLE SOURCE OF TRUTH for the TGS-2024049781 courseware.

Fast-Track Innovations with Agile Design Thinking and Generative AI (GenAI)

Every artifact — the slide deck (PPT), Lesson Plan (LP), Learner Guide (LG),
the activities/ folder and the assessment — is generated from (or aligned to)
the data in this module, so titles, topic numbering, activities, learning
outcomes and the schedule can never drift apart.

Content sources:
  * The legacy v3 master trainer deck (reference/) — carried forward.
  * Thoughtworks, Adaptovate, BMC, PMI, UX Magazine, The Design Gym,
    PremierAgile and Startup Frontier on how Design Thinking, Lean and Agile
    fit together — used to beef up the thin areas of the legacy deck.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Fast-Track Innovations with Agile Design Thinking and Generative AI (GenAI)"
SHORT_TITLE  = "Fast-Track Innovations with Agile Design Thinking and GenAI"
COURSE_CODE  = "TGS-2024049781"
VERSION      = "v4.0"
VERSION_DATE = "17 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2

# ------------------------------------------------------------------ skills framework
TSC_TITLE = "Design Thinking Practice"
TSC_CODE  = "ICT-ACE-5014-1.1"

TSC_ABILITIES = [
    "A1 – Integrate design thinking methodologies into processes to drive innovation across the organisation",
    "A2 – Develop strategies to proliferate design thinking across the organisation",
    "A3 – Synthesise information from different sources and stakeholders in order to fully understand the needs of end users",
    "A4 – Drive the development of new strategies to enhance products and/or services for the organisation",
    "A5 – Engage stakeholders during the design thinking process to uncover the motivations behind their actions and behaviours",
    "A6 – Cultivate design thinking as a viable tool and methodology to foster new innovations for the organisation",
    "A7 – Lead design thinking projects across the organisation",
]

TSC_KNOWLEDGE = [
    "K1 – Latest trends in design thinking",
    "K2 – Concept of innovation management",
    "K3 – Drivers of organisational growth and success",
    "K4 – Concept and principles of resource management",
    "K5 – Project management tools and techniques",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Integrate design thinking methodologies and agile principles to drive organisational innovation using generative AI.",
    "LO2: Synthesise stakeholder inputs to uncover end-user needs for successful innovation.",
    "LO3: Lead design thinking projects using project management tools and techniques to enhance organisational performance.",
    "LO4: Develop strategies for agile design thinking to enhance product and service innovation.",
]

# ------------------------------------------------------------------ ed-tools
ED_TOOLS = [
    dict(name="Design Thinking Studio",
         url="https://alfredang.github.io/designthinking/",
         desc="A shared 5-stage design thinking workspace (Empathize · Define · Ideate · Prototype · Test). "
              "The trainer clicks Create New Workspace and shares the workspace code or QR; learners click "
              "Join Workspace, enter the code and a display name, then post notes into the stage sections.",
         sections="Empathize (User Personas, User Pain Points, Interview Notes, Observation Notes, Empathy Map "
                  "Says/Thinks/Does/Feels) · Define (Problem Statement, How Might We, Key Insights, User Needs, "
                  "Success Criteria) · Ideate (Brainstorming Board, Crazy 8s, Solution Sketches, Idea Categories, "
                  "Voting & Prioritisation) · Prototype (Description, Screens/Wireframes, Feature List, User Flow, "
                  "Assumptions, Checklist) · Test (Test Plan, User Feedback, Test Results, Issues Found, "
                  "Improvements, Final Recommendations)"),
    dict(name="Padlet Classroom Board",
         url="https://alfredang.github.io/padlet/",
         desc="An online classroom board for posting, comparing and voting on group output. The trainer creates a "
              "classroom and shares the classroom code; learners join, then add posts (text, image, link, YouTube "
              "or PDF) into named sections, like the strongest posts and comment on each other's work.",
         sections="Classroom → Sections and Sub-sections → Posts (text · image · link · YouTube · PDF) with Likes "
                  "and Comments; sort by Newest first / Oldest first / Most liked; trainer can pin an Announcement"),
]

# ------------------------------------------------------------------ topics
# num, code, title, subtitle, weighting, concept bullets for the section
TOPICS = [
    dict(num=1, code="01",
         title="Foundations of Design Thinking, Agile, and Generative AI for Problem-Solving",
         subtitle="Design Thinking · Lean · Agile · Generative AI · The innovation operating system",
         weighting="25%",
         concepts=[
            "Design Thinking explores the problem space with empathy; Lean validates that a solution is viable; Agile builds it right, incrementally.",
            "Design Thinking asks 'are we building the right thing?'; Agile asks 'are we building the thing right?' — they are completing, not competing.",
            "The Double Diamond (Discover → Define → Develop → Deliver) alternates divergent and convergent thinking across two linked diamonds.",
            "Design Thinking's five stages — Empathise, Define, Ideate, Prototype, Test — are iterative and non-linear, not a waterfall.",
            "Generative AI compresses the expensive parts of the loop: synthesising research, generating idea volume, and drafting prototypes in minutes.",
            "AI accelerates the loop but never replaces the human judgement, empathy and validation that make innovation trustworthy.",
         ]),
    dict(num=2, code="02",
         title="Problem Framing and Ideation: Leveraging Design Thinking and Generative AI",
         subtitle="Framing · Personas · Empathy maps · HMW · Ideation · Rapid prototyping",
         weighting="25%",
         concepts=[
            "A design challenge is framed as a single memorable sentence, then converted into a 'How Might We' question that is neither too broad nor too narrow.",
            "A Point of View statement — [User] needs [need] because [insight] — turns raw research into a designable problem.",
            "Personas represent target users through goals, pain points, behaviours and demographics; build 3–5 detailed personas to start.",
            "An Empathy Map captures what the user Says, Thinks, Does and Feels, plus Pains and Gains, to expose contradictions.",
            "Ideation separates idea generation from idea evaluation — go for volume first, judge later; use Brainstorm, Brainwrite, Crazy 8s, Worst Possible Idea and SCAMPER.",
            "Prototypes are built to think: low-resolution, quick and cheap artefacts that make an idea experienceable and testable.",
            "GenAI is a research synthesiser and an idea multiplier — but every AI-generated persona or insight must be validated against real user evidence.",
         ]),
    dict(num=3, code="03",
         title="Agile Development and AI for Rapid Solution Delivery",
         subtitle="Agile mindset · Scrum · Backlogs · User stories · Estimation · Sprints with AI",
         weighting="25%",
         concepts=[
            "Being Agile is a mindset of responding to change; doing Agile is running the ceremonies — organisations need both.",
            "Scrum delivers the highest value in the shortest time through an empirical process of transparency, inspection and adaptation.",
            "The Scrum Team: Product Owner owns the 'what' and the backlog; Scrum Master enables the process; the Developers own the 'how'.",
            "Ideas decompose into Epics → Features → User Stories → Tasks; a user story is the 3 C's — Card, Conversation, Confirmation.",
            "Story points estimate relative size and complexity, not duration; velocity is measured only on fully 'done, done' stories.",
            "Dual-track agile runs a continuous discovery track (Design Thinking) beside a delivery track (Scrum sprints), feeding a validated backlog.",
            "GenAI drafts user stories and acceptance criteria, generates test data and summarises retrospectives — the team still owns the decision.",
         ]),
    dict(num=4, code="04",
         title="Scaling and Sustaining Innovations with Agile Design Thinking and Generative AI",
         subtitle="Scaling · Stakeholders · Sensemaking · Systems thinking · Resources · Metrics",
         weighting="25%",
         concepts=[
            "Scaling design thinking means changing the operating system — purpose and autonomy, measuring what matters, and deciding from learning.",
            "Hypothesis-Driven Development frames a change as a belief plus the metric that would prove or disprove it.",
            "Stakeholder buy-in for AI-driven innovation is earned with evidence and small wins, not with slideware.",
            "Sensemaking turns ambiguous, conflicting signals into a shared narrative the organisation can act on.",
            "Systems thinking sees interconnectedness, synthesis, emergence, feedback loops and causality — the whole, not the parts.",
            "Innovation metrics must span customer value, business value and societal value, and must drive an actual decision.",
            "Resource management with AI tools frees expert time for judgement work; governance keeps AI use responsible and auditable.",
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "Foundations, Problem Framing and Ideation with GenAI",
    2: "Agile Delivery, Scaling Innovation and Assessment",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 0.5 hour, open book.",
    practical="Case Study (CS) — a scenario-based innovation case, 1 hour, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
