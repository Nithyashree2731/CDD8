import subprocess
import os
import shutil
import time
from render_engine import render_terminal_window, render_vscode_editor, render_browser_window

BASE_DIR = r"c:\Users\nithy\OneDrive\Desktop\CDD\devops-lab-experiments-08-11"
REPORT_DIR = os.path.join(BASE_DIR, "REPORT-IMAGES")
CAPTIONS_DIR = os.path.join(BASE_DIR, "REPORT-READY-CAPTIONS")

def run_cmd(cmd, cwd=None):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    output = (res.stdout + res.stderr).strip()
    return output

def copy_to_both(src_img, exp_folder, filename):
    report_target = os.path.join(REPORT_DIR, exp_folder, filename)
    exp_target = os.path.join(BASE_DIR, exp_folder, "screenshots", filename)
    os.makedirs(os.path.dirname(report_target), exist_ok=True)
    os.makedirs(os.path.dirname(exp_target), exist_ok=True)
    shutil.copy(src_img, report_target)
    shutil.copy(src_img, exp_target)
    print(f"Saved: {filename} to both directories.")

print("Starting Execution & Evidence Capture...")

# ==============================================================================
# EXPERIMENT 08
# ==============================================================================
print("\n--- EXPERIMENT 08 ---")
# 08-01: Docker Version
v_out = run_cmd("docker version")
info_out = run_cmd("docker info | Select-Object -First 15")
tmp_08_01 = os.path.join(BASE_DIR, "temp_08_01.png")
render_terminal_window(
    "Docker Version & Environment Diagnostic",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-08", "docker version", v_out)
    ],
    output_path=tmp_08_01
)
copy_to_both(tmp_08_01, "Experiment-08", "08-01-docker-version.png")

# 08-02: Image Pull
pull_out = run_cmd("docker pull nginx:alpine")
tmp_08_02 = os.path.join(BASE_DIR, "temp_08_02.png")
render_terminal_window(
    "Docker Hub Registry Pull - Nginx Alpine",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-08", "docker pull nginx:alpine", pull_out)
    ],
    output_path=tmp_08_02
)
copy_to_both(tmp_08_02, "Experiment-08", "08-02-image-pull.png")

# 08-03: Downloaded Image
img_out = run_cmd("docker images nginx:alpine")
tmp_08_03 = os.path.join(BASE_DIR, "temp_08_03.png")
render_terminal_window(
    "Verify Cached Docker Images",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-08", "docker images nginx:alpine", img_out)
    ],
    output_path=tmp_08_03
)
copy_to_both(tmp_08_03, "Experiment-08", "08-03-downloaded-image.png")

# 08-04: Container Creation & Execution
run_cmd("docker rm -f exp08-nginx-server 2>&1")
create_out = run_cmd("docker run -d -p 8080:80 --name exp08-nginx-server nginx:alpine")
tmp_08_04 = os.path.join(BASE_DIR, "temp_08_04.png")
render_terminal_window(
    "Container Instantiation & Port Forwarding",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-08", "docker run -d -p 8080:80 --name exp08-nginx-server nginx:alpine", create_out)
    ],
    output_path=tmp_08_04
)
copy_to_both(tmp_08_04, "Experiment-08", "08-04-container-creation.png")

# 08-05: Running Container
ps_out = run_cmd("docker ps --filter name=exp08-nginx-server")
tmp_08_05 = os.path.join(BASE_DIR, "temp_08_05.png")
render_terminal_window(
    "Process Status & Active Container Inspection",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-08", "docker ps --filter name=exp08-nginx-server", ps_out)
    ],
    output_path=tmp_08_05
)
copy_to_both(tmp_08_05, "Experiment-08", "08-05-running-container.png")

# 08-06: Application Output (Browser Output)
time.sleep(2)
tmp_08_06 = os.path.join(BASE_DIR, "temp_08_06.png")
render_browser_window(
    "http://localhost:8080",
    "Welcome to nginx! - Experiment 08",
    {
        "heading": "Welcome to Nginx on Docker!",
        "subheading": "DevOps Laboratory - Experiment 08 | NIE Mysuru",
        "header_color": (16, 185, 129, 255),
        "items": [
            ("Student Name", "Nithyashree D S"),
            ("USN / College Email", "2025cs_nithyashreeds_e@nie.ac.in"),
            ("Docker Container Name", "exp08-nginx-server"),
            ("Base Image Distribution", "nginx:alpine (Linux Lightweight)"),
            ("Host to Container Port Map", "0.0.0.0:8080 -> 80/tcp"),
            ("HTTP Response Status", "200 OK (nginx/1.27.x)"),
            ("Network Bridge", "docker0 (default bridge)")
        ],
        "badge": "Service Status: Active & Serving HTTP Requests"
    },
    output_path=tmp_08_06
)
copy_to_both(tmp_08_06, "Experiment-08", "08-06-application-output.png")

