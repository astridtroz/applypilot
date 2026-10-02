from fastapi import FastAPI
from models import (
    Job,
    JobApplication,
)
from schema import (
    CreateJobIn,
    CreateJobOut,
    CreateJobApplicationIn,
    CreateJobApplicationOut,
)
from sqlalchemy.orm import Session
from db import engine

class JobService:

    async def create(data: CreateJobIn)-> CreateJobOut:
        with Session(engine) as session:
                job = Job(
                    **data.model_dump(mode='json')
                )
                session.add(job)
                session.commit()
                session.refresh(job)
        
        return job