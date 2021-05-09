import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

def test_list_expenses(client):
    response = client.get('/')
    assert response.status_code == 200

def test_add_expense(client):
    response = client.get('/add-expense')
    assert response.status_code == 200

    response = client.post('/add-expense')
    assert response.status_code == 200

def test_edit_expense(client):
    response = client.get('/edit-expense/<expense_id>')
    assert response.status_code == 200

    response = client.post('/edit-expense/<expense_id>')
    assert response.status_code == 200

def test_delete_expense(client):
    response = client.get('/delete-expense/<expense_id>')
    assert response.status_code == 200

def test_list_categories(client):
    response = client.get('/list-categories')
    assert response.status_code == 200

def test_add_category(client):
    response = client.get('/add-category')
    assert response.status_code == 200

    response = client.post('/add-category')
    assert response.status_code == 200

def test_edit_category(client):
    response = client.get('/edit-category/<category_id>')
    assert response.status_code == 200

    response = client.post('/edit-category/<category_id>')
    assert response.status_code == 200

def test_delete_category(client):
    response = client.get('/delete-category/<category_id>')
    assert response.status_code == 200

def test_statistics(client):
    response = client.get('/statistics')
    assert response.status_code == 200
