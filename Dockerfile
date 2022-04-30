# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

COPY Pipfile Pipfile.lock bootstrapdeploy.sh ./

RUN pip install pipenv

RUN pipenv install fugashi[unidic-lite]

RUN pipenv install --system --deploy

COPY tokenizer ./tokenizer

ENTRYPOINT ["/app/bootstrapdeploy.sh"]