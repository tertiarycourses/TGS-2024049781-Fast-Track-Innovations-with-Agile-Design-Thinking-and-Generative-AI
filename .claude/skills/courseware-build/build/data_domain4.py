"""
Topic 4 activities — Scaling and Sustaining Innovations with Agile Design Thinking and GenAI.

Real-world case studies, run on the course ed-tools:
  Design Thinking Studio — https://alfredang.github.io/designthinking/
  Padlet Classroom Board — https://alfredang.github.io/padlet/
"""

DOMAIN4 = [
    dict(
        num=10,
        topic=4,
        title="DBS Bank — Scaling Innovation Across 25,000 People",
        objective="LO4 · A2 · A6 · K2 · K3 — Develop strategies to proliferate design thinking across the organisation; drivers of organisational growth.",
        duration=50,
        case="Around 2014 DBS Bank set out to 'Make Banking Joyful' and to become a technology company delivering "
             "banking. Rather than launching an innovation lab and hoping it spread, DBS changed the operating "
             "system: it ran large-scale hackathons pairing bankers with start-ups, trained thousands of staff in "
             "customer journey thinking, moved the majority of its technology in-house from outsourced vendors, and "
             "adopted the discipline of measuring customer time saved — reporting tens of millions of customer hours "
             "eliminated from waiting and rework. Senior leaders were required to participate, not merely sponsor. "
             "DBS was subsequently named the world's best bank by multiple international publications. The "
             "instructive part is not the awards but the mechanism: DBS changed what got measured, who had "
             "authority, and what leaders personally did — and let the culture follow.",
        scenario="You have run one successful design thinking pilot in your department. Your director is impressed "
                 "and asks you to 'roll it out to the whole division' — 400 people — with no additional budget and "
                 "no change to existing KPIs.",
        desc="Learners analyse how a large regulated organisation actually scaled human-centred innovation, and build "
             "a realistic scaling plan that changes measurement, authority and leadership behaviour rather than "
             "merely running more training.",
        build="A one-page scaling plan for the learner's own organisation covering the first 90 days, the metric that "
              "would change, and the leadership behaviour required.",
        services="Padlet Classroom Board, ChatGPT or Microsoft Copilot",
        discussion=[
            "DBS measured 'customer hours saved'. Why is that a more powerful scaling lever than counting how many staff attended training?",
            "Your director offers no budget and no KPI change. What is the honest risk to the rollout, and how do you surface it professionally?",
            "DBS required leaders to participate rather than sponsor. What is the practical difference, and which does your organisation do?",
            "Which is harder to scale — the method, the mindset, or the authority to act on what you learn? Defend your ranking.",
            "Where would GenAI genuinely accelerate a 400-person rollout, and where would it create the illusion of progress?",
        ],
        debrief="Training 400 people produces 400 people who know the vocabulary and cannot use it, unless three "
                "other things change: what gets measured, who is allowed to decide, and what senior leaders visibly "
                "do. DBS's customer-hours-saved metric is instructive because it is a customer-value measure that "
                "the whole organisation could act on, unlike a training-completion count, which measures activity "
                "and changes nothing. The honest answer to the no-budget no-KPI-change instruction is that the "
                "rollout will produce awareness without behaviour — and the professional way to say so is to propose "
                "a smaller scope with a real metric attached rather than to accept an unachievable one. GenAI can "
                "genuinely help with scale here: producing training material, synthesising feedback from 400 people, "
                "spotting where teams are stuck. It cannot manufacture the authority that makes the method usable.",
        steps=[
            ("Rejoin the Padlet classroom board, Activity 10 section.", ""),
            ("Read the DBS case in the Learner Guide (Activity 10) with your group.", ""),
            ("Post the three mechanisms DBS used that were NOT training.", ""),
            ("For your own organisation, post one metric you would change and what behaviour that change would trigger.", ""),
            ("Ask ChatGPT: 'What are the most common failure modes when scaling design thinking in a large regulated organisation?' Evaluate its list against the DBS case.", ""),
            ("Draft your 90-day scaling plan: scope, metric, leadership behaviour, first team.", ""),
            ("Post it and comment on another group's plan, naming the assumption most likely to break.", ""),
        ],
        test="Your plan changes at least one measurement and one authority, not just the training calendar, and its "
             "scope is small enough to be real.",
    ),

    dict(
        num=11,
        topic=4,
        title="Boeing 737 MAX — Systems Thinking and the Cost of Local Optimisation",
        objective="LO4 · K2 · K4 — Systems thinking, feedback loops and causality; concept and principles of resource management.",
        duration=50,
        case="Boeing needed a fast, cheap answer to the Airbus A320neo. Fitting larger engines to the existing "
             "737 airframe changed the aircraft's pitch behaviour, so Boeing added MCAS, software that "
             "automatically pushed the nose down. Each decision was locally rational: "
             "reuse the airframe to save cost and time; solve the aerodynamic consequence in software; keep the "
             "aircraft under the same type rating so airlines would not need expensive pilot simulator training; "
             "therefore minimise what pilots were told about MCAS. Two crashes killed 346 people and the fleet was "
             "grounded worldwide for around 20 months. No single decision was insane in isolation. The system of "
             "decisions — commercial pressure, a reused airframe, a software patch, and a training omission driven "
             "by the commercial goal — was lethal. This is what a reinforcing feedback loop with no effective "
             "balancing loop looks like in practice.",
        scenario="Your organisation is under pressure to ship an AI-assisted feature before a competitor. Each team "
                 "is optimising its own deliverable. You have been asked to review the programme for systemic risk.",
        desc="Learners map a real systemic failure using interconnectedness, feedback loops and causality, then apply "
             "the same mapping to an AI-driven innovation programme to identify where local optimisation is "
             "producing global risk.",
        build="A causal loop map of the 737 MAX decision chain, and a systemic risk register for the learner's own "
              "AI-assisted programme.",
        services="Design Thinking Studio, Padlet Classroom Board, ChatGPT or Microsoft Copilot",
        discussion=[
            "Trace the chain: which decision made the next one seem necessary? Where could one balancing loop have broken it?",
            "Every decision was locally rational. What does that tell you about relying on individual good judgement as a safety mechanism?",
            "Who in the system had the information to see the whole picture, and what stopped that information from changing the outcome?",
            "Apply the same analysis to an AI-driven innovation programme. Where does speed pressure create a comparable blind spot?",
            "What is the systems-thinking equivalent of 'the scanner is too loud' — the local fix that hides the real problem?",
        ],
        debrief="Systems thinking is not an abstract philosophy; it is the discipline that catches failures no "
                "individual decision-maker can see. The 737 MAX chain is a textbook reinforcing loop: commercial "
                "urgency drove airframe reuse, which drove the software fix, which drove the training omission, each "
                "step justified by the previous one, with no balancing loop strong enough to interrupt it. Note who "
                "could have interrupted it — regulators, test pilots, engineers — and what neutralised them: "
                "delegated certification, schedule pressure, and a framing in which raising the concern meant "
                "arguing against the commercial case. For AI programmes the parallel is direct. Speed pressure "
                "produces a model shipped without evaluation, then a guardrail bolted on, then a monitoring gap "
                "because monitoring would slow the launch. The countermeasure is structural, not attitudinal: a "
                "named balancing mechanism with the authority to stop the line.",
        steps=[
            ("Open the Padlet classroom board, Activity 11 section.", ""),
            ("Read the 737 MAX case in the Learner Guide (Activity 11).", ""),
            ("On paper or in the workspace, draw the decision chain as a loop: each node is a decision, each arrow is 'made necessary'.", ""),
            ("Mark on your loop the single point where a balancing mechanism would have had the most leverage.", ""),
            ("Post a photo or description of your loop to Padlet.", ""),
            ("Now map YOUR AI-assisted programme the same way. Identify one reinforcing loop with no balancing counterpart.", ""),
            ("Ask ChatGPT to argue why your proposed balancing mechanism would be resisted, and prepare your response.", ""),
            ("Post your systemic risk register entry: the loop, the leverage point, the mechanism, and who has authority to trigger it.", ""),
        ],
        test="Your loop map shows causality rather than a timeline, and your risk register names a mechanism with a "
             "named owner who has authority to stop work.",
    ),

    dict(
        num=12,
        topic=4,
        title="Innovation Metrics — Designing KPIs That Change a Decision",
        objective="LO4 · A4 · K3 · K4 — Metrics and KPIs for measuring the success of innovation projects; resource management.",
        duration=45,
        case="Two innovation programmes reported to the same board. Programme A reported ideas submitted, workshops "
             "run, staff trained and prototypes built — all rising quarter on quarter. Programme B reported one "
             "number: the change in the time it took a customer to complete an application, and the resulting drop "
             "in abandoned applications. When budgets tightened, Programme A could not answer the question 'what "
             "decision would we make differently if this number moved?' and was cut. Its metrics measured activity, "
             "not consequence. Douglas Hubbard's test is the sharpest available: 'If a measurement matters at all, "
             "it is because it must have some conceivable effect on decisions and behaviour.' Thoughtworks adds the "
             "distinction most teams miss — validating that a problem is real, that a solution works, and that "
             "there is demand for it are three separate concerns needing three different tests.",
        scenario="You must present your innovation programme to a board that is deciding next year's budget. You have "
                 "one slide and four numbers.",
        desc="Learners audit vanity metrics against Hubbard's decision test, build a balanced measurement set "
             "spanning customer, business and societal value, and separate problem, solution and demand validation.",
        build="A four-metric innovation scorecard where every metric passes the decision test, plus a stated "
              "validation plan distinguishing problem, solution and demand.",
        services="Padlet Classroom Board, ChatGPT or Microsoft Copilot",
        discussion=[
            "Apply Hubbard's test to 'number of ideas submitted'. What decision would change if it doubled? If none, why is it still so popular?",
            "Separate problem validation, solution validation and demand validation. Give one test for each for your own concept.",
            "Which is harder to measure — customer value, business value or societal value — and what happens when you only measure the easy one?",
            "Your board wants a single number. What do you lose by giving them one, and how do you manage that?",
            "How could GenAI help build this scorecard, and how could it help you fool yourself with it?",
        ],
        debrief="Almost every group's first draft contains at least one activity metric — ideas submitted, workshops "
                "run, people trained — because they are easy to collect and always go up. Hubbard's test kills them "
                "on contact: if no plausible movement in the number would change any decision, the number is "
                "decoration and it will not survive a budget review. The three-validation split is the other common "
                "gap: a successful prototype test proves the solution works for people who already have the problem, "
                "and says nothing about how many people have it or whether they will pay. Teams routinely present "
                "solution-validation evidence as if it were demand evidence, which is how confidently-built products "
                "launch to silence. On GenAI: it will happily generate a plausible, well-formatted scorecard in "
                "seconds, and that fluency is precisely the risk — a metric set that looks professional and measures "
                "nothing consequential is harder to challenge than an obviously bad one.",
        steps=[
            ("Open the Padlet classroom board, Activity 12 section.", ""),
            ("List every metric your organisation currently uses to judge innovation. Be honest.", ""),
            ("Apply Hubbard's test to each: 'what decision would change if this number moved?' Strike out every metric that fails.", ""),
            ("Ask the AI: 'Propose 10 KPIs for an innovation programme, split into customer value, business value and societal value.'", ""),
            ("Apply the decision test to the AI's list too. Note how many fail.", ""),
            ("Build your four-metric scorecard: one customer, one business, one societal, one leading indicator.", ""),
            ("For your concept, write one test each for problem validation, solution validation and demand validation.", ""),
            ("Post your scorecard and challenge one metric on another group's board using Hubbard's test.", ""),
        ],
        test="Every metric on your scorecard has a stated decision attached to it, and your three validation tests are "
             "genuinely different tests rather than three versions of the same one.",
    ),
]
