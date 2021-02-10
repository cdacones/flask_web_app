# imports the Flask module from the flask package
from flask import Flask

# creates an object using the Flask module
app = Flask(__name__)

# tells the app when to call the view function by creating a URL route.
# all view functions are associated with a URL route
# route is a decorator
@app.route("/")
def hello():
    return "Hello World!";

# runs the application in main
if __name__ == "__main__":
    app.run()

# tells the app to show output in the browser, creates a view function
# def hello():
#   return "Hello World!";
