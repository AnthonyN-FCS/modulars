from config import *
import paho.mqtt.client as mqtt, json
import pprint
import datetime

# MQTT connection details
MQTT_BROKER_HOST = "10.4.139.142"
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

    payload_str = msg.payload.decode('utf-8')

    data_dict = json.loads(payload_str)

    for item in locations:
        if item.check_id(id) and item and item.check_data(data_dict):
            temperature_F = data_dict["temperature_C"] * 9/5 + 32
            temperature_C = data_dict["temperature_C"]
            time = data_dict["time"]
            id = data_dict["id"]
            humidity = data_dict["humidity"]

            current_datetime = datetime.datetime.now()
            current_hour = current_datetime.hour

            if current_hour == 7:
                item.send_data_at_7am(temperature_F,temperature_C,humidity,time)
            else:
                item.send_data(temperature_F,temperature_C,humidity,time)

# Set the MQTT client's on_connect and on_message callbacks
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to the MQTT broker
# keepalive set to 120 secs
mqtt_client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 120)





for item in locations:
    print(item)







if __name__ == "__main__":
    # Loop forever, processing MQTT messages as they come in
    mqtt_client.loop_forever()