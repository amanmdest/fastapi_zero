from http import HTTPStatus


def test_read_root_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Sub-Mundo!'}


def test_read_root_hello_world_html(client):
    response = client.get('/home')

    assert (
        response.text
        == """<html>
                <head>
                    <title> Nosso olá mundo </title>
                </head>
                <body>
                    <h1> Olá Mundo! </h1>
                </body>
            </html>"""
    )
