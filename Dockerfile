# FROM python:bookworm
FROM pytorch/pytorch:latest

LABEL maintainer=498rustam@gmail.com
ENV TZ=Europe/Moscow \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    curl \
    git \
    python3-venv \
    python3-pip \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/apt-packages

WORKDIR /app
COPY --link . .
# RUN python3 -m venv venv 
# ENV PATH="/app/venv/bin:$PATH"

# RUN pip install --no-cache-dir -U pip memory_profiler
# RUN pip install --no-cache-dir easyocr==1.7.1

ENV PYTHONPATH=/app
ENTRYPOINT ["/bin/bash"]
