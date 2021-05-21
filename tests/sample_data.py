""" This module contains functions that create and delete sample data that is needed for some of the tests. """

from models import Category, Expense
import datetime

def create_sample_data():
    """ 
        Creates sample data for testing.
        There should be 11 expenses totaling $101.00. All have the same category and date. 
    """
    
    # Creates a sample category and sample date that can be used to create sample expenses
    sample_category = Category(name='Test Category')
    sample_category.save()
    sample_date = datetime.date(2021, 1, 1)
    
    # Creates 11 sample expenses, last expense created has a lower amount so it can be tested to see if it is excluded in the top ten highest expenses graph
    for i in range(10):
        i += 1
        new_expense = Expense(name='Expense {}'.format(str(i)), category_id=sample_category.id, amount=10, date=sample_date)
        new_expense.save()
    new_expense = Expense(name='Expense 11', category_id=sample_category.id, amount=1, date=sample_date)
    new_expense.save()

def delete_sample_data():
    """ Deletes sample data created for testing. """
    for i in range(11):
        i += 1
        Expense.objects.get(name='Expense {}'.format(str(i))).delete()
    Category.objects.get(name='Test Category').delete()

def delete_existing_data():
    """ Deletes any existing data. """
    Expense.objects().delete()
    Category.objects().delete()