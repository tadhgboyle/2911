"""
This module defines blueprints and validation rules for any HTML forms needed in our Expense application
"""
from wtforms import Form, StringField, validators


class CategoryForm(Form):
    name = StringField('name', [validators.Length(min=3, max=64)])
    # used when editing a category to find it from the database, ignored when making new category
    category_id = StringField('category_id')
