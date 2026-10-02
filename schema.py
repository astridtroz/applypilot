from pydantic import (
    BaseModel,
    HttpUrl,
    Field
)
class JobIn(BaseModel):
    job_role: str
    company_name: str
    apply_link: str
    job_description: str   

class JobOut(BaseModel):
    id: int
    job_role: str
    company_name: str
    apply_link: str
    job_description: str

class CreateJobApplicationIn(BaseModel):
    job_link : HttpUrl = Field( max_length= 255)
    job_description:str 
    company_name: str = Field( min_length= 1, max_length= 255)
    job_role: str = Field(max_length= 255)

class CreateJobApplicationOut(CreateJobApplicationIn):
    id: int = Field(...)
    status:str = Field(max_length= 255)