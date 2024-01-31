import os, socket

from flask import Flask, render_template, redirect, url_for, request, jsonify, send_from_directory
import json

from pip._internal.utils import datetime

app = Flask(__name__)
session ={}
session = {}
socket.getaddrinfo('localhost', 5000)
LOCAL_IP = '192.168.1.103'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Scout", methods=["POST", "GET"])
def scout():
    try:
        if request.method == 'POST':
            data = request.get_json()  # Get the JSON data from the request
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

            try:
                with open(json_file_path, "w") as file:
                    json.dump(existing_data, file, indent=4)  # pretty-print the JSON data
            except Exception as e:
                print(f"An error occurred while writing to the file: {e}")

            return "Data saved successfully"
    except Exception as e:
        print(f"An error occurred: {e}")
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

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/Autonomous", methods=["POST", "GET"])
def Autonomus():
    return render_template("autonomous.html", local_ip=LOCAL_IP)

@app.route('/get-json')
def get_json():
    return send_from_directory('static', 'Data.json')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    app.secret_key = 'your_secret_key_here'

