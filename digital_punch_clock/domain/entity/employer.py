from datetime import time

from pydantic import BaseModel, Field


class EmployerEntity(BaseModel):
    registration: str = Field(pattern='\d{4}-.*')
    name: str
    position: str
    starts_work: time
    finishes_work: time