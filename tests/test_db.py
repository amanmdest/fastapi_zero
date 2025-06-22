from dataclasses import asdict

import pytest
from sqlalchemy import select

from fastapi_zero.models import Todo, User


@pytest.mark.asyncio
async def test_create_user_without_todos(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='test', email='test@test.com', password='secret'
        )

        session.add(new_user)
        await session.commit()

        user = await session.scalar(
            select(User).where(User.username == new_user.username)
        )

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'email': 'test@test.com',
        'password': 'secret',
        'created_at': time,
        'updated_at': time,
        'todos': [],
    }


@pytest.mark.asyncio
async def test_create_todo(session, mock_db_time, user):
    with mock_db_time(model=Todo) as time:
        new_todo = Todo(
            title='Test Todo',
            description='Test Desc',
            state='draft',
            user_id=user.id,
        )

        session.add(new_todo)
        await session.commit()

        todo = await session.scalar(select(Todo))

    assert asdict(todo) == {
        'id': 1,
        'description': 'Test Desc',
        'title': 'Test Todo',
        'state': 'draft',
        'user_id': 1,
        'created_at': time,
        'updated_at': time,
    }


@pytest.mark.asyncio
async def test_user_todo_realationship(session, user, todo):
    await session.refresh(user)
    user = await session.scalar(select(User).where(User.id == user.id))

    assert user.todos == [todo]
