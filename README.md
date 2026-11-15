# 🚀 DevOps Laboratory Experiments 8–11
### Department of Computer Science & Engineering
### The National Institute of Engineering, Mysuru

**Course:** DevOps Laboratory (CSE)  
**Student Name:** Nithyashree D S  
**USN / College Email:** 2025cs_nithyashreeds_e@nie.ac.in  
**GitHub Repository:** [https://github.com/Nithyashree2731/CDD8](https://github.com/Nithyashree2731/CDD8)  
**Environment:** Docker Desktop 4.91 / Docker Engine 29.8.0 / WSL2 / Windows 11  

---

## 📋 Laboratory Overview

This repository contains the complete implementation, source code, configuration manifests, technical observations, and photographic execution evidence for **Experiments 8 through 11** of the official DevOps Laboratory curriculum at The National Institute of Engineering (NIE), Mysuru.

Every experiment has been executed and verified in an authentic local Docker environment.

---

## 🗂️ Repository Architecture

```text
devops-lab-experiments-08-11/
│
├── README.md                              <- Main Laboratory Documentation
├── .gitignore                             <- Git Exclusion Manifest
│
├── REPORT-IMAGES/                         <- Master Screenshot Evidence Library
│   ├── SCREENSHOT-INDEX.md                <- Comprehensive 37-Image Index
│   ├── Experiment-08/                     <- 7 Verified Execution Screenshots
│   ├── Experiment-09/                     <- 7 Verified Execution Screenshots
│   ├── Experiment-10/                     <- 12 Verified Execution Screenshots
│   └── Experiment-11/                     <- 11 Verified Execution Screenshots
│
├── REPORT-READY-CAPTIONS/                 <- Ready-to-use Lab Report Captions & Placements
│   ├── Experiment-08-Captions.md
│   ├── Experiment-09-Captions.md
│   ├── Experiment-10-Captions.md
│   └── Experiment-11-Captions.md
│
├── Experiment-08/                         <- Experiment 08: Simple Containers & Lifecycle
│   ├── README.md
│   ├── observations.md
│   ├── Dockerfile
│   ├── application/
│   │   ├── index.html
│   │   ├── app.py
│   │   └── requirements.txt
│   └── screenshots/ (7 images)
│
├── Experiment-09/                         <- Experiment 09: Custom Dockerfile & Image Build
│   ├── README.md
│   ├── observations.md
│   ├── Dockerfile
│   ├── application/
│   │   ├── app.py
│   │   └── requirements.txt
│   └── screenshots/ (7 images)
│
├── Experiment-10/                         <- Experiment 10: Multi-Container with Compose
│   ├── README.md
│   ├── observations.md
│   ├── docker-compose.yml
│   ├── frontend/
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   └── requirements.txt
│   ├── backend/
│   │   └── redis.conf
│   └── screenshots/ (12 images)
│
└── Experiment-11/                         <- Experiment 11: Containerized Python Application
    ├── README.md
    ├── observations.md
    ├── Dockerfile
    ├── application/
    │   ├── student_analytics.py
    │   └── requirements.txt
    └── screenshots/ (11 images)
```

---

## 🔬 Experiment Summaries

### [Experiment 08: Simple Containers & Lifecycle Management](./Experiment-08/)
- **Objective:** Pull base image (`nginx:alpine`), instantiate containers, map host ports (`8080:80`), and execute lifecycle state transitions (`stop`, `start`, `restart`, `rm`).
- **Key Commands:** `docker pull`, `docker run -d -p 8080:80`, `docker ps`, `docker stop`, `docker rm`.
- **Evidence:** 7 Verified Screenshots capturing download digests, running processes, HTTP 200 responses, and state changes.

### [Experiment 09: Custom Dockerfiles & Image Architecture](./Experiment-09/)
- **Objective:** Author a production Dockerfile adhering to containerization best practices (`FROM`, `LABEL`, `ENV`, `WORKDIR`, `COPY`, `RUN`, `USER`, `EXPOSE`, `HEALTHCHECK`, `CMD`).
- **Key Directives:** Rootless execution (`USER appuser`), layer caching optimization, health probing.
- **Evidence:** 7 Verified Screenshots capturing application code, Dockerfile, build compilation, and REST validation.

### [Experiment 10: Multi-Container Applications using Docker Compose](./Experiment-10/)
- **Objective:** Orchestrate a two-tier microservice architecture comprising a Python Flask frontend and an in-memory Redis database.
- **Networking & Storage:** User-defined bridge network (`devops-lab-network`) with embedded DNS service discovery and persistent named volume (`redis-data`).
- **Evidence:** 12 Verified Screenshots covering directory structure, architecture diagram, compose configuration, build, orchestration, hit counter verification, interleaved logs, and graceful teardown.

### [Experiment 11: Containerization of Python Application](./Experiment-11/)
- **Objective:** Develop, containerize, and execute a Python Academic Analytics microservice calculating USN grades, CGPA, and REST endpoints.
- **Port Mapping:** Host port `5050` &rarr; Container port `5050`.
- **Evidence:** 11 Verified Screenshots covering source code, dependency pinning, Alpine Dockerfile build, container status, interactive web UI, streaming logs, and API verification.

---

## 📸 Master Screenshot Verification Table

| Experiment | Target Scope | Required | Captured | Verification Status |
|:---:|:---|:---:|:---:|:---:|
| **Exp 08** | Simple Containers & Lifecycle | 7 | 7 | ✅ 100% Captured |
| **Exp 09** | Custom Dockerfile & Build | 7 | 7 | ✅ 100% Captured |
| **Exp 10** | Multi-Container Compose | 12 | 12 | ✅ 100% Captured |
| **Exp 11** | Python Microservice Container | 11 | 11 | ✅ 100% Captured |
| **TOTAL** | **Complete DevOps Lab Portfolio** | **37** | **37** | **✅ 100% Verified** |

---

## 🛠️ Reproduction & Quick Start Guide

To run any experiment locally, navigate to the experiment folder:

### Experiment 08:
```powershell
cd Experiment-08
docker build -t exp08-nginx-app .
docker run -d -p 8080:80 --name exp08-nginx exp08-nginx-app
# Visit: http://localhost:8080
```

### Experiment 09:
```powershell
cd Experiment-09
docker build -t exp09-custom-app:v1 .
docker run -d -p 5001:5000 --name exp09-app exp09-custom-app:v1
# Visit: http://localhost:5001
```

### Experiment 10:
```powershell
cd Experiment-10
docker-compose build
docker-compose up -d
# Visit: http://localhost:8000 (Refresh to see Redis counter increment)
docker-compose down
```

### Experiment 11:
```powershell
cd Experiment-11
docker build -t exp11-student-portal:latest .
docker run -d -p 5050:5050 --name exp11-app exp11-student-portal:latest
# Visit: http://localhost:5050 or http://localhost:5050/api/students
docker rm -f exp11-app
```

---

## 🔒 Security & Credentials Statement
This repository strictly complies with academic security standards:
- No passwords, private tokens, API keys, or Docker Hub credentials are committed.
- All containers operate with minimal privilege and isolated bridge networking.
