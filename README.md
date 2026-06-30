# 🛰️ DroneScan

### Real-Time AI Drone Analytics & Object Detection — Built from Scratch

*From core computer-vision theory to a production-grade, edge-deployable drone analytics platform*

[![Stars](https://img.shields.io/github/stars/your-org/DroneScan?style=for-the-badge&logo=github&color=FFD700)](https://github.com/your-org/DroneScan/stargazers)
[![Forks](https://img.shields.io/github/forks/your-org/DroneScan?style=for-the-badge&logo=github&color=blue)](https://github.com/your-org/DroneScan/network/members)
[![Issues](https://img.shields.io/github/issues/your-org/DroneScan?style=for-the-badge&logo=github&color=red)](https://github.com/your-org/DroneScan/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-orange?style=for-the-badge)](CONTRIBUTING.md)

[🌐 Website](https://www.dronescan.io/) · [📖 Docs](docs/) · [🐛 Report Bug](.github/ISSUE_TEMPLATE/bug_report.md) · [💡 Request Feature](.github/ISSUE_TEMPLATE/feature_request.md)

---

## 📌 Why DroneScan?

Drones generate enormous volumes of aerial video, but turning that raw footage into actionable intelligence — in real time, without a constant cloud connection — remains a hard, under-documented engineering problem.

**DroneScan** is an open, hands-on project and curriculum for building a real-time AI drone analytics pipeline from the ground up: object detection, multi-object tracking, restricted-zone alerting, and edge-AI deployment, all explained and implemented step by step.

This isn't just a product demo — it's a complete guide to *how* a system like this is built, so you can learn it, extend it, or deploy your own version.

### ✨ What Sets This Apart

| Feature | Description |
|---|---|
| 🔬 **First-principles approach** | Understand the computer-vision and systems concepts behind real-time detection, not just how to call a model |
| 🏗️ **Build the full pipeline** | Detection → tracking → zone logic → alerting → dashboard, implemented end to end |
| ⚡ **Edge-AI focused** | Deploy on-device with no cloud dependency; sub-120ms inference latency target |
| 🎯 **94%+ detection accuracy** | Benchmarked detection pipeline with documented evaluation methodology |
| 💻 **100% runnable code** | Every chapter has tested, working code in the `/code` folder |
| 🤝 **Community-driven** | Open contributions, issue templates, and a clear roadmap |

---

## 🚀 Quick Start

### Option 1 — Read Online

👉 **https://www.dronescan.io/** — product overview and live waitlist.

### Option 2 — Clone & Run Locally

```bash
# Clone the repository
git clone https://github.com/your-org/DroneScan.git
cd DroneScan

# Install Python dependencies
pip install -r code/requirements/requirements.txt

# Run the detection pipeline on a sample video
python code/detection/run_detection.py --source assets/sample_clip.mp4

# Run the live dashboard (requires the detection pipeline running)
python code/dashboard/app.py
```

### Option 3 — Try the Edge Build

```bash
cd code/edge-deployment
python build_edge_bundle.py --target jetson
```

---

## 📚 Curriculum Overview

The project is organized into **4 structured parts**, mirroring how the system is actually built.

```
DroneScan
├── Part 1: Foundations                     (Chapters 1–3)
├── Part 2: Building the Detection Pipeline (Chapters 4–7)
├── Part 3: Tracking, Alerts & the API      (Chapters 8–10)
└── Part 4: Edge Deployment & Production    (Chapters 11–12)
```

### 📖 Chapter Index

| # | Chapter | Topics | Status |
|---|---|---|---|
| 0 | [Preface](docs/Preface.md) | Project origin, goals, how to use this repo | ✅ |
| **Part 1** | **Foundations** | | |
| 1 | [Introduction to Drone Analytics](docs/chapter1/Chapter1-Introduction-to-Drone-Analytics.md) | Problem space, use cases, system overview | ✅ |
| 2 | [Computer Vision Fundamentals](docs/chapter2/Chapter2-Computer-Vision-Fundamentals.md) | CNNs, anchors, NMS, evaluation metrics | ✅ |
| 3 | [Aerial Imagery Challenges](docs/chapter3/Chapter3-Aerial-Imagery-Challenges.md) | Scale, motion blur, lighting, small-object detection | ✅ |
| **Part 2** | **Building the Detection Pipeline** | | |
| 4 | [Object Detection from Scratch](docs/chapter4/Chapter4-Object-Detection-From-Scratch.md) | Building and training the detector | ✅ |
| 5 | [Model Optimization](docs/chapter5/Chapter5-Model-Optimization.md) | Quantization, pruning, latency tuning | ✅ |
| 6 | [Real-Time Inference Pipeline](docs/chapter6/Chapter6-Real-Time-Inference-Pipeline.md) | Frame buffering, async inference, 24 FPS target | ✅ |
| 7 | [Evaluation & Benchmarking](docs/chapter7/Chapter7-Evaluation-and-Benchmarking.md) | Accuracy, latency, and the 94%/120ms benchmarks | ✅ |
| **Part 3** | **Tracking, Alerts & the API** | | |
| 8 | [Multi-Object Tracking](docs/chapter8/Chapter8-Multi-Object-Tracking.md) | Track IDs, trails, re-identification | ✅ |
| 9 | [Zones & Anomaly Alerts](docs/chapter9/Chapter9-Zones-and-Anomaly-Alerts.md) | Restricted-zone logic, alert rules, notifications | ✅ |
| 10 | [Enterprise API](docs/chapter10/Chapter10-Enterprise-API.md) | REST/WebSocket API design for integrations | ✅ |
| **Part 4** | **Edge Deployment & Production** | | |
| 11 | [Edge-AI Deployment](docs/chapter11/Chapter11-Edge-AI-Deployment.md) | On-device inference, no-cloud architecture | ✅ |
| 12 | [Production Hardening](docs/chapter12/Chapter12-Production-Hardening.md) | Monitoring, failover, security considerations | ✅ |

---

## 🗺️ Who Is This For?

| **🧑‍💻 ML Engineers**<br>Building real-time CV pipelines | **🚁 Drone/UAV Developers**<br>Adding intelligence to existing hardware | **🏗️ Backend Engineers**<br>Designing the alerting/API layer | **🎓 Students & Researchers**<br>Studying applied real-time CV systems |
|---|---|---|---|

**Prerequisites:** Python · Basic familiarity with computer vision or ML concepts

---

## 🤝 Contributing

We welcome every form of contribution — from fixing a typo to adding a whole chapter or module.

1. **Fork** this repository
2. **Create** your branch: `git checkout -b feat/your-contribution`
3. **Commit**: `git commit -m 'feat: add chapter on X'`
4. **Push**: `git push origin feat/your-contribution`
5. **Open a Pull Request**

📋 Read the full [**Contributing Guide →**](CONTRIBUTING.md)

| Type | How |
|---|---|
| 🐛 Found a bug | [Open an Issue](.github/ISSUE_TEMPLATE/bug_report.md) |
| 💡 Feature idea | [Open a Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) |
| 📝 Improve content | Submit a Pull Request |
| 🌍 Translate | Open an issue to coordinate |

---

## 📜 Citation

```
@misc{dronescan2026,
  title  = {DroneScan: Real-Time AI Drone Analytics, Built from Scratch},
  author = {DroneScan Contributors},
  year   = {2026},
  url    = {https://github.com/your-org/DroneScan},
  note   = {GitHub repository}
}
```

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

**⭐ If DroneScan helps you, please star the repo — it helps others find it!**

Made with 🛰️ · [Website](https://www.dronescan.io/) · [Issues](.github/ISSUE_TEMPLATE) · [Discussions](https://github.com/your-org/DroneScan/discussions)
