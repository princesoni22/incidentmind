import pandas as pd

def parse_logs(file_path):

    logs = pd.read_csv(file_path)

    parsed_logs = []

    for _, row in logs.iterrows():

        parsed_logs.append({
            "timestamp": row["timestamp"],
            "service": row["service"],
            "level": row["level"],
            "message": row["message"]
        })

    return parsed_logs