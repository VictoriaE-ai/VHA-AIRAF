# VHA-AIRAF

## VictoryHealth Analytics — AI Readiness Assessment Framework

An evidence-informed framework prototype for exploring organisational readiness to adopt AI in adult social care, initially scoped to England.

**Status: development prototype. Not independently validated, a certification scheme or approval to deploy AI.**

VHA-AIRAF combines 30 questions across ten readiness pillars with four critical gates. It helps structure evidence review, identify gaps and prioritise improvement actions. The overall capability score and the named-use-case gate outcomes are reported separately, so a high percentage cannot conceal a failed prerequisite.

Developed by **Victoria Ekweani** as part of [VictoryHealth Analytics](https://github.com/VictoriaE-ai/VictoryHealth-Analytics), connecting healthcare analytics, engineering judgement and responsible AI adoption.

## Start here

1. [Read the fictional assessment report](examples/willow_worked_case/ASSESSMENT_REPORT.md).
2. [Inspect the fictional evidence pack](examples/willow_worked_case/evidence_pack.md).
3. [Explore the methodology and all 30 scoring rubrics](docs/master_framework.md).
4. [View the Python calculator](src/score_assessment.py) and [tests](tests/test_scoring.py).

## The question this project explores

**What evidence should an adult-social-care provider examine before deciding whether a particular AI use case is appropriate to pursue?**

Readiness involves more than selecting a tool. VHA-AIRAF considers leadership, data, infrastructure, staff capability, governance, privacy, safety, people's experience, operational change and evaluation.

## How it works

| Component | Purpose |
|---|---|
| Organisation assessment | Thirty questions, each scored 0–5 against draft evidence criteria. |
| Ten pillar profiles | Show strengths, gaps and unanswered questions by topic. |
| Named-use-case gates | Examine scoped prerequisites using separate linked evidence responses. |
| Evidence register | Connects each judgement to evidence, rationale and limitations. |
| Improvement plan | Records actions, owners and acceptance evidence. |

For a complete assessment, the organisation index is the score sum divided by 150, expressed as a percentage. Missing or insufficient evidence is recorded as **Unknown**, not zero. Incomplete assessments receive coverage information rather than a complete overall index or capability band. N/A exclusions are disabled in this prototype.

### Ten pillars

1. Leadership and AI Strategy
2. Data Readiness
3. Digital Infrastructure
4. Workforce Capability
5. Governance and Ethics
6. Information Governance, Privacy and Cybersecurity
7. Patient and Care Safety
8. Person-centred Care
9. Operational Readiness and Change
10. Measurement and Continuous Improvement

### Four critical gates

| Gate | Required questions |
|---|---|
| G1 — Data fitness and controlled flows | Q4, Q5, Q6 |
| G2 — Governance and accountability | Q13, Q14, Q15 |
| G3 — Information protection and security | Q16, Q17, Q18 |
| G4 — Safety, oversight and lifecycle review | Q19, Q20, Q21, Q30 |

Within a gate, any substantiated score of 0–1 produces **Red**. Otherwise, unresolved evidence produces **Unresolved**; any score of 2 produces **Amber**; all required scores of 3–5 produce **Prerequisites evidenced**. The calculator never averages away a failed requirement.

Passing the mapped gates does not resolve other material findings or authorise implementation. Thresholds, equal weights, capability bands and gate choices are provisional design decisions, not externally validated cut-offs.

## Worked example: Willow

Willow Example Care Service is entirely fictional. Its proposed activity is a non-live, local mock handover summariser using invented records. No real provider, resident, interview, exercise, supplier or care record is represented.

| Result | Illustrative finding |
|---|---|
| Organisation index | **73/150 = 48.7%** |
| Capability profile | Partially established |
| Response coverage | 30/30 |
| G1, G2 and G3 | Amber |
| G4 | **Red — Q21 human oversight scores 1** |

The scenario assigns management accountability but shows that staff cannot reliably reject incorrect outputs and lack allocated review time. The report retains this contradiction and identifies acceptance evidence for remediation. Its judgements are authored illustrations awaiting independent review; complete responses do not establish adequate evidence or safe use.

## Run the calculator

Use Python 3.10 or later. The calculator uses the standard library; no additional packages are required. Run from the repository root:

```bash
python src/score_assessment.py examples/willow_worked_case/assessment.json --output examples/willow_worked_case/calculated_report.json
python -m unittest discover -s tests -v
```

The input keeps organisation responses and named-use-case gate responses separate. The output preserves evidence references, score rationales, limitations, pillar results and actions.

**Verification:** 22 automated tests passed in the development environment, including subcases for gate items. Checks cover score validity, completeness, duplicate IDs/JSON keys, evidence references, date/version checks, band boundaries, gate precedence and the worked example. These tests establish specified software behaviour, not framework validity or the correctness of assessor judgements.

## Completed assets

- Draft methodology and scoring anchors for all 30 questions.
- Consolidated framework with an initial reference register and concept mapping.
- Standard-library Python calculator with automated tests.
- Three calculation fixtures demonstrating normal, failed-gate and missing-evidence behaviour.
- A fictional evidence-linked assessment report and prioritised action plan.

## Work in progress

- Complete source-to-question mapping and review changing guidance.
- Review wording, score anchors and proportionality with relevant practitioners.
- Have independent assessors score the same fictional evidence and examine disagreements.
- Align the earlier presentation, use-case library and comparative analysis with this draft.

## Planned development

1. Improve the assessor workbook and structured question-bank format.
2. Refine the methodology following practitioner and assessor feedback.
3. Consider an appropriately governed pilot to evaluate usability, evidence burden and assessor consistency.

No external validation, real-provider pilot or demonstrated safety improvement has been completed or claimed.

## Limitations and responsible use

This is a portfolio prototype, not a clinical decision tool, legal assessment or regulatory certification. The index is not a probability that an AI system is safe. Exercises demonstrate preparedness only to the extent supported by their evidence; they do not establish live effectiveness.

The calculator checks structure and calculation rules. It cannot establish whether submitted evidence is true, sufficient, current or applicable, whether an assessor is competent, or whether score anchors have been met. Human review remains essential. Do not put real personal data, confidential provider records or sensitive security details in public examples.

## References and versioning

The [master framework](docs/master_framework.md#reference-register--initial-verified-concept-mapping) records initial authoritative sources, URLs, dates, applicability and coverage limitations. The mapping is incomplete. External sources provide context; they do not endorse or validate VHA-AIRAF's scoring rules.

| Item | Version |
|---|---|
| Methodology | 1.2 consolidated draft |
| Calculator | 0.1.0 |
| Worked-example package | 0.2.0 draft |

See [CHANGELOG.md](CHANGELOG.md) for development history and [REVIEW_STATUS.md](REVIEW_STATUS.md) for outstanding checks. No reuse licence has yet been selected; no open-source licence grant is asserted by this draft. Third-party materials retain their own terms.
