"""
This is the controller for all Category objects.
It contains functions to list, create, edit and delete categories.
Code is in this controller so we can reuse the functions without accidentally running into circular imports.
"""

from models import Category
from flask import render_template

def list_categories(error=None, success=None):
    return render_template('views/list_categories.html', page_name='list_categories', page_title='List Categories', categories=Category.objects(), error=error, success=success)


def add_category():
    return render_template('views/category_form.html', page_name='add_category', page_title='Add Category')


def edit_category(category_id):
    category = __get_category(category_id)

    if category == None:
        return no_category_found()

    return render_template('views/category_form.html', page_name='edit_category', page_title='Edit Category', category=category)


def delete_category(category_id):
    category = __get_category(category_id)

    if category == None:
        return no_category_found('Cannot delete, no category found with that ID.')

    category.delete()

    return list_categories(success='Deleted category "{}"'.format(category.name))


def no_category_found(error_message='No category found with that ID'):
    return list_categories(error_message)


def __get_category(category_id):
    category = None

    try:
        category = Category.objects.get(id=category_id)
    except:
        return None

    return category
