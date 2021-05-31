from flask import Flask
import os
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
project_dir =os.path.dirname(os.path.abspath(__file__))
database_file="splite:///{}".format(os.path.join(project_dir,"bookdatabase.db"))

app.config["SQLALCHEMY_URI"] = database_file
db = SQLAlCHEMY(app)

class book(db.model):
    title = d.column(db.string(80), unique=true, nullable=false, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

@app.route("/"), methods=["GET", "POST"])

def home():
    if request.form:
        print(project_dir)
    return render_template("bookstore.html")