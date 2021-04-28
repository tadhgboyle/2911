from main import app
from flask import render_template


@app.route('/')
def expenses_list():
   return render_template('views/list_expenses.html', page_title='List Expenses')


@app.route('/add-expense')
def add_expense():
    return render_template('views/add_expense.html', page_title='Add Expense')


@app.route('/edit-expense')
def edit_expense():
    return render_template('views/edit_expense.html', page_title='Edit Expense')


@app.route('/delete-expense')
def delete_expense():
    return render_template('views/delete_expense.html', page_title='Delete Expense')


@app.route('/add-category')
def add_category():
    return render_template('views/add_category.html', page_title='Add Category')


@app.route('/edit-category')
def edit_category():
    return render_template('views/edit_category.html', page_title='Edit Category')


@app.route('/delete-category')
def delete_category():
    return render_template('views/delete_category.html', page_title='Delete Category')


@app.route('/statistics')
def statistics():
    return render_template('views/statistics.html', page_title='Statistics')
