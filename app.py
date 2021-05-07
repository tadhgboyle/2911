"""
This module creates and initializes the flask application instance. It also handles forwarding all requests to the application towards their respective controller.
"""

from flask import Flask, render_template
from models import db
from controllers import expense_controller, category_controller

def create_app():
    app = Flask(__name__)
    app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/2911'
    db.init_app(app)

    @app.route('/')
    def list_expenses():
        return expense_controller.list_expenses()


    @app.route('/add-expense', methods=['GET', 'POST'])
    def add_expense():
        return expense_controller.add_expense()


    @app.route('/edit-expense/<expense_id>', methods=['GET', 'POST'])
    def edit_expense(expense_id):
        return expense_controller.edit_expense(expense_id)


    @app.route('/delete-expense/<expense_id>')
    def delete_expense(expense_id):
        return expense_controller.delete_expense(expense_id)


    @app.route('/list-categories')
    def list_categories():
        return category_controller.list_categories()


    @app.route('/add-category', methods=['GET', 'POST'])
    def add_category():
        return category_controller.add_category()


    @app.route('/edit-category/<category_id>', methods=['GET', 'POST'])
    def edit_category(category_id):
        return category_controller.edit_category(category_id)


    @app.route('/delete-category/<category_id>')
    def delete_category(category_id):
        return category_controller.delete_category(category_id)


    @app.route('/statistics')
    def statistics():
        return render_template('views/statistics.html', page_name='statistics', page_title='Statistics')

    return app
