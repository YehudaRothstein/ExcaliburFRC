import os

from flask import Flask, render_template, redirect, url_for, request, jsonify, send_from_directory
import json

from pip._internal.utils import datetime

app = Flask(__name__)
session = {}

@app.route("/<name>")
def home_with_name(name):
    return render_template("index.html")


@app.route("/home")
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
    if request.method == 'POST':
        scout_data = request.form.to_dict()

        with open("static/Data.json", "w") as file:
            json.dump(scout_data, file)


    return render_template("Scout.html")

@app.route("/process_form", methods=["POST"])
def process_form():
    autonomus_data = request.form.to_dict()

    # Write to JSON file
    with open("static/Data.JSON", "w") as file:
        json.dump(autonomus_data, file)

    return "Data saved successfully"


@app.route("/Autonomous", methods=["POST", "GET"])
def Autonomus():
    return render_template("autonomous.html")

@app.route('/get-json')
def get_json():
    return send_from_directory('static', 'Data.json')

if __name__ == '__main__':
    app.run(host="10.97.227.83", port=5000, debug=True)
    app.secret_key = 'your_secret_key_here'

