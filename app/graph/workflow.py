from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.agents.timeline_agent import build_timeline
from app.agents.hypothesis_agent import generate_hypothesis
from app.agents.rag_agent import retrieve_similar_incidents
from app.agents.rca_writer import generate_rca

class IncidentState(TypedDict):

    parsed_logs: list
    timeline: list
    hypothesis: str
    incidents: list
    rca: str


def timeline_node(state):

    timeline = build_timeline(
        state["parsed_logs"]
    )

    return {
        "timeline": timeline
    }


def hypothesis_node(state):

    hypothesis = generate_hypothesis(
        state["timeline"]
    )

    return {
        "hypothesis": hypothesis
    }


def rag_node(state):

    incidents = retrieve_similar_incidents(
        state["hypothesis"]
    )

    return {
        "incidents": incidents
    }


def rca_node(state):

    rca = generate_rca(
        state["timeline"],
        state["hypothesis"],
        state["incidents"]
    )

    return {
        "rca": rca
    }

workflow = StateGraph(IncidentState)

workflow.add_node(
    "timeline",
    timeline_node
)

workflow.add_node(
    "hypothesis",
    hypothesis_node
)

workflow.add_node(
    "rag",
    rag_node
)

workflow.add_node(
    "rca",
    rca_node
)

workflow.set_entry_point(
    "timeline"
)

workflow.add_edge(
    "timeline",
    "hypothesis"
)

workflow.add_edge(
    "hypothesis",
    "rag"
)

workflow.add_edge(
    "rag",
    "rca"
)

workflow.add_edge(
    "rca",
    END
)

graph = workflow.compile()
