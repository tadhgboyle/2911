"""
This is the controller for all statistics pages.
"""


from flask import render_template
from models import Expense, Category


def show_statistics():

    category_spending_data = get_category_spending_data()

    category_spending = {
        'labels': [row['name'] for row in category_spending_data],
        'values': [row['total'] for row in category_spending_data]
    }

    return render_template('views/statistics.html', page_name='statistics', page_title='Statistics', category_spending=category_spending)


def get_category_spending_data():

    data = []

    categories = Category.objects()

    for category in categories:
        data.append({
            'name': category.name,
            'total': "{:.2f}".format(Expense.objects(category_id=category.id).sum('amount'))
        })

    return data
