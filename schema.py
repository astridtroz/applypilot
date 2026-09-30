from pydantic import (
    BaseModel,
    HttpUrl
)

class CreateJobApplicationIn(BaseModel):
    job_link : HttpUrl
    job_description:str
    company_name: str
    job_role: str

class CreateJobApplicationOut(CreateJobApplicationIn):
    id: int
    status:str