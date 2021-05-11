from urlshort import create_app


def test_shorted(client):
    response = client.get('/')
    assert b'Shorten' in response.data
