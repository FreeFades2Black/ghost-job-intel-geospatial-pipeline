# Multi-stage Dockerfile for Ghost Job Intel & Geospatial Pipeline
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python requirements
COPY requirements.txt* ./
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    pydantic \
    requests \
    pytest

# Copy application source
COPY src/ ./src/
COPY tests/ ./tests/
COPY ui/ ./ui/
COPY data/ ./data/

# Run Medallion pipeline to ensure latest Gold data is prepared
RUN python -c "from src.medallion.pipeline_bronze_ingestion import BronzeIngestionEngine; from src.medallion.pipeline_silver_lifecycle import SilverLifecycleEngine; from src.medallion.pipeline_gold_ghost_metrics import GoldGhostMetricsEngine; b = BronzeIngestionEngine(); b.run(); s = SilverLifecycleEngine(); s.run(); g = GoldGhostMetricsEngine(); g.run()" || true

# Non-root user
RUN addgroup --gid 10004 ghostapp && \
    adduser --uid 10004 --gid 10004 --disabled-password --gecos "" ghostapp && \
    chown -R ghostapp:ghostapp /app

USER 10004:10004

EXPOSE 8900

# Healthcheck
HEALTHCHECK --interval=15s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:8900/api/v1/ghost/summary || exit 1

# Launch FastAPI Uvicorn Server
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8900"]
