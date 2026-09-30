from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
    )
from sqlalchemy import String
from db import engine

class Base(DeclarativeBase):
    pass

class JobApplication(Base):
    __tablename__ = "job_application"

    
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String)
    job_link: Mapped[str] = mapped_column(String)
    job_description: Mapped[str] = mapped_column(String)
    company_name: Mapped[str] = mapped_column(String)
    job_role: Mapped[str] = mapped_column(String)

Base.metadata.create_all(engine)