from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

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

class User(db.Model) : 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #one to many relationship one author cna have many post, one post depends on one author
    #referencing the class Post
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model) : 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    #refrencing the table namen and column name not the class thats why user small case
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date}')"

posts = [
    {
        'author': 'Alice Stang',
        'title': 'The first blog post',
        'content': 'The first content',
        'date': '2018-12-26'
    },
    {
        'author': 'David Stang',
        'title': 'The second blog post',
        'content': 'The second content',
        'date': '2018-12-27'
    }
]

#define the routes
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Blog Page!')

@app.route("/about")
def about():
    return render_template('about.html', title='About page!')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #different alert messages possible
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    #else:
    #    flash('Login unsuccessful. Please check username, email and password.', 'danger')
    return render_template('register.html', title='Register', form=form) 

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'alice@stacom.de' and form.password.data == 'test' :
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form) 

#if you want to run it directly from python in debug mode without using the global 
if __name__=='__main__':
    app.run(debug=True)