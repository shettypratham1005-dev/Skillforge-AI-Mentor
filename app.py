from resume_analyzer import extract_resume_text, analyze_resume
from roadmap import (
    generate_roadmap,
    ask_mentor,
    analyze_task,
    generate_workplace_message,
    generate_checklist
)
from simulation import generate_simulation
import streamlit as st
score = 0
level = ""

if "latest_score" not in st.session_state:
    st.session_state.latest_score = 0

st.set_page_config(page_title="SkillForge AI", page_icon="🚀")

# =========================
# PAGE HEADER
# =========================

st.title("🚀 SkillForge AI Mentor")
st.subheader("AI Mentor for Freshers")

# =========================
# USER INFORMATION
# =========================

name = st.text_input("👤 Your Name")

role = st.selectbox(
    "💼 Select Role",
    [
        "Software Developer",
        "Data Scientist",
        "AI Engineer",
        "Machine Learning Engineer",
        "DevOps Engineer"
    ]
)

# =========================
# CUSTOM STYLING
# =========================

st.markdown("""
<style>
.main {
    padding-top: 2rem;
}

.stButton button {
    background-color: #00C853;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# RESUME ANALYZER
# =========================

st.markdown("---")
st.header("📄 Resume Analysis")

resume = st.file_uploader(
    "Upload Your Resume",
    type=["pdf"]
)

if resume is not None:

    resume_text = extract_resume_text(resume)

    st.write("DEBUG RESUME TEXT:")
    st.write(resume_text[:1000])

    if st.button("📄 Analyze Resume"):

        if not resume_text.strip():

            st.error(
                "❌ Could not extract text from resume."
            )

        else:

            with st.spinner(
                "Analyzing Resume..."
            ):

                analysis = analyze_resume(
                    resume_text,
                    role
                )

            st.subheader(
                "📋 Resume Analysis Report"
            )

            st.markdown(analysis)
            
# =========================
# PROGRESS TRACKER
# =========================

st.markdown("---")
st.header("📈 Learning Progress")

completed_days = st.slider(
    "Days Completed",
    0,
    30,
    0
)

st.progress(completed_days / 30)

st.write(
    f"✅ Progress: {completed_days}/30 Days Completed"
)

# =========================
# SKILL ASSESSMENT
# =========================

st.markdown("---")
st.header("📊 Skill Assessment")

python_skill = st.slider(
    "🐍 Python Skill Level",
    1,
    10,
    5
)

if python_skill > 5:
    st.success(f"🟢 Python Skill: {python_skill}/10")
else:
    st.error(f"🔴 Python Skill: {python_skill}/10")

git_skill = st.slider(
    "🔀 Git Skill Level",
    1,
    10,
    5
)

if git_skill > 5:
    st.success(f"🟢 Git Skill: {git_skill}/10")
else:
    st.error(f"🔴 Git Skill: {git_skill}/10")

sql_skill = st.slider(
    "🗄 SQL Skill Level",
    1,
    10,
    5
)

if sql_skill > 5:
    st.success(f"🟢 SQL Skill: {sql_skill}/10")
else:
    st.error(f"🔴 SQL Skill: {sql_skill}/10")

problem_solving = st.slider(
    "🧠 Problem Solving Skill",
    1,
    10,
    5
)

if problem_solving > 5:
    st.success(f"🟢 Problem Solving: {problem_solving}/10")
else:
    st.error(f"🔴 Problem Solving: {problem_solving}/10")

hours = st.selectbox(
    "⏰ Daily Time Available",
    [
        "1-2 Hours",
        "2-3 Hours",
        "3+ Hours"
    ]
)

# =========================
# READINESS SCORE
# =========================

if st.button("🎯 Generate Readiness Score"):

    if not name:
        st.warning("Please enter your name.")
        st.stop()

    score = (
        python_skill +
        git_skill +
        sql_skill +
        problem_solving
    ) / 40 * 100

    st.success(
        f"🎯 Industry Readiness Score: {score:.0f}/100"
    )

    st.session_state.latest_score = round(score)

    # Level Calculation
    if score < 30:
        level = "Absolute Beginner"
        st.error("🔴 Absolute Beginner")

    elif score < 50:
        level = "Beginner"
        st.warning("🟠 Beginner")

    elif score < 70:
        level = "Industry Starter"
        st.info("🟡 Industry Starter")

    elif score < 85:
        level = "Junior Ready"
        st.success("🟢 Junior Ready")

    else:
        level = "Strong Fresher"
        st.success("🏆 Strong Fresher")

    st.info(f"🏆 Level: {level}")

    with st.spinner("Generating AI Roadmap..."):

        roadmap = generate_roadmap(
            role,
            round(score)
        )

    st.markdown("---")
    st.subheader("📅 AI Generated Roadmap")

    st.write(roadmap)
   

    st.markdown("---")
    st.subheader("🏢 Industry Simulation")

    if st.button("🚀 Start Industry Simulation"):

     with st.spinner("Generating Industry Task..."):

        simulation = generate_simulation(role)

    st.write(simulation)

    st.markdown("---")
    st.subheader("👤 Profile Summary")

    st.write(f"**Name:** {name}")
    st.write(f"**Role:** {role}")
    st.write(f"**Daily Availability:** {hours}")

    st.subheader("📈 Skill Breakdown")

    st.write(f"🐍 Python: {python_skill}/10")
    st.write(f"🔀 Git: {git_skill}/10")
    st.write(f"🗄 SQL: {sql_skill}/10")
    st.write(f"🧠 Problem Solving: {problem_solving}/10")

# =========================
# PROFESSIONAL COMMUNICATION ASSISTANT
# =========================

st.markdown("---")

st.subheader("📢 Professional Communication Assistant")

message_type = st.selectbox(
    "Communication Type",
    [
        "Daily Standup",
        "Manager Update",
        "Email",
        "Slack Message",
        "Blocker Report"
    ]
)

work_update = st.text_area(
    "Describe your work update"
)

if st.button("📢 Generate Professional Update"):

    if work_update.strip() == "":
        st.warning("Please enter your work update.")

    else:

        with st.spinner(
            "Generating Professional Communication..."
        ):

            workplace_message = (
                generate_workplace_message(
                    role,
                    message_type,
                    work_update
                )
            )

        st.success(
            "✅ Professional Communication Generated"
        )

        st.markdown(workplace_message)

# =========================
# TASK CHECKLIST GENERATOR
# =========================

st.markdown("---")

st.subheader("✅ AI Task Checklist Generator")

task_input = st.text_area(
    "Enter manager assigned task for checklist generation"
)

if st.button("Generate Checklist"):

    if task_input.strip() == "":
        st.warning("Please enter a task.")

    else:

        with st.spinner(
            "Generating Checklist..."
        ):

            checklist = generate_checklist(
                role,
                task_input
            )

        st.success(
            "Checklist Generated Successfully"
        )

        st.markdown(checklist)

# =========================
# AI MENTOR CHAT
# =========================

st.markdown("---")
st.subheader("💬 Ask Your AI Mentor")

st.markdown("---")

st.subheader("🎯 Manager Task Simulator")

manager_task = st.text_area(
    "Enter task assigned by your manager"
)


if st.button("Analyze Task"):

    if manager_task.strip() == "":
        st.warning("Please enter a task.")
    else:

        with st.spinner("Analyzing task..."):

            result = analyze_task(
                role,
                manager_task
            )

        st.success("Task Analysis Complete")

        st.write(result)

user_question = st.text_input(
    "Ask any career, coding, learning, or industry question"
)

if st.button("🤖 Ask Mentor"):

    if user_question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            answer = ask_mentor(
                role,
                user_question
            )

        st.success("✅ Answer Generated")

        st.markdown(answer)