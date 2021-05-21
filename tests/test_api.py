"""
This test module contains integration testing for the api. It first runs tests to see if list_expenses and list_categories works correctly. 
It then goes through a sequence of tests where CRUD features are tested. All Flask requests are tested.
"""

import pytest
from app import create_app
from models import Category, Expense
import datetime
from .sample_data import create_sample_data, delete_sample_data, delete_existing_data

@pytest.fixture
def client():
    """ Creates client text fixture. """
    app = create_app()
    return app.test_client()

def test_list_expenses(client):
    """ Tests if homepage/list_expenses feature is working correctly. """
    
    # Deletes any existing data that may cause tests to fail
    delete_existing_data()
    
    # Creates sample data that will be used in test
    create_sample_data()

    # Tests GET success
    response = client.get('/')
    assert response.status_code == 200
    
    # Tests if HTML is being returned 
    assert response.content_type == 'text/html; charset=utf-8'
    
    # Tests if required elements are present 
    titles_headings = ['<title>List Expenses - Expenses</title>', '<h1 class="m-4">Your Expenses</h1>']
    table_headers = ['<th scope="col">Name</th>', '<th scope="col">Category</th>', '<th scope="col">Amount</th>', '<th scope="col">Date</th>']
    expense_elements = ['Expense 1', 'Expense 2', 'Expense 3', 'Expense 4', 'Expense 5', 'Expense 6', 'Expense 7', 'Expense 8', 'Expense 9', 'Expense 10', 'Expense 11', 'Test Category', '$10.00', '$1.00', '2021-01-01']
    other_elements = ['navbar', 'footer']
    elements = titles_headings + table_headers + expense_elements + other_elements
    for element in elements:
        assert element.encode() in response.data
    
    # Deletes sample data that was used in test
    delete_sample_data()

def test_list_categories(client):
    """ Tests if list_categories feature is working correctly. """

    # Creates sample data that will be used in test
    create_sample_data()

    # Tests GET success
    response = client.get('/list-categories')
    assert response.status_code == 200

    # Tests if HTML is being returned 
    assert response.content_type == 'text/html; charset=utf-8'

    # Tests if required elements are present 
    titles_headings = ['<title>List Categories - Expenses</title>', '<h1 class="m-4">Your Categories</h1>']
    table_headers = ['<th scope="col">Name</th>']
    category_elements = ['Test Category']
    other_elements = ['navbar', 'footer']
    elements = titles_headings + table_headers + category_elements + other_elements
    for element in elements:
        assert element.encode() in response.data
    
    # Deletes sample data that was used in test
    delete_sample_data()

def test_add_category(client):
    """ Tests if add_category feature works correctly. """

    # Tests GET success
    response = client.get('/add-category')
    assert response.status_code == 200

    # Tests if HTML is being returned 
    assert response.content_type == 'text/html; charset=utf-8'

    # Tests if required elements are present 
    titles_headings = ['<title>Add Category - Expenses</title>', '<h1 class="m-4">Create Category</h1>']
    form_elements = ['<label for="name" class="form-label">Category Name</label>']
    other_elements = ['navbar', 'footer']
    elements = titles_headings + form_elements + other_elements
    for element in elements:
        assert element.encode() in response.data   
   
    # Records number of existing categories prior to POST
    categories_length_before_post = len(Category.objects())
    
    # Tests POST success by creating sample category called 'Test Category'
    sample_data=dict(name='Test Category')
    response = client.post('/add-category', data=sample_data)
    assert response.status_code == 200
    
    # Tests if category was added succesfully or not
    if categories_length_before_post != len(Category.objects()):
        new_category = Category.objects.get(name='Test Category')
        assert new_category.name == 'Test Category'
        assert b'<strong>Success:</strong> Created new category &#34;Test Category&#34;.' in response.data
    elif categories_length_before_post == len(Category.objects()):
        assert b'<strong>Error:</strong>' in response.data

