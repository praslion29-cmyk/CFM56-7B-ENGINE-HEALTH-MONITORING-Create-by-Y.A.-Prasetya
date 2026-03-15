# CFM56-7B-ENGINE-HEALTH-MONITORING-Create-by-Y.A.-Prasetya
# CFM56-7B Engine Health Monitoring Dashboard  
**Created by Y.A. Prasetya**

## Overview
This project is a **Python Streamlit dashboard** for monitoring **CFM56-7B engine parameters**.  
It simulates an **Engine Health Monitoring system** similar to modern airline maintenance platforms, providing **real-time status, trend graphs, and maintenance recommendations**.

The dashboard is designed for:
- Aircraft Maintenance Engineers
- Reliability Engineers
- Aviation Data Analysts
- MRO Technical Development

---

## Features

### 1. Aircraft Information Input
- Date
- Aircraft Registration
- Engine Number
- Route

### 2. Engine Start Monitoring
- **EGT Start** monitoring  
- **Hot Start Detection**: EGT Start > 725°C triggers warning  
- Shows **possible cause** and **maintenance recommendation**

### 3. Takeoff Parameter Monitoring

Monitored engine parameters with **limits**:

| Parameter     | Max Limit | Status Logic (Normal / CAUTION / WARNING) |
|---------------|-----------|------------------------------------------|
| N1            | 102 %     | CAUTION = ≥ 95% limit                     |
| N2            | 105 %     | CAUTION = ≥ 95% limit                     |
| Oil Pressure  | 60 psi    | CAUTION = ≥ 95% limit                     |
| Oil Temp      | 150 °C    | CAUTION = ≥ 95% limit                     |
| Fuel Flow     | 5200 pph  | CAUTION = ≥ 95% limit                     |
| EGT Takeoff   | 950 °C    | CAUTION = ≥ 95% limit                     |
| Vibration     | 4 ips     | CAUTION = ≥ 95% limit                     |

- Status colors:
  - **Normal** = Green  
  - **CAUTION** = Orange (≥ 95% limit)  
  - **WARNING** = Red (> limit)  
- **Automatic maintenance advice** is shown when status is CAUTION or WARNING.

### 4. Fleet Monitoring
- Supports **multiple aircraft entries**  
- Displays **fleet table** with all recorded engine parameters

### 5. Engine Trend Monitoring
- Small trend charts for:
  - **EGT Takeoff**
  - **Fuel Flow**
  - **Vibration**
- Visualizes performance trends over multiple flights

### 6. Data Export
- **Save Data** → exports fleet data to `engine_monitoring.csv`  
- **PRINT REPORT** → use browser print functionality

---

## Technologies Used
- **Python 3.x**  
- **Streamlit** – interactive web dashboard  
- **Pandas** – data storage and processing  
- **Matplotlib** – parameter trend visualization  

---

## Installation

Install required libraries:

```bash
pip install -r requirements.txt
