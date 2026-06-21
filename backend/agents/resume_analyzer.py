from pypdf import PdfReader
from backend.agents.roadmap import client


def extract_resume_text(uploaded_file):
    """
    Extract text from uploaded PDF resume.
    """

    try:
        pdf = PdfReader(uploaded_file)

        text = ""

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:
        return f"Error reading PDF: {str(e)}"


def analyze_resume(resume_text, role):
    """
    Analyze resume using Gemini AI.
    """

    prompt = f"""
    You are an expert technical recruiter and career mentor.

    Analyze the following resume for the role:

    {role}

    Resume Content:
    {resume_text}

    Provide:

    1. Resume Score out of 100
    2. Strengths
    3. Weaknesses
    4. Missing Skills
    5. Recommended Learning Plan
    6. Industry Readiness Level
    """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text