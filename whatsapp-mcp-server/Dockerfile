# Python MCP Server Dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install uv package manager
RUN pip install uv

# Copy project files
COPY pyproject.toml .
COPY *.py ./

# Install dependencies using uv
RUN uv pip install --system -e .

# Environment variables
ENV BRIDGE_URL=http://localhost:8080
ENV DATABASE_PATH=/app/store/messages.db

# Volume for the shared store directory
VOLUME ["/app/store"]

# Default command - run the MCP server
CMD ["python", "main.py"]
