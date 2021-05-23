from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


from core.config import ALLOWED_HOSTS, DEBUG, PROJECT_NAME, VERSION
from core.events import create_start_app_handler
from api.list_view import router


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    #
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    #
    application.add_event_handler("startup", create_start_app_handler(application))
    application.include_router(router, )

    return application


app = get_application()
