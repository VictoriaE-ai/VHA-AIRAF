# VHA-AIRAF: consolidated methodology and scoring rubric

Version: 1.2 CONSOLIDATED DRAFT — 22 October 2026  
Owner: VictoryHealth Analytics / Victoria Ekweani  
Status: development prototype; not empirically validated or approved for operational decisions.

## Purpose and scope

This draft resolves inconsistencies in the reviewed v1.1 framework and its supporting presentation. It does not replace those originals until reviewed and adopted. Initial intended setting: adult social care in England. Wider healthcare and other UK jurisdictions require separate applicability review.

The framework structures evidence gathering and improvement planning. It provides neither certification nor permission to deploy AI. Scores do not measure the probability that an AI system is safe. Equal weights, thresholds and gate choices below are author-designed, provisional assumptions requiring evaluation.

## Two linked assessment records

1. **Organisation record:** the existing 30 questions across ten pillars, assessing current capability. Use the same question IDs across documents, CSV files and software.
2. **Use-case record:** one named application with an intended purpose, setting, affected people, data flows, supplier, accountable owner, human review process, failure modes, fallback arrangements and evaluation plan. Record use-case-specific evidence for applicable gates; an organisational score cannot substitute for it.

Assessments must identify the organisation, assessor, reviewer, date, question-bank version, methodology version and evidence cut-off date. Examples must use fictional organisations and synthetic evidence only.

## Responses and evidence

Every question has exactly one response state:

| State | Meaning | Calculation |
|---|---|---|
| Scored | Integer 0–5 supported by a recorded rationale and evidence review | Included in scored coverage and numerator |
| Unknown | Not answered, insufficient evidence or unresolved disagreement | No score; retained in denominator |
| Not applicable | Written rationale accepted by reviewer | Removed from denominator; disclosed separately |

Zero means confirmed absence of the capability, not missing information. A self-declaration alone may justify a hypothesis but does not establish that a process operates effectively: record Unknown if evidence cannot substantiate the proposed score. Unsupported numeric entries are invalid.

For this initial prototype all 30 organisational questions remain applicable. Do not enable N/A exclusions until a documented applicability rule and reviewer procedure exist. Use-case gate items cannot be excluded merely because an organisation does not yet have the capability. Record exclusions explicitly and do not return a gate outcome when applicability is unresolved.

Evidence register fields: evidence ID, description, location/reference, owner, date, review date, assessment scope, assessor findings and limitations. Avoid putting confidential evidence in a public repository; synthetic examples demonstrate the structure.

Documentary, operational and interview evidence should be considered together. A written policy does not prove consistent practice. Stale, contradictory or out-of-scope evidence requires a recorded resolution, otherwise the response remains Unknown.

## General score anchors

| Score | Proposed interpretation |
|---|---|
| 0 | Capability confirmed absent. |
| 1 | Informal awareness or isolated activity; no dependable process. |
| 2 | Documented or partially implemented process; material implementation gaps. |
| 3 | Implemented process with accountable ownership and evidence of routine operation. |
| 4 | Consistent operation with recorded checks, exceptions and corrective actions. |
| 5 | Sustained operation with outcome review and demonstrated improvement over time. |

These are common anchors, not a complete rubric. The anchors below propose question-specific criteria for scores 0–5; their adequacy requires practitioner review before assessor use. For multi-part questions, the lowest substantiated component limits the score; record component findings. Question-specific criteria must define the essential components rather than letting an assessor select only the strongest evidence.

Example for Q21 (human review): score 2 could mean a documented override process exists but staff cannot demonstrate it; score 3 requires an accountable, suitably competent reviewer and a demonstrated review/override/fallback process; scores 4–5 additionally need monitoring and improvement evidence. This illustrative anchor requires practitioner review.

Revise Q25 to assess demonstrated change capability through implementation evidence OR a credible plan and practical exercise, rather than requiring a history of major projects. Update the question bank and change log when adopting that wording.

## Score calculations

Let A be the number of applicable questions, S the number with substantiated numeric responses, and T their score sum.

- Coverage = 100 × S / A.
- Complete-assessment index = 100 × T / (5 × A), only when S = A and A > 0.
- When S < A, return **Assessment incomplete** with coverage and question-level findings; do not assign an overall band or present an answered-only percentage as the overall score.
- A = 0 is invalid. Duplicate or unexpected question IDs, noninteger scores, values outside 0–5 and unapproved exclusions are validation errors.
- Apply the same completeness rule to each pillar. Show completed pillar results even if another pillar is incomplete.
- Calculate using full precision. Round only display values to one decimal place; classify using the unrounded index.

Replace the previous assurance-sounding bands with provisional capability descriptions:

| Unrounded complete index | Capability profile |
|---|---|
| 0 ≤ index ≤ 20 | Foundational gaps |
| 20 < index ≤ 40 | Early development |
| 40 < index ≤ 60 | Partially established |
| 60 < index ≤ 80 | Established capabilities |
| 80 < index ≤ 100 | Strong documented capabilities |

These descriptions indicate assessed capability only. They do not establish implementation suitability or justify comparisons between providers with different scopes.

## Evidence type and exercise exceptions — consolidated clarification

The question-specific anchors below qualify the generic score-3 reference to routine operation. Where an anchor expressly permits a relevant practical demonstration, exercise, scenario check, rehearsal or representative collection test, it can support only the capability actually demonstrated. It cannot establish unobserved live performance. Questions with these provisions are Q2, Q7–Q11, Q18, Q20–Q22, Q24–Q26 and Q28–Q30. A reference to demonstration does not automatically permit a fictional exercise to replace an operating governance process; apply each anchor's conditions.

For every scored response record evidence_mode as operational, exercise, mixed or confirmed_absence, and record scope and limitations. Unknown responses have no numeric score or evidence_mode; retain the reason and any evidence reviewed. Scored responses still require evidence IDs and reviewer rationale. An exercise can support higher scores only where the specific anchor permits it and repeated improvement is substantiated. Never relabel exercise evidence as sustained live effectiveness.

Organisation responses and use-case gate responses are separate linked records. Each named use case needs a response for every gate item, even if it explicitly references applicable organisation evidence. Do not silently copy scores between scopes. When different evidence modes are combined, label the index “mixed evidence” and disclose question-level modes; readiness percentages are not comparable performance benchmarks.

Q25's revised wording is proposed in this master draft and retains the same ID. The earlier documents remain historical drafts. A new provider may demonstrate preparedness through an appropriate plan and exercise without claiming a live delivery history. No approval or adoption is implied by consolidation.

No public assessment should be issued without required metadata: scope, versions, assessor/reviewer, dates, response state, evidence IDs, rationale, evidence mode and limits, and action ownership. Machine validation can check that these fields exist; it cannot establish that the evidence is true or adequate.

## One critical-gate system

Replace the v1.1 pillar-average gate test and the presentation's alternative grouping with the following proposed question-level system. Scores are assessed for the named use case using relevant evidence and the same anchors. Organisation and use-case response records remain separate; explicit scoped references may reuse applicable evidence.

| Gate | Required questions |
|---|---|
| G1 Data fitness and controlled flows | Q4, Q5, Q6 |
| G2 Governance and accountability | Q13, Q14, Q15 |
| G3 Information protection and security | Q16, Q17, Q18 |
| G4 Safety, oversight and lifecycle review | Q19, Q20, Q21, Q30 |

Q6 is mandatory in this prototype: even a standalone application needs a documented understanding of its inputs, outputs and permitted data flows; system integration is not required where unnecessary. Q30 is mandatory for every use case: monitoring and stopping arrangements must be planned before a pilot. Organisational capability remains in the wider assessment rather than becoming a substitute gate.

For each gate, use the worst applicable required-question outcome:

- Any substantiated score 0–1: **Red — prerequisite gaps**.
- Otherwise, any Unknown or unresolved applicability: **Unresolved — insufficient evidence**.
- Otherwise, any score 2: **Amber — remediation required**.
- Otherwise, all required scores 3–5: **Prerequisites evidenced**.

If Red and Unknown coexist, display Red and disclose every unresolved item. For the overall gate summary, apply Red > Unresolved > Amber > Prerequisites evidenced. Never average gate scores or allow the overall index to override an individual failure.