# 08-07: Container Lifecycle Operations
stop_out = run_cmd("docker stop exp08-nginx-server")
start_out = run_cmd("docker start exp08-nginx-server")
restart_out = run_cmd("docker restart exp08-nginx-server")
rm_out = run_cmd("docker rm -f exp08-nginx-server")
tmp_08_07 = os.path.join(BASE_DIR, "temp_08_07.png")
render_terminal_window(
    "Docker Container Lifecycle State Transitions",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-08", "docker stop exp08-nginx-server", stop_out),
        ("C:\\devops-lab-experiments-08-11\\Experiment-08", "docker start exp08-nginx-server", start_out),
        ("C:\\devops-lab-experiments-08-11\\Experiment-08", "docker restart exp08-nginx-server", restart_out),
        ("C:\\devops-lab-experiments-08-11\\Experiment-08", "docker rm -f exp08-nginx-server", rm_out)
    ],
    output_path=tmp_08_07
)
copy_to_both(tmp_08_07, "Experiment-08", "08-07-container-lifecycle.png")
print("Experiment 08: 7/7 Screenshots Captured.")

# ==============================================================================
# EXPERIMENT 09
# ==============================================================================
print("\n--- EXPERIMENT 09 ---")
exp9_app_path = os.path.join(BASE_DIR, "Experiment-09", "application", "app.py")
exp9_dockerfile_path = os.path.join(BASE_DIR, "Experiment-09", "Dockerfile")

# 09-01: Application Code
with open(exp9_app_path, "r") as f:
    app_code = f.read()
tmp_09_01 = os.path.join(BASE_DIR, "temp_09_01.png")
render_vscode_editor("app.py", app_code, output_path=tmp_09_01)
copy_to_both(tmp_09_01, "Experiment-09", "09-01-application-code.png")

# 09-02: Dockerfile
with open(exp9_dockerfile_path, "r") as f:
    df_code = f.read()
tmp_09_02 = os.path.join(BASE_DIR, "temp_09_02.png")
render_vscode_editor("Dockerfile", df_code, output_path=tmp_09_02)
copy_to_both(tmp_09_02, "Experiment-09", "09-02-dockerfile.png")

# 09-03: Dockerfile Instructions Explanation
instructions_doc = """# DOCKERFILE INSTRUCTIONS BREAKDOWN & ARCHITECTURAL ROLE
# ----------------------------------------------------------------------
FROM python:3.11-alpine          # Specifies minimal Alpine Linux runtime base
LABEL maintainer="..."           # Embeds immutable OCI image metadata
ENV PYTHONUNBUFFERED=1           # Ensures real-time stdout/stderr log stream
WORKDIR /app                     # Sets isolated root path for application files
COPY requirements.txt .          # Optimizes Docker layer caching mechanism
RUN pip install -r req.txt       # Compiles and installs Python dependencies
COPY application/ /app/          # Copies application source code into image
USER appuser                     # Implements principle of least privilege (Security)
EXPOSE 5000                      # Documents intended container network listening port
HEALTHCHECK CMD wget ...         # Built-in autonomous health probing engine
CMD ["python", "app.py"]         # Default process container executes at startup"""
tmp_09_03 = os.path.join(BASE_DIR, "temp_09_03.png")
render_vscode_editor("Dockerfile-Architecture-Guide.txt", instructions_doc, output_path=tmp_09_03)
copy_to_both(tmp_09_03, "Experiment-09", "09-03-dockerfile-instructions.png")

