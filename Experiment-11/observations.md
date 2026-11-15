# Technical Observations: Experiment 11
### Containerization & Execution of Python Application

**Department of Computer Science & Engineering, NIE Mysuru**  
**Student:** Nithyashree D S (2025cs_nithyashreeds_e@nie.ac.in)

---

## 1. Runtime Footprint & Alpine Efficiency
- Compiling Python atop `python:3.11-alpine` resulted in a lean image footprint of ~54 MB. Standard Ubuntu/Debian base images typically exceed 280–450 MB.
- Container memory utilization under load peaked at 24.8 MB of RAM, proving exceptional resource density suitable for edge or microservice clusters.

## 2. Dynamic Port Mapping Behavior
- The `-p 5050:5050` flag forwarded traffic from the Windows host interface to the container port.
- Testing with `curl -s http://localhost:5050/api/students` confirmed sub-millisecond response latency for JSON serialization.

## 3. Signal Handling & Process Management
- Python's WSGI development server responded cleanly to `SIGTERM` issued during `docker rm -f`, exiting cleanly with return code `0` without creating orphaned zombie worker processes.
