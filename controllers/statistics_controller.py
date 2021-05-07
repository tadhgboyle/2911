"""
This is the controller for all statistics pages.
"""


from flask import render_template
from models import Expense, Category


def show_statistics():

    total_spent = get_total_spent()

    category_spending_data = get_category_spending_data()
    category_spending = {
        'labels': [row['name'] for row in category_spending_data],
        'values': [row['total'] for row in category_spending_data]
    }

    top_expenses_data = get_top_expenses_data()
    top_expenses = {
        'labels': [(row['name'] + ' on ' + str(row['date'])) for row in top_expenses_data],
        'values': [row['amount'] for row in top_expenses_data]
    }

    return render_template('views/statistics.html', page_name='statistics', page_title='Statistics', total_spent=total_spent, category_spending=category_spending, top_expenses=top_expenses)


def get_total_spent():
    """ Get total dollars spent """
    return Expense.objects().sum('amount')


def get_category_spending_data():
    """ Get number of dollars spent for each category """
    data = []

    categories = Category.objects()

    for category in categories:
        data.append({
            'name': category.name,
            'total': "{:.2f}".format(Expense.objects(category_id=category.id).sum('amount'))
        })

    return data


def get_top_expenses_data():
    """ Get top 10 expenses, sorted by amount spent """
    data = []

    expenses = Expense.objects().order_by('-amount').limit(10)

    for expense in expenses:
        data.append({
            'name': expense.name,
            'amount': expense.amount,
            'date': expense.date
        })

    return data
