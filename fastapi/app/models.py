from sqlmodel import SQLModel, Field
from enum import Enum


class Tasks(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    description: str
    category: str
