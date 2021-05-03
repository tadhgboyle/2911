from flask import Flask
from models import db, Expense

app = Flask(__name__)
app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/2911'

db.init_app(app)

import routes
