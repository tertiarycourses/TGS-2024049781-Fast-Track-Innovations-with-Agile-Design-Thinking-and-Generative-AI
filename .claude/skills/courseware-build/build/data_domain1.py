"""
Topic 1 activities — Foundations of Design Thinking, Agile, and Generative AI.

Real-world case studies. Every activity uses the course ed-tools:
  Design Thinking Studio — https://alfredang.github.io/designthinking/
  Padlet Classroom Board — https://alfredang.github.io/padlet/
"""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Airbnb — Diagnosing Why a Method Alone Does Not Save a Business",
        objective="LO1 · A1 · K1 · K2 — Integrate design thinking methodologies and agile principles to drive organisational innovation.",
        duration=45,
        case="Airbnb, 2009. The company was weeks from failing, stuck at roughly $200 revenue a week. The founders "
             "noticed a pattern in the New York listings: the photographs were terrible, taken on cheap phone cameras "
             "in bad light. Rather than run an A/B test or ship a feature, Paul Graham told them to fly to New York "
             "and meet the hosts. They rented a camera, went door to door, and replaced the amateur photos with "
             "professional ones. Within a week revenue roughly doubled. It was not a scalable act and it was not "
             "in any sprint backlog — but it was the insight that unlocked the business, and it later became a "
             "funded, scaled service.",
        scenario="Your team is the innovation unit of a regional marketplace platform whose bookings have flatlined. "
                 "Analytics show visitors browse and leave. The engineering team wants to A/B test the checkout "
                 "button. You suspect, as Airbnb did, that the real problem is not on the screen at all.",
        desc="Learners analyse the Airbnb turnaround to separate the three disciplines — Design Thinking (finding the "
             "right problem), Lean (validating the solution is worth building) and Agile (building it right) — and "
             "explain why starting with Agile alone would never have surfaced the photography insight.",
        build="A completed Padlet board mapping the Airbnb story onto Design Thinking / Lean / Agile, plus a group "
              "position statement on what the marketplace platform should do first.",
        services="Padlet Classroom Board, ChatGPT or Microsoft Copilot",
        discussion=[
            "Which of the three disciplines — Design Thinking, Lean or Agile — actually produced the photography insight, and why could the other two not have produced it?",
            "The founders did something deliberately unscalable. When is 'do things that don't scale' the right innovation strategy, and when is it an excuse to avoid rigour?",
            "Map the story onto the Double Diamond. Where does 'fly to New York and meet the hosts' sit — Discover, Define, Develop or Deliver?",
            "Your engineers want to A/B test the checkout button. Write the one question you would ask them to expose whether they are solving the right problem.",
            "How would you have used GenAI here — and what part of this story could GenAI NOT have done for you?",
        ],
        debrief="The photography insight came from Empathise, not from analytics. Agile would have optimised the wrong "
                "thing faster — a better checkout button on a listing nobody wanted to book. Lean's contribution was "
                "the cheap validation (a handful of listings, one week, one rented camera) before any engineering "
                "investment. The trap the class should name out loud: teams reach for Agile because it feels "
                "productive, and end up building the wrong thing right. GenAI could have clustered the review "
                "complaints and drafted interview guides in minutes, but it could not have sat in a host's living "
                "room and noticed the light. Empathy is still human work; AI compresses the analysis around it.",
        steps=[
            ("Trainer creates the Padlet classroom and shares the classroom code and QR with the class.", ""),
            ("Join the Padlet board at https://alfredang.github.io/padlet/ using the classroom code and your display name.", ""),
            ("Read the Airbnb case in the Learner Guide (Activity 1) with your group of 3–5.", ""),
            ("In the section 'Right Problem', post what the real problem was and the evidence for it.", ""),
            ("In the section 'Right Solution', post how the founders validated cheaply before scaling.", ""),
            ("In the section 'Build It Right', post what Agile delivery would look like once the insight is proven.", ""),
            ("Use ChatGPT to stress-test your position: paste your problem statement and ask it to argue the opposite case.", ""),
            ("Post your group's one-sentence recommendation for the marketplace platform, then Like the two strongest posts from other groups.", ""),
        ],
        test="Your board shows the story correctly split across all three disciplines, and your recommendation names a "
             "discovery action before any build action.",
    ),

    dict(
        num=2,
        topic=1,
        title="Netflix vs Blockbuster — Innovation as an Operating System",
        objective="LO1 · LO4 · A6 · K2 · K3 — Cultivate design thinking as a viable tool to foster new innovations; drivers of organisational growth.",
        duration=45,
        case="In 2000 Reed Hastings offered to sell Netflix to Blockbuster for $50 million. Blockbuster's CEO "
             "reportedly laughed him out of the room. Blockbuster had 9,000 stores and made a large share of its "
             "profit from late fees — a revenue stream that depended on customers being unhappy. Netflix removed late "
             "fees entirely, then cannibalised its own profitable DVD-by-mail business to launch streaming in 2007, "
             "then cannibalised licensed content by producing originals from 2013. Blockbuster filed for bankruptcy "
             "in 2010. Netflix did not win on a single idea; it won because it repeatedly ran the innovation loop "
             "against itself while its competitor optimised the business it already had.",
        scenario="You lead innovation at an established Singapore firm whose most profitable product line depends on "
                 "a customer inconvenience — a booking fee, a lock-in contract, or a manual process customers pay to "
                 "have done for them. A start-up has just launched a free alternative. The board wants a response by "
                 "the end of the quarter.",
        desc="Learners contrast an organisation that treated innovation as a repeatable operating system with one that "
             "optimised its existing model, and identify the specific organisational conditions — purpose, autonomy, "
             "and what gets measured — that allowed one to self-disrupt and prevented the other.",
        build="A Padlet comparison board plus a written 'what we would have to stop measuring' statement for the "
              "learner's own organisation.",
        services="Padlet Classroom Board, ChatGPT or Microsoft Copilot",
        discussion=[
            "Blockbuster's late fees were both its profit engine and its biggest customer pain point. What is the equivalent in your own organisation?",
            "Netflix cannibalised two of its own successful businesses. What made that organisationally possible, and what would block it where you work?",
            "'Measure things that matter' — what was Blockbuster measuring that made the decision to decline look rational at the time?",
            "Was Blockbuster's failure a failure of ideas, of execution, or of the operating system around both? Defend your answer.",
            "Where could GenAI have given Blockbuster early warning, and would leadership have believed it?",
        ],
        debrief="Blockbuster did not lack information — it lacked an operating system that let unwelcome information "
                "change a decision. Its metrics rewarded protecting late-fee revenue, so every rational manager "
                "defended it. This is the 'measure things that matter' principle in its negative form: a metric that "
                "cannot change a decision is decoration, and a metric that punishes the future protects the past. "
                "Netflix's advantage was structural, not creative: purpose and autonomy at the top, cheap "
                "experiments underneath, and a willingness to let a new bet eat an old one. GenAI would have "
                "flagged the trend, but the barrier was never detection — it was the incentive to act.",
        steps=[
            ("Rejoin the Padlet classroom board and open the Activity 2 section.", ""),
            ("In your group, list every Blockbuster metric you can infer from the case in the sub-section 'What they measured'.", ""),
            ("Post one metric from your own organisation that quietly protects the status quo.", ""),
            ("Ask ChatGPT: 'What early signals should a DVD rental chain have tracked in 2000 to detect streaming disruption?' and evaluate whether those signals were knowable then.", ""),
            ("Post your group's answer to 'what we would have to STOP measuring to innovate honestly'.", ""),
            ("Comment on another group's post, naming one risk in their proposal.", ""),
        ],
        test="Your board names at least one real metric in your own organisation that discourages innovation, and one "
             "concrete change to it.",
    ),

    dict(
        num=3,
        topic=1,
        title="Positioning GenAI in the Innovation Loop — Where It Helps and Where It Lies",
        objective="LO1 · K1 — Latest trends in design thinking; how generative AI enhances design thinking and agile processes.",
        duration=40,
        case="A Singapore bank's innovation team used a large language model to generate customer personas for a new "
             "savings product aimed at gig-economy workers. The AI produced five polished, confident personas in "
             "under a minute, complete with names, incomes, quotes and frustrations. The team built a concept around "
             "'Marcus, 29, a Grab driver saving for a HDB flat'. When they finally ran six real interviews, the actual "
             "gig workers' dominant anxiety was not saving for a flat at all — it was irregular income smoothing "
             "within a single month, and a deep distrust of anything that locked their money away. The AI personas "
             "were plausible, internally consistent, well-written, and wrong. They were a compression of what the "
             "internet says about gig workers, not evidence about these gig workers.",
        scenario="Your team has two weeks to produce a validated problem statement. A colleague proposes skipping the "
                 "interviews because 'the AI personas are good enough and we're behind schedule'.",
        desc="Learners run the same persona-generation task through a GenAI tool, then interrogate the output against "
             "an evidence test, to build a working rule for where GenAI belongs in the design thinking loop and where "
             "its confident fluency becomes a liability.",
        build="A GenAI-generated persona set annotated with evidence gaps, and a group 'AI use rule' posted to Padlet.",
        services="ChatGPT or Microsoft Copilot, Padlet Classroom Board",
        discussion=[
            "The AI personas were plausible but wrong. What property of large language models makes fluent output a poor proxy for truth?",
            "Which parts of the design thinking loop can GenAI genuinely accelerate, and which parts must stay human? Draw the line and justify it.",
            "Your colleague says the interviews can be skipped. Give the strongest version of their argument, then rebut it.",
            "How would you make an AI-generated persona falsifiable — what evidence would prove it wrong?",
            "What governance would you put in place so AI-generated insight is always labelled as unvalidated?",
        ],
        debrief="A language model generates the statistically likely, not the locally true. That is exactly what you "
                "want for divergence — volume, range, provocations, first drafts — and exactly what you must not "
                "trust for convergence, where a wrong-but-confident persona sends a whole quarter's work in the wrong "
                "direction. The workable rule most groups arrive at: use GenAI to widen the funnel and to synthesise "
                "evidence you already collected; never use it as the evidence itself. Practically, every AI-generated "
                "artefact should carry a provenance label — who or what produced it, and what real-world evidence has "
                "since confirmed or refuted it. Note also the failure was caught only because someone eventually "
                "talked to six real people; six interviews is a small price for not building the wrong product.",
        steps=[
            ("Open ChatGPT or Microsoft Copilot.", ""),
            ("Prompt: 'Create 3 detailed user personas for a savings product aimed at gig-economy workers in Singapore. Include name, age, income pattern, goals, frustrations and a representative quote.'", ""),
            ("Read the output as a group and mark every claim that is an assumption rather than evidence.", ""),
            ("Prompt the AI again: 'For each persona, list what evidence would be required to confirm it, and what would falsify it.'", ""),
            ("Compare the two outputs — note how much more useful the second framing is.", ""),
            ("Draft your group's one-sentence rule for using GenAI in discovery and post it to the Padlet Activity 3 section.", ""),
            ("Like the rule you find most defensible from another group and comment why.", ""),
        ],
        test="Your annotated persona set clearly separates assumption from evidence, and your posted rule states both "
             "where GenAI is allowed and where it is not.",
    ),
]
