from app.agents.log_parser import parse_logs
from app.agents.timeline_agent import build_timeline
from app.agents.hypothesis_agent import generate_hypothesis

logs = parse_logs(
    "incident_data/logs/sample_logs.csv"
)

timeline = build_timeline(logs)

result = generate_hypothesis(timeline)

print(result)