from flask import Flask, render_template, request

'''
It creates a an instance of flask class,
which will be your WSGI(web server gateway interface) application.

'''

## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>welcome to this flask course online</H1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"<h1>Thank you, {name}! Your email {email} has been received.</h1>"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)