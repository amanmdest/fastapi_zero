from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_read_root_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Sub-Mundo!'}
