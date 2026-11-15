# Technical Observations: Experiment 09
### Custom Dockerfiles & Containerized Application Build

**Department of Computer Science & Engineering, NIE Mysuru**  
**Student:** Nithyashree D S (2025cs_nithyashreeds_e@nie.ac.in)

---

## 1. Build Cache Optimization Analysis
- By isolating `COPY application/requirements.txt /app/requirements.txt` from the application code copy (`COPY application/app.py /app/app.py`), the heavy step `RUN pip install` is cached across code modifications.
- Re-running `docker build` after updating application source completed in under 1.2 seconds due to Docker's content-addressable layer cache (`Using cache`).

## 2. Security Assessment (Root vs. Non-Root)
- Traditional containers execute as UID 0 (`root`), creating a critical vulnerability where a container breakout could compromise the host OS kernel.
- Adding `RUN adduser -D -u 1001 appuser` and switching via `USER appuser` constrained all executing processes to unprivileged boundaries without access to system-level configuration files outside `/app`.

## 3. Autonomous Health Probe Dynamics
- The directive `HEALTHCHECK --interval=30s --timeout=5s ... CMD wget ...` enabled Docker daemon self-monitoring.
- Running `docker ps` confirmed container transition from `health: starting` to `healthy` upon the first successful HTTP 200 response from `/health`.
