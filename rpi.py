import paho.mqtt.client as mqtt
import time
import json

# MQTT setup
broker = "windows_pc_ip"  # Replace with the IP address of the Windows PC running Mosquitto
port = 1883
topic = "sensor/data"

client = mqtt.Client()
client.connect(broker, port, 60)

def send_data():
    # Example data to send
    data = {
        "temperature": 22.5,
        "humidity": 60,
        "rain_level": 0.1
    }
    payload = json.dumps(data)
    client.publish(topic, payload)
    print(f"Data sent: {payload}")

try:
    while True:
        send_data()
        time.sleep(10)  # Send data every 10 seconds

except KeyboardInterrupt:
    print("Disconnected")
    client.disconnect()
