import os
from dotenv import load_dotenv
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# =========================
# AI MENTOR CHAT
# =========================

def ask_mentor(role, question):

    prompt = f"""
    You are a Senior {role} Mentor.

    Act like a real industry mentor.

    Rules:
    - Explain in beginner-friendly language
    - Give practical examples
    - Explain industry best practices
    - Suggest next learning steps
    - If coding related, provide code examples
    - If career related, provide roadmap guidance

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text


# =========================
# MANAGER TASK ANALYSIS
# =========================

def analyze_task(role, task):

    prompt = f"""
    You are a Senior {role} Mentor.

    Analyze the following manager-assigned task.

    Task:
    {task}

    Provide:
    1. Task Understanding
    2. Required Skills
    3. Step-by-Step Approach
    4. Common Mistakes
    5. Expected Deliverables
    """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text

# =========================
# PROFESSIONAL COMMUNICATION
# =========================

def generate_workplace_message(
    role,
    message_type,
    work_update
):

    prompt = f"""
    You are a Senior {role} Team Lead.

    Convert the following update into a professional workplace communication.

    Communication Type:
    {message_type}

    Work Update:
    {work_update}

    Make it professional,
    concise,
    industry-ready,
    and beginner-friendly.
    """

    response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
    )
    return response.text


# =========================
# TASK CHECKLIST GENERATOR
# =========================

def generate_checklist(role, task):

    prompt = f"""
    You are a Senior {role} Team Lead.

    The fresher has received this task:

    {task}

    Generate:

    1. Task Breakdown
    2. Step-by-step Checklist
    3. Deliverables
    4. Testing Requirements

    Format everything as checkboxes.

    Example:

    ☐ Understand Requirements
    ☐ Create Database Schema
    ☐ Implement API
    """

    response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

    return response.text


# =========================
# ROADMAP GENERATOR
# =========================

def generate_roadmap(role, score, resume_text=""):

    if role == "Software Developer":

        prompt = f"""
        You are a Senior Software Engineering Mentor.

        Create a personalized Day-wise 30-Day Roadmap.

        Readiness Score: {score}

        Resume Information:
        {resume_text}

        Topics:
        - Python
        - Git
        - SQL
        - APIs
        - Debugging
        - Testing
        - Projects
        - Industry Workflow

        Create Day 1 to Day 30.
        """

    elif role == "Data Scientist":

        prompt = f"""
        You are a Senior Data Science Mentor.

        Create a personalized Day-wise 30-Day Roadmap.

        Readiness Score: {score}

        Resume Information:
        {resume_text}

        Topics:
        - Python
        - Pandas
        - NumPy
        - Data Cleaning
        - EDA
        - Data Visualization
        - Statistics
        - Machine Learning Basics
        - End-to-End Project

        Create Day 1 to Day 30.
        """

    elif role == "AI Engineer":

        prompt = f"""
        You are a Senior AI Engineer Mentor.

        Create a personalized Day-wise 30-Day Roadmap.

        Readiness Score: {score}

        Resume Information:
        {resume_text}

        Topics:
        - Prompt Engineering
        - LLMs
        - RAG
        - Vector Databases
        - AI Agents
        - Gemini APIs
        - AI Projects

        Create Day 1 to Day 30.
        """

    elif role == "Machine Learning Engineer":

        prompt = f"""
        You are a Senior Machine Learning Engineer Mentor.

        Create a personalized Day-wise 30-Day Roadmap.

        Readiness Score: {score}

        Resume Information:
        {resume_text}

        Topics:
        - Python for ML
        - NumPy
        - Pandas
        - Statistics
        - Data Preprocessing
        - Feature Engineering
        - Machine Learning Algorithms
        - Scikit-Learn
        - Model Evaluation
        - Model Deployment

        Create Day 1 to Day 30.
        """

    elif role == "DevOps Engineer":

        prompt = f"""
        You are a Senior DevOps Engineer Mentor.

        Create a personalized Day-wise 30-Day Roadmap.

        Readiness Score: {score}

        Resume Information:
        {resume_text}

        Topics:
        - Linux
        - Shell Scripting
        - Git
        - Docker
        - Kubernetes
        - Jenkins
        - AWS
        - Monitoring

        Create Day 1 to Day 30.
        """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text