from models import Category
from flask import render_template

def list_categories(error=None, success=None):
    return render_template('views/list_categories.html', page_name='list_categories', page_title='List Categories', categories=Category.objects(), error=error, success=success)


def add_category():
    return render_template('views/category_form.html', page_name='add_category', page_title='Add Category')


def edit_category(category_id):
    category = None

    try:
        category = Category.objects.get(id=category_id)
    except:
        return no_category_found()

    if category == None:
        return no_category_found()

    return render_template('views/category_form.html', page_name='edit_category', page_title='Edit Category', category=category)


def delete_category(category_id):
    return list_categories(success='Deleted category')


def no_category_found():
    return list_categories('No category found with that ID')