def test_add_expense(client):
    """ Tests if the add_expense feature works correctly. """

    # Tests GET success
    response = client.get('/add-expense')
    assert response.status_code == 200

    # Tests if HTML is being returned 
    assert response.content_type == 'text/html; charset=utf-8'

    # Tests if required elements are present 
    titles_headings = ['<title>Add Expense - Expenses</title>', '<h1 class="m-4">Add Expense</h1>']
    form_elements = ['<label for="name" class="form-label">Expense Name</label>',
                   '<label for="categories" class="form-label">Category</label>',
                   '<label for="amount" class="form-label">Amount</label>',
                   '<label for="date" class="form-label">Date</label>']
    other_elements = ['navbar', 'footer']
    elements = titles_headings + form_elements + other_elements
    for element in elements:
        assert element.encode() in response.data   

    # Records number of existing expenses prior to POST
    expenses_length_before_post = len(Expense.objects())
    
    # Gets sample category created earlier called 'Test Category' required for POST sample data
    sample_category = Category.objects.get(name='Test Category')
    
    # Creates sample date object required for POST sample data
    sample_date = datetime.date(2021, 1, 1)
    
    # Tests POST success by creating sample expense called 'Test Expense'
    sample_data = dict(name='Test Expense', category_id=sample_category.id, amount=50, date=sample_date)
    response = client.post('/add-expense', data=sample_data)
    assert response.status_code == 200

    # Tests if expense was added succesfully or not
    if expenses_length_before_post != len(Expense.objects()):
        new_expense = Expense.objects.get(name='Test Expense')
        assert new_expense.name == 'Test Expense'
        assert new_expense.category_id == sample_category.id
        assert new_expense.amount == 50
        assert new_expense.date == sample_date
        assert b'<strong>Success:</strong> Created new expense &#34;Test Expense&#34;.' in response.data
        expense_elements = ['<th>Test Expense</th>', '<th>Test Category</th>', '<th>$50.00</th>', '<th>{}</th>'.format(sample_date.strftime("%Y-%m-%d"))]
        for element in expense_elements:
            assert element.encode() in response.data
    elif expenses_length_before_post == len(Expense.objects()):
        assert b'<strong>Error:</strong>' in response.data

def test_edit_category(client):
    """ Tests if edit_category feature works correctly. """

    # Gets sample category created earlier called 'Test Category' whos ID is required for GET url and POST sample data
    sample_category = Category.objects.get(name='Test Category')
    
    # Tests GET success
    response = client.get('/edit-category/{}'.format(str(sample_category.id)))
    assert response.status_code == 200

    # Tests if HTML is being returned
    assert response.content_type == 'text/html; charset=utf-8'
    
    # Tests if required elements are present
    titles_headings = ['<title>Edit Category - Expenses</title>', '<h1 class="m-4">Edit Category</h1>']
    form_elements = ['<label for="name" class="form-label">Category Name</label>', 'value="Test Category"']
    other_elements = ['navbar', 'footer']
    elements = titles_headings + form_elements + other_elements
    for element in elements:
        assert element.encode() in response.data   

    # Tests POST success by editing sample category created earlier to 'Test Category 2'
    sample_data = dict(category_id=sample_category.id, name='Test Category 2')
    response = client.post('/edit-category/{}'.format(str(sample_category.id)), data=sample_data)
    assert response.status_code == 200

    # Tests if category was edited succesfully or not
    if b'<strong>Error:</strong> A category with that name already exists.' not in response.data:
        edited_category = Category.objects.get(name='Test Category 2')
        assert edited_category.id == sample_category.id
        assert edited_category.name == 'Test Category 2'
        assert b'<strong>Success:</strong> Updated category &#34;Test Category 2&#34;.' in response.data
        assert edited_category.id == Expense.objects.get(name='Test Expense').category_id  # Tests if sample expense's category changed

