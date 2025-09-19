FROM python:3.13-slim

RUN useradd -Ms /sbin/nologin -u 1000 app

COPY ./packages /src
WORKDIR /src
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install -e $(ls | xargs realpath)

ENV UVICORN_HOST=0.0.0.0
ENTRYPOINT ["uvicorn", "oasync:app"]