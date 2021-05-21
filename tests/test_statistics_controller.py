""" This module contains all testing for the statistics controller. """

import pytest
from controllers import statistics_controller
from models import Expense
import datetime
from .sample_data import create_sample_data, delete_sample_data

def test_get_total_spent():
    """ Tests if get_total_spent returns the correct total. """
    
    # Creates sample data that will be used in test
    create_sample_data()

    # Compares return values to sample data
    assert statistics_controller.get_total_spent(None, None) == Expense.objects().sum('amount')
    assert int(statistics_controller.get_total_spent(None, None)) == 101
    assert statistics_controller.get_total_spent(datetime.date(2021, 1, 1), datetime.date(2021, 2, 1)) == Expense.objects().sum('amount')
    assert statistics_controller.get_total_spent(datetime.date(2021, 1, 1), datetime.date(2021, 2, 1)) == 101

    # Deletes sample data that was used in test
    delete_sample_data()

def test_get_average_expense_amount():
    """ Tests if get_average_expenses returns the correct value. """

    # Creates sample data that will be used in test
    create_sample_data()

    # Compares return values to sample data
    assert round(statistics_controller.get_average_expense_amount(None, None), 2) == 9.18
    assert round(statistics_controller.get_average_expense_amount(datetime.date(2021, 1, 1), datetime.date(2021, 2, 1)), 2) == 9.18

    # Deletes sample data that was used in test
    delete_sample_data()

def test_get_category_spending_data():
    """ Tests if get_category_data returns the correct categories. """

    # Creates sample data that will be used in test
    create_sample_data()
    
    # Compares return values to sample data
    assert statistics_controller.get_category_spending_data(None, None) == [{'name': 'Test Category', 'total': '101.00'}]
    assert statistics_controller.get_category_spending_data(datetime.date(2021, 1, 1), datetime.date(2021, 2, 1)) == [{'name': 'Test Category', 'total': '101.00'}]

    # Deletes sample data that was used in test
    delete_sample_data()

def test_get_top_expenses_data():
    """ Tests if get_top_expenses returns the correct expenses. """

    # Creates sample data that will be used in test
    create_sample_data()

    # Compares return values to sample data
    top_expenses = statistics_controller.get_top_expenses_data(None, None)
    for expense in top_expenses:
        assert expense['name'] != 'Expense 11'
    top_expenses = statistics_controller.get_top_expenses_data(datetime.date(2021, 1, 1), datetime.date(2021, 2, 1))
    for expense in top_expenses:
        assert expense['name'] != 'Expense 11'

    # Deletes sample data that was used in test
    delete_sample_data()