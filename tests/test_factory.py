from app import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello/Wei')
    data = response.get_json()

    assert data['message'] == "Hello, Wei!"
    assert not data['message'] == "Hello, Nobody!"
    assert not data['message'] == "Hello, Ko!"
