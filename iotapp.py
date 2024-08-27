from flask import Flask, render_template, request, redirect, url_for, jsonify
import paho.mqtt.client as paho
from paho import mqtt
import json
import os
app = Flask(__name__)
# MQTT Configuration
mqtt_broker = os.getenv('MQTT_BROKER', '7a5ac4b86d0a408292b06e2abd774619.s1.eu.hivemq.cloud')
mqtt_port = int(os.getenv('MQTT_PORT', 8883))
mqtt_username = os.getenv('MQTT_USERNAME', 'iot-test')
mqtt_password = os.getenv('MQTT_PASSWORD', 'Welcome1@')
client_id = 'iot-test'

mqtt_client = paho.Client(client_id=client_id, userdata=None, protocol=paho.MQTTv5)

pico_data_topic = 'pico/sensors/data'
pico_control_topic = 'pico/led/control'
sensor_data = {'temperature': None, 'potentiometer': None, 'distance': None}


def on_connect(client, userdata, flags, rc, properties):
    '''
    '''
    print("Connected with result code " + str(rc))
    if rc == 0:
        print(f"Subscribing to topic: {pico_data_topic}")
        mqtt_client.subscribe(pico_data_topic)
    else:
        print(f"Failed to connect with result code: {rc}")


def on_message(client, userdata, msg):
    '''
    '''
    global sensor_data
    payload = msg.payload.decode('utf-8')
    try:
        sensor_data = json.loads(payload)
        print(f"Received data: {sensor_data}")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")


mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to MQTT broker
try:
    mqtt_client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    mqtt_client.username_pw_set(mqtt_username, mqtt_password)
    mqtt_client.connect(mqtt_broker, mqtt_port, 60)
    mqtt_client.loop_start()
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sensor-data')
def sensor_data_api():
    return jsonify(sensor_data)


@app.route('/control', methods=['POST'])
def control_led():
    led_color = request.form['color']
    state = int(request.form['state'])
    command = {
        'led': led_color,
        'state': state
    }
    mqtt_client.publish(pico_control_topic, json.dumps(command))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
