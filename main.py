from fastapi import FastAPI
from schema import (
    CreateJobIn,
    CreateJobOut,
    CreateJobApplicationIn,
    CreateJobApplicationOut,
)
from services import (
    JobService
)

app = FastAPI()

@app.post("/jobs" , status_code=201)
async def create( data: CreateJobIn)-> CreateJobOut:
    return await JobService.create(data=data)

@