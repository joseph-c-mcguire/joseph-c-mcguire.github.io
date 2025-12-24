# Python backend Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire source code first (including src, pyproject.toml, README.md, etc.)
COPY . .

# Install Python dependencies from pyproject.toml
RUN pip install --no-cache-dir -e . && \
    pip install --no-cache-dir gunicorn

# Expose port
EXPOSE 8000

# Run with gunicorn
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "joseph_mcguire_backend.main:app"]
