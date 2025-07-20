from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from sqlalchemy import asc
from api.route.scheme import Task, TasksList, UpdateTask

from api.db.session import get_session

router = APIRouter()


@router.get("/", response_model=TasksList)
def get_tasks(
    session: Session = Depends(get_session)
):
    query = select(Task).order_by(asc("completed")).limit(30)
    result = session.exec(query).all()

    return TasksList(
        tasks=list(result),
        count=len(result)
    )


@router.post("/", response_model=Task)
def create_task(
    payload: Task,
    session: Session = Depends(get_session)
):
    data = payload.model_dump()
    obj = Task.model_validate(data)
    print(obj)

    session.add(obj)
    session.commit()
    session.refresh(obj)

    return obj


@router.put("/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    payload: UpdateTask,
    session: Session = Depends(get_session)
):
    query = select(Task).where(Task.id == task_id)
    obj = session.exec(query).first()

    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Can't find task with provided id")

    data = payload.model_dump()
    for k, v in data.items():
        setattr(obj, k, v)

    session.commit()
    session.refresh(obj)

    return obj


@router.delete("/{task_id}", response_model=Task)
def delete_task(
    task_id: int,
    session: Session = Depends(get_session)
):
    query = select(Task).where(Task.id == task_id)
    obj = session.exec(query).first()

    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There are no task with this id"
        )

    session.delete(obj)
    session.commit()

    return obj
