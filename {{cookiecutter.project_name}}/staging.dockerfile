FROM python:3.8.3-buster

ENV PYTHONUNBUFFERED=1 DOCKER=1 DEBIAN_FRONTEND=noninteractive PYTHONWARNINGS=ignore::UserWarning:setuptools.distutils_patch:26

RUN mkdir /{{cookiecutter.project_name}}

COPY . /{{cookiecutter.project_name}}/

WORKDIR /{{cookiecutter.project_name}}/

RUN pip install --upgrade pip
RUN pip install poetry uvicorn
RUN poetry config virtualenvs.create false --local && poetry install --no-root
