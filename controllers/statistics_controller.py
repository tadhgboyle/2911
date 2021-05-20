"""
This is the controller for all statistics pages.
"""


from flask import render_template, request, url_for
from models import Expense, Category
from datetime import datetime


def show_statistics():

    date = None
    fixed_date = None
    next_date = None

    if 'date' in request.args:
        date = request.args['date']
        fixed_date = datetime.strptime('01-' + date, '%d-%m-%Y').date()
        month = fixed_date.month + 1
        if month == 13:
            month = 1
        next_date = datetime.strptime('01-' + str(month) + '-' + str(fixed_date.year),'%d-%m-%Y').date()

    total_spent = get_total_spent(fixed_date, next_date)
    average_expense_amount = get_average_expense_amount(fixed_date, next_date)

    category_spending_data = get_category_spending_data(fixed_date, next_date)
    category_spending = {
        'labels': [row['name'] for row in category_spending_data],
        'values': [row['total'] for row in category_spending_data]
    }

    top_expenses_data = get_top_expenses_data(fixed_date, next_date)
    top_expenses = {
        'labels': [(row['name'] + ' on ' + str(row['date'])) for row in top_expenses_data],
        'values': [row['amount'] for row in top_expenses_data]
    }

    statistics_url = url_for('statistics')

    return render_template('views/statistics.html', page_name='statistics', page_title='Statistics', total_spent=total_spent, average_expense_amount=average_expense_amount, category_spending=category_spending, top_expenses=top_expenses, statistics_url=statistics_url, date=date)


def get_total_spent(date, next_date):
    """ Get total dollars spent """
    if date is None:
        return Expense.objects().sum('amount')

    amount = 0

    for expense in Expense.objects():
        if expense.date >= date and expense.date <= next_date:
            amount += expense.amount

    return amount


def get_average_expense_amount(date, next_date):
    """ Get average expense amount """
    if date is None:
        return Expense.objects().average('amount')
    
    total = 0
    num = 0
    for expense in Expense.objects():
        if expense.date >= date and expense.date <= next_date:
            total += expense.amount
            num += 1

    try:
        return total / num
    except ZeroDivisionError:
        return 0


def get_category_spending_data(date, next_date):
    """ Get number of dollars spent for each category """
    data = []

    categories = Category.objects()

    for category in categories:
        if date is None:
            data.append({
                'name': category.name,
                'total': "{:.2f}".format(Expense.objects(category_id=category.id).sum('amount'))
            })
        else:
            amount = 0
            for expense in Expense.objects():
                if expense.date >= date and expense.date <= next_date and expense.category_id == category.id:
                    amount += expense.amount

            data.append({
                'name': category.name,
                'total': "{:.2f}".format(amount)
            })

    return data


def get_top_expenses_data(date, next_date):
    """ Get top 10 expenses, sorted by amount spent """
    data = []

    if date is None:
        expenses = Expense.objects().order_by('-amount').limit(10)
    else:
        expenses = []
        num = 1
        for expense in Expense.objects().order_by('-amount'):
            if expense.date >= date and expense.date <= next_date and num <= 10:
                expenses.append(expense)
                num += 1

    for expense in expenses:
        data.append({
            'name': expense.name,
            'amount': expense.amount,
            'date': expense.date
        })

    return data

