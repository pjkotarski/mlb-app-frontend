from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
#from passlib.apps import custom_app_context as pwd_context


app = Flask(__name__)
#following lines will need to be modified for the new postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:asd123@localhost:5432/sharks1')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#begin considering options for how the backend should be set up
#so that it is easily scallable

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), index = True)
    email = db.Column(db.String(64))
    passhash = db.Column(db.String(128))
    favTeam = db.Column(db.String(8))



    #this top method will take the password pased by user and assign
    #a hash to it this password is then not used agian
    def hash_password(self, password):
        self.passhash = pwd_context.encrypt(password)

    #verify password will take the attempted hash_password input and test
    def verify_password(self, password):
        return pwd_context.verify(password, self.passhash)
