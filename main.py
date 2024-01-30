import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import json

app = Flask(__name__)

app = Flask(__name__)
session = {}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/Scout", methods=["POST", "GET"])
def scout():
    if request.method == 'POST':
        data = request.form.to_dict()

        # Load existing data from the JSON file
        existing_data = []
        json_file_path = "static/Data.json"
        if os.path.exists(json_file_path):
            with open(json_file_path, "r") as file:
                existing_data = json.load(file)

        # Append new form data to the existing data
        existing_data.append(data)

        # Write the updated data back to the JSON file
        with open(json_file_path, "w") as file:
            json.dump(existing_data, file)

        return "Data saved successfully"

    return render_template("Scout.html")

@app.route('/get-json-data')
def get_json_data():
    return send_from_directory('static', 'Data.json')

# Your other existing routes...

@app.route("/process_form", methods=["POST"])
def process_form():
    # Get data from the form
    scout_data = request.form.to_dict()

    # Write data to the JSON file
    with open("static/Data.json", "w") as file:
        json.dump(scout_data, file)

    return "Data saved successfully"




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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    app.secret_key = 'your_secret_key_here'
