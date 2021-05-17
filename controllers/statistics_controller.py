"""
This is the controller for all statistics pages.
"""


from flask import render_template, request, url_for
from models import Expense, Category


def show_statistics():

    total_spent = get_total_spent()
    average_expense_amount = get_average_expense_amount()

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

    statistics_url = url_for('statistics')

    date = None

    if 'date' in request.args:
        date = request.args['date']

    return render_template('views/statistics.html', page_name='statistics', page_title='Statistics', total_spent=total_spent, average_expense_amount=average_expense_amount, category_spending=category_spending, top_expenses=top_expenses, statistics_url=statistics_url, date=date)


def get_total_spent():
    """ Get total dollars spent """
    return Expense.objects().sum('amount')


def get_average_expense_amount():
    """ Get average expense amount """
    return Expense.objects().average('amount')


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

# def display_specific_time_graph():
#     """ displays a certain graph based on the query strings (url parameters) """

#     arg1 = request.args['arg1']

#     return 'Arg1 : ' + arg1


