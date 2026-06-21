from sqlalchemy import Column, Integer, String, Text
from backend.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Assessment(Base):

    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    skill = Column(String)

    score = Column(Integer)


class Roadmap(Base):

    __tablename__ = "roadmaps"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    day = Column(Integer)

    task = Column(Text)


class Progress(Base):

    __tablename__ = "progress"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    task = Column(Text)

    status = Column(String)

class UserHistory(Base):
    __tablename__ = "user_history"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    feature = Column(String)
    input_text = Column(String)
    output_text = Column(String)