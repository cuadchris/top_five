from app import app
from flask import render_template
from app.model import topfive

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')

@app.route("/topfive")
def topFive():
    return render_template('topfive.html', title="Top Five", topfive = topfive)