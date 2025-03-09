import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "test/topic"

client = mqtt.Client()

client.connect(BROKER, PORT, 60)