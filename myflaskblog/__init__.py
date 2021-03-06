import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
#__name__ is a special variable in python that is just the name of the module.
#if we run the script with python directly its equal to __main__
#that flask knows where to look for templates and static files etc.
app = Flask(__name__)
#generated with python import secrets and secret.token_hex(16)
app.config['SECRET_KEY']='0048eb592aa1faf4bc89e5ca99a68a85'
#set database SQL lite for now
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
#create a SQL Instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
#in bootstrap info is blue colored info alert
login_manager.login_message_category='info'
#email server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] =587
app.config['MAIL_USE_TLS'] =True
app.config['MAIL_USERNAME'] =os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] =os.environ.get('EMAIL_PASS')
mail = Mail(app)


#has to be done below otherwise stuck in a import loop between zhe files
from myflaskblog import routes

