from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Hello, World!</h1>"

@app.route("/skillset/update")
def updateskillset():
    return render_template("updateskill.html")