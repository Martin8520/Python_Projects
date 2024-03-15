from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def todo():
    return render_template("fizzbuzz.html")


def square(value):
    return (value ** 0.5).is_integer()


app.jinja_env.tests["square"] = square
