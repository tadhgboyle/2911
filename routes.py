from main import app
from flask import render_template


@app.route('/')
def list_expenses():
   return render_template('views/list_expenses.html', page_name='list_expenses', page_title='List Expenses')


@app.route('/add-expense')
def add_expense():
    return render_template('views/add_expense.html', page_name='add_expense', page_title='Add Expense')


@app.route('/edit-expense')
def edit_expense():
    return render_template('views/edit_expense.html', page_name='edit_expense', page_title='Edit Expense')


@app.route('/delete-expense')
def delete_expense():
    return render_template('views/delete_expense.html', page_name='delete_expense', page_title='Delete Expense')


@app.route('/list-categories')
def list_categories():
    return render_template('views/list_categories.html', page_name='list_categories', page_title='List Categories')


@app.route('/add-category')
def add_category():
    return render_template('views/add_category.html', page_name='add_category', page_title='Add Category')


@app.route('/edit-category')
def edit_category():
    return render_template('views/edit_category.html', page_name='edit_category', page_title='Edit Category')


@app.route('/delete-category')
def delete_category():
    return render_template('views/delete_category.html', page_name='delete_category', page_title='Delete Category')


@app.route('/statistics')
def statistics():
    return render_template('views/statistics.html', page_name='statistics', page_title='Statistics')
