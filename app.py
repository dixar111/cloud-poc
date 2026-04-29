from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Codespaces Docker çalışıyor")

    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("{{ message }}", message)

    return html

@app.route("/about")
def about():
    return "<h2>Bu proje Docker + Flask PoC çalışmasıdır</h2>"

app.run(host="0.0.0.0", port=5000)
