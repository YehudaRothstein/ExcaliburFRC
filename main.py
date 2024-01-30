import os, json
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)
session ={}

@app.route("/")
def home():
    return render_template("index.html")

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
    return render_template("new.html")

@app.route("/test_new")
def test_new():
    return render_template("new.html")

@app.route("/ReportBugs", methods=["POST", "GET"])
def ReportBug():
    return render_template("Report.html")


if __name__ == '__main__':
    app.secret_key = 'your_secret_key_here'
    app.run(host="192.168.1.103", port=5000, debug=True)