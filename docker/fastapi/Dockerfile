FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 FASTAPI_APP=app.py

# Build-time argument that controls which ML wheels to install.
# Valid values: cpu (default), cu118, cu121, cu122, etc. Use cpu on CI/servers without NVIDIA GPUs.
# NOTE: TensorFlow and PyTorch are no longer installed in this Docker image.
# For ML workloads, install them in your local environment or extend this image.
ARG INSTALL_TARGET=cpu
# Auto-detection is disabled since ML packages are not installed in this base image
ARG AUTO_DETECT=0

WORKDIR /app

# system dependencies required by some ML packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       wget \
       git \
       ca-certificates \
       libsndfile1 \
       libasound2 \
       libglib2.0-0 \
       libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# upgrade pip/wheel first
RUN pip install --upgrade pip setuptools wheel

# copy requirements and install python deps
COPY requirements/fastapi/requirements.txt /tmp/requirements.txt

# Install standard requirements only (no ML packages)
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# copy app source (compose mounts ./app-fastapi:/app during development)
COPY ./app-fastapi /app

EXPOSE 5011

# Default command: run uvicorn. Assumes the FastAPI app is available as `app` in `app.py`.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5011"]
# Default command: run uvicorn. Assumes the FastAPI app is available as `app` in `app.py`.
