
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/birds")
def birdPage():
    return render_template("bird.html")


@app.route("/seasons")
def seasonsPage():

    now = datetime.now()

    current_month = now.strftime("%B")

    current_year = now.year

    return render_template("seasons.html", month=current_month, year=current_year)

@app.route("/birdfact")
def birdFacts():
    Bird_name = "Common Kingfisher"
    Scientific_name = "Alcedo atthis"
    habitat = "Rivers, lakes and ponds"
    Diet = "Fish and aquatic insects"
    return render_template("birdfact.html", Bird_name=Bird_name, Scientific_name=Scientific_name, habitat=habitat, Diet=Diet)

@app.route("/favoritebird")
def favoriteBird():
    bird_name = "Common Kingfisher"
    reason = "Beautiful colors and amazing fishing skills"
    return render_template("favoritebird.html", bird_name=bird_name, reason=reason)