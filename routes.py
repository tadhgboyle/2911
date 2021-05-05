"""
This module handles forwarding all requests to the application towards their respective controller.
"""

# TODO: Move form logic to controllers
# TODO: form Validation errors display to user 

from main import app
from flask import render_template, request
import expense_controller
import category_controller
from models import Expense, Category
from forms import ExpenseForm, CategoryForm


@app.route('/')
def list_expenses():
    return expense_controller.list_expenses()


@app.route('/add-expense', methods=['GET', 'POST'])
def add_expense():

    form = ExpenseForm(request.form)
    if request.method == 'POST' and form.validate(): 
        expense = Expense(name=form.name.data, category_id=form.category_id.data, amount=form.amount.data, date=form.date.data)
        expense.save()
        return expense_controller.list_expenses(success='Created new expense "{}".'.format(form.name.data))

    return expense_controller.add_expense()


@app.route('/edit-expense/<expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):

    form = ExpenseForm(request.form)
    if request.method == 'POST' and form.validate():
        expense = Expense.objects.get(id=form.expense_id.data)
        expense.name = form.name.data
        expense.category_id = form.category_id.data
        expense.amount = form.amount.data
        expense.date = form.date.data
        expense.save()
        return expense_controller.list_expenses(success='Updated expense "{}".'.format(form.name.data))

    return expense_controller.edit_expense(expense_id)


@app.route('/delete-expense/<expense_id>')
def delete_expense(expense_id):
    return expense_controller.delete_expense(expense_id)


@app.route('/list-categories')
def list_categories():
    return category_controller.list_categories()


@app.route('/add-category', methods=['GET', 'POST'])
def add_category():

    form = CategoryForm(request.form)
    if request.method == 'POST' and form.validate():
        category = Category(name=form.name.data)
        category.save()
        return category_controller.list_categories(success='Created new category "{}".'.format(form.name.data))

    return category_controller.add_category()


@app.route('/edit-category/<category_id>', methods=['GET', 'POST'])
def edit_category(category_id):

    form = CategoryForm(request.form)
    if request.method == 'POST' and form.validate():
        category = Category.objects.get(id=form.category_id.data)
        category.name = form.name.data
        category.save()
        return category_controller.list_categories(success='Updated category "{}".'.format(form.name.data))

    return category_controller.edit_category(category_id)


@app.route('/delete-category/<category_id>')
def delete_category(category_id):
    return category_controller.delete_category(category_id)


@app.route('/statistics')
def statistics():
    return render_template('views/statistics.html', page_name='statistics', page_title='Statistics')
