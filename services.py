from fastapi import (
    FastAPI,
    HTTPException,
)
from models import (
    Job,
    JobApplication,
)
from schema import (
    JobIn,
    JobOut,
    CreateJobApplicationIn,
    CreateJobApplicationOut,
)
from sqlalchemy.orm import Session
from sqlalchemy import (
    select,
    delete,
)
from db import engine
class JobService:

    async def create(data: JobIn)-> JobOut:
        with Session(engine) as session:
                job = Job(
                    **data.model_dump(mode='json')
                )
                session.add(job)
                session.commit()
                session.refresh(job)
        
        return job

    async def get()-> list[JobOut]:
        with Session(engine) as session:
             jobs = session.scalars(select(Job)).all()

        return jobs

    async def get_by_id(id:int)->JobOut:
        with Session(engine) as session:
            job = session.scalar(select(Job).where(Job.id == id))

        if job is None:
            raise HTTPException(status_code=404, detail= f"No job found with id = {id}")
        return job

    async def put(id:int, data:JobIn)->JobOut:
        with Session(engine) as session:
            job = session.scalar(select(Job).where(Job.id == id))
            if job is None:
               raise HTTPException(status_code=404, detail=f"Job with id = {id} not found")
            job.job_role = data.job_role
            job.company_name = data.company_name
            job.apply_link = data.apply_link
            job.job_description = data.job_description
            session.commit()
            session.refresh(job)
        return job    

    async def delete(id:int)->str:
        with Session(engine) as session:
            job = session.scalar(select(Job).where(Job.id == id))
            if job is None:
                raise HTTPException(status_code=404, detail=f"Job with id = {id} not found")  
            session.delete(job)
            session.commit()
          
            return f"Deleted job with id {id}"          
        
        