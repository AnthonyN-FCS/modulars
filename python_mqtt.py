import paho.mqtt.client as mqtt, json

# MQTT connection details
MQTT_BROKER_HOST = "10.4.131.115"
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = "RTL_433"

# Create an MQTT client instance
mqtt_client = mqtt.Client(client_id='Mr_Boyd_test')

# Callback for when the MQTT client receives a CONNACK response from the MQTT broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")

    # Subscribe to the MQTT topic
    mqtt_client.subscribe(MQTT_TOPIC)

# Callback for when a message is received on the MQTT topic
def on_message(mqtt_client, userdata, msg):
    print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "'")
    #decode message, prep record for database write

# Set the MQTT client's on_connect and on_message callbacks
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT broker
# keepalive set to 120 secs
mqtt_client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 120)

if __name__ == "__main__":
    # Loop forever, processing MQTT messages as they come in
    mqtt_client.loop_forever()
