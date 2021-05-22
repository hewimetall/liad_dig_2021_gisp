FROM python:3.9
RUN mkdir -p /fastapi
WORKDIR /fastapi
COPY  requerens.pip /fastapi/
RUN pip install -r requerens.pip
COPY . /fastapi
