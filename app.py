from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Varsayılan mesaj")
    return f"<h1>{message}</h1>"

app.run(host="0.0.0.0", port=5000)
