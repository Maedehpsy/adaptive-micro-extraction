# 🚀 Adaptive Micro-Extraction

Self-healing architecture for automatic microservice migration with auto-rollback.

## 🎯 Problem

| Challenge | Impact |
|-----------|--------|
| Migration is risky | Downtime, data loss |
| Manual rollback is slow | Hours to recover |
| No safety net | Fear of change |

## ✅ Solution

**Watch → Decide → Act → Verify → Rollback (if needed)**


## 🛠️ Architecture Components

| Component | File | Responsibility |
|-----------|------|----------------|
| **Watcher** | `watcher.py` | Collect CPU, memory, response time |
| **Decider** | `decider.py` | Decide if migration needed |
| **Actuator** | `actuator.py` | Execute migration |
| **Rollback** | `rollback.py` | Restore if failed |

## 🏗️ Tech Stack

- **Python** - Core language
- **Docker** - Containerization
- **Kubernetes** - Orchestration (planned)
- **Prometheus** - Monitoring (planned)

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/Maedehpsy/adaptive-micro-extraction.git

# Run
docker-compose up

# Test
python src/main.py
