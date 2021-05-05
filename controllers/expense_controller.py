"""
This is the controller for all Expense objects.
It contains functions to list, create, edit and delete expenses.
Code is in this controller so we can reuse the functions without accidentally running into circular imports.
"""


from models import Expense, Category
from flask import render_template, request
from forms import ExpenseForm
from utils import parse_form_errors


def list_expenses(error=None, success=None):
    return render_template('views/list_expenses.html', page_name='list_expenses', page_title='List Expenses', expenses=Expense.objects(), error=error, success=success)


def add_expense():

    form = ExpenseForm(request.form)
    if request.method == 'POST':
        if form.validate(): 
            expense = Expense(name=form.name.data, category_id=form.category_id.data, amount=form.amount.data, date=form.date.data)
            expense.save()
            return list_expenses(success='Created new expense "{}".'.format(form.name.data))
        else:
            return render_template('views/expense_form.html', page_name='add_expense', page_title='Add Expense', categories=Category.objects(), errors=parse_form_errors(form.errors.items()))

    return render_template('views/expense_form.html', page_name='add_expense', page_title='Add Expense', categories=Category.objects())


def edit_expense(expense_id):

    form = ExpenseForm(request.form)
    if request.method == 'POST':
        expense = Expense.objects.get(id=form.expense_id.data)
        if form.validate():
            expense.name = form.name.data
            expense.category_id = form.category_id.data
            expense.amount = form.amount.data
            expense.date = form.date.data
            expense.save()
            return list_expenses(success='Updated expense "{}".'.format(form.name.data))
        else:
            return render_template('views/expense_form.html', page_name='edit_expense', page_title='Edit Expense', expense=expense, categories=Category.objects(), errors=parse_form_errors(form.errors.items()))

    expense = __get_expense(expense_id)

    if expense == None:
        return no_expense_found()

    return render_template('views/expense_form.html', page_name='edit_expense', page_title='Edit Expense', expense=expense, categories=Category.objects())


def delete_expense(expense_id):

    expense = __get_expense(expense_id)

    if expense == None:
        return no_expense_found('Cannot delete, no expense found with that ID.')

    expense.delete()

    return list_expenses(success='Deleted expense "{}".'.format(expense.name))


def no_expense_found(error_message='No expense found with that ID'):
    return list_expenses(error_message)


def __get_expense(expense_id):

    expense = None

    try:
        expense = Expense.objects.get(id=expense_id)
    except:
        return None

    return expense
