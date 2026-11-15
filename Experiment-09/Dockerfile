# ==============================================================================
# EXPERIMENT 09: CUSTOM DOCKERFILE FOR CONTAINERIZED PYTHON MICROSERVICE
# Department of Computer Science & Engineering, NIE Mysuru
# ==============================================================================

# 1. Base Image: Lean official Python Alpine Linux distribution
FROM python:3.11-alpine

# 2. Metadata Labels: Provides provenance, ownership, and versioning info
LABEL maintainer="Nithyashree D S <2025cs_nithyashreeds_e@nie.ac.in>" \
      institute="The National Institute of Engineering, Mysuru" \
      experiment="09" \
      description="Custom Python Microservice Container"

# 3. Environment Variables: Ensures immediate log flushing and sets port
ENV PYTHONUNBUFFERED=1 \
    PORT=5000 \
    APP_ENV=production

# 4. Working Directory: Sets execution directory inside the container
WORKDIR /app

# 5. Dependency Management: Copy requirements first to leverage Docker layer caching
COPY application/requirements.txt /app/requirements.txt

# 6. Install Dependencies: Cache-busting installation
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy Application Code: Copies source code into current WORKDIR
COPY application/app.py /app/app.py

# 8. Security: Create and switch to non-root user
RUN adduser -D -u 1001 appuser && \
    chown -R appuser:appuser /app
USER appuser

# 9. Expose Port: Informs Docker of runtime communication port
EXPOSE 5000

# 10. Container Healthcheck: Periodic probe to confirm service vitality
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:5000/health || exit 1

# 11. Entry Command: Execution command invoked when container starts
CMD ["python", "app.py"]
