from http import HTTPStatus

from fastapi_zero.models import User
from fastapi_zero.schemas import UserPublic


def test_create_user(client, mock_db_time):
    with mock_db_time(model=User) as time:
        response = client.post(
            '/users/',
            json={
                'username': 'alice',
                'email': 'alice@example.com',
                'password': 'secret',
            },
        )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
        'created_at': time.isoformat(),
        'updated_at': time.isoformat(),
    }


def test_create_user_username_already_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': user.username,
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {
        'detail': 'Username already exists',
    }


def test_create_user_email_already_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': user.email,
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {
        'detail': 'Email already exists',
    }


def test_list_users(client, user, token, mock_db_time):
    with mock_db_time(model=User):
        user_schema = UserPublic.model_validate(user).model_dump()
        user_schema['created_at'] = user_schema['created_at'].isoformat()
        user_schema['updated_at'] = user_schema['updated_at'].isoformat()

        response = client.get(
            '/users/', headers={'Authorization': f'Bearer {token}'}
        )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_read_user_with_id(client, user, mock_db_time):
    with mock_db_time(model=User):
        response = client.get(f'/users/{user.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'created_at': (user.created_at).isoformat(),
        'updated_at': (user.updated_at).isoformat(),
    }


def test_read_user_with_id_returns_not_found(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found!',
    }


def test_update_user(client, user, token, mock_db_time):
    with mock_db_time(model=User):
        response = client.put(
            f'/users/{user.id}',
            json={
                'username': user.username,
                'email': 'bob@example.com',
                'password': user.password,
            },
            headers={'Authorization': f'Bearer {token}'},
        )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': user.id,
        'username': user.username,
        'email': 'bob@example.com',
        'created_at': (user.created_at).isoformat(),
        'updated_at': (user.updated_at).isoformat(),
    }


def test_update_returns_not_enough_permissions(client, other_user, token):
    response = client.put(
        f'/users/{other_user.id}',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}


def test_update_integrity_error(client, user, other_user, token):
    response = client.put(
        f'/users/{user.id}',
        json={
            'username': 'fausto',
            'email': other_user.email,
            'password': 'mynewpassword',
        },
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username or Email already exists'}


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


def test_delete_returns_not_enough_permissions(client, other_user, token):
    response = client.delete(
        f'/users/{other_user.id}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}
