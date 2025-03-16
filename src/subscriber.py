# Importing the paho.mqtt library to interact with the MQTT protocol
import paho.mqtt.client as mqtt

# Defining the broker address, port, and topic
BROKER = "broker.hivemq.com"  # Broker address
PORT = 1883  # Port for connection (default MQTT port)
TOPIC = "test/topic"  # The topic to subscribe to for receiving messages

# Defining the callback function that handles incoming messages
def on_message(client, userdata, msg):
    # This function gets called when a message is received
    # It prints the message payload and the topic from which the message was received
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

# Creating an MQTT Client object to establish communication
client = mqtt.Client()

# Assigning the callback function to handle incoming messages
client.on_message = on_message

# Connecting to the broker using the address, port, and timeout duration
client.connect(BROKER, PORT, 60)

# Subscribing to the specified topic to receive messages
client.subscribe(TOPIC)

# Printing a message to indicate that the client is now listening for messages
print("Listening for messages...")

# Starting the loop that keeps the script running and processes incoming messages
client.loop_forever()