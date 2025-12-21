from http import HTTPStatus

import jwt
import pytest
from fastapi import HTTPException
from jwt import decode

from fastapi_zero.security import (
    create_access_token,
    get_current_user,
)


def test_jwt(settings):
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)

    assert decoded['test'] == data['test']
    assert 'exp' in decoded


def test_jwt_invalid_token(client):
    response = client.delete(
        'users/1', headers={'Authorization': 'Bearer invalid-token'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


@pytest.mark.asyncio
async def test_jwt_without_sub(session):
    token = create_access_token(data={'test': 'test'})
    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(session=session, token=token)

    assert excinfo.value.status_code == HTTPStatus.UNAUTHORIZED
    assert excinfo.value.detail == 'Could not validate credentials'


@pytest.mark.asyncio
async def test_jwt_user_not_found_in_db(session, settings):
    token = jwt.encode(
        {'sub': 'milk@shake.com'},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(session=session, token=token)

    assert excinfo.value.status_code == HTTPStatus.UNAUTHORIZED
    assert excinfo.value.detail == 'Could not validate credentials'
