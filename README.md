# Working on Expenses

## Running the Flask server
- cd into directory, do 'python3 -m venv venv' (on windows: 'py -3 -m venv venv)
- and then run `source venv/bin/activate` (on windows: `source venv/scripts/activate`)
- (if first time working) run `pip3 install Flask && pip install flask_mongoengine`
- type `export FLASK_APP=main.py`
- type `export FLASK_ENV=development` (this will reload the flask server when you save code changes)
- type `flask run`
- visit `http://localhost:5000` in your web browser
- try not to break anything!

## About HTML pages
- to reduce reused code, all our html pages will "extend" the base html page `templates/layout.html`
    - this layout page has the doctype, header, and basic page layout tags already
- all pages for each section of the app are in `templates/views/` directory
    - for example, the List Expenses page is `templates/views/list_expenses.html`