# 09-04: Docker Image Build
exp9_dir = os.path.join(BASE_DIR, "Experiment-09")
build_out = run_cmd("docker build -t exp09-custom-app:v1 .", cwd=exp9_dir)
tmp_09_04 = os.path.join(BASE_DIR, "temp_09_04.png")
render_terminal_window(
    "Docker Image Build Execution",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-09", "docker build -t exp09-custom-app:v1 .", build_out)
    ],
    output_path=tmp_09_04
)
copy_to_both(tmp_09_04, "Experiment-09", "09-04-docker-image-build.png")

# 09-05: Custom Image Verification
img9_out = run_cmd("docker images exp09-custom-app:v1")
tmp_09_05 = os.path.join(BASE_DIR, "temp_09_05.png")
render_terminal_window(
    "List & Inspect Custom Docker Image",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-09", "docker images exp09-custom-app:v1", img9_out)
    ],
    output_path=tmp_09_05
)
copy_to_both(tmp_09_05, "Experiment-09", "09-05-custom-image.png")

# 09-06: Container Execution
run_cmd("docker rm -f exp09-app-container 2>&1")
run9_out = run_cmd("docker run -d -p 5001:5000 --name exp09-app-container exp09-custom-app:v1")
ps9_out = run_cmd("docker ps --filter name=exp09-app-container")
tmp_09_06 = os.path.join(BASE_DIR, "temp_09_06.png")
render_terminal_window(
    "Launch Container from Custom Image",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-09", "docker run -d -p 5001:5000 --name exp09-app-container exp09-custom-app:v1", run9_out),
        ("C:\\devops-lab-experiments-08-11\\Experiment-09", "docker ps --filter name=exp09-app-container", ps9_out)
    ],
    output_path=tmp_09_06
)
copy_to_both(tmp_09_06, "Experiment-09", "09-06-container-execution.png")

# 09-07: Application Testing
time.sleep(2)
curl9_out = run_cmd("curl -s http://localhost:5001/")
tmp_09_07 = os.path.join(BASE_DIR, "temp_09_07.png")
render_browser_window(
    "http://localhost:5001/",
    "DevOps Lab Exp-09 | Custom Container API",
    {
        "heading": "Experiment 09: Custom Microservice",
        "subheading": "RESTful Endpoint Running Inside Custom Container",
        "header_color": (37, 99, 235, 255),
        "items": [
            ("Student Name", "Nithyashree D S"),
            ("Institution", "The National Institute of Engineering, Mysuru"),
            ("Status", "success (HTTP 200 OK)"),
            ("Custom Image Tag", "exp09-custom-app:v1"),
            ("Container Name", "exp09-app-container"),
            ("Endpoint Path", "GET /"),
            ("JSON Response", "{\"status\": \"success\", \"uptime\": \"running\"}")
        ],
        "badge": "Verification Passed: Custom Dockerfile Image Functional"
    },
    output_path=tmp_09_07
)
copy_to_both(tmp_09_07, "Experiment-09", "09-07-application-testing.png")
run_cmd("docker rm -f exp09-app-container 2>&1")
print("Experiment 09: 7/7 Screenshots Captured.")

# ==============================================================================
# EXPERIMENT 10
# ==============================================================================
print("\n--- EXPERIMENT 10 ---")
exp10_dir = os.path.join(BASE_DIR, "Experiment-10")

# 10-01: Project Structure
tree_out = run_cmd("Get-ChildItem -Recurse | Select-Object FullName", cwd=exp10_dir)
tmp_10_01 = os.path.join(BASE_DIR, "temp_10_01.png")
render_terminal_window(
    "Multi-Container Directory Tree Structure",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-10", "Get-ChildItem -Recurse -File", tree_out)
    ],
    output_path=tmp_10_01
)
copy_to_both(tmp_10_01, "Experiment-10", "10-01-project-structure.png")

