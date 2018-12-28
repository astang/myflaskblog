from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#__name__ is a special variable in python that is just the name of the module.
#if we run the script with python directly its equal to __main__
#that flask knows where to look for templates and static files etc.
app = Flask(__name__)
#generated with python import secrets and secret.token_hex(16)
app.config['SECRET_KEY']='0048eb592aa1faf4bc89e5ca99a68a85'
#set database SQL lite for now
app.config['SQLAlchemy_DATABASE_URI'] ='sqlite:///site.db'
#create a SQL Instance
db = SQLAlchemy(app)

#has to be done below otherwise stuck in a import loop between zhe files
from myflaskblog import routes
