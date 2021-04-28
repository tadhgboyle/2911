# Working on Expenses

## Running the Flask server
- cd into directory and run `source venv/bin/activate`
- (if first time working) run `pip3 install Flask`
- type `export FLASK_APP=main.py`
- type `export FLASK_ENV=development` (this will reload the flask server when you save code changes)
- type `flask run`
- try not to break anything!

## About HTML pages
- to reduce reused code, all our html pages will "extend" the base html page `templates/layout.html`
    - this layout page has the doctype, header, and basic page layout tags already
- all pages for each section of the app are in `templates/views/` directory
    - for example, the List Expenses page is `templates/views/list_expenses.html`