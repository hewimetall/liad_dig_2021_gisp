from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from core import config as settings


async def init_app(app: FastAPI) -> bool:
    register_tortoise(
        app,
        db_url=get_db_uri(
            user=settings.POSTGRESQL_USERNAME,
            passwd=settings.POSTGRESQL_PASSWORD,
            host=settings.POSTGRESQL_HOSTNAME,
            db=settings.POSTGRESQL_DATABASE
        ),
        modules={"models": ["db.model"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    return True


def get_db_uri(user, passwd, host, db):
    return f"postgres://{user}:{passwd}@{host}:5432/{db}"
