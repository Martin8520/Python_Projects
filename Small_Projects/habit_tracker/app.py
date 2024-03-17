from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
habits = ["Test habit", "Test habit 2", "Rest"]


def date_range(start: datetime.date):
    dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
    return dates


@app.route("/")
def index():
    return render_template("index.html", habits=habits, title="Habit Tracker - Home", date_range=date_range)


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habits.append(request.form.get("habit"))

    return render_template("add_habit.html", title="Habit Tracker - Add Habit")
