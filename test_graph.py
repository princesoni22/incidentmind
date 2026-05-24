from app.agents.log_parser import parse_logs
from app.graph.workflow import graph

logs = parse_logs(
    "incident_data/logs/sample_logs.csv"
)

result = graph.invoke({
    "parsed_logs": logs
})

print(result["rca"])
