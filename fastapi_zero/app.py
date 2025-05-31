from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.routers import auth, users
from fastapi_zero.schemas import (
    Message,
)

app = FastAPI(title='Bala')

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Sub-Mundo!'}


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
