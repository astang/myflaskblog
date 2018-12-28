from flask import render_template, url_for, flash, redirect
from myflaskblog import app
from myflaskblog.forms import RegistrationForm, LoginForm
from myflaskblog.models import User, Post

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