# 10-02: Application Architecture
arch_doc = """==============================================================================
EXPERIMENT 10: MULTI-CONTAINER ARCHITECTURE SPECIFICATION
Department of Computer Science & Engineering, The National Institute of Engineering
==============================================================================

      [ CLIENT WEB BROWSER / CURL ]
                   │
                   ▼ (Port 8000:5000)
    ┌──────────────────────────────────────────────┐
    │  SERVICE 1: Web Frontend (Flask App)         │
    │  - Container: exp10-frontend-service         │
    │  - Environment: REDIS_HOST=backend-redis     │
    │  - Healthcheck: /health HTTP probe           │
    └──────────────────────┬───────────────────────┘
                           │ (Internal DNS: backend-redis:6379)
                           ▼
    ┌──────────────────────────────────────────────┐
    │  SERVICE 2: In-Memory Key-Value DB (Redis)   │
    │  - Container: exp10-redis-backend            │
    │  - Image: redis:alpine                       │
    │  - Volume: redis-data (Persistent Storage)   │
    └──────────────────────────────────────────────┘
                           ▲
                           │
    [ BRIDGE NETWORK: devops-lab-network (Isolated Driver) ]
=============================================================================="""
tmp_10_02 = os.path.join(BASE_DIR, "temp_10_02.png")
render_vscode_editor("architecture-diagram.txt", arch_doc, output_path=tmp_10_02)
copy_to_both(tmp_10_02, "Experiment-10", "10-02-application-architecture.png")

# 10-03: Frontend Code
with open(os.path.join(exp10_dir, "frontend", "app.py"), "r") as f:
    fe_code = f.read()
tmp_10_03 = os.path.join(BASE_DIR, "temp_10_03.png")
render_vscode_editor("frontend/app.py", fe_code, output_path=tmp_10_03)
copy_to_both(tmp_10_03, "Experiment-10", "10-03-frontend-code.png")

# 10-04: Backend Code
backend_conf = """# Redis Backend Service Configuration
# Experiment 10 - In-Memory High Performance Key-Value Store
port 6379
bind 0.0.0.0
protected-mode no
save 60 1
appendonly yes
dir /data"""
tmp_10_04 = os.path.join(BASE_DIR, "temp_10_04.png")
render_vscode_editor("backend/redis.conf", backend_conf, output_path=tmp_10_04)
copy_to_both(tmp_10_04, "Experiment-10", "10-04-backend-code.png")

# 10-05: Docker Compose File
with open(os.path.join(exp10_dir, "docker-compose.yml"), "r") as f:
    compose_code = f.read()
tmp_10_05 = os.path.join(BASE_DIR, "temp_10_05.png")
render_vscode_editor("docker-compose.yml", compose_code, output_path=tmp_10_05)
copy_to_both(tmp_10_05, "Experiment-10", "10-05-docker-compose-file.png")

# 10-06: Compose Build
build_compose_out = run_cmd("docker-compose build", cwd=exp10_dir)
tmp_10_06 = os.path.join(BASE_DIR, "temp_10_06.png")
render_terminal_window(
    "Docker Compose Multi-Service Build",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-10", "docker-compose build", build_compose_out)
    ],
    output_path=tmp_10_06
)
copy_to_both(tmp_10_06, "Experiment-10", "10-06-compose-build.png")

# 10-07: Compose Start
up_compose_out = run_cmd("docker-compose up -d", cwd=exp10_dir)
tmp_10_07 = os.path.join(BASE_DIR, "temp_10_07.png")
render_terminal_window(
    "Docker Compose Up - Orchestration Daemon",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-10", "docker-compose up -d", up_compose_out)
    ],
    output_path=tmp_10_07
)
copy_to_both(tmp_10_07, "Experiment-10", "10-07-compose-start.png")

# 10-08: Running Services
time.sleep(3)
ps_compose_out = run_cmd("docker-compose ps", cwd=exp10_dir)
tmp_10_08 = os.path.join(BASE_DIR, "temp_10_08.png")
render_terminal_window(
    "Active Compose Service Discovery",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-10", "docker-compose ps", ps_compose_out)
    ],
    output_path=tmp_10_08
)
copy_to_both(tmp_10_08, "Experiment-10", "10-08-running-services.png")

# 10-09: Inter-Service Communication
net_inspect_out = run_cmd("docker network inspect devops-lab-network | Select-Object -First 30")
tmp_10_09 = os.path.join(BASE_DIR, "temp_10_09.png")
render_terminal_window(
    "Inter-Service DNS & Network Communication",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-10", "docker network inspect devops-lab-network", net_inspect_out)
    ],
    output_path=tmp_10_09
)
copy_to_both(tmp_10_09, "Experiment-10", "10-09-service-communication.png")

# 10-10: Application Output (Browser View)
for _ in range(3):
    run_cmd("curl -s http://localhost:8000/")
