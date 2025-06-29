from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template('index.html')

@main.route("/algorithms")
def algorithms():
    return render_template("algorithms.html")

@main.route("/data-structures")
def data_structures():
    return render_template("data_structures.html")