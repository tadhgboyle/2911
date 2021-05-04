"""
This is the controller for all Expense objects.
It contains functions to list, create, edit and delete expenses.
Code is in this controller so we can reuse the functions without accidentally running into circular imports.
"""

from models import Expense
from flask import render_template

def list_expenses(error=None, success=None):
    return render_template('views/list_expenses.html', page_name='list_expenses', page_title='List Expenses', expenses=Expense.objects(), error=error, success=success)


def add_expense():
    return render_template('views/expense_form.html', page_name='add_expense', page_title='Add Expense')


def edit_expense(expense_id):
    expense = __get_expense(expense_id)

    if expense == None:
        return no_expense_found()

    return render_template('views/expense_form.html', page_name='edit_expense', page_title='Edit Expense', expense=expense)


def delete_expense(expense_id):

    expense = __get_expense(expense_id)

    if expense == None:
        return no_expense_found('Cannot delete, no expense found with that ID.')

    expense.delete()

    return list_expenses(success='Deleted expense')


def no_expense_found(error_message='No expense found with that ID'):
    return list_expenses(error_message)


def __get_expense(expense_id):
    expense = None

    try:
        expense = Expense.objects.get(id=expense_id)
    except:
        return None

    return expense
