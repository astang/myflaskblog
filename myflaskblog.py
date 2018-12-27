from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
#__name__ is a special variable in python that is just the name of the module.
#if we run the script with python directly its equal to __main__
#that flask knows where to look for templates and static files etc.
app = Flask(__name__)
#generated with python import secrets and secret.token_hex(16)
app.config['SECRET_KEY']='0048eb592aa1faf4bc89e5ca99a68a85'

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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form) 

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form) 

#if you want to run it directly from python in debug mode without using the global 
if __name__=='__main__':
    app.run(debug=True)