FROM python:3.10.14-slim as builder

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git

# Install Poetry
RUN pip3 install poetry==1.8.2
WORKDIR /src
COPY pyproject.toml poetry.lock /src/

# virtual env is created in "/app/.venv" directory
ENV POETRY_NO_INTERACTION=1 \
POETRY_VIRTUALENVS_IN_PROJECT=1 \
POETRY_VIRTUALENVS_CREATE=true \
POETRY_CACHE_DIR=/tmp/poetry_cache

# Install dependencies in a cache
RUN --mount=type=cache,target=/tmp/poetry_cache \
    PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring \
    poetry install --only main --no-root

FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Los_Angeles

# update and install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common \
    libsm6 libxext6 libxrender-dev curl git \
    && rm -rf /var/lib/apt/lists/*

# install python
RUN add-apt-repository ppa:deadsnakes/ppa &&  \
    apt-get install -y build-essential python3.10 python3.10-dev python3-pip && \
    rm -rf /var/lib/apt/lists/*
RUN update-alternatives --install /usr/local/bin/python python \
    /usr/bin/python3.10 10

# install poetry
RUN pip3 install poetry==1.8.2

# copy source install requirements
COPY --from=builder /src/ /src/
COPY openad_model_property_service  /src/openad_model_property_service
COPY README.md /src
ENV PATH="/src/.venv/bin:$PATH"

# install root package
RUN poetry --directory=/src/ install --only main

# set permissions for OpenShift
# from https://docs.openshift.com/container-platform/4.5/openshift_images/create-images.html#images-create-guide-general_create-images
RUN mkdir -p ./oracle /.config /.cache /.gt4sd /.paccmann && \
    chgrp -R 0 ./oracle /.config /.cache /.gt4sd /.paccmann && \
    chmod -R g=u ./oracle /.config /.cache /.gt4sd /.paccmann
# excluding the .venv directory from recursive permissions
RUN find /src -path /src/.venv -prune -o -print | xargs chgrp 0 && \
    find /src -path /src/.venv -prune -o -exec chmod g=u {} +

EXPOSE 8080 80

CMD ["/src/.venv/bin/python", "/src/openad_model_property_service/service.py"]
