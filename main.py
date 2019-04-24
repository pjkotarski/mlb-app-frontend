from flask import flask, render_template
import subprocess
from create_db import app, db, User

#okay, how do you want the API to work?


'''
    there are two sides to this, that which loads the main shit and htat which loads the
    api stuff that you're downloading otherwise.

    the api stuff you can load in with your qualifiers for what piece of data it is that your
    want.

    we can try to do this wth the standings page right now, along with start creating the models for a user,
    their username password, favorite team and shit like that.


'''

@app.route('/')
def index():
