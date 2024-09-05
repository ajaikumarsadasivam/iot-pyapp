import pytest
from unittest.mock import patch
import sys
sys.path.append('../')
from app import app, mqtt_client


class TestMQTT:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    @patch('app.mqtt_client.connect')
    @patch('app.mqtt_client.loop_start')
    def test_mqtt_connection(self, mock_connect, mock_loop_start):
        mock_connect.return_value = 0  # Simulate successful connection
        mock_loop_start.return_value = None

        # Assuming connect_mqtt() is called when app starts
        from app import connect_mqtt
        connect_mqtt()

        mock_connect.assert_called_once()
        mock_loop_start.assert_called_once()

    @patch('app.mqtt_client.publish')
    def test_publish_message(self, mock_publish):
        mock_publish.return_value = None

        with app.test_client() as client:
            response = client.post('/control', data={'color': 'red', 'state': '1'})
            mock_publish.assert_called_once()
            assert response.status_code == 302  # Redirect after POST

    @patch('app.mqtt_client.subscribe')
    def test_subscribe_to_topic(self, mock_subscribe):
        mock_subscribe.return_value = None

        from app import on_connect
        on_connect(mqtt_client, None, None, 0, None)  # Simulate successful connection

        mock_subscribe.assert_called_once_with('pico/sensors/data')
