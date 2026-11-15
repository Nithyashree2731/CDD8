# Technical Observations: Experiment 10
### Multi-Container Applications Using Docker Compose

**Department of Computer Science & Engineering, NIE Mysuru**  
**Student:** Nithyashree D S (2025cs_nithyashreeds_e@nie.ac.in)

---

## 1. Embedded DNS & Service Discovery
- Unlike the default `docker0` bridge network which requires legacy `--link` flags or explicit IP addressing, custom user-defined bridge networks (`devops-lab-network`) include automatic DNS resolution.
- The Flask frontend resolved the Redis database using the service name `backend-redis`, which Docker's DNS dynamically translated to the container's internal IP (`172.x.x.x`).

## 2. Dependency Management & Startup Timing
- The `depends_on: - backend-redis` clause ensured that Docker Compose initialized the Redis storage engine prior to bootstrapping the Python web worker.
- Persistent state was preserved inside the named Docker volume `redis-data`, ensuring count continuity even across container restarts.

## 3. Aggregated Log Multiplexing
- Running `docker-compose logs` dynamically color-coded and multiplexed log streams from both `exp10-frontend-service` and `exp10-redis-backend`, providing unified observability across the distributed system.
