from app.services.llm_service import llm

def generate_hypothesis(timeline):

    formatted_timeline = "\n".join(timeline)

    prompt = f"""
    You are an expert Site Reliability Engineer.

    Analyze the following incident timeline.

    Identify:

    1. Most probable root cause
    2. Cascading failures
    3. Affected systems
    4. Confidence score (0-100)

    Timeline:
    {formatted_timeline}

    Return a detailed analysis.
    """

    response = llm.invoke(prompt)

    return response.content