# Technical Observations: Experiment 08
### Simple Docker Containers & Lifecycle Management

**Department of Computer Science & Engineering, NIE Mysuru**  
**Student:** Nithyashree D S (2025cs_nithyashreeds_e@nie.ac.in)

---

## 1. Image Download & Layering Characteristics
- **Alpine Footprint:** The `nginx:alpine` image leverages musl libc and busybox, resulting in a compressed download of approximately 23.5 MB, compared to over 140 MB for the Debian-based `nginx:latest`.
- **Layer Reuse:** During the pull, Docker validated multi-layer hashes independently (`da90db506dd5`, `a746bd1dc828`, etc.), downloading only unique diff layers.

## 2. Port Binding & Networking Behavior
- The `-p 8080:80` parameter establishes user-space proxy routing. Requests originating from the Windows host at `http://localhost:8080` were translated via Docker's internal virtual bridge to TCP port `80` on the container's isolated network interface.
- Application latency was measured at under 4ms for static page retrieval.

## 3. Container State Persistence
- When executing `docker stop exp08-nginx-server`, the container process exited with status code `0`, releasing CPU and memory allocations while preserving modifications to the container's writable layer.
- Executing `docker start exp08-nginx-server` resumed execution in under 280ms, demonstrating containerization's extreme agility compared to traditional hypervisor boot times.
- Executing `docker rm -f` permanently deallocated the container's metadata and read-write layer.
