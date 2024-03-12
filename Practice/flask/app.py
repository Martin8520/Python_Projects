from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/data_structures/")
def render_data_structures():

    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    car = {
        "brand": "BMW",
        "model": "M5",
        "year": "2020",
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {
        "movies": movies,
        "car": car,
        "moons": moons,
    }
    return render_template("data_structures.html", movies=movies, car=car, moons=moons)
