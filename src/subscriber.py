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