from pydantic import (
    BaseModel,
    HttpUrl,
    Field
)

class CreateJobApplicationIn(BaseModel):
    job_link : HttpUrl = Field( max_length= 255)
    job_description:str 
    company_name: str = Field( min_length= 1, max_length= 255)
    job_role: str = Field(max_length= 255)

class CreateJobApplicationOut(CreateJobApplicationIn):
    id: int = Field(...)
    status:str = Field(max_length= 255)