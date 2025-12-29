from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.routers import auth, todos, users
from fastapi_zero.schemas import (
    Message,
)

app = FastAPI(title='FastAPI Zero')

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/home/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_root_html():
    return """<html>
                <head>
                    <title> Nosso olá mundo </title>
                </head>
                <body>
                    <h1> Olá Mundo! </h1>
                </body>
            </html>"""
