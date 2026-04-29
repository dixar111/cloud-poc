from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Codespaces Docker çalışıyor")
    return render_template("index.html", message=message)

@app.route("/about")
def about():
    return "<h2>Bu proje Docker + Flask PoC çalışmasıdır.</h2>"

app.run(host="0.0.0.0", port=5000)
