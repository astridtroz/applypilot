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

class ApplicationIn(BaseModel):
    status: str = Field(max_length=255, min_length=1)
    
class ApplicationOut(BaseModel):
    id: int = Field(...)
    job_id: int = Field(...)
    status:str = Field(max_length= 255)