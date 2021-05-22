from typing import Callable

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from db.events import init_app


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        app.mount("/static", StaticFiles(directory="static"), name="static")
        init_app(app)

    return start_app