Gate thresholds are design proposals, not regulatory requirements. A prerequisite-evidenced result means only that the listed requirements have supporting evidence. Suitability for a live trial still needs the relevant organisational, professional and specialist decisions for that application. The framework does not automate those decisions.

## Required report output

Display: scope and versions; completeness; overall capability profile if complete; ten pillar findings; all four gate outcomes; evidence limitations; and actions with owners, due dates and acceptance evidence. Keep implementation decisions separate and record who made them and why.

Recommendations should follow the specific gap. Red and unresolved gate items receive attention before optimising a percentage. A 30/90/180-day action plan is an example schedule, not a requirement to progress despite unmet controls.

## Worked logic checks

| Fictional scenario | Expected result |
|---|---|
| All 30 scores are 5 except Q21 = 0 | 145/150 = 96.7%; strong documented capabilities; G4 Red; no affirmative deployment recommendation. |
| All 30 scores are 5 except Q16 = Unknown | Coverage 29/30 = 96.7%; no overall band; G3 Unresolved. |
| All scores are 3 | 90/150 = 60%; partially established; gate prerequisites evidenced if use-case evidence also supports all required scores. |
| All scores are 3 except Q30 = 2 | 89/150 = 59.3%; G4 Amber; remediation required. |
| A critical pillar contains 0, 5, 5 | Pillar score 66.7%; the zero still makes its associated gate Red. |
| Score 6, score 2.5 or duplicate Q21 | Reject input; do not issue assessment output. |

Add tests for exact band boundaries, missing non-gate answers, every gate's failure path, unresolved applicability and display rounding. These test calculation consistency, not framework validity.

## Development and validation plan

1. Review the drafted question-specific anchors and prepare a structured question bank; reconcile the framework, use-case library and presentation against this single methodology.
2. Build the calculator and fictional examples. Independently check arithmetic and gate outcomes against hand-worked cases.
3. Obtain adult-social-care, information-governance and safety practitioner critique. Have two assessors independently score the same fictional evidence; examine disagreement and revise ambiguous questions.
4. Consider a consented, appropriately governed pilot to evaluate usability, completion time, evidence burden and assessor consistency. Do not claim predictive validity or improved safety from a small usability pilot.

## GitHub preparation

Recommended separate repository: VHA-AIRAF, linked from VictoryHealth-Analytics. Start with README.md, docs/methodology.md, data/questions.csv, examples/, src/ and tests/. Add the corrected presentation and reference mapping after alignment.

Use repository release v0.1.0 for the initial development prototype; document that this repository version differs from methodology document version 1.2. Archive the original v1.1 materials as historical drafts and do not imply the presentation's previous sample scores were produced by this new method.

No repository creation, commits, uploads or portfolio edits are authorised by this draft. Prepare reviewable files first; obtain Victoria's approval before external changes.


## Complete question rubric

## Q1 — Strategy linked to care objectives

**Pillar:** Leadership and AI Strategy. **Gate:** not a critical gate question.

**Assessment question:** Is there an AI/digital strategy linked to care objectives?

**Essential components:** defined care/service objectives; explicit connection to proposed AI use; accountable owner; priorities and realistic resources; review arrangements.

| Score | Observable criteria |
|---|---|
| 0 | Records review and responsible-lead discussion confirm no strategy, direction or agreed care objectives for AI/digital adoption. |
| 1 | Leaders can describe an aspiration, but its connection to care objectives, ownership or priorities is informal. |
| 2 | A documented draft connects proposed AI/digital activity to care objectives and identifies ownership and resource needs, but approval or implementation is incomplete. |
| 3 | An approved, proportionate plan includes all essential components; evidence shows the owner uses it to prioritise actual preparation or adoption decisions. |
| 4 | Reviews track progress, resources, risks and exceptions against the plan; records show corrective decisions when delivery differs from expectations. |
| 5 | Repeated reviews demonstrate that feedback and measured outcomes have improved priorities, resource allocation or the strategy itself. |

**Evidence examples:** strategy or short approved plan; care improvement priorities; management decisions; named owner; resourcing records; review minutes and change history.

**Challenge prompt:** “Show one decision that changed because of the care objectives in this plan.” A general digital strategy counts only where its treatment of AI opportunities and limitations is explicit enough for the assessed scope.

**Typical action:** draft a proportionate plan linking one defined service problem to an accountable owner, resources and review date.

## Q2 — Leadership understanding of AI

**Pillar:** Leadership and AI Strategy. **Gate:** not a critical gate question.

**Assessment question:** Do leaders understand AI opportunities, limitations and risks?

**Essential components:** understanding of intended benefits; uncertainty and erroneous outputs; relevant data and bias risks; human accountability; escalation and specialist advice.

| Score | Observable criteria |
|---|---|
| 0 | A recorded discussion or scenario exercise confirms responsible leaders lack basic understanding across the essential components. |
| 1 | Some awareness or training exists, but leaders cannot explain material limitations or their responsibilities in a relevant scenario. |
| 2 | Leaders can describe benefits and material risks, with briefing or training records, but decision-making practice or escalation arrangements remain incomplete. |
| 3 | Responsible leaders demonstrate the essential components through an appropriate scenario or decision record and use a defined route for escalation and specialist advice. |
| 4 | Periodic checks identify gaps in leadership understanding; decisions and escalations are reviewed and corrective learning is recorded. |
| 5 | Repeated reviews demonstrate improvement in leadership decisions and learning arrangements, including responses to changed technology or emerging risks. |

**Evidence examples:** briefing records; scenario responses; decision minutes; escalation contacts; follow-up actions. Attendance at training alone does not establish understanding.

**Challenge prompt:** “An AI-generated summary omits an important care detail. What would you do, who remains accountable, and when would you seek help?” Do not require technical model-development expertise from leaders unless their role needs it.

**Typical action:** run a role-relevant scenario exercise and document learning needs and escalation routes.

## Q3 — Defined use cases and measurable value

**Pillar:** Leadership and AI Strategy. **Gate:** not a critical gate question.

**Assessment question:** Have specific use cases with measurable value been identified?

**Essential components:** service problem; intended purpose and boundaries; affected users; baseline or documented baseline-collection plan; measurable benefits and balancing measures for unintended harm; owner; comparison with a reasonable non-AI option.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no specific use case or service problem has been identified. |
| 1 | A tool or broad idea is proposed, but the problem, intended users or expected value is unclear. |
| 2 | A use-case brief defines the problem, purpose, users and proposed measures, but essential components remain incomplete or unreviewed. |
| 3 | An accountable owner has reviewed a complete brief with stakeholders; its measures, baseline approach, boundaries and non-AI comparison are specific enough to guide an evaluation. |
| 4 | Use-case selection and preparation are checked against the brief; review records address assumptions, baseline quality, feasibility and unintended effects. |
| 5 | Repeated portfolio reviews show that evaluation findings improve use-case selection and measures, including documented decisions to revise or reject unsuitable ideas. |

**Evidence examples:** use-case briefs; problem statements; process measures; stakeholder feedback; options appraisal; prioritisation decisions. A claimed percentage saving without a defensible baseline or evaluation plan is not demonstrated value.

**Challenge prompt:** “Why consider AI for this problem, and what result would show that a simpler process change is preferable?” A well-supported decision not to adopt AI can demonstrate effective capability.

**Typical action:** complete one use-case brief before expanding the tool list.

## Q4 — Data fitness for the intended purpose

**Pillar:** Data Readiness. **Gate:** G1 Data fitness and controlled flows.

**Assessment question:** Is the relevant data reliable, accurate and complete enough for its intended use?

**Essential components:** defined data and intended purpose; relevant quality dimensions and acceptance criteria; documented checks; findings and limitations; ownership and disposition of unacceptable data. Review completeness, accuracy, consistency, timeliness and representativeness where relevant, explaining exclusions.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no data-fitness assessment exists, or relevant data is known to be materially unsuitable without a controlled response. |
| 1 | Data is available and described informally, but there are no dependable checks or defined acceptance criteria. |
| 2 | Data sources, checks and proposed criteria are documented and partly applied, but material suitability gaps or unresolved findings remain. |
| 3 | Relevant checks have been completed against justified criteria for the defined purpose; findings support suitability within stated limits, and ownership and exception handling are evidenced. |
| 4 | Repeated quality checks monitor fitness and exceptions; records show corrective action or restrictions when acceptance criteria are not met. |
| 5 | Review over time demonstrates improved data fitness or detection of defects, with criteria and controls revised in response to findings and changes. |

