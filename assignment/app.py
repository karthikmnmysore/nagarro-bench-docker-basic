# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My Simple Flask App!"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Important: bind to 0.0.0.0 so it works in Docker
    app.run(host="0.0.0.0", port=5000, debug=True)
