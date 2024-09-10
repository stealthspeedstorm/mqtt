import paho.mqtt.client as mqtt

# MQTT setup
broker = "localhost"
port = 1883

# Topics to subscribe to
topics = [
    "sensor/rpi1",
    "sensor/rpi2",
    "sensor/rpi3"
]

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    for topic in topics:
        client.subscribe(topic)
        print(f"Subscribed to {topic}")

def on_message(client, userdata, msg):
    topic = msg.topic
    data = msg.payload.decode()
    print(f"Received message on {topic}: {data}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

try:
    client.loop_forever()

except KeyboardInterrupt:
    print("Disconnected")
    client.disconnect()
