"""
Topic 2 activities — Problem Framing and Ideation with Design Thinking and GenAI.

Real-world case studies, run on the course ed-tools:
  Design Thinking Studio — https://alfredang.github.io/designthinking/
  Padlet Classroom Board — https://alfredang.github.io/padlet/
"""

DOMAIN2 = [
    dict(
        num=4,
        topic=2,
        title="GE Adventure Series — Reframing the Problem Instead of Fixing the Machine",
        objective="LO2 · A3 · A5 — Synthesise information from different sources and stakeholders to fully understand end-user needs.",
        duration=50,
        case="GE Healthcare's MRI scanners were technically excellent, but designer Doug Dietz watched a small child "
             "cry with terror in front of one of his own machines. He learned that up to 80% of paediatric patients "
             "had to be sedated to complete a scan — which meant an anaesthetist on standby, longer slots, higher "
             "cost and real clinical risk. The engineering brief would have been 'make the scanner quieter and "
             "faster'. Dietz reframed it: the problem was not the machine's noise, it was a terrifying experience "
             "for a frightened child. The team painted the scanner rooms as pirate ships, jungles and space "
             "adventures, and trained operators to narrate the scan as an adventure — 'hold very still while the "
             "ship goes through the asteroid field'. Sedation rates for paediatric patients dropped dramatically "
             "(reported as low as around 10% in redesigned suites), patient satisfaction rose sharply, and throughput "
             "improved. Not one component of the scanner's imaging technology was changed.",
        scenario="You work for a Singapore polyclinic group. Elderly patients frequently miss or abandon their health "
                 "screening appointments. The operations team's proposed solution is an SMS reminder system with a "
                 "confirm button. Screening uptake has not moved in two years despite three reminder revamps.",
        desc="Learners practise the reframing move that turns a technical brief into a human one: building an empathy "
             "map from the case, extracting a Point of View statement, and generating How Might We questions at the "
             "right altitude — neither so broad they are useless nor so narrow they smuggle in the solution.",
        build="A completed Empathize and Define stage in the Design Thinking Studio: empathy map, POV statement and a "
              "voted set of How Might We questions for the polyclinic scenario.",
        services="Design Thinking Studio, ChatGPT or Microsoft Copilot",
        discussion=[
            "The engineering brief was 'make the scanner quieter'. Dietz's brief was different. State both as problem statements and explain what the reframe unlocked.",
            "GE changed the experience, not the technology. In the polyclinic scenario, what is the 'paint the scanner' equivalent — and what is the 'make it quieter' trap?",
            "Write a How Might We that is too broad, one that is too narrow, and one that is just right. What makes the third one workable?",
            "Whose perspective is missing from an empathy map built only from the operations team's data?",
            "Sedation rate was the number that proved the redesign worked. What single number would prove your polyclinic solution worked?",
        ],
        debrief="Reframing is the highest-leverage move in design thinking and the one teams skip under deadline "
                "pressure. 'Make the scanner quieter' produces an incrementally better scanner; 'how might we make a "
                "frightened seven-year-old feel brave' produces a pirate ship. Note what did not change: the imaging "
                "hardware, the physics, the budget for a new machine. The constraint was the same; the problem "
                "statement was different. The altitude test for a How Might We question: if there is only one obvious "
                "answer it is too narrow (the solution is hiding inside the question); if you cannot imagine any "
                "concrete answer it is too broad. For the polyclinic, the reminder-system framing assumes the barrier "
                "is forgetting. If the real barrier is fear of a bad result, fear of cost, or having nobody to "
                "accompany them, no reminder will ever fix it — and two years of flat uptake is the evidence.",
        steps=[
            ("Trainer clicks Create New Workspace at https://alfredang.github.io/designthinking/ and shares the workspace code or QR.", ""),
            ("Click Join Workspace, enter the code and your display name.", ""),
            ("Open the Empathize stage. In Empathy Map, post to Says, Thinks, Does and Feels for an elderly patient who skipped a screening.", ""),
            ("Post at least two entries into User Pain Points that are NOT about forgetting the appointment.", ""),
            ("Move to the Define stage. In Problem Statement, write a POV: '[User] needs [need] because [insight]'.", ""),
            ("In How Might We Questions, post three HMW questions at different altitudes.", ""),
            ("Use ChatGPT to generate five more HMW variants, then post only the ones that pass the altitude test.", ""),
            ("Vote on the HMW questions using the voting control; the top-voted question carries into Activity 5.", ""),
        ],
        test="Your Define stage holds a POV statement traceable to a specific empathy-map entry, and a top-voted HMW "
             "question that neither names a solution nor is too vague to answer.",
    ),

    dict(
        num=5,
        topic=2,
        title="IDEO Shopping Cart — Volume, Then Judgement",
        objective="LO2 · LO4 · A3 — Ideation and brainstorming techniques enhanced by generative AI.",
        duration=50,
        case="In 1999, ABC's Nightline gave the design firm IDEO five days to redesign the supermarket shopping cart "
             "on camera. The team did not start by designing. They went out and observed shoppers, interviewed store "
             "managers about theft and maintenance, and talked to a child-safety expert. They then ran structured "
             "brainstorms under explicit rules — defer judgement, encourage wild ideas, build on the ideas of others, "
             "go for quantity, stay focused, one conversation at a time, be visual — and generated a large volume of "
             "concepts before converging. The result was a modular cart with detachable hand baskets, a child seat "
             "designed for safety, and a scanning system that skipped the checkout queue. Crucially it was never "
             "meant for mass production; it was a provocation that demonstrated the process. The famous rule from "
             "that studio: separate idea generation from idea evaluation, because judging while generating kills the "
             "unusual ideas first.",
        scenario="Carry forward the top-voted How Might We question from Activity 4. Your team has 25 minutes to "
                 "generate and converge on ideas for the polyclinic screening challenge, with a GenAI tool available "
                 "as an idea multiplier.",
        desc="Learners run a disciplined divergence–convergence cycle using Crazy 8s and structured brainstorming, "
             "amplify it with GenAI, then converge with dot voting — experiencing directly why mixing generation and "
             "evaluation suppresses the best ideas.",
        build="A populated Ideate stage — brainstorming board, Crazy 8s, categorised ideas and a voted shortlist of "
              "three concepts to prototype.",
        services="Design Thinking Studio, ChatGPT or Microsoft Copilot",
        discussion=[
            "IDEO's rules include 'defer judgement' and 'encourage wild ideas'. What actually happens in a meeting when these are not enforced?",
            "You generated ideas manually, then with AI. Compare the two sets — which was more diverse, and which was more useful?",
            "The cart was never mass-produced. What is the value of a prototype that was never meant to ship?",
            "Under what conditions does GenAI reduce the diversity of ideas in a room instead of increasing it?",
            "Who should have the final vote on which idea proceeds — and what does that choice say about your organisation?",
        ],
        debrief="Two effects usually show up in the room. First, the manual round produces fewer ideas but more "
                "surprising ones, because they come from lived context the model does not have; the AI round produces "
                "more ideas but they cluster around the conventional centre of the training distribution. The "
                "productive pattern is manual-first, then AI to extend — running AI first anchors everyone to its "
                "framing and measurably narrows the room. Second, groups that skip the 'defer judgement' rule "
                "converge far too early on the safe idea. The IDEO cart matters precisely because it was never "
                "shipped: a prototype's job is to make an idea arguable and testable, not to be the final answer. "
                "Dot voting is not democracy for its own sake — it surfaces which ideas the group can actually rally "
                "behind before anyone spends money.",
        steps=[
            ("Open the Ideate stage in the Design Thinking Studio workspace.", ""),
            ("Round 1 — silent, manual. Each person posts at least four ideas into Brainstorming Board. No discussion, no judging.", ""),
            ("Round 2 — Crazy 8s. Eight rapid variations on the most promising idea, posted into Crazy 8s Ideas.", ""),
            ("Round 3 — AI amplification. Prompt: 'Give 15 diverse solution concepts for [your HMW question], including 3 deliberately unconventional ones.'", ""),
            ("Post only the AI ideas that add something your group did not already have.", ""),
            ("Group everything into themes using Idea Categories.", ""),
            ("Dot vote in Voting & Prioritisation and shortlist the top three concepts.", ""),
            ("Record in the workspace which of the three shortlisted ideas came from a human and which from the AI.", ""),
        ],
        test="Your Ideate stage shows a clear divergence phase and a separate convergence phase, with three shortlisted "
             "concepts and their provenance recorded.",
    ),

    dict(
        num=6,
        topic=2,
        title="Rapid Prototyping with AI — From Concept to Testable Artefact in One Hour",
        objective="LO2 · LO4 · A4 — Prototyping with AI-driven tools: rapid development and feedback.",
        duration=50,
        case="A hospital innovation team in Singapore needed to test whether a self-service kiosk would reduce queue "
             "times at a specialist outpatient clinic. The traditional route — a scoped software build — would have "
             "taken a quarter and a budget approval. Instead the team used a GenAI tool to draft the screen copy and "
             "flow, printed the screens on paper, and ran a 'Wizard of Oz' test in the clinic corridor: a staff "
             "member sat behind a curtain and swapped the paper screens by hand while real patients used it. Within "
             "two days they learned that elderly patients did not fail at the touchscreen — they abandoned at the "
             "point where the kiosk asked for an NRIC, because they were not sure whether it was safe to enter it in "
             "public view. That single insight redirected the entire design, and it cost nothing but paper and two "
             "afternoons. Had they built the software first, they would have discovered it after the budget was spent.",
        scenario="Take the top-voted concept from Activity 5. You have 50 minutes to make it testable by a real person "
                 "— not to build it.",
        desc="Learners use GenAI to draft prototype content and user flows, assemble a low-fidelity prototype, and "
             "define an explicit test plan with falsifiable assumptions — practising 'build to think' rather than "
             "'build to ship'.",
        build="A low-fidelity prototype (paper, slide or wireframe) with a written test plan, listed assumptions and "
              "the criteria that would prove the concept wrong.",
        services="Design Thinking Studio, ChatGPT or Microsoft Copilot, Adobe Firefly (optional)",
        discussion=[
            "The kiosk team learned the real barrier was privacy, not usability. Which of your assumptions, if wrong, would sink your concept fastest?",
            "What is the cheapest possible artefact that would still generate a real reaction from a real user?",
            "'Build to think, not to ship.' What is the risk of a prototype that looks too polished?",
            "Where did GenAI genuinely save time here, and where would relying on it have hidden the privacy insight?",
            "Write the one question you would ask a test user that could prove your concept wrong.",
        ],
        debrief="A prototype's purpose is to buy information at the lowest possible price. The kiosk team bought a "
                "quarter's worth of learning for two afternoons and a stack of paper. Note the specific trap in "
                "polished prototypes: when an artefact looks finished, test users critique surface details and "
                "politely withhold fundamental objections — a rough paper screen invites honest reaction in a way a "
                "clean mockup does not. GenAI is genuinely excellent at the drafting layer here: screen copy, flow "
                "logic, edge cases, even the interview script. What it cannot do is stand in the corridor and watch "
                "a 74-year-old hesitate over her NRIC. Every prototype should ship with its falsification criteria "
                "written down in advance; a test you cannot fail is a demonstration, not a test.",
        steps=[
            ("Open the Prototype stage in the Design Thinking Studio workspace.", ""),
            ("Post your concept in one paragraph into Prototype Description.", ""),
            ("Prompt the AI: 'Draft the user flow and screen-by-screen copy for [your concept]. Flag the three steps most likely to cause drop-off.'", ""),
            ("Post the flow into User Flow and the key screens into Screens / Wireframes.", ""),
            ("List every assumption your concept depends on in Assumptions — be ruthless.", ""),
            ("Optionally use Adobe Firefly to generate a visual for the concept.", ""),
            ("Move to the Test stage and write a Test Plan: who you would test with, the task you would set, and what result would prove you wrong.", ""),
            ("Swap workspaces with another group, run their prototype as a user, and post honest feedback into their User Feedback section.", ""),
        ],
        test="Your prototype can be run by someone from another group without you explaining it, and your test plan "
             "states in advance what result would falsify the concept.",
    ),
]
