from main import app
from flask import render_template

@app.route('/')
def list_expenses():
    expenses = [
        {
            'id': 1,
            'name': 'Expense 1',
            'category': 'Food',
            'amount': 50.44,
            'date': '2002-11-23'
        },
        {
            'id': 2,
            'name': 'Expense 2',
            'category': 'Shopping',
            'amount': 22.53,
            'date': '2002-11-24'
        },
        {
            'id': 3,
            'name': 'Expense 3',
            'category': 'Food',
            'amount': 74.33,
            'date': '2002-11-24'
        }
    ]

    return render_template('views/list_expenses.html', page_name='list_expenses', page_title='List Expenses', expenses=expenses)


@app.route('/add-expense')
def add_expense():
    return render_template('views/add_expense.html', page_name='add_expense', page_title='Add Expense')


@app.route('/edit-expense/<int:expense_id>')
def edit_expense(expense_id):
    return render_template('views/edit_expense.html', page_name='edit_expense', page_title='Edit Expense')


@app.route('/delete-expense/<int:expense_id>')
def delete_expense(expense_id):
    return list_expenses()


@app.route('/list-categories')
def list_categories():
    categories = [
        {
            'id': 1,
            'name': 'Food'
        },
        {
            'id': 2,
            'name': 'Shopping'
        },
        {
            'id': 3,
            'name': 'Automobile'
        },
        {
            'id': 4,
            'name': 'Entertainment'
        },
        {
            'id': 5,
            'name': 'Bills'
        }
    ]

    return render_template('views/list_categories.html', page_name='list_categories', page_title='List Categories', categories=categories)


@app.route('/add-category')
def add_category():
    return render_template('views/add_category.html', page_name='add_category', page_title='Add Category')


@app.route('/edit-category/<int:category_id>')
def edit_category(category_id):
    return render_template('views/edit_category.html', page_name='edit_category', page_title='Edit Category')


@app.route('/delete-category/<int:category_id>')
def delete_category(category_id):
    return list_categories()


@app.route('/statistics')
def statistics():
    return render_template('views/statistics.html', page_name='statistics', page_title='Statistics')