def test_edit_expense(client):
    """ Tests if edit_expense feature works correctly. """

    # Gets sample expense created earlier called 'Test Expense' whos ID is required for GET url and POST sample data
    sample_expense = Expense.objects.get(name='Test Expense')

    # Tests GET success
    response = client.get('/edit-category/{}'.format(str(sample_expense.id)))
    assert response.status_code == 200

    # Tests if HTML is being returned
    assert response.content_type == 'text/html; charset=utf-8'

    # Gets sample category edited earlier called 'Test Category 2' whos ID is required for POST sample data
    sample_category = Category.objects.get(name='Test Category 2')
    
    # Creates sample date object required for POST sample data
    sample_date = datetime.date(2021, 1, 31)

    # Tests POST success by editing sample expense created earlier name to 'Test Expense 2'. Also edits amount and date attributes.
    sample_data = dict(expense_id=sample_expense.id, name='Test Expense 2', category_id=sample_category.id, amount=100, date=sample_date)
    response = client.post('/edit-expense/{}'.format(str(sample_expense.id)), data=sample_data)
    assert response.status_code == 200

    # Tests if expense was edited succesfully or not     
    if b'<strong>Error:</strong> An expense with that name already exists.' not in response.data:
        edited_expense = Expense.objects.get(name='Test Expense 2')
        assert edited_expense.name == 'Test Expense 2'
        assert edited_expense.category_id == sample_category.id
        assert edited_expense.amount == 100
        assert edited_expense.date == sample_date
        assert b'<strong>Success:</strong> Updated expense &#34;Test Expense 2&#34;.' in response.data

def test_delete_expense(client):
    """ Tests if delete_expense feature works correctly. """

    # Records number of existing expenses prior to deleting
    expenses_length_before_delete = len(Expense.objects())

    # Gets sample expense that was edited to 'Test Expense 2'
    sample_expense = Expense.objects.get(name='Test Expense 2')
    
    # Tests GET success (automatically deletes expense)
    response = client.get('/delete-expense/{}'.format(str(sample_expense.id)))
    assert response.status_code == 200
    
    # Tests if HTML is being returned
    assert response.content_type == 'text/html; charset=utf-8'
    
    # Tests if expense was deleted succesfully or not     
    assert expenses_length_before_delete != len(Expense.objects())
    assert b'<strong>Success:</strong> Deleted expense &#34;Test Expense 2&#34;.' in response.data

def test_delete_category(client):
    """ Tests if delete_category feature works correctly. """
    
    # Records number of existing categories prior to deleting
    categories_length_before_delete = len(Category.objects())
    
    # Gets sample category that was edited to 'Test Category 2'
    sample_category = Category.objects.get(name='Test Category 2')
    
    # Tests GET success (automatically deletes category)
    response = client.get('/delete-category/{}'.format(str(sample_category.id)))
    assert response.status_code == 200

    # Tests if HTML is being returned
    assert response.content_type == 'text/html; charset=utf-8'
    
    # Tests if category was deleted succesfully or not     
    assert categories_length_before_delete != len(Category.objects())
    assert b'<strong>Success:</strong> Deleted category &#34;Test Category 2&#34;.' in response.data

def test_statistics(client):
    """ Tests if statistics feature works correctly. """

    # Creates sample data that will be used in test
    create_sample_data()

    # Tests GET success
    response = client.get('/statistics')
    assert response.status_code == 200

    # Tests if HTML is being returned
    assert response.content_type == 'text/html; charset=utf-8'

    # Tests if required elements are present
    titles_headings = ['<title>Statistics - Expenses</title>', 'Total Expendatures (month of None): $101.00', 'Average Expense Amount: $9.18']
    other_elements = ['navbar', 'footer']
    graph_1_elements = ["labels: ['Test Category']", "data: ['101.00']", 'Spent per Category (month of None)']
    graph_2_elements = ["labels: ['Expense 9 on 2021-01-01', 'Expense 10 on 2021-01-01', 'Expense 5 on 2021-01-01', 'Expense 8 on 2021-01-01', 'Expense 6 on 2021-01-01', 'Expense 4 on 2021-01-01', 'Expense 2 on 2021-01-01', 'Expense 1 on 2021-01-01', 'Expense 3 on 2021-01-01', 'Expense 7 on 2021-01-01']",
                        'label: "Expense Amount"', 'data: [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]', 'Top 10 Expenses (month of None)']
    elements = titles_headings + graph_1_elements + graph_2_elements + other_elements
    for element in elements:
        assert element.encode() in response.data
    assert b'Expense 11 on 2021-01-01' not in response.data

    # Deletes sample data that was used in test
    delete_sample_data()