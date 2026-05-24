from app.agents.rag_agent import retrieve_similar_incidents

query = """
MongoDB timeout caused payment processing failures
and API outage
"""

results = retrieve_similar_incidents(query)

for result in results:
    print("\n")
    print(result)
