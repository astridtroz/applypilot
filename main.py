from fastapi import FastAPI
from schema import (
    JobIn,
    JobOut,
    ApplicationOut,
    ApplicationIn,
)
from services import (
    JobService,
    ApplicationService,
)

app = FastAPI()

@app.post("/jobs" , status_code=201)
async def create( data: JobIn)-> JobOut:
    return await JobService.create(data=data)

@app.get("/jobs")
async def get()-> list[JobOut]:
    return await JobService.get()

@app.get("/jobs/{id}")
async def get_by_id(id:int)->JobOut:
    return await JobService.get_by_id(id=id)

@app.put("/jobs/{id}")
async def put(id:int, data:JobIn)-> JobOut:
    return await JobService.put(id, data)

@app.delete("/jobs/{id}")
async def delete(id:int)->str:
    return await JobService.delete(id)

@app.post("/jobs/{id}/application")
async def create(job_id:int)->ApplicationOut:
    return await ApplicationService.create(job_id)

@app.get("/applications")
async def get_applications() -> list[ApplicationOut]:
    return await ApplicationService.get()

@app.get("/applications/{id}")
async def get_application_by_id(id: int) -> ApplicationOut:
    return await ApplicationService.get_by_id(id=id)

@app.get("/jobs/{job_id}/application")
async def get_application_by_job_id(job_id: int) -> ApplicationOut:
    return await ApplicationService.get_by_job_id(job_id=job_id)

@app.put("/applications/{id}")
async def update_application(id: int, data: ApplicationIn) -> ApplicationOut:
    return await ApplicationService.put(id, data)

@app.delete("/applications/{id}")
async def delete_application(id: int) -> str:
    return await ApplicationService.delete(id)