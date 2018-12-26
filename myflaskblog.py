from flask import Flask
#__name__ is a special variable in python that is just the name of the module.
#if we run the script with python directly its equal to __main__
#that flask knows where to look for templates and static files etc.
app = Flask(__name__)

#define the routes
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page!</h1>"

#if you want to run it directly from python in debug mode without using the global 
if __name__=='__main__':
    app.run(debug=True)