"""
Main initialization module for the Expenses application.
You will not need to edit this file, likely ever.
"""

from app import create_app

app = create_app()
app.run(debug=True)
