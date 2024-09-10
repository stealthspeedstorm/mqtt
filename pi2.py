import paho.mqtt.client as mqtt
import time
import json

# MQTT setup
broker = "windows_pc_ip"  # Replace with the IP address of the Windows PC running Mosquitto
port = 1883

# Unique topics for each RPi
topics = {
    "rpi1": "sensor/rpi1",
    "rpi2": "sensor/rpi2",
    "rpi3": "sensor/rpi3"
}

client = mqtt.Client()
client.connect(broker, port, 60)

def send_data(rpi_id):
    topic = topics[rpi_id]
    # Example data to send
    data = {
        "temperature": 22.5,
        "humidity": 60,
        "rain_level": 0.1
    }
    payload = json.dumps(data)
    client.publish(topic, payload)
    print(f"Data sent to {topic}: {payload}")

try:
    rpi_id = "rpi1"  # Change this to "rpi2" or "rpi3" for other RPis
    while True:
        send_data(rpi_id)
        time.sleep(10)  # Send data every 10 seconds

except KeyboardInterrupt:
    print("Disconnected")
    client.disconnect()
