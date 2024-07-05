from flask import Blueprint, flash, render_template

view = Blueprint('view', __name__)

@view.route("/")
def home():
  return render_template("home.html")