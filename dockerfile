#------------------INTERMEDIATE BUILD------------------------
FROM python:3.10.14-slim as builder

RUN pip install poetry==1.7.1


ENV DEBIAN_FRONTEND=noninteractive \
  POETRY_VERSION=${POETRY_VERSION} \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=1 \
  POETRY_VIRTUALENVS_IN_PROJECT=1 \
  POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --without dev --no-root

RUN poetry add gdal==3.8.0



#------------------FINAL BUILD------------------------
FROM  python:3.10.14-slim
WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libgdal-dev \
    gcc \
    g++


ENV VIRTUAL_ENV=/app/.venv \
  PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}



ENV GDAL_LIBRARY_PATH="/app/.venv/lib/python3.10/site-packages/osgeo/gdal301.dll" \
    GEOS_LIBRARY_PATH="/app/.venv/lib/python3.10/site-packages/osgeo/geos_c.dll"

COPY . /app

CMD ["python", "manage.py", "runserver"]