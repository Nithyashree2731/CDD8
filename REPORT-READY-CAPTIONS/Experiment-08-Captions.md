# Report-Ready Captions: Experiment 08
### Experiment Title: Simple Docker Containers & Lifecycle Management
**Course:** DevOps Laboratory (CSE) | **Institution:** The National Institute of Engineering, Mysuru  
**Student:** Nithyashree D S (2025cs_nithyashreeds_e@nie.ac.in)

---

### Figure 8.1
- **File:** `REPORT-IMAGES/Experiment-08/08-01-docker-version.png`
- **Caption:** `Figure 8.1 – Verification of Docker Engine version, build commit, and system architecture.`
- **Placement:** Section 9 (Procedure) -> Step 1: Environment Inspection.
- **Narrative Context:** Insert after executing `docker version` and `docker info` to document the active container runtime environment.

---

### Figure 8.2
- **File:** `REPORT-IMAGES/Experiment-08/08-02-image-pull.png`
- **Caption:** `Figure 8.2 – Pulling the official Nginx Alpine base image from Docker Hub registry.`
- **Placement:** Section 9 (Procedure) -> Step 2: Image Acquisition.
- **Narrative Context:** Insert after running `docker pull nginx:alpine` to illustrate the multi-layer image download process and sha256 digest validation.

---

### Figure 8.3
- **File:** `REPORT-IMAGES/Experiment-08/08-03-downloaded-image.png`
- **Caption:** `Figure 8.3 – Local Docker image repository verification displaying cached images.`
- **Placement:** Section 9 (Procedure) -> Step 3: Local Image Inspection.
- **Narrative Context:** Insert after running `docker images nginx:alpine` to confirm image ID, creation date, and disk footprint.

---

### Figure 8.4
- **File:** `REPORT-IMAGES/Experiment-08/08-04-container-creation.png`
- **Caption:** `Figure 8.4 – Instantiation of container in detached mode with host port forwarding.`
- **Placement:** Section 9 (Procedure) -> Step 4: Container Creation.
- **Narrative Context:** Insert after executing `docker run -d -p 8080:80 --name exp08-nginx-server nginx:alpine` showing the generated container UUID.

---

### Figure 8.5
- **File:** `REPORT-IMAGES/Experiment-08/08-05-running-container.png`
- **Caption:** `Figure 8.5 – Active process table inspection showing running container and port mappings.`
- **Placement:** Section 9 (Procedure) -> Step 5: Container Status Verification.
- **Narrative Context:** Insert after running `docker ps` to demonstrate the active `Up` status and port binding (`0.0.0.0:8080->80/tcp`).

---

### Figure 8.6
- **File:** `REPORT-IMAGES/Experiment-08/08-06-application-output.png`
- **Caption:** `Figure 8.6 – Web browser interface verifying HTTP 200 response from containerized application.`
- **Placement:** Section 9 (Procedure) -> Step 6: Application Functional Validation.
- **Narrative Context:** Insert in the Results section to demonstrate end-to-end network connectivity and web page serving from the container.

---

### Figure 8.7
- **File:** `REPORT-IMAGES/Experiment-08/08-07-container-lifecycle.png`
- **Caption:** `Figure 8.7 – Sequential execution of container lifecycle transitions (Stop, Start, Restart, and Remove).`
- **Placement:** Section 9 (Procedure) -> Step 7: Container Lifecycle Management.
- **Narrative Context:** Insert in the Lifecycle Operations subsection to document state transitions and container cleanup.
