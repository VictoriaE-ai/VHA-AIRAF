import streamlit as st

st.set_page_config(
    page_title="VHA-AIRAF Dashboard",
    layout="wide"
)

st.title("VHA-AIRAF Dashboard")
st.write("VictoryHealth Analytics — AI Readiness Assessment Framework")

st.warning(
    "Development prototype. Not independently validated "
    "or approved for operational decisions."
)

st.write("Welcome. This dashboard will display readiness scores and critical gates.")

from pathlib import Path
import json

example_file = (
    Path(__file__).resolve().parent
    / "examples"
    / "willow_worked_case"
    / "assessment.json"
)

if st.button("Load fictional Willow example"):
    try:
        assessment = json.loads(
            example_file.read_text(encoding="utf-8")
        )
        st.session_state["assessment"] = assessment
        st.session_state.pop("report", None)
        st.success("Fictional Willow example loaded.")
    except (OSError, json.JSONDecodeError) as error:
        st.error(f"Could not load the example: {error}")

if "assessment" in st.session_state:
    st.write(
        "Organisation:",
        st.session_state["assessment"]["metadata"]["organisation"]
    )
    st.caption("Entirely fictional data for demonstration.")

from src.score_assessment import assess

if "assessment" in st.session_state:
    if st.button("Calculate assessment"):
        try:
            st.session_state["report"] = assess(
                st.session_state["assessment"]
            )
        except ValueError as error:
            st.session_state.pop("report", None)
            st.error(f"Assessment could not be calculated: {error}")

if "report" in st.session_state:
    report = st.session_state["report"]
    organisation = report["organisation"]

    st.subheader("Assessment results")

    score = organisation["index_percent"]
    score_text = (
        f"{score:.1f}%" if score is not None else "Incomplete"
    )

    st.metric("Organisation capability score", score_text)
    st.metric(
        "Assessment coverage",
        f"{organisation['coverage_percent']:.1f}%"
    )

    st.write(
        "Capability profile:",
        organisation["capability_profile"] or "Not assigned"
    )
    st.write(
        "Critical-gate summary:",
        report["gate_summary"].replace("_", " ").upper()
    )

    st.caption(
        "Fictional demonstration only. "
        "The score does not establish safety or permission to deploy."
    )

if "report" in st.session_state:
    st.subheader("Critical gates")

    gate_names = {
        "G1": "Data fitness and controlled flows",
        "G2": "Governance and accountability",
        "G3": "Information protection and security",
        "G4": "Safety, oversight and lifecycle review",
    }

    for gate_id, gate in st.session_state["report"]["gates"].items():
        label = f"{gate_id} — {gate_names[gate_id]}"
        status = gate["status"]

        if status == "red":
            st.error(f"{label}: RED — prerequisite gaps")
        elif status == "amber":
            st.warning(f"{label}: AMBER — remediation required")
        elif status == "unresolved":
            st.info(f"{label}: UNRESOLVED — insufficient evidence")
        else:
            st.success(f"{label}: PREREQUISITES EVIDENCED")

        questions = (
            gate["red_questions"]
            + gate["unresolved_questions"]
            + gate["amber_questions"]
        )

        if questions:
            st.write("Questions requiring attention:", ", ".join(questions))

if "report" in st.session_state:
    st.subheader("Download results")

    report_json = json.dumps(
        st.session_state["report"],
        indent=2,
        ensure_ascii=False
    )

    st.download_button(
        label="Download assessment results",
        data=report_json,
        file_name="VHA_AIRAF_fictional_assessment_results.json",
        mime="application/json"
    )

if "report" in st.session_state:
    st.subheader("Readiness by pillar")

    pillar_rows = []

    for name, pillar in st.session_state["report"]["pillars"].items():
        pillar_rows.append({
            "Pillar": name,
            "Score (%)": pillar["index_percent"],
            "Coverage (%)": pillar["coverage_percent"]
        })

    st.dataframe(pillar_rows, hide_index=True)

if "report" in st.session_state:
    st.subheader("Pillar score chart")

    chart_rows = []

    for name, pillar in st.session_state["report"]["pillars"].items():
        if pillar["index_percent"] is not None:
            chart_rows.append({
                "Pillar": name,
                "Score (%)": pillar["index_percent"]
            })

    if chart_rows:
        st.bar_chart(
            chart_rows,
            x="Pillar",
            y="Score (%)",
            horizontal=True,
            sort=False,
            height=500
        )

    st.caption(
        "Only complete pillar scores are plotted. "
        "Higher scores do not override failed critical gates."
    )

if "report" in st.session_state:
    st.subheader("Improvement actions")
    st.caption(
        "These owners and dates are fictional examples, "
        "not real assignments or deadlines."
    )

    actions = st.session_state["report"]["actions"]

    if actions:
        for number, action in enumerate(actions, start=1):
            with st.expander(
                f"Action {number}: {action['description']}"
            ):
                st.write("Owner:", action["owner"])
                st.write("Illustrative due date:", action["due_date"])
                st.write(
                    "Evidence needed to complete this action:",
                    action["acceptance_evidence"]
                )
    else:
        st.info("No improvement actions are recorded.")


