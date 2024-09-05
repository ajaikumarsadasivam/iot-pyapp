class Config:
    TESTING = False
    DEBUG = False


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    MQTT_BROKER = "7a5ac4b86d0a408292b06e2abd774619.s1.eu.hivemq.cloud"
    MQTT_PORT = "8883"
    MQTT_USERNAME = "iot-test"
    MQTT_PASSWORD = "Welcome1@"