**Evidence examples:** data inventory; dictionary; profiling results; sample checks against appropriate reference records; acceptance criteria; issue log; documented restrictions. Do not invent a universal completeness percentage: the criterion must be justified for the intended purpose.

**Challenge prompt:** “Which data defect could most seriously affect this use case, and how would you detect it before relying on the output?” Organisational checks demonstrate capability; G1 also requires evidence that covers the particular use case's inputs, including externally supplied data where relevant.

**Typical action:** define purpose-specific quality criteria, run checks and document whether unresolved defects prevent reliance on the data.

## Q5 — Data-quality processes

**Pillar:** Data Readiness. **Gate:** G1 Data fitness and controlled flows.

**Assessment question:** Are data-quality, validation and correction processes established?

**Essential components:** responsibilities; validation at appropriate points; issue reporting and correction; traceability of changes; review arrangements and escalation.

| Score | Observable criteria |
|---|---|
| 0 | Records review and responsible-staff discussion confirm no defined quality, validation or correction process. |
| 1 | Staff fix errors informally; responsibility and traceability are inconsistent or absent. |
| 2 | A process defines validation, responsibilities and correction, but implementation, traceability or review is incomplete. |
| 3 | The process operates for the assessed scope; staff can demonstrate validation, issue escalation, authorised correction and a traceable record of changes. |
| 4 | Checks track recurring defects and process exceptions; records show review of correction quality and action on unresolved or repeated problems. |
| 5 | Repeated reviews demonstrate improved prevention or detection of recurring defects, with verified changes to the process and staff guidance. |

**Evidence examples:** procedures; validation rules; staff demonstration; issue/correction log; access responsibilities; audit trail; quality-review decisions. A one-off cleaned spreadsheet supports Q4 findings but does not itself establish an ongoing Q5 process.

**Challenge prompt:** “Show how an error is reported, who can correct it, how the change is recorded and how downstream users are informed when needed.”

**Typical action:** establish a named owner and traceable issue-to-resolution workflow, then demonstrate it on a fictional defect.

## Q6 — Appropriate access and controlled data flows

**Pillar:** Data Readiness. **Gate:** G1 Data fitness and controlled flows.

**Assessment question:** Can relevant data be accessed and combined appropriately?

**Essential components:** identified inputs and outputs; purpose and authorised access; controlled transfer/linkage where required; supplier/external destinations; recording and review of access and exceptions. Standalone tools still need an input/output and access-control assessment.

| Score | Observable criteria |
|---|---|
| 0 | Evidence confirms required access or data handling is uncontrolled, or necessary data cannot be accessed with no workable controlled route. |
| 1 | Staff informally obtain or move data, but permissions, destinations or responsibility are unclear and controls are unreliable. |
| 2 | Data flows, access responsibilities and proposed controls are documented, but implementation, permission verification or transfer checks have material gaps. |
| 3 | Relevant flows and destinations are documented; authorised access and necessary transfers/linkages are demonstrated with appropriate checks, responsibility and exception handling. |
| 4 | Reviews check access, transfers and exceptions; records demonstrate removal of inappropriate permissions and correction of handling failures. |
| 5 | Repeated reviews show improved access or flow controls, with changes verified after supplier, workflow or system changes. |

**Evidence examples:** data-flow map; role/access matrix; access approval and removal records; controlled test transfers; linkage checks; supplier destination records; exception log. If combining data is unnecessary, record the rationale and demonstrate controlled standalone handling.

**Challenge prompt:** “Where does an input go, who can see it, and what happens to its copies and outputs?” Escalate uncertainty about permitted handling to the appropriate qualified reviewer rather than treating a technical test as proof of legal compliance.

**Typical action:** map the complete flow and demonstrate the authorised route with synthetic records before relying on it.

## Q7 — Infrastructure sufficiency

**Pillar:** Digital Infrastructure. **Gate:** not a critical gate question.

**Assessment question:** Is infrastructure sufficient for the intended AI-enabled service?

**Essential components:** defined connectivity, device and platform requirements; capacity and availability checks; accessibility/usability in the working environment; responsibility for upkeep; a workable fallback for disruption.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms essential infrastructure or a viable fallback is absent, making the defined service impracticable. |
| 1 | Basic equipment/connectivity exists, but requirements and limitations have not been assessed reliably. |
| 2 | Requirements and upgrade/fallback plans are documented and partly tested, with material gaps in capacity, availability or supportability. |
| 3 | Relevant equipment and connectivity meet documented requirements in a representative check; ownership and a demonstrated disruption fallback are in place. |
| 4 | Availability, capacity and exceptions are checked against the requirements; records show action on faults and ineffective fallback arrangements. |
| 5 | Repeated review demonstrates improved resilience or capacity planning, with changes retested in representative conditions. |

**Evidence examples:** requirement checklist; asset inventory; connectivity/capacity tests; availability records; maintenance arrangements; disruption exercise. Do not prescribe a fixed bandwidth or uptime target without a use-case justification.

**Challenge prompt:** “What happens if the connection or device fails during a busy shift, and has the fallback been demonstrated?”

**Typical action:** check the working environment against explicit requirements and exercise the fallback.

## Q8 — Integration and workflow compatibility

**Pillar:** Digital Infrastructure. **Gate:** not a critical gate question.

**Assessment question:** Can current systems work appropriately with the proposed AI/digital tool?

**Essential components:** workflow and system boundaries; required interfaces or controlled manual steps; data meaning and matching; test criteria and exception handling; responsibilities and change/rollback arrangements.

| Score | Observable criteria |
|---|---|
| 0 | A required connection/workflow is known to be infeasible or uncontrolled, with no viable alternative. |
| 1 | Compatibility is assumed from a supplier claim or informal process; workflow and failure points are not understood. |
| 2 | Interface or standalone workflow requirements and tests are documented, but testing or controls leave material gaps. |
| 3 | Representative tests demonstrate the chosen workflow, including data meaning, matching and error handling; accountable owners and workable change/rollback arrangements are evidenced. |
| 4 | Interface/manual-transfer errors and changes are reviewed; retesting and corrective actions address exceptions and version changes. |
| 5 | Repeated reviews demonstrate improved interoperability or reduced transfer errors, with verified improvements to tests and change controls. |

**Evidence examples:** workflow diagrams; interface specifications; field mappings; synthetic test records; error cases; acceptance decisions; change and rollback records. A supplier demonstration alone does not establish local compatibility.

**Challenge prompt:** “Could the right information be attached to the wrong person, lose its meaning or fail to reach the next system? Show the checks.” Where standalone operation is justified, test the complete standalone process rather than penalising absence of an interface.

**Typical action:** test realistic normal, mismatched, missing and failed-transfer cases using synthetic data.

## Q9 — Technical support and maintenance

**Pillar:** Digital Infrastructure. **Gate:** not a critical gate question.

**Assessment question:** Is technical support available for implementation and ongoing maintenance?

**Essential components:** named internal ownership; defined supplier/support responsibilities; incident triage and escalation; update/change arrangements; recovery/fallback and supplier-exit responsibilities.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no accountable support or maintenance arrangement for the intended service. |
| 1 | Staff rely on an informal contact; coverage, escalation or maintenance responsibility is unclear. |
| 2 | A support model identifies owners, contacts and maintenance needs, but coverage, escalation or recovery arrangements remain untested or incomplete. |
| 3 | Support responsibilities and response expectations match the use case; a recorded incident or appropriate exercise demonstrates triage, escalation and recovery, with controlled update and exit responsibilities. |
| 4 | Support performance, maintenance and exceptions are reviewed; records show corrective action when support or recovery expectations are missed. |
| 5 | Repeated reviews show improved support effectiveness or recovery, with updates to arrangements and verified corrective actions. |

