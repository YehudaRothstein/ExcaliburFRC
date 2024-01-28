from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Excalibur 6738 ScoutSystem <H1>6738<H1>"


if __name__ == __name__:
    app.run()
