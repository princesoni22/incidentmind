from app.agents.log_parser import parse_logs
from app.agents.timeline_agent import build_timeline
from app.agents.hypothesis_agent import generate_hypothesis
from app.agents.rag_agent import retrieve_similar_incidents
from app.agents.rca_writer import generate_rca

logs = parse_logs(
    "incident_data/logs/sample_logs.csv"
)

timeline = build_timeline(logs)

hypothesis = generate_hypothesis(
    timeline
)

incidents = retrieve_similar_incidents(
    hypothesis
)

report = generate_rca(
    timeline,
    hypothesis,
    incidents
)

print(report)
