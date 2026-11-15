# Report-Ready Captions: Experiment 10
### Experiment Title: Multi-Container Applications Using Docker Compose
**Course:** DevOps Laboratory (CSE) | **Institution:** The National Institute of Engineering, Mysuru  
**Student:** Nithyashree D S (2025cs_nithyashreeds_e@nie.ac.in)

---

### Figure 10.1
- **File:** `REPORT-IMAGES/Experiment-10/10-01-project-structure.png`
- **Caption:** `Figure 10.1 – Multi-container project directory tree separating frontend, backend, and compose configurations.`
- **Placement:** Section 8 (Architecture & Design) -> Directory Layout.
- **Narrative Context:** Insert at the beginning of the experiment walkthrough to show the modular project layout.

---

### Figure 10.2
- **File:** `REPORT-IMAGES/Experiment-10/10-02-application-architecture.png`
- **Caption:** `Figure 10.2 – Multi-tier architecture diagram showing Flask frontend, Redis cache, and isolated bridge network.`
- **Placement:** Section 8 (Architecture & Design) -> System Topology.
- **Narrative Context:** Insert in the architecture section to illustrate how client traffic traverses the host port into the frontend container, which then queries the Redis backend over internal DNS.

---

### Figure 10.3
- **File:** `REPORT-IMAGES/Experiment-10/10-03-frontend-code.png`
- **Caption:** `Figure 10.3 – Flask frontend application logic implementing Redis connection pooling and atomic counter incrementation.`
- **Placement:** Section 9 (Procedure) -> Step 3: Frontend Implementation.
- **Narrative Context:** Insert displaying `frontend/app.py` source code.

---

### Figure 10.4
- **File:** `REPORT-IMAGES/Experiment-10/10-04-backend-code.png`
- **Caption:** `Figure 10.4 – Backend Redis database configuration specifying persistence intervals and memory policies.`
- **Placement:** Section 9 (Procedure) -> Step 4: Backend Service Setup.
- **Narrative Context:** Insert displaying Redis configuration and service parameters.

---

### Figure 10.5
- **File:** `REPORT-IMAGES/Experiment-10/10-05-docker-compose-file.png`
- **Caption:** `Figure 10.5 – Docker Compose specification file (docker-compose.yml) orchestrating multi-service topology.`
- **Placement:** Section 9 (Procedure) -> Step 5: Compose Authoring.
- **Narrative Context:** Insert displaying the YAML file containing `services`, `ports`, `networks`, `volumes`, and `depends_on`.

---

### Figure 10.6
- **File:** `REPORT-IMAGES/Experiment-10/10-06-compose-build.png`
- **Caption:** `Figure 10.6 – Multi-service compilation and dependency caching via docker-compose build.`
- **Placement:** Section 9 (Procedure) -> Step 6: Compose Build Phase.
- **Narrative Context:** Insert showing terminal build output for all composite containers.

---

### Figure 10.7
- **File:** `REPORT-IMAGES/Experiment-10/10-07-compose-start.png`
- **Caption:** `Figure 10.7 – Initializing and launching multi-container environment in detached mode using docker-compose up -d.`
- **Placement:** Section 9 (Procedure) -> Step 7: Service Orchestration.
- **Narrative Context:** Insert showing network creation, volume allocation, and container initialization.

---

### Figure 10.8
- **File:** `REPORT-IMAGES/Experiment-10/10-08-running-services.png`
- **Caption:** `Figure 10.8 – Process listing showing both frontend and backend services in active state.`
- **Placement:** Section 9 (Procedure) -> Step 8: Service State Verification.
- **Narrative Context:** Insert displaying `docker-compose ps` with healthy service states.

---

### Figure 10.9
- **File:** `REPORT-IMAGES/Experiment-10/10-09-service-communication.png`
- **Caption:** `Figure 10.9 – Internal network inspection verifying container IP assignments and inter-service connectivity.`
- **Placement:** Section 9 (Procedure) -> Step 9: Inter-Service Network Validation.
- **Narrative Context:** Insert showing bridge network configuration and attached container endpoints.

---

### Figure 10.10
- **File:** `REPORT-IMAGES/Experiment-10/10-10-application-output.png`
- **Caption:** `Figure 10.10 – Web browser UI displaying live hit counter synchronized with the Redis database backend.`
- **Placement:** Section 14 (Results) -> Multi-Service Validation.
- **Narrative Context:** Insert in the Results section to demonstrate real-time data persistence across services.

---

### Figure 10.11
- **File:** `REPORT-IMAGES/Experiment-10/10-11-container-logs.png`
- **Caption:** `Figure 10.11 – Aggregated real-time logging stream from frontend and backend containers.`
- **Placement:** Section 9 (Procedure) -> Step 11: Service Log Inspection.
- **Narrative Context:** Insert showing interleaved logging output demonstrating synchronous request processing.

---

### Figure 10.12
- **File:** `REPORT-IMAGES/Experiment-10/10-12-compose-stop.png`
- **Caption:** `Figure 10.12 – Graceful multi-container teardown and network cleanup via docker-compose down.`
- **Placement:** Section 9 (Procedure) -> Step 12: Application Teardown.
- **Narrative Context:** Insert at the end of the procedure demonstrating resource cleanup without data corruption.
