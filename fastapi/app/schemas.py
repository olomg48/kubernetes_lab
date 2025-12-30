from sqlmodel import SQLModel
from typing import List, Optional

class TaskRead(SQLModel):
    id: int
    description: str

class TaskCreate(SQLModel):
    description: str

class TaskUpdate(SQLModel):
    description: str