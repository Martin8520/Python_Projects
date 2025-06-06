from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Joe")


@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)


@views.route("/json")
def get_json():
    return jsonify({"name": "Tim", "age": "35", "address": "125 Homer Street"})


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


@views.route("/go-to-json")
def go_to_home():
    return redirect(url_for("views.get_json"))
