APAN FastAPI example app

This folder contains a minimal FastAPI application used for testing the `apan-fast-api` service.

Files
- `app.py` - minimal FastAPI app with `/`, `/health`, and `/predict` endpoints.

Run with Docker Compose

1. Build and start the service:

   docker compose build apan-fast-api
   docker compose up apan-fast-api

2. The FastAPI app will be available at http://localhost:5011 (host port).

Example requests

Health check:

    curl http://localhost:5011/health

Predict example:

    curl -X POST http://localhost:5011/predict -H "Content-Type: application/json" -d '{"values": [1,2,3.5]}'

Note: the Docker image for this service installs TensorFlow and PyTorch CPU wheels which are large. Building the image will download large files and may take several minutes and significant disk space.

Build-time options

You can control which PyTorch wheels are installed using a build-arg `INSTALL_TARGET`.

- CPU (default):

    docker compose build --build-arg INSTALL_TARGET=cpu apan-fast-api

- NVIDIA CUDA (example for CUDA 11.8 wheels):

    docker compose build --build-arg INSTALL_TARGET=cu118 apan-fast-api

Notes:
- Installing CUDA-enabled PyTorch requires appropriate CUDA libraries on the host or base image and compatible drivers. This Dockerfile does not provide system CUDA libraries — use a CUDA-enabled base image for GPU support.
- TensorFlow here is the CPU wheel. For GPU TensorFlow, pick an appropriate base image and wheel matching the CUDA/cuDNN versions.

Metal (Apple MPS) on macOS

Metal (MPS) is supported only on macOS (Apple Silicon / M1/M2). It cannot be used from a standard Linux Docker container. To use Metal on macOS, install and run natively on your Mac:

```bash
# Create venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

# TensorFlow (Apple/Metal)
pip install tensorflow-macos tensorflow-metal

# PyTorch (MPS/Metal)
pip install --extra-index-url https://download.pytorch.org/whl/metal.html torch torchvision

# Quick checks
python -c "import tensorflow as tf; print(tf.__version__, tf.config.list_physical_devices())"
python -c "import torch; print(torch.__version__, torch.backends.mps.is_available())"
```

If you want a local development flow on macOS that uses Metal while keeping Docker for CI, run the app locally on macOS and use Docker images for CI with `INSTALL_TARGET=cpu`.
