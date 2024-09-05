import pytest
from app import create_app, db
from app.model.user import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200

def test_create_user(client):
    response = client.post('/users', json={'username': 'test', 'email': 'test@example.com'})
    assert response.status_code == 201
    assert response.get_json()['username'] == 'test'
