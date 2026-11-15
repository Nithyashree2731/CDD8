# ==============================================================================
# EXPERIMENT 11: CONTAINERIZATION OF PYTHON APPLICATION
# Department of Computer Science & Engineering, NIE Mysuru
# ==============================================================================

FROM python:3.11-alpine

LABEL maintainer="Nithyashree D S <2025cs_nithyashreeds_e@nie.ac.in>"
LABEL institute="The National Institute of Engineering, Mysuru"
LABEL course="DevOps Laboratory (CSE)"
LABEL experiment="11"

WORKDIR /app

# Optimize layer caching
COPY application/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY application/student_analytics.py /app/student_analytics.py

# Configure container environment
ENV PYTHONUNBUFFERED=1 \
    PORT=5050

EXPOSE 5050

CMD ["python", "student_analytics.py"]
