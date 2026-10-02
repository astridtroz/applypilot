from fastapi import FastAPI
from schema import (
    JobIn,
    JobOut,
    UpdateJobIn,
    CreateJobApplicationIn,
    CreateJobApplicationOut,
)
from services import (
    JobService
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
async def put(data:UpdateJobIn)-> JobOut:
    return await JobService.put(data)

