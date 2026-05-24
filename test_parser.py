from app.agents.log_parser import parse_logs

logs = parse_logs(
    "incident_data/logs/sample_logs.csv"
)

print(logs)