from app import app
from flask import render_template

# view functions
@app.route('/')
@app.route('/home')
def index():
    user = {'username': 'Daniel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ] # Mock object for a system of users 
    return render_template('home.html', title='Home', user=user , posts=posts)