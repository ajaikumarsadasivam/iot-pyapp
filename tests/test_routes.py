import pytest
import sys
sys.path.append('../')
import app


class TestRoutes:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    def test_index_route(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b"Temperature" in response.data  # Check for expected content

    def test_control_route(self, client):
        response = client.post('/control', data={'color': 'red', 'state': '1'})
        assert response.status_code == 302  # Check for redirection

    def test_sensor_data_route(self, client):
        response = client.get('/sensor-data')
        assert response.status_code == 200
        assert b"temperature" in response.data  # Check for JSON keys