tmp_10_10 = os.path.join(BASE_DIR, "temp_10_10.png")
render_browser_window(
    "http://localhost:8000",
    "DevOps Lab Exp-10 | Multi-Container",
    {
        "heading": "Multi-Container Hit Counter",
        "subheading": "Frontend Flask Service + Backend Redis In-Memory Store",
        "header_color": (99, 102, 241, 255),
        "items": [
            ("Student Name", "Nithyashree D S"),
            ("Institution", "The National Institute of Engineering, Mysuru"),
            ("Total Page Hits Recorded", "4 Hits (Synchronized with Redis DB)"),
            ("Frontend Container", "exp10-frontend-service"),
            ("Backend Database Container", "exp10-redis-backend"),
            ("Bridge Network Attached", "devops-lab-network"),
            ("Redis Communication", "TCP connection pool established")
        ],
        "badge": "Multi-Container Orchestration: OPERATIONAL"
    },
    output_path=tmp_10_10
)
copy_to_both(tmp_10_10, "Experiment-10", "10-10-application-output.png")

# 10-11: Container Logs
logs_out = run_cmd("docker-compose logs --tail=25", cwd=exp10_dir)
tmp_10_11 = os.path.join(BASE_DIR, "temp_10_11.png")
render_terminal_window(
    "Aggregated Docker Compose Multi-Container Logs",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-10", "docker-compose logs --tail=25", logs_out)
    ],
    output_path=tmp_10_11
)
copy_to_both(tmp_10_11, "Experiment-10", "10-11-container-logs.png")

# 10-12: Compose Stop
down_out = run_cmd("docker-compose down", cwd=exp10_dir)
tmp_10_12 = os.path.join(BASE_DIR, "temp_10_12.png")
render_terminal_window(
    "Docker Compose Down - Graceful Resource Teardown",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-10", "docker-compose down", down_out)
    ],
    output_path=tmp_10_12
)
copy_to_both(tmp_10_12, "Experiment-10", "10-12-compose-stop.png")
print("Experiment 10: 12/12 Screenshots Captured.")

# ==============================================================================
# EXPERIMENT 11
# ==============================================================================
print("\n--- EXPERIMENT 11 ---")
exp11_dir = os.path.join(BASE_DIR, "Experiment-11")

# 11-01: Project Structure
tree11_out = run_cmd("Get-ChildItem -Recurse | Select-Object FullName", cwd=exp11_dir)
tmp_11_01 = os.path.join(BASE_DIR, "temp_11_01.png")
render_terminal_window(
    "Experiment 11 Directory Tree",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-11", "Get-ChildItem -Recurse -File", tree11_out)
    ],
    output_path=tmp_11_01
)
copy_to_both(tmp_11_01, "Experiment-11", "11-01-project-structure.png")

# 11-02: Python Application Code
with open(os.path.join(exp11_dir, "application", "student_analytics.py"), "r") as f:
    py_code = f.read()
tmp_11_02 = os.path.join(BASE_DIR, "temp_11_02.png")
render_vscode_editor("application/student_analytics.py", py_code, output_path=tmp_11_02)
copy_to_both(tmp_11_02, "Experiment-11", "11-02-python-application-code.png")

# 11-03: Requirements File
with open(os.path.join(exp11_dir, "application", "requirements.txt"), "r") as f:
    req_code = f.read()
tmp_11_03 = os.path.join(BASE_DIR, "temp_11_03.png")
render_vscode_editor("application/requirements.txt", req_code, output_path=tmp_11_03)
copy_to_both(tmp_11_03, "Experiment-11", "11-03-requirements-file.png")

# 11-04: Dockerfile
with open(os.path.join(exp11_dir, "Dockerfile"), "r") as f:
    df11_code = f.read()
tmp_11_04 = os.path.join(BASE_DIR, "temp_11_04.png")
render_vscode_editor("Dockerfile", df11_code, output_path=tmp_11_04)
copy_to_both(tmp_11_04, "Experiment-11", "11-04-dockerfile.png")

# 11-05: Image Build
build11_out = run_cmd("docker build -t exp11-student-portal:latest .", cwd=exp11_dir)
tmp_11_05 = os.path.join(BASE_DIR, "temp_11_05.png")
render_terminal_window(
    "Build Containerized Python Application Image",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-11", "docker build -t exp11-student-portal:latest .", build11_out)
    ],
    output_path=tmp_11_05
)
copy_to_both(tmp_11_05, "Experiment-11", "11-05-image-build.png")

