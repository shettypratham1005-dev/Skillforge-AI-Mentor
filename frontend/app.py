import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
from backend.database.database import engine
from backend.database.models import Base

Base.metadata.create_all(bind=engine)

import streamlit as st

import streamlit as st

from backend.auth.auth import (
    register_user,
    login_user
)

from backend.utils.pdf_generator import generate_pdf

from backend.agents.resume_analyzer import (
    extract_resume_text,
    analyze_resume
)
import sys

print("PYTHON PATH USED:")
print(sys.executable)

from backend.auth.security import hash_password
from backend.database.database import SessionLocal
from backend.database.models import UserHistory
from backend.database.crud import save_history
from backend.database.models import User

from backend.agents.roadmap import (
    generate_roadmap,
    ask_mentor,
    analyze_task,
    generate_workplace_message,
    generate_checklist
)

from backend.agents.simulation import (
    generate_simulation
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="SkillForge AI Mentor",
    page_icon="🚀",
    layout="wide"
)

# =========================
# SESSION STATE
# =========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# =========================
# LOGIN / REGISTER
# =========================

if not st.session_state.logged_in:

    st.title("🔐 SkillForge AI Login")

    menu = st.radio(
        "Choose Option",
        [
            "Login",
            "Register"
        ]
    )


    # =====================
    # REGISTER
    # =====================

    if menu == "Register":

        reg_name = st.text_input("Name")

        reg_email = st.text_input("Email")

        reg_password = st.text_input(
            "Password",
            type="password"
        )


        if st.button("Register"):

            db = SessionLocal()

            hashed_password = hash_password(
                reg_password
            )


            new_user = User(
                name=reg_name,
                email=reg_email,
                password=hashed_password
            )


            db.add(new_user)

            db.commit()

            db.close()


            st.success(
                "Registration Successful"
            )


    # =====================
    # LOGIN
    # =====================

    elif menu == "Login":

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )


        if st.button("Login"):

            user = login_user(
                email,
                password
            )


            if user:

                st.session_state.logged_in = True

                st.session_state.user_name = user.name

                st.session_state.user_id = user.id

                st.success(
                    "Login Successful"
                )

                st.rerun()


            else:

                st.error(
                    "Invalid Credentials"
                )
# =========================
# MAIN APP
# =========================

