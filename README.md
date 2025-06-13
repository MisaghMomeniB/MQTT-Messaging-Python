# 📡 MQTT Messaging (Python)

A lightweight and configurable **MQTT pub/sub messaging tool** in Python. Built using the popular **Paho MQTT client**, it’s designed for rapid prototyping of IoT messaging, automation workflows, or testing pub/sub systems.

---

## 📋 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Usage Examples](#usage-examples)  
6. [Code Structure](#code-structure)  
7. [Security & Tips](#security--tips)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## 💡 Overview

This project wraps basic MQTT functionality—**connecting**, **publishing**, and **subscribing**—into a reusable Python tool. Leveraging the **Paho MQTT client**, it supports features essential for IoT messaging such as QoS control, TLS settings, and auto-reconnect logic :contentReference[oaicite:1]{index=1}.

---

## ✅ Features

- 🔌 Connect to MQTT brokers using TCP or WebSocket  
- 📢 Publish messages with customizable **QoS** and optional retain flag  
- 📩 Subscribe to topics with callback handling  
- 🔁 Auto-reconnect for improved reliability  
- 🌐 TLS/SSL support & optional username/password authentication :contentReference[oaicite:2]{index=2}  
- 📄 Simple CLI interface or importable module

---

## 🛠️ Prerequisites

- Python **3.7+**  
- MQTT broker access (e.g., Mosquitto, EMQX, HiveMQ, or cloud broker)  
- Required package:

```bash
pip install paho-mqtt
````

---

## ⚙️ Installation

```bash
git clone https://github.com/MisaghMomeniB/MQTT-Messaging-Python.git
cd MQTT-Messaging-Python
pip install -r requirements.txt  # or 'pip install paho-mqtt'
```

---

## 🚀 Usage Examples

### 🔗 Connect & Subscribe

```python
from mqtt_messaging import MQTTPublisher, MQTTSubscriber

# Subscribe example
sub = MQTTSubscriber(broker='broker.emqx.io', topic='my/topic', port=1883)
sub.connect()
sub.subscribe()
sub.loop_forever()  # listens indefinitely
```

### 📤 Publish Messages

```python
pub = MQTTPublisher(broker='broker.emqx.io', port=1883, qos=1, retain=True)
pub.connect()
pub.publish('my/topic', 'Hello MQTT! 😊')
pub.disconnect()
```

### 📦 CLI Example

```bash
python mqtt_tool.py --mode pub --topic my/topic --message "testing 123" --qos 1
python mqtt_tool.py --mode sub --topic my/topic --broker demo.mosquitto.org
```

---

## 📁 Code Structure

```
MQTT-Messaging-Python/
├── mqtt_tool.py          # CLI wrapper
├── mqtt_messaging.py     # Core publish & subscribe classes
├── requirements.txt      # Dependencies
└── README.md             # This file
```

* `MQTTPublisher`: MQTT client for publishing
* `MQTTSubscriber`: MQTT client for subscribing with callback support
* CLI script parses basic flags and invokes classes

---

## 🔒 Security & Tips

* ⚙️ Use `client.tls_set(...)` and `username_pw_set()` for secure, authenticated connections ([github.com][1], [emqx.com][2], [hivemq.com][3])
* Auto-reconnect ensures resilience in unstable networks ([emqx.com][2])
* Set **QoS** appropriately (`0`, `1`, `2`) for guaranteed delivery or low latency
* Consider using Last Will & Testament (LWT) for failure messaging in IoT deployments

---

## 🤝 Contributing

Enhancements are welcome! Suggestions include:

* 🔁 Support for batch publishing or message queues
* 📊 Add message logging or replay functionality
* 🌐 Support for MQTT v5 features: message expiry, shared subscriptions
* 🧪 Add unit tests with pytest/mock
* 📦 Package as a pip-installable library

To contribute:

1. Fork the repository
2. Create a branch (`feature/...`)
3. Implement tests and document changes
4. Open a Pull Request

---

## 📄 License

Released under the **MIT License**. See `LICENSE` for details.
