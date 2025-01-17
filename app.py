from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///empskills.db')

db = SQLAlchemy(app)

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    skills= db.column(db.Text())

with app.app_context():
    if not os.path.exists('empskills.db'):
        db.create_all()

@app.route("/")
def homepage():
    return "<h1>Hello, World!</h1>"

@app.route("/skillset/update", methods=["GET","POST"])
def updateskillset():
    if request.method == "POST":
        email = request.form.get("email")
        skills = request.form.get("skills")
        new_skill = Skills(email=email, skills=skills)
        db.session.add(new_skill)
        db.session.commit()
        return render_template("updateskill.html", success="Skillset updated successfully")
    return render_template("updateskill.html")