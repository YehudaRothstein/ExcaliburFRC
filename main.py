from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/<name>")
def home_with_name(name):
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("new.html")


# Rename the conflicting route function
@app.route("/test_new")
def test_new():
    return render_template("new.html")


@app.route("/ReportBugs", methods=["POST", "GET"])
def ReportBug():
    return render_template("Report.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route("/Scout", methods=["POST", "GET"])
def Scout():
    return render_template("Scout.html")


@app.route("/Autonomus", methods=["POST", "GET"])
def Autonomus():
    return render_template("autonomous.html")


# New route for form processing
@app.route("/process_form", methods=["POST"])
def process_form():
    # Process form data here if needed

    # Redirect to /Autonomus
    return redirect(url_for('Autonomous'))


if __name__ == '__main__':
    app.run()
