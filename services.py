from fastapi import FastAPI
from models import JobApplication
from schema import (
    CreateJobApplicationIn,
    CreateJobApplicationOut,
)
from sqlalchemy.orm import Session
from db import engine

