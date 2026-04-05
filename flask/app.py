from flask import Flask

'''
It creates a an instance of flask class,
which will be your WSGI(web server gateway interface) application.

'''

## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this flask course online"

if __name__ == "__main__":
    app.run(debug=True)