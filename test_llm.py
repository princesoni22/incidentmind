from app.services.llm_service import llm

response = llm.invoke(
    "Explain root cause analysis in one sentence."
)

print(response.content)
