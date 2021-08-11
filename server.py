from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def intro():
    return render_template("index.html", name="Gauri")
