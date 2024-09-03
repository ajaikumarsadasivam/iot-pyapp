# My IoT Application

![Release](https://img.shields.io/github/v/release/ajaikumarsadasivam/iot-pyapp)
![License](https://img.shields.io/github/license/ajaikumarsadasivam/iot-pyapp)

## About the Application

The IoT Application is a Python-based MQTT project designed to interact with a Raspberry Pi Pico Wh. The application includes MQTT functionality to communicate with various sensors (like temperature, and humidity) and control LEDs based on received commands. Additionally, the application can download and apply code updates from an S3 bucket, making it easy to maintain and update your IoT devices remotely.

### Key Features
- **MQTT Communication**: Supports publishing sensor data and receiving commands to control LEDs.
- **TLS Support**: Secures MQTT communication with TLS.
- **Flask Web Application**: A simple web interface to display data and send commands to the IoT device.

## Getting Started

### Prerequisites

- Python 3.x
- Paho-MQTT Library
- Flask Framework
- Docker (for containerization)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ajaikumarsadasivam/iot-pyapp.git
   cd your-repo

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

3. **Run the Application**:
    ```bash
    python app.py

4. **Running with Docker**:
    ```bash
    docker build -t my-iot-app .
    docker run -p 5000:5000 my-iot-app

### Configuration

Configure your MQTT broker, S3 bucket, and other environment variables by creating a .env file in the root directory:

    MQTT_BROKER_URL=mqtt.yourbroker.com
    MQTT_BROKER_PORT=8883
    MQTT_USERNAME=your_username
    MQTT_PASSWORD=your_password
    S3_BUCKET_URL=https://s3.amazonaws.com/your-bucket

### Usage

After setting up, you can access the Flask web interface on http://localhost:5000. The interface allows you to:

- View the latest sensor data.
- Control the LEDs connected to the Raspberry Pi Pico W.

### Links

- Latest Release: ![View Latest Release](https://github.com/ajaikumarsadasivam/iot-pyapp/releases/latest)
- Latest Package: ![Download Latest Package](https://github.com/ajaikumarsadasivam/iot-pyapp/packages)
- Documentation: ![Project Documentation](https://github.com/ajaikumarsadasivam/iot-pyapp/blob/main/README.md)

### Contributing

<TBU>

### License

<TBU>