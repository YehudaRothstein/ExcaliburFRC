from flask import Flask, render_template, redirect, url_for, request, jsonify
import json

app = Flask(__name__)

JSON_FILE_PATH = "form_data.json"


def update_json_file(data):
    with open(JSON_FILE_PATH, 'w') as json_file:
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

    Data = {
        "amp_value": amp_value,
        "speaker_value": speaker_value,
        "qual_number": qual_number,
        "team": team
    }

    update_json_file(Data)

    return redirect(url_for('Autonomus'))


@app.route("/get_form_data", methods=["GET"])
def get_form_data():
    with open(JSON_FILE_PATH, 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)


if __name__ == '__main__':
    app.run(host="10.97.227.171", port=5000)
