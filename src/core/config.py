from fastapi.templating import Jinja2Templates

ALLOWED_HOSTS = "*"
DEBUG = True
PROJECT_NAME = "fine"
VERSION = '0.1'

# datebase
POSTGRESQL_USERNAME = 'pguser'
POSTGRESQL_PASSWORD = 'pguser'
POSTGRESQL_HOSTNAME = 'dbpostgres'
POSTGRESQL_DATABASE = 'pgdb_fastapi'

templates = Jinja2Templates(directory="templates")
