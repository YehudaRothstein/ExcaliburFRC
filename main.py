import os

from flask import Flask, render_template, redirect, url_for, request, jsonify
import json

from pip._internal.utils import datetime

app = Flask(__name__)

JSON_FILE_PATH = "form_data.json"


def update_json_file(data):
    with open("C:\\Users\\excal\\PycharmProjects\\ExcaliburFRC\\Scout\\Data.JSON", 'w') as json_file:
        json.dump(data, json_file)


@app.route("/<name>")
def home_with_name(name):
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("new.html")


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


@app.route("/process_form", methods=["POST"])
def process_form():
    amp_value = int(request.form.get("amp_value"))
    speaker_value = int(request.form.get("speaker_value"))
    qual_number = request.form.get("qual_number")
    team = request.form.get("team")

    data = {
        "amp_value": amp_value,
        "speaker_value": speaker_value,
        "qual_number": qual_number,
        "team": team
    }

    # Generate a filename based on the current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_filename = f"Data_{timestamp}.json"
    json_filepath = os.path.join("C:\\Users\\excal\\PycharmProjects\\ExcaliburFRC\\Scout\\Data.JSON")

    # Save data to the JSON file
    update_json_file(data, json_filepath)

    return redirect(url_for('Autonomus'))


if __name__ == '__main__':
    app.run()
