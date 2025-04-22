![github banner](https://github.com/user-attachments/assets/29d42856-8943-4d68-82d2-2fe9fb687146)![github banner](https://github.com/user-attachments/assets/6b68aa91-b1a5-4700-8ad8-ecde63270925)![github banner](https://github.com/user-attachments/assets/70d083ca-ecb5-4989-81b6-9dee3be24ffa)![github banner](https://github.com/user-attachments/assets/90d943ed-f889-45da-a8d5-64595b61a234)

# MQTT Messaging System with Python 📡

This project demonstrates how to use **MQTT (Message Queuing Telemetry Transport)** with Python for real-time communication between devices or applications. We’ll be using the **paho-mqtt** library to create both a **Publisher** and a **Subscriber** that send and receive messages via an MQTT Broker.

## 📋 **Requirements**
- Python 3.x
- **paho-mqtt** library
- A running MQTT Broker (e.g., HiveMQ, Mosquitto)

## ⚙️ **Setup**

1. **Install Dependencies**:
   To install the required `paho-mqtt` library, run:
   ```sh
   pip install paho-mqtt
   ```

2. **Set up MQTT Broker**:
   - You can use a public MQTT broker like [HiveMQ](https://www.hivemq.com/public-mqtt-broker/) or set up your own using **Mosquitto**.
   - If you want to run a local MQTT broker, you can install **Mosquitto** using the following commands:
     - On Ubuntu:
       ```sh
       sudo apt update
       sudo apt install mosquitto mosquitto-clients
       sudo systemctl enable mosquitto
       sudo systemctl start mosquitto
       ```
     - For other systems, please follow the [Mosquitto installation guide](https://mosquitto.org/download/).

---

## 🖥️ **Publisher Code (Sending Messages)**

### `publisher.py`

This script sends a message to a specific topic in the MQTT broker.

```python
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "test/topic"

client = mqtt.Client()

client.connect(BROKER, PORT, 60)

client.publish(TOPIC, "Hello MQTT from Python!")

client.disconnect()
```

### Explanation:
1. **Importing the library**: `paho.mqtt.client` provides the functionality to interact with MQTT.
2. **Broker and Port Setup**: The MQTT broker we’re connecting to is `broker.hivemq.com` on port `1883`.
3. **Connect to the Broker**: We establish a connection to the broker using `client.connect()`.
4. **Publishing the Message**: We publish the message "Hello MQTT from Python!" to the topic `"test/topic"`.
5. **Disconnecting**: After publishing the message, we disconnect from the broker.

---

## 📡 **Subscriber Code (Receiving Messages)**

### `subscriber.py`

This script listens to a specific topic and prints any messages that are sent to that topic.

```python
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "test/topic"

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client()

client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.subscribe(TOPIC)

print("Listening for messages...")
client.loop_forever()
```

### Explanation:
1. **Importing the library**: We use `paho.mqtt.client` to interact with MQTT.
2. **Broker and Port Setup**: We connect to the same MQTT broker `broker.hivemq.com` on port `1883`.
3. **Define `on_message` Function**: This function is triggered when a new message is received. It prints the message payload and the topic.
4. **Connect to the Broker**: We connect to the broker using `client.connect()`.
5. **Subscribe to a Topic**: We subscribe to the topic `"test/topic"` to listen for messages.
6. **Loop to Listen for Messages**: `client.loop_forever()` keeps the program running and waiting for new messages indefinitely.

---

## 🚀 **How to Run the Code**

1. **Start the Subscriber**:
   Open a terminal and run:
   ```sh
   python subscriber.py
   ```
   The Subscriber will now be listening for messages on the specified topic.

2. **Run the Publisher**:
   In a separate terminal, run:
   ```sh
   python publisher.py
   ```
   The Publisher will send a message to the MQTT broker.

3. **Observe**:
   - Once you run the Publisher, you’ll see the message received by the Subscriber in the terminal running `subscriber.py`.

---

## 🧑‍💻 **Extending the Project**

You can further extend this project to:
- **Two-way Communication**: Implement both publishing and subscribing in the same script.
- **Message Persistence**: Store received messages in a database (e.g., SQLite or MongoDB).
- **Security**: Add authentication to the MQTT connection with user credentials or use TLS encryption for secure communication.
- **Quality of Service (QoS)**: MQTT allows different levels of QoS to ensure message delivery reliability. You can experiment with different QoS settings when publishing or subscribing.

---

## 🔧 **Troubleshooting**

- If you encounter connection issues, make sure the MQTT broker is running and reachable.
- Check for any firewall or network configuration that may block the connection to the broker.

---

## 💬 **Questions or Issues?**
Feel free to open an issue in the repository if you have any questions or need assistance with setup!

---

Good luck with your MQTT project! 🚀
