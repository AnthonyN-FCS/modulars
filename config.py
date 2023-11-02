from influxdb import InfluxDBClient
# example write operation and query operation to InfluxDB V1.8



class Sensor:
    def __init__(self,sensorID, location, measurement):
        self.username = 'python_user'
        self.password = 'python_user_pw'
        self.database = 'modulars_2023'
        self.influx_host = "10.4.139.142"

        self.sensorID = sensorID
        self.location = location
        self.measurement = measurement

        

    
    def __str__(self):
        return f"Location: {self.location}, sensorID: {self.sensorID}"

    def check_id(self,id):
        return self.sensorID == id
    
    def check_data(self, data):
        if not data["id"] or not data["temperature_C"] or not data["humidity"]:
            return False
        return True

    def send_data(self,temperature_F,temperature_C,humidity,time):
        data = [
        {
            "measurement": "norris",
            "tags": {
                "meterID": self.sensorID,
                "room_name": self.location,
            },
            "fields": {
                "temperature_F": temperature_F,
                "temperature_C": temperature_C,
                "humidity": humidity,
            }
            }
        ]

        client = InfluxDBClient(host = self.influx_host, port = 8086, username = self.username, password = self.password, database = self.database)

        client.write_points(data)

        client.close()
        print(f"Received data: {time}")

    def send_data_at_7am(self,temperature_F,temperature_C,humidity):
        data = [
        {
            "measurement": "norris_7am",
            "tags": {
                "meterID": self.sensorID,
                "room_name": self.location,
            },
            "fields": {
                "temperature_F": temperature_F,
                "temperature_C": temperature_C,
                "humidity": humidity,
            }
            }
        ]

        client = InfluxDBClient(host = self.influx_host, port = 8086, username = self.username, password = self.password, database = self.database)

        client.write_points(data)

        client.close()
    
locations = [
    Sensor(10223, 'outside', "anthony"),
    Sensor(1687, 'room1', "anthony"),
    Sensor(7938, 'room2', "anthony"),
    Sensor(7024, 'room3', "anthony"),
    Sensor(12896, 'room4', "anthony"),
]
