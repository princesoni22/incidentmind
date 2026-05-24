from app.services.llm_service import llm


def generate_rca(
    timeline,
    hypothesis,
    incidents
):

    formatted_timeline = "\n".join(timeline)
    formatted_incidents = "\n\n".join(incidents)

    prompt = f"""
    You are an expert Site Reliability Engineer.

    Create a professional Root Cause Analysis report.

    Timeline:
    {formatted_timeline}

    AI Hypothesis:
    {hypothesis}

    Similar Historical Incidents:
    {formatted_incidents}

    Generate:

    1. Incident Summary
    2. Root Cause
    3. Cascading Failures
    4. Impact
    5. Resolution Recommendations
    6. Prevention Strategy
    """

    response = llm.invoke(prompt)

    return response.content