else:

    st.sidebar.success(
        f"Welcome {st.session_state.user_name}"
    )

    page = st.sidebar.selectbox(
        "Navigation",
        [
            "Dashboard",
            "History"
        ]
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user_name = ""

        st.rerun()

    # =====================
    # DASHBOARD
    # =====================

    if page == "Dashboard":

        st.title("🚀 SkillForge AI Mentor")

        name = st.text_input(
            "Enter Your Name",
            value=st.session_state.user_name
        )

        role = st.selectbox(
            "Select Role",
            [
                "Software Developer",
                "Data Scientist",
                "AI Engineer",
                "Machine Learning Engineer",
                "DevOps Engineer"
            ]
        )

        # =====================
        # RESUME ANALYZER
        # =====================

        st.markdown("---")
        st.header("📄 Resume Analyzer")

        resume = st.file_uploader(
            "Upload Resume (PDF)",
            type=["pdf"]
        )

        if resume is not None:

            if st.button(
                "Analyze Resume"
            ):

                with st.spinner(
                    "Reading Resume..."
                ):

                    resume_text = (
                        extract_resume_text(
                            resume
                        )
                    )

                st.subheader(
                    "Extracted Resume Text"
                )

                st.write(
                    resume_text[:1000]
                )

                with st.spinner(
                    "Analyzing Resume..."
                ):

                    report = analyze_resume(
                        resume_text,
                        role
                    )

                save_history(
                    name=name,
                    role=role,
                    feature="Resume Analysis",
                    input_text="Resume Uploaded",
                    output_text=report
                )

                st.success(
                    "Resume Analysis Complete"
                )

                st.markdown(report)

                pdf_file = generate_pdf(
                    report,
                    "resume_report.pdf"
                )

                with open(
                    pdf_file,
                    "rb"
                ) as file:

                    st.download_button(
                        "📄 Download Report",
                        file,
                        "resume_report.pdf",
                        "application/pdf"
                    )

        # =====================
        # ROADMAP
        # =====================

        st.markdown("---")
        st.header("📊 Readiness Score")

        score = st.slider(
            "Select Score",
            0,
            100,
            50
        )

        if st.button(
            "Generate Roadmap"
        ):

            resume_text = ""

            if resume is not None:

                resume_text = (
                    extract_resume_text(
                        resume
                    )
                )

            roadmap = generate_roadmap(
                role,
                score,
                resume_text
            )

            save_history(
                name=name,
                role=role,
                feature="Roadmap",
                input_text=f"Score: {score}",
                output_text=roadmap
            )

            st.markdown(roadmap)

            roadmap_pdf = generate_pdf(
                roadmap,
                "roadmap.pdf"
            )

            with open(
                roadmap_pdf,
                "rb"
            ) as file:

                st.download_button(
                    "📥 Download Roadmap",
                    file,
                    "roadmap.pdf",
                    "application/pdf"
                )

        # =====================
        # SIMULATION
        # =====================

        st.markdown("---")
        st.header("🏢 Industry Simulation")

        if st.button(
            "Generate Simulation"
        ):

            simulation = (
                generate_simulation(
                    role
                )
            )

            save_history(
                name=name,
                role=role,
                feature="Simulation",
                input_text=role,
                output_text=simulation
            )

            st.markdown(
                simulation
            )

        # =====================
        # MENTOR CHAT
        # =====================

        st.markdown("---")
        st.header("💬 Ask Mentor")

        question = st.text_input(
            "Ask a Question"
        )

        if st.button(
            "Ask Mentor"
        ):

            answer = ask_mentor(
                role,
                question
            )

            save_history(
                name=name,
                role=role,
                feature="Mentor Chat",
                input_text=question,
                output_text=answer
            )

            st.markdown(answer)

        # =====================
        # TASK ANALYZER
        # =====================

        st.markdown("---")
        st.header("🎯 Task Analyzer")

        task = st.text_area(
            "Manager Assigned Task"
        )

        if st.button(
            "Analyze Task"
        ):

            result = analyze_task(
                role,
                task
            )

            save_history(
                name=name,
                role=role,
                feature="Task Analysis",
                input_text=task,
                output_text=result
            )

            st.markdown(result)

        # =====================
        # COMMUNICATION
        # =====================

        st.markdown("---")
        st.header(
            "📢 Professional Communication"
        )

        message_type = st.selectbox(
            "Communication Type",
            [
                "Email",
                "Manager Update",
                "Daily Standup",
                "Slack Message"
            ]
        )

        work_update = st.text_area(
            "Work Update"
        )

        if st.button(
            "Generate Communication"
        ):

            result = (
                generate_workplace_message(
                    role,
                    message_type,
                    work_update
                )
            )

            save_history(
                name=name,
                role=role,
                feature="Communication",
                input_text=work_update,
                output_text=result
            )

            st.markdown(result)

        # =====================
        # CHECKLIST
        # =====================

        st.markdown("---")
        st.header(
            "✅ Checklist Generator"
        )

        task_input = st.text_area(
            "Task For Checklist"
        )

        if st.button(
            "Generate Checklist"
        ):

            checklist = (
                generate_checklist(
                    role,
                    task_input
                )
            )

            save_history(
                name=name,
                role=role,
                feature="Checklist",
                input_text=task_input,
                output_text=checklist
            )

            st.markdown(checklist)

    # =====================
    # HISTORY PAGE
    # =====================

    elif page == "History":

        st.title("📚 User History")

        db = SessionLocal()

        records = db.query(
            UserHistory
        ).order_by(
            UserHistory.id.desc()
        ).all()

        if not records:

            st.warning(
                "No history found."
            )

        else:

            for record in records:

                st.subheader(
                    record.feature
                )

                st.write(
                    f"Name: {record.name}"
                )

                st.write(
                    f"Role: {record.role}"
                )

                st.write(
                    "Input:"
                )

                st.write(
                    record.input_text
                )

                st.write(
                    "Output:"
                )

                st.write(
                    record.output_text
                )

                st.markdown("---")

        db.close()