**Evidence examples:** responsibility matrix; support agreement; service hours and escalation contacts; issue log; update records; recovery exercise; exit plan. An outsourced model is acceptable if accountability and practical access to support are demonstrated.

**Challenge prompt:** “Who responds outside normal hours if this service fails, and what does staff do while waiting?” Expectations should reflect potential consequences rather than an arbitrary response-time target.

**Typical action:** document and exercise a support scenario, including unavailable supplier support.

## Q10 — Staff understanding of AI

**Pillar:** Workforce Capability. **Gate:** not a critical gate question.

**Assessment question:** Do relevant staff understand basic AI concepts and limitations for their roles?

**Essential components:** recognition of AI's role in the workflow; uncertain/incorrect outputs; appropriate reliance and human responsibility; permitted information handling; routes to challenge and escalate concerns.

| Score | Observable criteria |
|---|---|
| 0 | A documented, relevant staff check confirms essential understanding is absent across the assessed scope. |
| 1 | Some staff awareness exists, but important misconceptions or unclear responsibilities remain. |
| 2 | Role-relevant learning and basic checks exist, but coverage or understanding of essential components has material gaps. |
| 3 | A justified assessment of relevant roles/shifts demonstrates essential understanding and appropriate responses to realistic scenarios; gaps are identified and addressed before affected staff rely on the tool. |
| 4 | Refresher checks and feedback identify misconceptions and coverage gaps; records show targeted corrective learning and reassessment. |
| 5 | Repeated reviews show improved understanding and application, with learning adapted after incidents, workflow changes or new limitations. |

**Evidence examples:** role/shift coverage record; learning materials; scenario responses; observed demonstrations; staff feedback and reassessment records. Course attendance or a few confident volunteers alone does not demonstrate workforce-wide capability. Document how staff were selected and the limits of the evidence.

**Challenge prompt:** “An AI output looks convincing but conflicts with the care record. What would you check, and how would you raise the concern?” Use accessible assessment formats and do not confuse confidence or technical vocabulary with competence.

**Typical action:** conduct role-appropriate scenario checks, record coverage and address the identified gaps.

## Q11 — Staff digital skills

**Pillar:** Workforce Capability. **Gate:** not a critical gate question.

**Assessment question:** Do relevant staff have sufficient digital skills for their roles?

**Essential components:** role-specific digital tasks; practical ability to complete them; recognition and escalation of errors; accessibility and support needs; representative coverage of relevant roles and shifts.

| Score | Observable criteria |
|---|---|
| 0 | Documented practical checks confirm that essential digital tasks cannot be performed across the assessed scope, with no effective support arrangement. |
| 1 | Some staff perform basic tasks, but substantial task, role or shift gaps remain and support is informal. |
| 2 | Required tasks and learning/support needs are documented and partly assessed, but material competence or coverage gaps remain. |
| 3 | Practical checks across a justified selection of relevant roles/shifts demonstrate essential tasks, error escalation and use of support; identified gaps are addressed before affected staff perform unsupported tasks. |
| 4 | Competence checks and support feedback identify recurring problems and coverage gaps; reassessment confirms targeted corrective action. |
| 5 | Repeated reviews demonstrate improved task performance or fewer recurrent errors, with learning and accessible support revised accordingly. |

**Evidence examples:** role/task matrix; observed demonstrations with synthetic records; error scenarios; support and reassessment records; coverage rationale. A self-rated confidence survey alone is insufficient.

**Challenge prompt:** “Show how you enter, find and correct information in this workflow, and what you do if you cannot complete the task.” Assessment formats should accommodate relevant support needs without concealing inability to perform essential tasks reliably.

**Typical action:** identify essential tasks and assess them practically, then address gaps and reassess affected staff.

## Q12 — Ongoing learning and development

**Pillar:** Workforce Capability. **Gate:** not a critical gate question.

**Assessment question:** Is ongoing digital/AI learning and development provided?

**Essential components:** accountable learning owner; role-based induction and refresh arrangements; protected access to learning/support; checks of understanding/application; updates after changes, incidents or identified gaps.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no organised digital/AI learning or development provision for relevant staff. |
| 1 | Isolated learning opportunities exist, without dependable ownership, coverage or follow-up. |
| 2 | A role-based plan identifies induction, refresh needs and responsibilities, but delivery, access or effectiveness checks are materially incomplete. |
| 3 | Relevant learning is delivered through an operating programme; records demonstrate role coverage, practical access, effectiveness checks and follow-up of identified gaps. |
| 4 | Reviews track delivery, accessibility, staff feedback and learning outcomes; corrective action addresses missed groups and ineffective content. |
| 5 | Repeated reviews demonstrate improved application or sustained resolution of learning gaps, with content and delivery updated after relevant changes and findings. |

**Evidence examples:** learning plan; induction and refresher materials; role/shift coverage; staff release arrangements; assessment outcomes; change-triggered updates. Attendance records show delivery, not effectiveness.

**Challenge prompt:** “How would you identify and train staff affected by a changed tool or workflow, including temporary staff?”

**Typical action:** create and operate a proportionate learning cycle with an owner, coverage tracking and post-learning checks.

## Q13 — Formal review before use

**Pillar:** Governance and Ethics. **Gate:** G2 Governance and accountability.

**Assessment question:** Are proposed AI/digital systems formally reviewed before use?

**Essential components:** defined review scope and triggers; documented intended purpose and risk considerations; proportionate supplier/evidence scrutiny; relevant stakeholder and specialist input; authorised decisions with conditions, residual uncertainties and re-review arrangements.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms there is no pre-use review process, or tools within scope are used despite a known missing required internal review without a controlled response. |
| 1 | Informal approval occurs, but evidence, responsibilities, conditions or decision records are unreliable. |
| 2 | A review process and checklist exist and are partly applied, but material evidence, specialist input or decision controls remain incomplete. |
| 3 | A completed relevant review demonstrates the essential components; the decision, conditions, owner and change/re-review triggers are recorded and acted upon. |
| 4 | Checks examine review completion, conditions and exceptions; records show action on bypassed reviews, overdue conditions or significant changes. |
| 5 | Repeated reviews demonstrate improved scrutiny and follow-through, with the process revised after lessons, supplier changes or emerging limitations. |

**Evidence examples:** intake form; review checklist; supplier evidence questions; meeting/decision record; conditions register; re-review decisions. A complete review can result in rejection or deferral: adoption is not required to demonstrate good governance.

**Challenge prompt:** “Show a decision to approve, restrict, defer or reject a tool, and how staff know the limits of that decision.” An uncompleted template or a fictional training exercise alone does not establish operation of an organisation's review process; record limits explicitly.

**Typical action:** complete a proportionate review of a defined proposal and record the outcome, conditions and accountable decision-maker.

## Q14 — Fairness, transparency and accountability

**Pillar:** Governance and Ethics. **Gate:** G2 Governance and accountability.

**Assessment question:** Are fairness, bias, transparency and accountability assessed?

**Essential components:** people and groups potentially affected; plausible unequal impacts and evidence limitations; understandable explanation of the tool's role and limits; human responsibility; route to question or challenge effects; controls, monitoring and response to concerns.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms there is no consideration of essential components, or a known material concern is ignored without a controlled response. |
| 1 | General ethical commitments exist, but affected groups, practical risks or responsibilities are not examined dependably. |
| 2 | A structured assessment identifies affected people and concerns, but evidence, accessible explanations, challenge routes or mitigation plans have material gaps. |
| 3 | A completed assessment addresses each essential component for the scope; relevant stakeholder input or justified alternatives inform controls, responsibilities and a demonstrated route to raise concerns. |
| 4 | Reviews examine concerns, evidence limitations and monitoring across relevant groups where feasible; corrective decisions and communication are recorded. |
| 5 | Repeated reviews demonstrate improved assessment, communication or mitigation, supported by follow-up evidence rather than an unsupported claim that bias has been eliminated. |

**Evidence examples:** impact assessment; stakeholder input; accessible user information; supplier evaluation limitations; group-level evaluation where appropriate and supportable; concern/response records. Explain why particular comparisons are relevant and what cannot be assessed. Do not invent group metrics where evidence is inadequate, or collect sensitive information solely to satisfy this rubric without appropriate review.

