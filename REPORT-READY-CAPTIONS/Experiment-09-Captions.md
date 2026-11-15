# Report-Ready Captions: Experiment 09
### Experiment Title: Custom Dockerfiles & Containerized Application Build
**Course:** DevOps Laboratory (CSE) | **Institution:** The National Institute of Engineering, Mysuru  
**Student:** Nithyashree D S (2025cs_nithyashreeds_e@nie.ac.in)

---

### Figure 9.1
- **File:** `REPORT-IMAGES/Experiment-09/09-01-application-code.png`
- **Caption:** `Figure 9.1 – Python Flask REST microservice implementation with system metadata endpoints.`
- **Placement:** Section 8 (Application Design) -> Source Code Structure.
- **Narrative Context:** Insert to showcase the application source code (`app.py`) implementing health check and REST endpoints.

---

### Figure 9.2
- **File:** `REPORT-IMAGES/Experiment-09/09-02-dockerfile.png`
- **Caption:** `Figure 9.2 – Comprehensive Dockerfile specification adhering to containerization best practices.`
- **Placement:** Section 9 (Procedure) -> Step 2: Dockerfile Authoring.
- **Narrative Context:** Insert to present the complete Dockerfile structure including `FROM`, `WORKDIR`, `COPY`, `RUN`, `USER`, `EXPOSE`, `HEALTHCHECK`, and `CMD`.

---

### Figure 9.3
- **File:** `REPORT-IMAGES/Experiment-09/09-03-dockerfile-instructions.png`
- **Caption:** `Figure 9.3 – Detailed technical breakdown of Dockerfile directives and their operational impact.`
- **Placement:** Section 7 (Theory) -> Dockerfile Directives Explained.
- **Narrative Context:** Insert alongside the technical explanation of layer caching, rootless execution, and health probes.

---

### Figure 9.4
- **File:** `REPORT-IMAGES/Experiment-09/09-04-docker-image-build.png`
- **Caption:** `Figure 9.4 – Step-by-step compilation of custom Docker image via docker build CLI.`
- **Placement:** Section 9 (Procedure) -> Step 4: Docker Image Compilation.
- **Narrative Context:** Insert after executing `docker build -t exp09-custom-app:v1 .` demonstrating intermediary layer caching and image tagging.

---

### Figure 9.5
- **File:** `REPORT-IMAGES/Experiment-09/09-05-custom-image.png`
- **Caption:** `Figure 9.5 – Local Docker repository listing verifying the compiled image and disk usage.`
- **Placement:** Section 9 (Procedure) -> Step 5: Image Verification.
- **Narrative Context:** Insert after running `docker images exp09-custom-app:v1` showing image ID, repository tag, and size.

---

### Figure 9.6
- **File:** `REPORT-IMAGES/Experiment-09/09-06-container-execution.png`
- **Caption:** `Figure 9.6 – Instantiating container from the custom image with port forwarding.`
- **Placement:** Section 9 (Procedure) -> Step 6: Container Execution.
- **Narrative Context:** Insert after `docker run -d -p 5001:5000` and `docker ps` confirming active execution under non-root user.

---

### Figure 9.7
- **File:** `REPORT-IMAGES/Experiment-09/09-07-application-testing.png`
- **Caption:** `Figure 9.7 – Functional testing of the containerized microservice via HTTP request.`
- **Placement:** Section 14 (Results) -> Functional Verification.
- **Narrative Context:** Insert in the Results section to demonstrate the browser and JSON responses returned by the container.
