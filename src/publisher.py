# Importing the paho.mqtt library to interact with the MQTT protocol
import paho.mqtt.client as mqtt

# Defining the broker address, port, and topic
BROKER = "broker.hivemq.com"  # Broker address
PORT = 1883  # Port for connection (default MQTT port)
TOPIC = "test/topic"  # The topic to which the message will be published

# Creating an MQTT Client object to establish communication
client = mqtt.Client()

# Connecting to the broker using the address, port, and timeout duration
client.connect(BROKER, PORT, 60)

# Publishing the message "Hello, Im Misagh" to the defined topic
client.publish(TOPIC, "Hello, Im Misagh")

# Disconnecting from the broker after the message is sent
client.disconnect()