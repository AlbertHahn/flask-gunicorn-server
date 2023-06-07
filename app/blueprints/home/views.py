from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder="templates")

@home.route("/")
def show_home():
        return render_template('index.html')