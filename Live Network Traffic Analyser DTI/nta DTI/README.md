# Network Traffic Analyzer

A Python-based **Network Traffic Monitoring and Analysis Tool** that captures packets in real time, stores traffic data, analyzes network behavior, and visualizes statistics through a live dashboard.

This project demonstrates basic **network monitoring, traffic analysis, and anomaly detection** using Python.

---

# Features

* Real-time packet capturing using **Scapy**
* Traffic logging into a **CSV dataset**
* Detection of **suspicious traffic patterns**
* **Protocol usage analysis**
* Identification of **top source IP addresses**
* **Live monitoring dashboard** built with Streamlit
* Graphical visualization of network traffic trends

---
# Project Structure

```
network-traffic-analyzer
│
├── packet_capture.py      # Captures network packets using Scapy
├── analyzer.py            # Analyzes captured traffic data
├── dashboard.py           # Real-time monitoring dashboard
├── traffic_data.csv       # Packet dataset (generated automatically)
└── README.md
```

---
# Technologies Used

* Python
* Scapy
* Pandas
* Streamlit
* Matplotlib
* CSV Logging

---
# Installation

## 1. Clone the Repository

```
git clone https://github.com/yourusername/network-traffic-analyzer.git
cd network-traffic-analyzer
```

## 2. Install Required Dependencies

```
pip install scapy pandas streamlit matplotlib
```

---

# Usage

## Step 1 — Start Packet Capture

Run the packet capture script to start collecting network traffic.

```
sudo python packet_capture.py
```

Captured packets will be stored in:

```
traffic_data.csv
```

---

## Step 2 — Analyze Traffic Data

Run the analyzer script to detect suspicious activity and summarize traffic.

```
python analyzer.py
```

This will display:

* Top source IP addresses
* Protocol usage statistics
* Suspicious traffic alerts

---

## Step 3 — Launch Live Monitoring Dashboard

Start the Streamlit dashboard:

```
streamlit run dashboard.py
```

The dashboard will open automatically in your browser.

---

# Dashboard Features

The dashboard provides:

🟢 **Network Status Indicator**

📈 **Live Traffic Graph**

📊 **Protocol Distribution Pie Chart**

🌐 **Top Source IP Table**

🚨 **Suspicious Traffic Alerts**

---

# Suspicious Traffic Detection

The analyzer flags IP addresses that generate an unusually high number of packets.

Example alert:

```
⚠ ALERT: Suspicious traffic detected from 192.168.1.10 (75 packets)
```

This can help identify:

* Potential **DDoS attacks**
* Network flooding
* Abnormal traffic sources

---
# Requirements

Python **3.8+**

Libraries used:

* scapy
* pandas
* streamlit
* matplotlib

Install them using:

```
pip install scapy pandas streamlit matplotlib
```

---

# Security Note

Packet capturing requires **root/administrator privileges**.

Run packet capture using:

```
sudo python packet_capture.py
```

---






