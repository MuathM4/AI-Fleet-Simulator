# AI-Fleet-Simulator

An advanced, real-time vehicle telemetry data logger designed to build ground-truth datasets for AI-driven fleet management and driver behavior analysis.

## 🚀 Overview
This repository contains the data collection pipeline that extracts high-fidelity physics and driving metrics from Euro Truck Simulator 2 (ETS2). The captured data simulates industrial IoT telematics units (like an MPU6050 accelerometer/gyroscope setup) to log speed, orientation, advanced vehicle dynamics, and automated driving event labels.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Format:** CSV (Ground Truth Dataset)
- **API Integration:** ETS2 Telemetry Server

## 📊 Telemetry Features & Features Logged
- **Advanced Vehicle Dynamics:** Steering angle, multi-axis G-forces (`Accel_X`, `Accel_Y`, `Accel_Z`).
- **Contextual Driving Data:** Speed vs. Speed Limit, RPM, Gear, Throttle, and Brake inputs.
- **Fleet Analytics:** Fuel consumption percentage, vehicle component wear (Engine, Tires, Chassis).
- **Automated Labeling:** Real-time driving status classification including `Normal`, `Speeding`, `Hard Braking`, and `Harsh Cornering` (calculated using physical lateral G-forces).

## 📂 Project Structure
- `telemetry_logger.py`: The core Python script capturing and filtering live telemetry.
- `.gitignore`: Configured to exclude heavy dataset CSV files from version control.
