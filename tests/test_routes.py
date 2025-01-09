import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200

def test_create_user(client):
    response = client.post('/users', json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
