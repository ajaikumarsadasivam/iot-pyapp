**Release Date:** 2024-09-03

## Overview
This release includes the initial implementation of the Flask web application. The python application is designed to work together, allowing the Raspberry Pi Pico W to receive sensor data and send commands to control LEDs.

### Flask Python App

#### New Features
- **MQTT Integration**: The Flask app connects to the MQTT broker and displays real-time data.

#### Known Issues
- **Connection Refusal**: The Flask app may experience connection refusals with the MQTT broker.

### Technical Notes
- **Dependency Updates**: Flask-SocketIO and Paho-MQTT libraries are required.

### Download and Installation
- **Flask Python App**: Available in the `iot-pyapp` repository.

### Contributors
- **User**: Developed the MQTT Pico W script and Flask app.

### Feedback and Support
If you encounter any issues or have feedback, please contact [ajaikumar.sadasivam@gmail.com](mailto:ajaikumar.sadasivam@gmail.com)