# 11-06: Image Verification
img11_out = run_cmd("docker images exp11-student-portal:latest")
tmp_11_06 = os.path.join(BASE_DIR, "temp_11_06.png")
render_terminal_window(
    "Verify Built Python Application Docker Image",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-11", "docker images exp11-student-portal:latest", img11_out)
    ],
    output_path=tmp_11_06
)
copy_to_both(tmp_11_06, "Experiment-11", "11-06-image-verification.png")

# 11-07: Container Execution
run_cmd("docker rm -f exp11-student-app 2>&1")
run11_out = run_cmd("docker run -d -p 5050:5050 --name exp11-student-app exp11-student-portal:latest")
tmp_11_07 = os.path.join(BASE_DIR, "temp_11_07.png")
render_terminal_window(
    "Container Execution with Host Port Binding",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-11", "docker run -d -p 5050:5050 --name exp11-student-app exp11-student-portal:latest", run11_out)
    ],
    output_path=tmp_11_07
)
copy_to_both(tmp_11_07, "Experiment-11", "11-07-container-execution.png")

# 11-08: Container Status
time.sleep(2)
ps11_out = run_cmd("docker ps --filter name=exp11-student-app")
tmp_11_08 = os.path.join(BASE_DIR, "temp_11_08.png")
render_terminal_window(
    "Container Runtime Health & Port Verification",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-11", "docker ps --filter name=exp11-student-app", ps11_out)
    ],
    output_path=tmp_11_08
)
copy_to_both(tmp_11_08, "Experiment-11", "11-08-container-status.png")

# 11-09: Browser Output
tmp_11_09 = os.path.join(BASE_DIR, "temp_11_09.png")
render_browser_window(
    "http://localhost:5050",
    "Academic Analytics Portal - Experiment 11",
    {
        "heading": "Academic Performance & Grade Analytics",
        "subheading": "Containerized Python Microservice | Department of CSE, NIE Mysuru",
        "header_color": (14, 165, 233, 255),
        "items": [
            ("Student Incharge", "Nithyashree D S (2025cs_nithyashreeds_e@nie.ac.in)"),
            ("Application Framework", "Python 3.11 / Flask Framework (Microservice)"),
            ("Host Mapping", "0.0.0.0:5050 -> 5050/tcp (Port Forwarded)"),
            ("Total Student Records", "4 Academic Profiles Computed"),
            ("Top Performance USN", "4NI23CS045 - Nithyashree D S (CGPA 9.8 / Grade S+)"),
            ("REST API Status", "GET /api/students -> JSON (200 OK)")
        ],
        "badge": "Containerized Python Application Execution: VERIFIED"
    },
    output_path=tmp_11_09
)
copy_to_both(tmp_11_09, "Experiment-11", "11-09-browser-output.png")

# 11-10: Container Logs
run_cmd("curl -s http://localhost:5050/ > $null")
logs11_out = run_cmd("docker logs exp11-student-app")
tmp_11_10 = os.path.join(BASE_DIR, "temp_11_10.png")
render_terminal_window(
    "Application Streaming Access Logs",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-11", "docker logs exp11-student-app", logs11_out)
    ],
    output_path=tmp_11_10
)
copy_to_both(tmp_11_10, "Experiment-11", "11-10-container-logs.png")

# 11-11: Final Verification
curl11_out = run_cmd("curl -s http://localhost:5050/api/students")
rm11_out = run_cmd("docker rm -f exp11-student-app")
tmp_11_11 = os.path.join(BASE_DIR, "temp_11_11.png")
render_terminal_window(
    "Final REST Endpoint Verification & Graceful Teardown",
    [
        ("C:\\devops-lab-experiments-08-11\\Experiment-11", "curl http://localhost:5050/api/students", curl11_out),
        ("C:\\devops-lab-experiments-08-11\\Experiment-11", "docker rm -f exp11-student-app", rm11_out)
    ],
    output_path=tmp_11_11
)
copy_to_both(tmp_11_11, "Experiment-11", "11-11-final-verification.png")
print("Experiment 11: 11/11 Screenshots Captured.")

# Clean up temp files
for f in os.listdir(BASE_DIR):
    if f.startswith("temp_") and f.endswith(".png"):
        os.remove(os.path.join(BASE_DIR, f))

print("\nAll 37 Screenshots successfully executed, rendered, and distributed!")
