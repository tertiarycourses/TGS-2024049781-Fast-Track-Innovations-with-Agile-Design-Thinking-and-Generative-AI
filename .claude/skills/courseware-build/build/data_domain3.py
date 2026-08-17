"""
Topic 3 activities — Agile Development and AI for Rapid Solution Delivery.

Real-world case studies, run on the course ed-tools:
  Design Thinking Studio — https://alfredang.github.io/designthinking/
  Padlet Classroom Board — https://alfredang.github.io/padlet/
"""

DOMAIN3 = [
    dict(
        num=7,
        topic=3,
        title="Spotify — Reading a Scaling Model Honestly",
        objective="LO3 · A7 · K5 — Agile frameworks for managing innovation projects; project management tools and techniques.",
        duration=45,
        case="In 2012 Henrik Kniberg and Anders Ivarsson published a paper describing how Spotify organised engineering "
             "into Squads, Tribes, Chapters and Guilds. It spread worldwide as 'the Spotify Model' and was copied by "
             "hundreds of organisations. What most of those organisations missed was the disclaimer in the paper "
             "itself: it was a snapshot of a journey, not a framework, and Spotify had already moved on. Kniberg later "
             "stated plainly that Spotify does not use 'the Spotify Model' and that people should not copy it. "
             "Organisations that copied the structure — renaming teams 'squads' and departments 'tribes' — routinely "
             "failed to copy the culture of trust and autonomy that made it work, and ended up with the same "
             "hierarchy under new labels. The lesson: practices without principles are a short-lived Band-Aid.",
        scenario="Your management team has returned from a conference and wants to 'implement the Spotify Model' "
                 "across three departments by the end of the quarter. You have been asked to write the "
                 "implementation plan.",
        desc="Learners examine the most-copied agile scaling model in the industry and diagnose why structural "
             "copying fails, then distinguish the transferable principles from the non-transferable artefacts — "
             "the core skill in leading design thinking and agile projects across an organisation.",
        build="A Padlet board separating Spotify's transferable principles from its non-transferable structures, and "
              "a one-page counter-proposal to the 'implement it by Q4' instruction.",
        services="Padlet Classroom Board, ChatGPT or Microsoft Copilot",
        discussion=[
            "Spotify's own authors say do not copy it. Why did hundreds of organisations copy it anyway?",
            "Separate the list: which parts of the model are structures (copyable) and which are cultures (not directly copyable)?",
            "'Practices without principles are a short-lived Band-Aid. And principles without practices are a fruitless exercise in philosophy.' Give a workplace example of each failure mode.",
            "Your management wants it done by Q4. Write the one question that reframes the request without being insubordinate.",
            "How might GenAI help you assess organisational readiness before a rollout — and what would it get wrong?",
        ],
        debrief="Renaming a department a 'tribe' changes nothing; devolving budget authority to it changes everything. "
                "The copyable parts are the visible artefacts — squad names, chapter structures, guild meetings. The "
                "parts that actually generated the results are autonomy backed by real decision rights, alignment "
                "through a clear mission, and a tolerance for teams choosing different practices. Those cannot be "
                "installed by reorganisation chart. The professional move when handed 'implement it by Q4' is not "
                "refusal but reframing: ask what outcome the leadership team actually wants — faster delivery, "
                "better retention, fewer handoffs — and then propose the smallest change that could plausibly move "
                "it, run in one team first. PremierAgile's guidance applies directly: start small, low-risk and "
                "high-value, one to three attempts before scaling.",
        steps=[
            ("Rejoin the Padlet classroom board and open the Activity 7 section.", ""),
            ("Read the Spotify case in the Learner Guide (Activity 7) with your group.", ""),
            ("In the sub-section 'Structures', post the parts of the model that are organisational artefacts.", ""),
            ("In the sub-section 'Principles', post the underlying beliefs that made those artefacts work.", ""),
            ("Ask ChatGPT: 'What conditions must be true in an organisation for autonomous squads to outperform a functional hierarchy?' and evaluate its answer critically.", ""),
            ("Draft your counter-proposal: one team, one quarter, one measurable outcome. Post it.", ""),
            ("Read another group's counter-proposal and comment with the biggest risk you see in it.", ""),
        ],
        test="Your board cleanly separates structure from principle, and your counter-proposal names one team, one "
             "outcome and one metric rather than an organisation-wide rollout.",
    ),

    dict(
        num=8,
        topic=3,
        title="From Hills to Backlog — Converting Ideas into Stories with GenAI",
        objective="LO3 · LO4 · K5 — Converting ideas into agile features, stories and tasks with GenAI; project management tools and techniques.",
        duration=55,
        case="IBM runs a two-day Design Thinking and Agile workshop in which Day 1 produces 'Hills' — outcome "
             "statements in the form 'As a [who], I want [what], so that [wow]' — and Day 2 converts them into 20–30 "
             "user stories, prioritises them into three releases and sizes them with Planning Poker. In one "
             "documented session, a manufacturing user's need for inventory data started as a vague 'in minutes'. The "
             "team pushed until it became '5 minutes', and the justification made the requirement real: the data had "
             "to be available before the morning manager meeting. That specificity is what separates an outcome you "
             "can test from an aspiration you cannot. IBM prioritises releases as 'Cupcake, Birthday Cake, Wedding "
             "Cake' — where the cupcake is a complete, satisfying cake at small scale, not a slice of an unfinished one.",
        scenario="Take the prototype concept your group validated in Activity 6. Your product trio — product manager, "
                 "designer, engineer — now has one hour to turn it into a release-one backlog that a delivery team "
                 "could actually start on Monday.",
        desc="Learners write a measurable Hill, use GenAI to expand it into user stories with acceptance criteria, "
             "critique and correct the AI output, prioritise into the three-cake release model and size the stories "
             "with relative estimation.",
        build="A prioritised release-one backlog: one Hill, 8–12 user stories with acceptance criteria, a "
              "Cupcake/Birthday/Wedding split and story-point estimates.",
        services="Design Thinking Studio, Padlet Classroom Board, ChatGPT or Microsoft Copilot",
        discussion=[
            "Compare a Hill ('so that [wow]') with a user story ('so that [reason]'). What does the Hill capture that the story loses?",
            "The team pushed 'in minutes' to '5 minutes'. What forced the specificity, and what would have happened without it?",
            "Review the AI-generated stories. What did it get structurally right, and what did it get wrong about your context?",
            "Explain 'Cupcake' to someone who thinks an MVP is 'version one with features removed'. Where is the difference?",
            "Story points measure size and complexity, not duration. Why does the distinction matter for a team's velocity?",
        ],
        debrief="GenAI is genuinely good at the mechanical layer of this task — it produces well-formed stories with "
                "plausible acceptance criteria in seconds, and it rarely forgets the syntax. What it cannot supply is "
                "context: your constraints, your regulatory environment, your legacy integration, your users' actual "
                "tolerance for change. The reliable pattern is AI drafts, humans decide. Watch for the two "
                "characteristic AI failures in the room: stories that are technically well-formed but describe "
                "features nobody validated, and acceptance criteria that restate the story instead of defining a "
                "testable condition. On the cake model — the point of the cupcake is that a person could genuinely "
                "enjoy it and it stands alone. A slice of unfinished wedding cake is not a smaller product, it is a "
                "broken one, and shipping it teaches you nothing except that users dislike broken things.",
        steps=[
            ("Open the Padlet classroom board, Activity 8 section.", ""),
            ("Write ONE Hill for your concept: 'As a [who], I want [what], so that [wow]'. Make the wow measurable.", ""),
            ("Post the Hill and have another group challenge its measurability. Revise it.", ""),
            ("Prompt the AI: 'Convert this Hill into 10 user stories in the form As a/I want/so that, each with 2-3 testable acceptance criteria.'", ""),
            ("Review every story. Delete the ones that assume something you never validated. Rewrite the weak acceptance criteria.", ""),
            ("Split the surviving stories into Cupcake, Birthday Cake and Wedding Cake releases.", ""),
            ("Size the Cupcake stories using relative points (1, 2, 3, 5, 8) — discuss any estimate where the group differs by more than two cards.", ""),
            ("Post your final release-one backlog to Padlet and Like the backlog you would most want to inherit as a developer.", ""),
        ],
        test="Your Cupcake release is genuinely shippable and useful on its own, every story has testable acceptance "
             "criteria, and you can point to which stories you deleted from the AI output and say why.",
    ),

    dict(
        num=9,
        topic=3,
        title="Running Dual-Track Agile — A Sprint Simulation with AI Assistance",
        objective="LO3 · LO1 · A7 · K5 — Using generative AI for faster iterations and feedback in agile sprints; lead design thinking projects.",
        duration=50,
        case="Marty Cagan describes the most common failure he sees in teams that believe they are agile: 'many people "
             "essentially doing little mini-waterfalls within their Scrum framework' — the product manager writes "
             "requirements, hands them to a designer who produces annotated wireframes, who hands them to a delivery "
             "team to build and test. Each handoff looks like collaboration and is actually a queue. The dual-track "
             "alternative runs discovery and delivery simultaneously in one team: the product trio continuously "
             "validates ideas cheaply while the delivery track builds the already-validated ones. Jeff Patton's line "
             "is the justification: 'The most expensive way to test your idea is to build production quality "
             "software.' Discovery's job is to kill ideas cheaply — 'if we're doing discovery right, we substantially "
             "change and kill lots of ideas.'",
        scenario="Your team is running Sprint 1 on the Cupcake release from Activity 8. Mid-sprint, a stakeholder "
                 "arrives with an urgent new request and a competitor announcement. You must decide what happens to "
                 "the sprint, the backlog and the discovery track.",
        desc="Learners simulate a compressed sprint — planning, a daily stand-up, a mid-sprint disruption, a review "
             "and a retrospective — running a discovery track in parallel, and use GenAI to accelerate the "
             "administrative parts of the ceremonies without surrendering the decisions.",
        build="A completed sprint simulation record: sprint goal, committed backlog, stand-up notes, a documented "
              "disruption decision, review outcome and an AI-assisted retrospective with three actions.",
        services="Padlet Classroom Board, Design Thinking Studio, ChatGPT or Microsoft Copilot",
        discussion=[
            "A stakeholder interrupts mid-sprint. What are your options, and what does each one cost in trust, focus and delivery?",
            "Cagan calls handoffs 'little mini-waterfalls'. Where do handoffs disguised as collaboration happen in your organisation?",
            "Discovery's job is partly to kill ideas. Why is killing an idea a success, and why do organisations rarely reward it?",
            "Which ceremony did GenAI genuinely improve, and which one would it damage if you let it run unsupervised?",
            "Your velocity drops because the team spent time on discovery. How do you explain that to a manager who only tracks delivery?",
        ],
        debrief="The disruption is the real lesson. Teams that protect the sprint goal and route the new request into "
                "the discovery track keep both their focus and their responsiveness; teams that swap scope mid-sprint "
                "lose the sprint and teach stakeholders that interrupting works. Note the asymmetry — the request "
                "does not have to wait long, it just has to be validated before it displaces committed work. On AI in "
                "ceremonies: it is excellent at summarising stand-up notes, clustering retrospective themes and "
                "drafting the sprint report, and it is actively harmful if it runs the retrospective itself, because "
                "the value of a retrospective is the team saying uncomfortable things to each other, not a tidy "
                "summary. Watch for velocity anxiety: a team doing genuine discovery will show lower delivery "
                "velocity and higher decision quality, which is only a problem if the organisation measures the "
                "wrong one.",
        steps=[
            ("Assign roles in your group: Product Owner, Scrum Master, and 2-3 Developers.", ""),
            ("Sprint Planning — agree a one-sentence sprint goal and pull Cupcake stories that fit. Post to Padlet.", ""),
            ("Run a 3-minute stand-up: each person states progress, next step and blockers.", ""),
            ("The trainer introduces the mid-sprint disruption. Decide as a team: absorb, defer, or swap. Document the decision AND the reasoning.", ""),
            ("In parallel, run the discovery track — open the Test stage in the Design Thinking Studio and log what you would validate before the new request enters a sprint.", ""),
            ("Sprint Review — present your Cupcake increment to another group acting as stakeholders and capture their feedback.", ""),
            ("Retrospective — each person posts one Keep, one Drop, one Try. Then ask the AI to cluster the themes.", ""),
            ("Compare the AI's clustering with your own reading of the room, and agree three concrete actions.", ""),
        ],
        test="Your sprint record shows a protected sprint goal, a documented and justified disruption decision, and "
             "three retrospective actions with named owners.",
    ),
]
