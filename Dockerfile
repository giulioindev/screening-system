FROM python:3.13-slim-bullseye AS base
RUN pip install poetry==2.0.1
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

FROM base AS builder    
WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --only main && rm -rf "$POETRY_CACHE_DIR"

FROM builder AS dev
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"
RUN poetry self add poetry-plugin-shell
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
RUN apt-get update && apt-get install -y curl gettext wget
WORKDIR /app
COPY . .
RUN poetry install --only dev && rm -rf "$POETRY_CACHE_DIR"
EXPOSE 8000
ENTRYPOINT ["./scripts/start.sh "]

FROM python:3.13-slim-bullseye AS prod
ENV VIRTUAL_ENV=/app/.venv \
PATH="/app/.venv/bin:$PATH" \
PYTHONUNBUFFERED=1 \
PYTHONDONTWRITEBYTECODE=1
RUN apt-get update && apt-get install -y curl gettext wget && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
WORKDIR /app
COPY . .
EXPOSE 8000
ENTRYPOINT ["./scripts/start.sh "]