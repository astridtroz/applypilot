from fastapi import FastAPI
from schema import (
    JobIn,
    JobOut,
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
async def put(id:int, data:JobIn)-> JobOut:
    return await JobService.put(id, data)

@app.delete("/jobs/{id}")
async def delete(id:int)->str:
    return await JobService.delete(id)