from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)


@app.route("/data_structures/")
def render_data_structures():

    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    return render_template("data_structures.html", movies=movies)
