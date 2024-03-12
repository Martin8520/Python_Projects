from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)


@app.route("/expressions/")
def hello_world():
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    first_name = "Captain"
    last_name = "Marvel"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": 10,
        "apple_amount": 20,
        "donate_amount": 15,
        "first_name": "Captain",
        "last_name": "Marvel",
        }
    return render_template("expressions.html", **kwargs)
