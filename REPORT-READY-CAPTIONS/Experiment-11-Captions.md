# Report-Ready Captions: Experiment 11
### Experiment Title: Containerization & Execution of Python Application
**Course:** DevOps Laboratory (CSE) | **Institution:** The National Institute of Engineering, Mysuru  
**Student:** Nithyashree D S (2025cs_nithyashreeds_e@nie.ac.in)

---

### Figure 11.1
- **File:** `REPORT-IMAGES/Experiment-11/11-01-project-structure.png`
- **Caption:** `Figure 11.1 – Directory layout for the containerized Python Academic Analytics application.`
- **Placement:** Section 8 (Project Layout) -> Step 1: Directory Structure.
- **Narrative Context:** Insert showing root folder containing `application/`, `requirements.txt`, and `Dockerfile`.

---

### Figure 11.2
- **File:** `REPORT-IMAGES/Experiment-11/11-02-python-application-code.png`
- **Caption:** `Figure 11.2 – Python Flask source code computing student grade analytics, CGPA, and JSON endpoints.`
- **Placement:** Section 9 (Procedure) -> Step 2: Application Development.
- **Narrative Context:** Insert displaying the core business logic of `student_analytics.py`.

---

### Figure 11.3
- **File:** `REPORT-IMAGES/Experiment-11/11-03-requirements-file.png`
- **Caption:** `Figure 11.3 – Pinned Python dependencies specification file (requirements.txt).`
- **Placement:** Section 9 (Procedure) -> Step 3: Dependency Specification.
- **Narrative Context:** Insert showing dependency specifications ensuring reproducible builds.

---

### Figure 11.4
- **File:** `REPORT-IMAGES/Experiment-11/11-04-dockerfile.png`
- **Caption:** `Figure 11.4 – Production Dockerfile configuring Python 3.11 Alpine runtime with port 5050 exposure.`
- **Placement:** Section 9 (Procedure) -> Step 4: Dockerfile Configuration.
- **Narrative Context:** Insert displaying Dockerfile instructions.

---

### Figure 11.5
- **File:** `REPORT-IMAGES/Experiment-11/11-05-image-build.png`
- **Caption:** `Figure 11.5 – Terminal output of docker build command compiling exp11-student-portal:latest image.`
- **Placement:** Section 9 (Procedure) -> Step 5: Container Image Compilation.
- **Narrative Context:** Insert showing step-by-step layer building and image generation.

---

### Figure 11.6
- **File:** `REPORT-IMAGES/Experiment-11/11-06-image-verification.png`
- **Caption:** `Figure 11.6 – Local Docker image repository listing confirming the creation of the application image.`
- **Placement:** Section 9 (Procedure) -> Step 6: Image Verification.
- **Narrative Context:** Insert after executing `docker images` confirming repository tag, image ID, and size.

---

### Figure 11.7
- **File:** `REPORT-IMAGES/Experiment-11/11-07-container-execution.png`
- **Caption:** `Figure 11.7 – Container execution command mapping host port 5050 to container port 5050.`
- **Placement:** Section 9 (Procedure) -> Step 7: Container Instantiation.
- **Narrative Context:** Insert showing detached container instantiation with port binding.

---

### Figure 11.8
- **File:** `REPORT-IMAGES/Experiment-11/11-08-container-status.png`
- **Caption:** `Figure 11.8 – Active container inspection verifying container health and status.`
- **Placement:** Section 9 (Procedure) -> Step 8: Container Status Check.
- **Narrative Context:** Insert showing `docker ps` with active container status.

---

### Figure 11.9
- **File:** `REPORT-IMAGES/Experiment-11/11-09-browser-output.png`
- **Caption:** `Figure 11.9 – Web browser interface rendering dynamic student grade analytics from container.`
- **Placement:** Section 14 (Results) -> Application Verification.
- **Narrative Context:** Insert in the Results section showing the operational web portal interface.

---

### Figure 11.10
- **File:** `REPORT-IMAGES/Experiment-11/11-10-container-logs.png`
- **Caption:** `Figure 11.10 – Real-time HTTP access logs captured from the running Python container.`
- **Placement:** Section 9 (Procedure) -> Step 10: Container Log Analysis.
- **Narrative Context:** Insert showing incoming GET requests recorded by Flask server.

---

### Figure 11.11
- **File:** `REPORT-IMAGES/Experiment-11/11-11-final-verification.png`
- **Caption:** `Figure 11.11 – Verification of REST API endpoint via curl and subsequent graceful container removal.`
- **Placement:** Section 9 (Procedure) -> Step 11: Final Validation & Teardown.
- **Narrative Context:** Insert showing JSON payload verification and cleanup.
