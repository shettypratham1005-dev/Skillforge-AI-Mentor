from fastapi import FastAPI
from pydantic import BaseModel

from backend.agents.roadmap import (
    generate_roadmap,
    ask_mentor,
    analyze_task,
    generate_workplace_message,
    generate_checklist
)

from backend.agents.simulation import generate_simulation

app = FastAPI(
    title="SkillForge AI Mentor API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "SkillForge AI Mentor Backend Running"
    }


class RoadmapRequest(BaseModel):
    role: str
    score: int


class MentorRequest(BaseModel):
    role: str
    question: str


class TaskRequest(BaseModel):
    role: str
    task: str


class CommunicationRequest(BaseModel):
    role: str
    message_type: str
    work_update: str


@app.post("/roadmap")
def roadmap(req: RoadmapRequest):

    result = generate_roadmap(
        req.role,
        req.score
    )

    return {"roadmap": result}


@app.post("/mentor")
def mentor(req: MentorRequest):

    result = ask_mentor(
        req.role,
        req.question
    )

    return {"answer": result}


@app.post("/simulation")
def simulation(req: MentorRequest):

    result = generate_simulation(
        req.role
    )

    return {"simulation": result}


@app.post("/analyze-task")
def task_analysis(req: TaskRequest):

    result = analyze_task(
        req.role,
        req.task
    )

    return {"analysis": result}


@app.post("/checklist")
def checklist(req: TaskRequest):

    result = generate_checklist(
        req.role,
        req.task
    )

    return {"checklist": result}


@app.post("/communication")
def communication(req: CommunicationRequest):

    result = generate_workplace_message(
        req.role,
        req.message_type,
        req.work_update
    )

    return {"message": result}