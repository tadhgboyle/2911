from main import app
from flask import render_template


@app.route('/')
def expenses_list():
   return 'Your expenses'


@app.route('/add-expense')
def add_expense():
    return 'Add expense'


@app.route('/edit-expense')
def edit_expense():
    return 'Edit expense'


@app.route('/delete-expense')
def delete_expense():
    return 'Delete expense'


@app.route('/add-category')
def add_category():
    return 'Add category'


@app.route('/edit-category')
def edit_category():
    return 'Edit category'


@app.route('/delete-category')
def delete_category():
    return 'Delete category'


@app.route('/statistics')
def statistics():
    return 'Statistics'


@app.route('/template')
def test():
    return render_template('test.html', user={'first_name': 'Tadhg', 'last_name': 'Boyle'})
