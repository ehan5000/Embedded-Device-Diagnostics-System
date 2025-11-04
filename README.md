Working in progress will update.

# 📟 Embedded Device Diagnostics System

A lightweight **embedded diagnostics simulation** inspired by real-world hardware test systems used at Nokia and other embedded engineering environments.  
This project demonstrates live telemetry generation, visualization, and logging using **C++**, **Python (Flask)**, and **HTML/JavaScript** — all runnable locally with no external dependencies.

---

## 🧠 Overview

The system mimics how embedded devices send real-time diagnostic data (e.g., temperature, voltage, and fault status) over a serial or MQTT interface to a dashboard.  
It includes three core components:

| File | Description |
|------|--------------|
| `device_simulator.cpp` | Simulates a device streaming diagnostic logs (C++ terminal output). |
| `mqtt_dashboard.py` | Flask backend generating random telemetry and serving it via web routes. |
| `static_dashboard.html` | Real-time HTML log viewer that displays the latest telemetry updates from the backend. |

---

## 🧩 Features

- Real-time temperature and voltage telemetry  
- Randomized FAULT/OK states for simulated device testing  
- Auto-updating dashboard at `localhost:5000`  
- JSON API endpoint (`/data`) for external monitoring or log viewers  
- Standalone HTML visualizer with scrolling logs  

---

## ⚙️ Installation

### 1️⃣ Clone or Download
```bash

Install dependencies:
pip install -r requirements.txt

Run it: python mqtt_dashboard.py or run the device simulator: g++ device_simulator.cpp -o device_simulator
./device_simulator 

git clone https://github.com/ehan5000/Embedded-Diagnostics-System.git
cd Embedded-Diagnostics-System
