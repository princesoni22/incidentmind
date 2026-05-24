from app.agents.log_parser import parse_logs
from app.agents.timeline_agent import build_timeline

logs = parse_logs(
    "incident_data/logs/sample_logs.csv"
)

timeline = build_timeline(logs)

for event in timeline:
    print(event)