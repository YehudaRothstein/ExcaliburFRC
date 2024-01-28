from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<name>")
def home_with_name(name):
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("new.html")

@app.route("/test")
def test():
    return render_template("new.html")

@app.route("/ReportBugs", methods=["POST", "GET"])
def ReportBug():
    return render_template("Report.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == '__main__':
    app.run()
