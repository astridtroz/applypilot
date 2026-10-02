from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    )
from sqlalchemy import (
    String,
    ForeignKey
)
from db import engine

class Base(DeclarativeBase):
    pass

class Job(Base):
    __tablename__ = "job"
    id: Mapped[int] = mapped_column(primary_key=True)
    job_role: Mapped[str] = mapped_column(String)
    company_name: Mapped[str] = mapped_column(String)
    job_description: Mapped[str] = mapped_column(String)
    apply_link: Mapped[str] = mapped_column(String)
    
class JobApplication(Base):
    __tablename__ = "job_application"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    job_id : Mapped[int] = mapped_column(ForeignKey("job.id"))
    status: Mapped[str] = mapped_column(String)
    

Base.metadata.create_all(engine)