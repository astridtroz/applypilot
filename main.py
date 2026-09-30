from fastapi import FastAPI
from models import JobApplication
from schema import (
    CreateJobApplicationIn,
    CreateJobApplicationOut,
)
from sqlalchemy.orm import Session
from db import engine

app = FastAPI()

@app.post("/jobs")
def create( data: CreateJobApplicationIn)-> CreateJobApplicationOut:
    with Session(engine) as session:
        application = JobApplication(
            status = "pending",
            **data.model_dump(mode='json')
        )
        session.add(application)
        session.commit()
        session.refresh(application)

    return application
    