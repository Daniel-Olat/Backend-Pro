from app import app
from flask import render_template

# view functions
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Daniel'}
    return render_template('index.html', title='Home', user=user)