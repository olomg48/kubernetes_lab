from sqlmodel import SQLModel
from typing import List, Optional

class TaskRead(SQLModel):
    id: int
    description: str
    category: str

class TaskCreate(SQLModel):
    description: str
    category: str

class TaskUpdate(SQLModel):
    description: str
    category: str