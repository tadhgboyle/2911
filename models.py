"""
This module defines models (aka blueprints) for any objects we need in the Expense application.
"""

from flask_mongoengine import MongoEngine
from wtforms import Form, StringField, validators

db = MongoEngine()


class Expense(db.Document):

    name = db.StringField(required=True, max_length=64)
    category_id = db.ObjectIdField(required=True)
    amount = db.FloatField(required=True)
    date = db.DateTimeField(required=True)

    meta = {
        'collection': 'expenses',
        'ordering': 'date'
    }

    def category(self):
        """ Get corresponding category model for this expense """
        return Category.objects.get(id=self.category_id)


class Category(db.Document):

    name = db.StringField(required=True, max_length=64)

    meta = {
        'collection': 'categories',
        'ordering': 'name'
    }

class CategoryForm(Form):
    name = StringField('name', [validators.Length(min=3, max=64)])
    category_id = StringField('category_id') # used when editing a category to find it from the database, ignored when making new category