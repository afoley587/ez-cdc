FROM python:3.9.18-slim

ENV POETRY_VER=1.7.1

RUN mkdir /app

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry==$POETRY_VER && \
    poetry export -f requirements.txt -o requirements.txt --without-hashes && \
    pip install -r requirements.txt && \
    rm -rf requirements.txt

COPY cdc_test/* /app/

CMD ["python", "main.py"]