from fastapi import Depends, APIRouter, Response, HTTPException
from sqlmodel import Session, select
from typing import List
from ..db import get_session
from ..models import Tasks
from ..schemas import TaskRead, TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get(path="/list", response_model=List[TaskRead])
def get_tasks(*, session: Session = Depends(get_session)):
    tasks = session.exec(select(Tasks)).all()
    return tasks


@router.get(path="/get/{task_id}", response_model=TaskRead)
def get_single_task(*, session: Session = Depends(get_session), task_id: int):
    task = session.get(Tasks, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post(path="/create", response_model=TaskCreate)
def create_task(*, session: Session = Depends(get_session), task: TaskCreate):
    db_task = Tasks.model_validate(task, from_attributes=True)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.patch("/update/{task_id}", response_model=TaskRead)
def update_task(*, session: Session = Depends(get_session), task_id: int, task: TaskUpdate):
    db_task = session.get(Tasks, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task_data = task.model_dump(exclude_unset=True)
    db_task.sqlmodel_update(task_data)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.delete(path="/delete/{task_id}")
def remove_task(*, session: Session = Depends(get_session), task_id: int):
    task = session.get(Tasks, task_id)
    session.delete(task)
    session.commit()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}