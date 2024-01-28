from flask import Flask, redirect, url_for
#CoBranch
app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Excalibur 6738 ScoutSystem <H1>6738<H1>"
@app.route("/admin")
def admin(name):
     return redirect(url_for("/"))


if __name__ == __name__:
    app.run()
