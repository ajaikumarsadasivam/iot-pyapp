import os
class Config:
    TESTING = False
    DEBUG = False


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    MQTT_BROKER = os.getenv('MQTT_BROKER')
    MQTT_PORT = int(os.getenv('MQTT_PORT', 8883))
    MQTT_USERNAME = os.getenv('MQTT_USERNAME')
    MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')
