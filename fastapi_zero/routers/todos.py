from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.database import get_session
from fastapi_zero.models import Todo, User
from fastapi_zero.schemas import (
    FilterTodo,
    Message,
    TodoList,
    TodoPublic,
    TodoSchema,
    TodoUpdate,
)
from fastapi_zero.security import get_current_user

router = APIRouter(prefix='/todos', tags=['todos'])

T_CurrentUser = Annotated[User, Depends(get_current_user)]
T_Session = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', response_model=TodoPublic)
async def create_todo(
    todo: TodoSchema, user: T_CurrentUser, session: T_Session
):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        state=todo.state,
        user_id=user.id,
    )

    session.add(db_todo)
    await session.commit()
    await session.refresh(db_todo)

    return db_todo


@router.get('/', status_code=HTTPStatus.OK, response_model=TodoList)
async def list_todos(
    session: T_Session,
    user: T_CurrentUser,
    filter_todos: Annotated[FilterTodo, Query()],
):
    query = select(Todo).where(Todo.user_id == user.id)

    if filter_todos.title:
        query = query.filter(Todo.title.contains(filter_todos.title))

    if filter_todos.description:
        query = query.filter(
            Todo.description.contains(filter_todos.description)
        )

    if filter_todos.state:
        query = query.filter(Todo.state == filter_todos.state)

    todos = await session.scalars(
        query.offset(filter_todos.offset).limit(filter_todos.limit)
    )

    return {'todos': todos.all()}


@router.patch(
    '/{todo_id}', status_code=HTTPStatus.OK, response_model=TodoPublic
)
async def patch_todo(
    session: T_Session, user: T_CurrentUser, todo: TodoUpdate, todo_id: int
):
    db_todo = await session.scalar(
        select(Todo).where(Todo.user_id == user.id, Todo.id == todo_id)
    )

    if not db_todo:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Task not found.'
        )

    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)

    session.add(db_todo)
    await session.commit()
    await session.refresh(db_todo)

    return db_todo


@router.delete('/{todo_id}', response_model=Message)
async def delete_todo(session: T_Session, user: T_CurrentUser, todo_id: int):
    db_todo = await session.scalar(
        select(Todo).where(Todo.user_id == user.id, Todo.id == todo_id)
    )

    if not db_todo:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Task not found.'
        )

    await session.delete(db_todo)
    await session.commit()

    return {'message': 'Task has been deleted successfully.'}