**Challenge prompt:** “Who could be disadvantaged, what evidence supports that judgement, and how could an affected person challenge an outcome?” Technical model explanations alone do not establish meaningful transparency for residents or staff.

**Typical action:** identify affected groups and plausible harms, document evidence limitations, and demonstrate an accessible explanation and concern route.

## Q15 — Governance ownership

**Pillar:** Governance and Ethics. **Gate:** G2 Governance and accountability.

**Assessment question:** Is AI governance ownership clearly assigned?

**Essential components:** named accountable organisational owner; clear role and decision authority; allocation of operational/specialist responsibilities; escalation and absence cover; records demonstrating that ownership operates.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no person or group accepts accountability for AI governance in the assessed scope. |
| 1 | A person is informally associated with AI, but their authority, duties or escalation responsibilities are unclear. |
| 2 | Roles and ownership are documented, but authority, cover, resources or practical operation remain materially incomplete. |
| 3 | Appointed owners understand and exercise their responsibilities; decision authority, escalation, cover and required specialist access are evidenced through relevant records. |
| 4 | Checks track decisions, escalations and assigned actions; records show correction of ownership gaps, unresolved responsibilities and overdue actions. |
| 5 | Repeated reviews demonstrate improved accountability and follow-through, with arrangements updated after organisational or service changes. |

**Evidence examples:** appointment/role record; proportionate responsibility matrix; delegated authority; meeting/action records; escalation examples; cover and continuity arrangements. Small providers do not need a new committee if existing governance can demonstrably fulfil these responsibilities. Supplier support does not substitute for organisational accountability.

**Challenge prompt:** “Who can stop use, who resolves an unresolved concern, and who covers that authority when the owner is absent?”

**Typical action:** name the accountable owner and document their authority, responsibilities, cover and escalation route; then demonstrate these through a real preparation decision.

## Q16 — Protection of personal and confidential information

**Pillar:** Information Governance, Privacy and Cybersecurity. **Gate:** G3 Information protection and security.

**Assessment question:** Are personal and confidential data protected in the assessed workflow?

**Essential components:** understood information types and purposes; accountable information-governance review of permitted handling; access and disclosure controls; proportionate collection, retention and disposal arrangements; supplier destinations and secondary use; handling of mistakes and exceptions.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms protection arrangements are absent, or known material exposure is left without an effective controlled response. |
| 1 | Basic confidentiality awareness or isolated controls exist, but information handling, ownership or safeguards are unreliable. |
| 2 | Information flows and safeguards are documented and partly implemented; material gaps remain in review, access, retention, supplier handling or exception response. |
| 3 | The defined workflow has an accountable information-governance review and demonstrated handling controls across all essential components, with limitations and responsibilities recorded. |
| 4 | Checks examine access, handling and disposal exceptions; records show correction of inappropriate disclosure, retention or supplier-handling concerns. |
| 5 | Repeated reviews demonstrate improved protection and fewer recurring control failures, with changes verified after workflow or supplier updates. |

**Evidence examples:** information inventory and flow map; relevant specialist review; role permissions; retention/disposal records; supplier handling terms and configuration checks; controlled demonstrations; issue log. Assess the actual configuration and workflow, not a provider's general marketing statement.

**Challenge prompt:** “What prevents staff from putting a confidential care record into an unapproved tool, and how would a mistake be detected and handled?”

**Typical action:** obtain a scoped information-governance review, resolve material handling gaps and demonstrate the agreed controls using synthetic records.

## Q17 — Cybersecurity and supplier risk assessment

**Pillar:** Information Governance, Privacy and Cybersecurity. **Gate:** G3 Information protection and security.

**Assessment question:** Are cyber risks assessed for proposed tools and suppliers?

**Essential components:** defined assets, connections and threats; proportionate supplier scrutiny; access/configuration and update controls; vulnerability and incident escalation; resilience/recovery arrangements; ownership and review after changes.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no cyber-risk assessment or controls for the scope, or a known material exposure is ignored without a controlled response. |
| 1 | Generic security assurances or isolated checks exist, but scope, responsibility or risk response is unreliable. |
| 2 | Risks, supplier questions and proposed controls are documented and partly addressed, with material gaps in verification, recovery or follow-up. |
| 3 | A proportionate completed assessment supports the defined configuration and supplier arrangement; controls, unresolved limitations, ownership and a demonstrated escalation/recovery route are recorded. |
| 4 | Reviews track configuration, updates, supplier changes and risk exceptions; records show follow-up and verification of corrective actions. |
| 5 | Repeated reviews demonstrate improved prevention, detection or recovery, with lessons incorporated into supplier scrutiny and system controls. |

**Evidence examples:** scoped risk review; supplier evidence and its limitations; configuration/access checks; update responsibilities; vulnerability escalation records; backup/recovery exercise. A certificate, questionnaire or penetration-test summary can contribute evidence but cannot establish that the local deployment is secure.

**Challenge prompt:** “What happens if the supplier is compromised or access is unavailable, and who decides whether this workflow must stop?”

**Typical action:** review the proposed configuration and supplier dependencies with competent support, prioritise unresolved exposures and exercise recovery. Do not run intrusive security tests without appropriate authorisation.

## Q18 — Privacy and security competence

**Pillar:** Information Governance, Privacy and Cybersecurity. **Gate:** G3 Information protection and security.

**Assessment question:** Are relevant staff trained and able to apply privacy, confidentiality and secure-use practices?

**Essential components:** role-relevant learning; coverage across relevant roles/shifts and temporary staff; practical understanding of approved handling and access; recognition/reporting of mistakes or suspicious activity; refresh and reassessment arrangements.

| Score | Observable criteria |
|---|---|
| 0 | Corroborated review confirms no relevant provision and no demonstrated understanding of essential practices across the assessed scope. |
| 1 | Basic awareness or some attendance records exist, but material misconceptions, coverage or reporting gaps remain. |
| 2 | Learning and competence checks are partly delivered, but practical application, role coverage or reassessment has material gaps. |
| 3 | A justified coverage review and practical scenarios demonstrate essential practices; affected staff receive appropriate support and reassessment before unsupported use. |
| 4 | Checks identify recurring misconceptions, incidents and missed groups; records demonstrate targeted learning and verification that gaps are addressed. |
| 5 | Repeated reviews demonstrate improved secure practice and learning effectiveness, with content updated after tool changes or lessons. |

**Evidence examples:** role/shift coverage; training materials; scenario responses; observed synthetic-data demonstrations; reporting-route awareness; reassessment records. Attendance alone cannot establish competence, and a few volunteers cannot establish coverage without a justified selection method.

**Challenge prompt:** “You have sent a care summary to the wrong destination. What do you do first, and whom do you contact?” Evaluate recognition and use of the local response procedure rather than recalling unsupported legal deadlines.

**Typical action:** check role-relevant handling and reporting scenarios, document coverage, and reassess identified gaps.

## Q19 — Safety impact assessment

**Pillar:** Patient and Care Safety. **Gate:** G4 Safety, oversight and lifecycle review.

**Assessment question:** Is safety impact assessed before the proposed AI-enabled technology is used?

**Essential components:** intended use and boundaries; affected people and workflow; plausible failure modes and harms; competent review and stakeholder input; controls, fallback and unresolved risks; acceptance/escalation responsibilities and review triggers.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no safety impact assessment, or a known material hazard is ignored without a controlled response. |
| 1 | Generic safety statements or informal discussion exist, but specific harms, controls or ownership are unclear. |
| 2 | A structured assessment identifies relevant hazards and proposed controls, but review, verification or handling of unresolved risks has material gaps. |
| 3 | A completed, competently reviewed assessment addresses all essential components; controls and fallback have relevant verification evidence, and unresolved limitations and decision responsibilities are explicit. |
| 4 | Reviews examine control effectiveness, incidents/near misses and changes; corrective decisions and re-verification are recorded. |
| 5 | Repeated reviews demonstrate improved hazard identification or control effectiveness, with lessons incorporated into assessment and verification practices. |

