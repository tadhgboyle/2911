from main import app
from models import Expense, Category
from flask import render_template


@app.route('/')
def list_expenses():
    return render_template('views/list_expenses.html', page_name='list_expenses', page_title='List Expenses', expenses=Expense.objects())


@app.route('/add-expense')
def add_expense():
    return render_template('views/add_expense.html', page_name='add_expense', page_title='Add Expense')


@app.route('/edit-expense/<expense_id>')
def edit_expense(expense_id):
    return render_template('views/edit_expense.html', page_name='edit_expense', page_title='Edit Expense')


@app.route('/delete-expense/<expense_id>')
def delete_expense(expense_id):
    return list_expenses()


@app.route('/list-categories')
def list_categories():
    return render_template('views/list_categories.html', page_name='list_categories', page_title='List Categories', categories=Category.objects())


@app.route('/add-category')
def add_category():
    return render_template('views/add_category.html', page_name='add_category', page_title='Add Category')


@app.route('/edit-category/<category_id>')
def edit_category(category_id):
    return render_template('views/edit_category.html', page_name='edit_category', page_title='Edit Category')


@app.route('/delete-category/<category_id>')
def delete_category(category_id):
    return list_categories()


@app.route('/statistics')
def statistics():
    return render_template('views/statistics.html', page_name='statistics', page_title='Statistics')
