from typing import Callable

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from db.events import init_app
from db.run_load_data import save_data
from ml.main import DataProcess

def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        app.mount("/static", StaticFiles(directory="static"), name="static")
        DataProcess()
        await init_app(app)
    return start_app