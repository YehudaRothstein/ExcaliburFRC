
import os, socket

from flask import Flask, render_template, redirect, url_for, request, jsonify, send_from_directory
import json

from pip._internal.utils import datetime

app = Flask(__name__)
session = {}
socket.getaddrinfo('localhost', 5000)

LOCAL_IP = socket.gethostbyname(socket.gethostname())

@app.route("/Scout", methods=["POST", "GET"])
def scout():
    if request.method == 'POST':
        data = request.form.to_dict()
        existing_data = {}
        json_file_path = "static/Data.json"
        if os.path.exists(json_file_path) and os.path.getsize(json_file_path) > 0:
            with open(json_file_path, "r") as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    print("JSONDecodeError: The file is empty or not properly formatted")

        key = data['team']
        if key not in existing_data:
            existing_data[key] = []
        existing_data[key].append(data)

        with open(json_file_path, "w") as file:
            json.dump(existing_data, file, indent=4)  # pretty-print the JSON data

        return "Data saved successfully"

    return render_template("Scout.html")

@app.route('/get-json-data')
def get_json_data():
    return send_from_directory('static', 'Data.json')

@app.route("/process_form", methods=["POST"])
def process_form():
    return "Form processed successfully"

@app.route("/home")
def test():
    return render_template("new.html", local_ip=LOCAL_IP)

@app.route("/test_new")
def test_new():
    return render_template("new.html", local_ip=LOCAL_IP)

@app.route("/ReportBugs", methods=["POST", "GET"])
def ReportBug():
  return render_template("Report.html", local_ip=LOCAL_IP)



@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



@app.route("/process_form", methods=["POST"])
def process_form():
    autonomus_data = request.form.to_dict()

    # Write to JSON file
    with open("static/Data.JSON", "w") as file:
        json.dump(autonomus_data, file)

    return "Data saved successfully"


@app.route("/Autonomous", methods=["POST", "GET"])
def Autonomus():
    return render_template("autonomous.html", local_ip=LOCAL_IP)

@app.route('/get-json')
def get_json():
    return send_from_directory('static', 'Data.json')

if __name__ == '__main__':
    app.run(host=LOCAL_IP, port=5000, debug=True)
    app.secret_key = 'your_secret_key_here'
    app.run(host="192.168.1.103", port=5000, debug=True)