from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template("first_page.html")


@app.route("/second")
def hello_world_fancy():
    return render_template("second_page.html")
