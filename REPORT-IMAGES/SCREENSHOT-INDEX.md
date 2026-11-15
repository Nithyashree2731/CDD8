# 📸 DevOps Laboratory Screenshot Evidence Index
### The National Institute of Engineering, Mysuru
**Department of Computer Science & Engineering**  
**Course:** DevOps Laboratory (CSE)  
**Student Name:** Nithyashree D S  
**USN / College Email:** 2025cs_nithyashreeds_e@nie.ac.in  
**Repository:** [https://github.com/Nithyashree2731/CDD8](https://github.com/Nithyashree2731/CDD8)  
**Total Images Captured:** 37 / 37 (100% Verified)

---

## Summary of Screenshot Allocation

| Experiment | Title | Required | Captured | Status |
|:---:|:---|:---:|:---:|:---:|
| **Exp 08** | Simple Containers & Lifecycle Management | 7 | 7 | ✅ Captured |
| **Exp 09** | Custom Dockerfile & Image Build | 7 | 7 | ✅ Captured |
| **Exp 10** | Multi-Container Application with Compose | 12 | 12 | ✅ Captured |
| **Exp 11** | Containerization of Python Application | 11 | 11 | ✅ Captured |
| **Total** | **All 4 Experiments** | **37** | **37** | **100% Complete** |

---

## 🔬 Experiment 08: Simple Docker Containers & Lifecycle

| Filename | Figure | Procedure Step | Description | Demonstration | Status |
|---|---|---|---|---|:---:|
| `08-01-docker-version.png` | Figure 8.1 | Step 1 | Docker Version & Client/Server Info | Verifies Docker Desktop v4.91 / Engine v29.8 | Captured |
| `08-02-image-pull.png` | Figure 8.2 | Step 2 | Pulling Nginx Alpine Base Image | Downloads official OCI image layers from Docker Hub | Captured |
| `08-03-downloaded-image.png` | Figure 8.3 | Step 3 | Verifying Cached Docker Images | Confirms `nginx:alpine` exists in local repository | Captured |
| `08-04-container-creation.png` | Figure 8.4 | Step 4 | Container Instantiation & Port Mapping | Runs `nginx:alpine` in detached mode mapping host port 8080 | Captured |
| `08-05-running-container.png` | Figure 8.5 | Step 5 | Inspecting Active Containers | Confirms container status `Up` with healthy port binding | Captured |
| `08-06-application-output.png` | Figure 8.6 | Step 6 | HTTP Endpoint Verification | Browser view confirming HTTP 200 response from Nginx | Captured |
| `08-07-container-lifecycle.png` | Figure 8.7 | Step 7 | Container Lifecycle Operations | Execution of `stop`, `start`, `restart`, and `rm` | Captured |

---

## 🔬 Experiment 09: Custom Dockerfiles & Image Architecture

| Filename | Figure | Procedure Step | Description | Demonstration | Status |
|---|---|---|---|---|:---:|
| `09-01-application-code.png` | Figure 9.1 | Step 1 | Flask REST API Application Source | Python application source code with healthcheck endpoint | Captured |
| `09-02-dockerfile.png` | Figure 9.2 | Step 2 | Production Dockerfile Definition | Complete Dockerfile with 11 production directives | Captured |
| `09-03-dockerfile-instructions.png` | Figure 9.3 | Step 3 | Directive Architecture & Explanation | Comprehensive instruction-by-instruction breakdown | Captured |
| `09-04-docker-image-build.png` | Figure 9.4 | Step 4 | Docker Build Execution | Layered image build execution tagged `exp09-custom-app:v1` | Captured |
| `09-05-custom-image.png` | Figure 9.5 | Step 5 | Custom Image Verification | Verification of newly created image in Docker image index | Captured |
| `09-06-container-execution.png` | Figure 9.6 | Step 6 | Launching Custom Container | Instantiating container with port 5001:5000 binding | Captured |
| `09-07-application-testing.png` | Figure 9.7 | Step 7 | Endpoint Functional Validation | Web response validating JSON payload and container health | Captured |

---

## 🔬 Experiment 10: Multi-Container Systems with Docker Compose

| Filename | Figure | Procedure Step | Description | Demonstration | Status |
|---|---|---|---|---|:---:|
| `10-01-project-structure.png` | Figure 10.1 | Step 1 | Compose Project Directory Tree | File hierarchy separating frontend, backend, and compose | Captured |
| `10-02-application-architecture.png` | Figure 10.2 | Step 2 | Architecture Specification | System topology showing Flask, Redis, and Bridge network | Captured |
| `10-03-frontend-code.png` | Figure 10.3 | Step 3 | Frontend Application Code | Flask web application using Redis connection pool | Captured |
| `10-04-backend-code.png` | Figure 10.4 | Step 4 | Backend Redis Configuration | Configuration specifications for in-memory database | Captured |
| `10-05-docker-compose-file.png` | Figure 10.5 | Step 5 | Compose Specification File | Multi-service definition with ports, networks, volumes | Captured |
| `10-06-compose-build.png` | Figure 10.6 | Step 6 | Multi-Service Build Execution | Build process constructing services specified in compose file | Captured |
| `10-07-compose-start.png` | Figure 10.7 | Step 7 | Compose Up Daemon Launch | Creating isolated bridge network and launching containers | Captured |
| `10-08-running-services.png` | Figure 10.8 | Step 8 | Compose Service Status | Discovery showing frontend and backend in running state | Captured |
| `10-09-service-communication.png` | Figure 10.9 | Step 9 | Inter-Service Network Validation | DNS resolution and bridge network inspect details | Captured |
| `10-10-application-output.png` | Figure 10.10 | Step 10 | Application Hit Counter UI | Browser output displaying synchronized Redis visit counter | Captured |
| `10-11-container-logs.png` | Figure 10.11 | Step 11 | Aggregated Multi-Service Logs | Real-time interleaved logs from both frontend and backend | Captured |
| `10-12-compose-stop.png` | Figure 10.12 | Step 12 | Graceful Resource Teardown | `docker compose down` stopping containers and network | Captured |

---

## 🔬 Experiment 11: Containerization of Python Application

| Filename | Figure | Procedure Step | Description | Demonstration | Status |
|---|---|---|---|---|:---:|
| `11-01-project-structure.png` | Figure 11.1 | Step 1 | Microservice Directory Structure | Project organization containing code, requirements, Dockerfile | Captured |
| `11-02-python-application-code.png` | Figure 11.2 | Step 2 | Academic Portal Python Source | Grade analytics microservice computing CGPA and stats | Captured |
| `11-03-requirements-file.png` | Figure 11.3 | Step 3 | Python Requirements File | Pinned dependency specifications for deterministic builds | Captured |
| `11-04-dockerfile.png` | Figure 11.4 | Step 4 | Python Production Dockerfile | Lean container definition using official Python Alpine base | Captured |
| `11-05-image-build.png` | Figure 11.5 | Step 5 | Container Image Compilation | `docker build` process creating `exp11-student-portal` | Captured |
| `11-06-image-verification.png` | Figure 11.6 | Step 6 | Image Metadata Verification | Verifying image size, tags, and layer composition | Captured |
| `11-07-container-execution.png` | Figure 11.7 | Step 7 | Container Execution & Port Map | Detached container run mapping host port 5050 to 5050 | Captured |
| `11-08-container-status.png` | Figure 11.8 | Step 8 | Container Runtime Inspection | Verifying active container status and healthy state | Captured |
| `11-09-browser-output.png` | Figure 11.9 | Step 9 | Academic Portal Web Interface | Browser rendering interactive student grades & statistics | Captured |
| `11-10-container-logs.png` | Figure 11.10 | Step 10 | Container Streaming Logs | HTTP access logs recorded within the container runtime | Captured |
| `11-11-final-verification.png` | Figure 11.11 | Step 11 | REST API Verification & Cleanup | Terminal validation of `/api/students` and clean removal | Captured |

---
*Generated and verified automatically for NIE Mysuru DevOps Laboratory Report submission.*
