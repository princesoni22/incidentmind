import os
import json

from langchain_core.documents import Document

from app.rag.chroma_store import vectorstore

docs = []

folder = "incident_data/historical_incidents"

for file in os.listdir(folder):

    with open(f"{folder}/{file}", "r") as f:

        data = json.load(f)

        text = (
            f"Incident: {data['incident']}\n"
            f"Root Cause: {data['root_cause']}\n"
            f"Resolution: {data['resolution']}"
        )

        docs.append(
            Document(page_content=text)
        )

vectorstore.add_documents(docs)

vectorstore.persist()

print("Historical incidents ingested successfully.")