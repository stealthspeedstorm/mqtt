import paho.mqtt.client as mqtt

# MQTT setup
broker = "localhost"
port = 1883
topic = "sensor/data"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    print(f"Received message: {data}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

try:
    client.loop_forever()

except KeyboardInterrupt:
    print("Disconnected")
    client.disconnect()
