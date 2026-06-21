from backend.agents.roadmap import client


def generate_simulation(role):

    prompt = f"""
    You are a Team Lead in a software company.

    The employee has joined as a fresher {role}.

    Generate:

    1. Company Name
    2. Project Name
    3. Day 1 Assigned Task
    4. Requirements
    5. Deadline
    6. Mentor Hint
    7. Expected Deliverable

    Make it realistic and beginner friendly.
    """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text