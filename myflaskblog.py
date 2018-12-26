from flask import Flask, render_template
#__name__ is a special variable in python that is just the name of the module.
#if we run the script with python directly its equal to __main__
#that flask knows where to look for templates and static files etc.
app = Flask(__name__)

post = [
    {
        'author': 'Alice Stang',
        'titel': 'The first blog post',
        'content': 'The first content',
        'date': '2018-12-26'
    },
    {
        'author': 'David Stang',
        'titel': 'The second blog post',
        'content': 'The second content',
        'date': '2018-12-27'
    }
]

#define the routes
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', post=post)

@app.route("/about")
def about():
    return render_template('about.html')

#if you want to run it directly from python in debug mode without using the global 
if __name__=='__main__':
    app.run(debug=True)