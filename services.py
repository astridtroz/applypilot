from fastapi import (
    HTTPException,
)
from models import (
    Job,
    Application,
)
from schema import (
    JobIn,
    JobOut,
    ApplicationOut,
    ApplicationIn,
)
from sqlalchemy.orm import Session
from sqlalchemy import (
    select,
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
        
class ApplicationService:

    async def create(job_id:int)->ApplicationOut:
        with Session(engine) as session:
            job = session.scalar(select(Job).where(Job.id == job_id))
            
            if job is None:
                raise HTTPException(status_code=404, detail= f"No job found with id = {job_id}")

            application = session.scalar(select(Application).where((Application.job_id == job_id)))
            if application is not None:
                raise HTTPException(status_code=409, detail="already applied")
            
            application = Application(job_id = job_id, status = "applied")
            session.add(application)
            session.commit()
            session.refresh(application)
        return application
    
    async def get()-> list[ApplicationOut]:
        with Session(engine) as session:
            applications = session.scalars(select(Application)).all()

        return applications

    async def get_by_id(id:int)->ApplicationOut:
        with Session(engine) as session:
            application = session.scalar(select(Application).where(Application.id == id))

        if application is None:
            raise HTTPException(status_code=404, detail= f"No Application found with id = {id}")
        return application

    async def get_by_job_id(job_id:int)->ApplicationOut:
        with Session(engine) as session:
            application = session.scalar(select(Application).where(Application.job_id == job_id))

        if application is None:
            raise HTTPException(status_code=404, detail= f"No Application found with job id = {job_id}")
        return application

    async def put(id:int, data:ApplicationIn)->ApplicationOut:
        with Session(engine) as session:
            application = session.scalar(select(Application).where(Application.id == id))
            if application is None:
               raise HTTPException(status_code=404, detail=f"Application with id = {id} not found")
            application.status = data.status
            session.commit()
            session.refresh(application)
        return application    

    async def delete(id:int)->str:
        with Session(engine) as session:
            application = session.scalar(select(Application).where(Application.id == id))
            if application is None:
                raise HTTPException(status_code=404, detail=f"application with id = {id} not found")  
            session.delete(application)
            session.commit()
          
            return f"Deleted application with id {id}"          
 