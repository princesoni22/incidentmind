from datetime import datetime

def build_timeline(parsed_logs):

    sorted_logs = sorted(
        parsed_logs,
        key=lambda x: datetime.strptime(
            x["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )
    )

    timeline = []

    for log in sorted_logs:

        event = (
            f"[{log['timestamp']}] "
            f"{log['service']} "
            f"({log['level']}): "
            f"{log['message']}"
        )

        timeline.append(event)

    return timeline