**Evidence examples:** scoped safety assessment; hazard/action register; workflow review; relevant practitioner input; control tests; fallback exercise; recorded decisions and triggers. Formal requirements depend on the application and setting and need separate specialist applicability review; this score establishes none automatically.

**Challenge prompt:** “What could go wrong if the output is wrong, late, missing or overtrusted, and how do you know the safeguards would work?” Include workload, missed visits and indirect harms where relevant, not only model accuracy.

**Typical action:** map a defined workflow's hazards, assign owners, test controls proportionately and record what remains unresolved before any implementation decision.

## Q20 — Incident reporting and escalation

**Pillar:** Patient and Care Safety. **Gate:** G4 Safety, oversight and lifecycle review.

**Assessment question:** Can digital/AI incidents and near misses be reported, escalated and followed through?

**Essential components:** accessible reporting route; recognition of safety/technical/information concerns; triage and accountable escalation; immediate protection/fallback; investigation and action tracking; feedback and learning. Local procedures must identify who assesses any external reporting obligations.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no usable reporting/escalation route, or a known serious concern is left without an effective response. |
| 1 | Staff rely on informal contacts; recognition, triage, response ownership or follow-through is unreliable. |
| 2 | Procedures and contacts exist and are partly introduced, but staff access, practical escalation or action tracking has material gaps. |
| 3 | A recorded relevant incident response or appropriate exercise demonstrates reporting, triage, escalation, immediate protection and action tracking; responsible staff know their roles and feedback route. |
| 4 | Reviews track reporting, response quality and action closure; records show correction of delays, missed escalations or ineffective follow-up. |
| 5 | Repeated reviews demonstrate improved detection, response or prevention of recurrence, with learning verified in revised procedures and practice. |

**Evidence examples:** procedure and reporting form; staff demonstration; contact/cover arrangements; incident or exercise log; action and feedback records; escalation decisions. No history of reported incidents is neither evidence of safety nor a reason to invent incidents: an exercise may demonstrate readiness, with its limitations disclosed.

**Challenge prompt:** “An AI alert fails and a resident may have been affected. How do you protect the person, preserve relevant information, escalate and track what happens next?”

**Typical action:** exercise a realistic scenario with synthetic details, including unavailable contacts, and verify ownership and action closure.

## Q21 — Effective human oversight

**Pillar:** Patient and Care Safety. **Gate:** G4 Safety, oversight and lifecycle review.

**Assessment question:** Can suitably competent humans review, challenge and override important AI outputs?

**Essential components:** named review roles and authority; competence, information and time to scrutinise outputs; clear limits on reliance; ability to challenge, correct, reject or stop use and apply a workable fallback; escalation and traceability of decisions.

| Score | Observable criteria |
|---|---|
| 0 | Evidence confirms important outputs cannot receive effective human scrutiny or intervention, with no workable controlled alternative. |
| 1 | Human review is claimed, but roles, authority, practical capacity or routes to challenge are unreliable. |
| 2 | Review and override procedures identify roles and limits, but competence, workflow capacity, demonstration or fallback has material gaps. |
| 3 | A relevant demonstration shows that suitably competent reviewers have the information, time and authority to challenge an output, intervene and use fallback; decisions and escalation are traceable. |
| 4 | Checks examine review quality, workload, overrides and exceptions; corrective action addresses ineffective scrutiny, excessive reliance or failed intervention. |
| 5 | Repeated reviews demonstrate improved oversight or intervention effectiveness, with verified changes to workflow, support and reviewer preparation. |

**Evidence examples:** responsibility and workflow records; review criteria; synthetic scenarios containing incorrect outputs; override/stop demonstrations; capacity assessment; decision logs; fallback exercise. A person clicking approval, a nominal sign-off or an unused override button is not evidence of meaningful oversight.

**Challenge prompt:** “Show how a reviewer detects and rejects a plausible but wrong output during a busy shift. What happens next?” Review must occur early enough to affect the relevant decision. Record limitations if the demonstration does not reproduce live pressures.

**Typical action:** define accountable reviewers, test realistic error and fallback scenarios, and resolve authority or capacity gaps before relying on outputs.

## Q22 — Care experience and dignity

**Pillar:** Person-centred Care. **Gate:** not a critical gate question.

**Assessment question:** Is the effect on individual care experience, dignity and preferences considered?

**Essential components:** likely benefits and burdens for affected people; dignity, autonomy and preferences; effect on human contact and staff attention; means of expressing concerns; practical responses and review measures.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no consideration of affected people's experience, or a known material adverse effect is ignored without a controlled response. |
| 1 | General person-centred statements exist, but practical effects, preferences or responsibilities are unclear. |
| 2 | An assessment identifies likely effects and proposed responses, but relevant input, practical arrangements or review measures remain incomplete. |
| 3 | A completed assessment informs the defined workflow; relevant preferences, human contact, dignity and concern routes are addressed through documented arrangements and appropriate demonstration or stakeholder review. |
| 4 | Feedback and experience measures are reviewed; records show responses to burdens, reduced human contact or unmet preferences. |
| 5 | Repeated reviews demonstrate improved experience or resolution of recurring concerns, with changes checked against the views of affected people where feasible. |

**Evidence examples:** experience assessment; accessible feedback; preference-handling process; workflow walk-through; qualitative and balancing measures; action records. Do not infer improved care experience solely from staff time saved or model accuracy.

**Challenge prompt:** “Could this tool make a person feel watched, unheard or less able to influence their care, and how would you respond?”

**Typical action:** review the proposed workflow from the person's perspective and define how experience and preferences will influence decisions.

## Q23 — Meaningful involvement

**Pillar:** Person-centred Care. **Gate:** not a critical gate question.

**Assessment question:** Are service users and, where appropriate, families, carers or advocates meaningfully involved?

**Essential components:** justified involvement approach; accessible and voluntary opportunities; attention to underrepresented voices; appropriate roles for families/carers/advocates; recorded feedback, decision influence and response to participants.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no involvement approach or effort, or relevant views are deliberately excluded without a defensible response. |
| 1 | Informal or one-way consultation occurs, with unclear coverage, accessibility or influence on decisions. |
| 2 | An involvement plan identifies relevant people and methods and is partly implemented, but coverage, support or feedback-to-decision records have material gaps. |
| 3 | Proportionate involvement has occurred through accessible methods; records explain participation and limitations, how views affected decisions, and how responses were shared. |
| 4 | Reviews examine participation gaps and whether people could influence decisions; corrective actions improve inclusion and feedback loops. |
| 5 | Repeated reviews demonstrate improved meaningful participation and responsiveness, supported by participant feedback and documented decision changes. |

**Evidence examples:** stakeholder map; accessible materials; anonymised themes; participation/coverage rationale; decision-response log; advocate input where appropriate. A satisfaction survey or information leaflet alone does not demonstrate meaningful influence.

**Challenge prompt:** “Show a concern or suggestion that changed the proposal, or explain transparently why it did not.” Family or carer input does not automatically substitute for the person's own voice or establish authority to decide for them. Where direct involvement is difficult or declined, document respectful attempts, support, appropriate alternative input and limitations; do not pressure participation to earn a score.

**Typical action:** use an accessible involvement method, record resulting decisions and close the feedback loop with participants.

## Q24 — Accessibility and digital exclusion

**Pillar:** Person-centred Care. **Gate:** not a critical gate question.

**Assessment question:** Are accessibility barriers and digital exclusion assessed and addressed?

**Essential components:** relevant communication, sensory, cognitive, language, practical and digital-access needs; accessible information and interaction; support and workable alternative routes; representative testing/feedback; ownership and resolution of barriers.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no accessibility/exclusion assessment, or a known material barrier is left without an effective controlled response. |
| 1 | General accessibility commitments or ad hoc help exist, but specific needs and alternatives are unclear. |
| 2 | Relevant barriers and proposed adjustments are documented, but testing, support or workable alternatives have material gaps. |
| 3 | Appropriate testing and feedback support the defined accessible workflow; staff can demonstrate help and practical alternative routes, with remaining limitations and owners recorded. |
| 4 | Reviews examine exclusion, access failures and use of alternatives; corrective actions address barriers and verify that adjustments work. |
| 5 | Repeated reviews demonstrate improved access or reduced recurring exclusion, with testing and support revised after lessons and changes. |

