# Use official Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY config/requirements.txt ./

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r config/requirements.txt

# Copy application code
COPY src/ ./src

# Set entrypoint
CMD ["python", "src/main.py"]
