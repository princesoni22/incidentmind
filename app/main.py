from fastapi import FastAPI, UploadFile
import pandas as pd

from app.graph.workflow import graph

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "IncidentMind Running"
    }

@app.post("/analyze")
async def analyze(
    file: UploadFile
):

    temp_file = f"temp_{file.filename}"

    with open(temp_file, "wb") as f:
        f.write(await file.read())

    logs = pd.read_csv(temp_file)

    parsed_logs = logs.to_dict(
        orient="records"
    )

    result = graph.invoke({
        "parsed_logs": parsed_logs
    })

    return {
        "timeline": result["timeline"],
        "hypothesis": result["hypothesis"],
        "incidents": result["incidents"],
        "rca": result["rca"]
    }