**Evidence examples:** needs/barrier assessment; accessible formats; supported demonstrations; relevant user feedback; alternative-route exercise; barrier/action log. A vendor's accessibility claim is supporting evidence, not proof that the local end-to-end service is accessible. Staff-only applications still require assessment of staff access and downstream effects on residents.

**Challenge prompt:** “How does someone get an equivalent workable service if they cannot use this interface, lack digital access or need communication support?” Do not assume a translation feature alone resolves language or comprehension barriers.

**Typical action:** test realistic access needs and the alternative workflow, document limitations and resolve material barriers.

## Q25 — Demonstrated change capability

**Pillar:** Operational Readiness and Change. **Gate:** not a critical gate question.

**Original v1.1 concept:** Has the organisation implemented major digital/operational change successfully?

**Proposed revised question:** Can the organisation plan, coordinate and review a proportionate digital/operational change, demonstrated through relevant implementation evidence or a credible plan and practical exercise?

**Change rationale:** A history of large projects is not the only way to demonstrate capability. Preserve question ID Q25, but flag this wording change in the canonical question bank and change log before adoption. It remains proposed, not an unrecorded replacement of the original.

**Essential components:** accountable owner; affected roles and workflow; realistic resources, milestones and communication; risk, dependency and fallback arrangements; acceptance criteria and review of lessons.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no capacity or workable arrangement to plan and coordinate the assessed change. |
| 1 | Informal change activity exists, but ownership, practical planning or coordination is unreliable. |
| 2 | A credible plan identifies essential components, but resourcing, coordination or practical demonstration has material gaps. |
| 3 | Relevant implementation evidence OR a credible plan plus a recorded practical exercise demonstrates essential components, including coordination, failure response and acceptance decisions; limitations are explicit. |
| 4 | Repeated implementation checks or exercises review dependencies, milestones and exceptions; records show corrective actions and verification that weaknesses are addressed. |
| 5 | Review across successive change activities or exercises demonstrates improved coordination and preparedness, with lessons incorporated and retested; evidence type and limits remain explicit. |

**Evidence examples:** proportionate plan; role/resource allocation; communication records; milestone checks; implementation or exercise log; fallback and acceptance decisions; lessons/actions. For an exercise-only evidence base, label the score as demonstrated preparedness, not a record of successful live transformation. A generic discussion or untested plan alone cannot reach score 3.

**Challenge prompt:** “A key staff member is unavailable and the supplier misses a milestone. Show who decides what changes and how the service continues.”

**Typical action:** build a realistic small-change plan and exercise a disruption scenario, then record and address the resulting lessons.

## Q26 — Workflow understanding and documentation

**Pillar:** Operational Readiness and Change. **Gate:** not a critical gate question.

**Assessment question:** Are workflows documented well enough to identify appropriate AI opportunities and their consequences?

**Essential components:** current workflow and intended changes; roles and handovers; information/decision points; exceptions and fallback; validation with people doing the work; ownership and updates.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no dependable understanding or documentation of the relevant workflow and its key responsibilities. |
| 1 | Informal descriptions exist, but handovers, exceptions or decision points are unclear. |
| 2 | A workflow map or equivalent record identifies essential elements, but validation, exceptions or proposed changes have material gaps. |
| 3 | Relevant staff have validated the workflow; a representative walk-through demonstrates roles, handovers, information use and fallback, with an owner and update arrangements. |
| 4 | Checks compare documented workflow with practice; records show correction of workarounds, unclear handovers and changes. |
| 5 | Repeated reviews demonstrate improved workflow reliability or documentation accuracy, with lessons incorporated and verified. |

**Evidence examples:** proportionate process map; standard work; staff walk-through; handover and exception cases; change history. A polished diagram without staff validation is insufficient.

**Challenge prompt:** “Where could this proposed tool add work, obscure responsibility or interrupt a handover?”

**Typical action:** map and validate one end-to-end workflow, including a failed or missing output and the fallback.

## Q27 — Staff participation in transformation

**Pillar:** Operational Readiness and Change. **Gate:** not a critical gate question.

**Assessment question:** Are staff supported to participate meaningfully in transformation?

**Essential components:** representation of affected roles/shifts; practical time and accessible channels; ability to raise concerns without discouragement; response and decision influence; support for workload or role changes.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no supported participation route, or concerns are deliberately suppressed without a controlled response. |
| 1 | Ad hoc consultation occurs, but coverage, time or follow-up is unreliable. |
| 2 | Participation arrangements identify groups and channels, but access, coverage, workload support or responses have material gaps. |
| 3 | Relevant staff participate through workable arrangements; records show concerns considered, decisions explained and practical support for affected roles. |
| 4 | Reviews examine representation, workload and response quality; corrective action addresses excluded groups and unresolved concerns. |
| 5 | Repeated reviews demonstrate improved participation or resolution of recurring change burdens, supported by staff feedback and documented changes. |

**Evidence examples:** role/shift coverage; protected participation arrangements; anonymised feedback themes; decision-response log; workload support and follow-up. Agreement with management is not a scoring criterion; informed dissent may demonstrate effective participation.

**Challenge prompt:** “Show a staff concern that changed the proposal or received an explained response, including feedback from less visible shifts.”

**Typical action:** provide realistic participation opportunities and close the feedback loop on concerns.

## Q28 — Quality, safety and efficiency indicators

**Pillar:** Measurement and Continuous Improvement. **Gate:** not a critical gate question.

**Assessment question:** Are appropriate quality, safety and efficiency indicators defined and usable?

**Essential components:** measures tied to service objectives; clear definitions, numerators/denominators where relevant and data sources; owners and collection cadence; baseline or a documented baseline-collection approach; interpretation of uncertainty and balancing measures; review and action triggers.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no relevant indicators or workable measurement approach. |
| 1 | Broad targets or isolated numbers exist, without dependable definitions, sources or ownership. |
| 2 | A measurement plan defines proposed indicators and responsibilities, but data availability, baseline approach or interpretation has material gaps. |
| 3 | Definitions and sources are established; a representative collection/calculation demonstrates usability, with baseline arrangements, balancing measures, review ownership and justified action triggers. |
| 4 | Reviews examine completeness, consistency, trends and unintended effects; records show correction of measurement problems and action on findings. |
| 5 | Repeated reviews demonstrate improved measurement usefulness or decision-making, with definitions and checks refined without concealing adverse trends. |

**Evidence examples:** metric dictionary; sample calculation; data-quality check; baseline plan/results; review record. Not every measure requires a percentage: qualitative experience evidence may be appropriate. Do not imply causation from a trend alone.

**Challenge prompt:** “What might improve on the dashboard while care quality worsens, and which balancing measure would reveal it?”

**Typical action:** define a small useful measure set and demonstrate reliable collection before expanding a dashboard.

## Q29 — Benefits evaluation

**Pillar:** Measurement and Continuous Improvement. **Gate:** not a critical gate question.

**Assessment question:** Can expected AI benefits be evaluated credibly against costs, burdens and alternatives?

**Essential components:** explicit benefit claims; baseline/comparison approach; relevant outcomes and balancing measures; total resource implications; evaluation responsibilities and decision criteria; uncertainty and limitations.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no defined benefits or credible way to evaluate them. |
| 1 | Benefits are asserted using generic claims or supplier estimates, without a dependable local evaluation approach. |
| 2 | An evaluation plan identifies outcomes, costs and comparisons, but baseline, feasibility, ownership or decision criteria have material gaps. |
| 3 | A complete, reviewed evaluation plan has demonstrably feasible collection/comparison arrangements, clear decision criteria and recorded limitations; claims remain prospective until results exist. |
| 4 | Pilot results or an appropriate evaluation rehearsal are checked against the plan; sensitivity to assumptions, missing information and unintended effects is examined and corrective decisions recorded. |
| 5 | Repeated evaluation cycles demonstrate improvements to evaluation quality and decision-making, including revising or rejecting unsupported benefits; actual outcomes and rehearsals remain clearly distinguished. |

**Evidence examples:** evaluation protocol; baseline/comparator; resource model; data-collection demonstration; results or rehearsal record; decision log. Synthetic results can test feasibility and arithmetic, not establish real benefits. Time saved does not automatically equal cash savings or better care.

**Challenge prompt:** “What result would make you stop pursuing this use case, and what alternative explanation could account for an apparent improvement?”

**Typical action:** specify a feasible baseline/comparison and decision criteria before making a public benefits claim.

## Q30 — Review, change and stopping arrangements

**Pillar:** Measurement and Continuous Improvement. **Gate:** G4 Safety, oversight and lifecycle review.

**Assessment question:** Are digital/AI tools reviewed after implementation, with effective arrangements to change, suspend or stop use when needed?

**Essential components:** accountable reviewer; scheduled and event-triggered reviews; monitoring of performance, safety, experience and supplier/workflow changes; thresholds for escalation or suspension; authority and practical fallback/exit; action tracking and reassessment before restart.

| Score | Observable criteria |
|---|---|
| 0 | Review confirms no review/stopping arrangement, or a known material failure is left in use without an effective controlled response. |
| 1 | An informal intention to review exists, but ownership, triggers or stop/fallback authority is unreliable. |
| 2 | A review and stopping plan identifies responsibilities and triggers, but monitoring, practical suspension/fallback or restart checks have material gaps. |
| 3 | Review arrangements operate for the assessed scope; a relevant record or practical demonstration verifies monitoring inputs, escalation, authority to stop, fallback and restart checks. A pre-pilot demonstration may establish preparedness only, with that limit explicit. |
| 4 | Repeated review or exercise records examine missed signals and changes; corrective actions verify that escalation, suspension and restart controls work. |
| 5 | Reviews over time demonstrate improved detection and lifecycle decisions, with lessons incorporated and retested; distinguish exercise-based preparedness from observed live effectiveness. |

**Evidence examples:** review schedule and owner; trigger register; monitoring sample; supplier-change notification arrangements; stop/fallback demonstration; action and restart-decision records. No actual incident or suspension is required to demonstrate preparedness. A documented plan alone cannot reach score 3.

**Challenge prompt:** “The supplier changes the model and performance deteriorates. Who notices, who can suspend use, how does care continue and what is needed before restart?”

**Typical action:** exercise a deterioration/change scenario, including stop authority and fallback, before relying on the system.

## Reference register — initial verified concept mapping

Access date for all entries: 22 October 2026. These four sources were opened and inspected. The mapping below is editorial interpretation of relevant concepts, not a clause-by-clause compliance assessment. No source validates the 0–5 scale, weights, thresholds, bands or gate mapping. The normative design of VHA-AIRAF remains its author's responsibility.

| ID | Reference and URL | Source date/status | Locator and scope |
|---|---|---|---|
| R1 | Department of Health and Social Care (2026), [Using AI in adult social care](https://www.gov.uk/guidance/using-ai-in-adult-social-care) | Published 29 September 2026; guidance | Best practice guidance and its subheadings; social-care AI context. |
| R2 | Information Commissioner's Office (2023), [Guidance on AI and data protection](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/) | Page states updated 15 March 2023; currently flagged under review following the Data (Use and Access) Act | Overview identifies accountability, accuracy, fairness, transparency, security and individual rights. Check current detailed chapters before relying on legal interpretation. |
| R3 | Department of Health and Social Care (2026), [Adult social care digital skills framework](https://www.gov.uk/government/publications/adult-social-care-digital-skills-framework/adult-social-care-digital-skills-framework) | Published 29 September 2026; applies to England | Themes 1–7; workforce skills and person-centred technology. |
| R4 | NHS Digital (2022), [Applicability of DCB 0129 and DCB 0160](https://digital.nhs.uk/services/clinical-safety/applicability-of-dcb-0129-and-dcb-0160) | Published/last edited 27 May 2022 | Applicability introduction; England health and adult social care. Applicability guide, not an audited mapping to standard requirements. |

The mapping deliberately includes “author extension” where these inspected pages do not directly substantiate the complete criterion. Further authoritative evidence is needed for detailed infrastructure, support, incident-response and clinical-safety anchors. The full ICO chapters and DCB standards have not been audited here. Other comparators from the original documents, including ISO/IEC 42001, DSPT and the National Commission recommendations, are not yet incorporated into this verified register. Omission means unfinished mapping, not irrelevance.

## Question-to-source mapping

| Question | Source locator | Relationship/limitation |
|---|---|---|
| Q1 | R1: Introduce an AI policy; R3: Theme 1, strategic decisions | Planning concept; detailed strategy anchors are author extension. |
| Q2 | R3: Theme 1, leadership level | Leadership concept; scenario criteria are author extension. |
| Q3 | R1: choosing tools | Problem/value concept. |
| Q4 | R1: high quality data; R2: accuracy overview | Quality concept; acceptance thresholds are local design. |
| Q5 | R3: Theme 4 | Data management concept; audit workflow is author extension. |
| Q6 | R2: security/minimisation overview | Partial concept link; detailed access/flow controls need deeper mapping. |
| Q7 | R3: Theme 2 | Partial skills link; infrastructure assurance is author extension. |
| Q8 | R3: Theme 2 | Partial skills link; interface verification is author extension. |
| Q9 | R3: Theme 2 | Partial skills link; support/exit controls need further sources. |
| Q10 | R1: workforce upskilling | Learning concept. |
| Q11 | R3: Theme 2 | Practical digital skills concept. |
| Q12 | R3: Theme 7 | Continuing development concept. |
| Q13 | R1: choosing tools | Review concept; formal decision controls are author extension. |
| Q14 | R2: fairness/transparency overview | Concept mapping; detailed chapters still to review. |
| Q15 | R1: human review | Accountability concept. |
| Q16 | R2: security/minimisation and rights overview | Concept mapping; no legal-compliance conclusion. |
| Q17 | R3: Theme 5 | Security skills concept; supplier assurance needs deeper mapping. |
| Q18 | R3: Theme 5 | Secure practice concept. |
| Q19 | R4: applicability introduction | Conditional context only; hazard criteria require standard-level mapping. |
| Q20 | R4: applicability introduction | Conditional context only; incident criteria remain author extension. |
| Q21 | R1: human review | Oversight concept; override testing is author extension. |
| Q22 | R3: Theme 1 | Person-centred practice concept. |
| Q23 | R1: choosing tools; R3: Theme 1 | Involvement concept. |
| Q24 | R3: Themes 1–2 | Accessibility concept. |
| Q25 | R3: Theme 1, managing change | Change concept; exercise option is author extension. |
| Q26 | R3: Theme 1 | Partial implementation link; workflow anchors are author extension. |
| Q27 | R1: AI policy consultation | Participation concept. |
| Q28 | R1: measurable outcomes | Measurement concept. |
| Q29 | R1: financial cost | Evaluation concept; comparison design is author extension. |
| Q30 | R1: continuous improvement | Review concept; stopping/restart controls are author extension. |

## Consolidation change log and review backlog

- Combined methodology and all six question sections; confirmed exactly one rubric for every ID Q1–Q30.
- Clarified exercise exceptions, evidence modes and separate organisation/use-case evidence scope. These clarifications govern this master draft; they do not retroactively alter the historical component files.
- Retained the proposed Q25 wording change and four question-based gates; no pillar-average gate test applies.
- Added an initial verified concept-source register with dates, links, locators and explicit coverage gaps. This is not yet a complete regulatory/evidence matrix.
- Kept all scoring criteria provisional; removed no need for independent assessor trials or practitioner review.

Before publication: review every anchor with relevant practitioners; verify deeper source mappings and changing guidance; check that exercise evidence cannot inflate claims of live effectiveness; trial inter-assessor consistency on fictional evidence; then implement and test the calculator. Revise the original presentation, comparative analysis and use-case library against the adopted version before claiming alignment.

## Provenance

Based on Victoria's four supplied VHA-AIRAF documents and the methodology/six rubric drafts prepared in this conversation. Their detailed score anchors are author-designed proposals. External references provide conceptual context, not endorsement. No GitHub or other external publication was changed during consolidation.
