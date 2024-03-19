import os, json
from flask import Flask, render_template,request, send_from_directory, redirect,  flash

app = Flask(__name__)
session ={}
users = {
    'admin': '1234'
}
@app.route("/")
def home():
    return render_template("new.html")

@app.route("/Scout", methods=["POST", "GET"])
def scout():
    try:
        if request.method == 'POST':
            data = request.get_json()
            json_file_path = "/home/yehudarothstein/mysite/static/Data.JSON"
            existing_data = []

            if os.path.exists(json_file_path) and os.path.getsize(json_file_path) > 0:
                with open(json_file_path, "r") as file:
                    try:
                        existing_data = json.load(file)
                    except json.JSONDecodeError:
                        print("JSONDecodeError: The file is empty or not properly formatted")
            existing_data.append(data)
            try:
                with open(json_file_path, "w") as file:
                    json.dump(existing_data, file, indent=4)
            except Exception as e:
                print(f"An error occurred while writing to the file: {e}")

            return "Thanks For Submmiting - Exclaibur Scouting System Dev Team"
            return redirect("https://yehudarothstein.pythonanywhere.com/Scout")
    except Exception as e:
        print(f"An error occurred: {e}")
    return render_template("Scout.html")

@app.route('/getdata')
def get_json_data():
    return send_from_directory('Data', '/home/yehudarothstein/mysite/static/Data.JSON')

@app.route("/process_form", methods=["POST"])
def process_form():
    return "Form processed successfully"

@app.route("/home")
def test():
    return render_template('test.html')


@app.route("/snake")
def test_new():
    return render_template("snake.html")


@app.route("/ReportBugs", methods=["POST", "GET"])
def ReportBug():
  return render_template("Report.html")

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect("https://yehudarothstein.pythonanywhere.com/")
    else:
        flash('Invalid username or password')
        return redirect("https://yehudarothstein.pythonanywhere.com/login")


@app.route("/Autonomous", methods=["POST", "GET"])
def Autonomus():
    return render_template("autonomous.html")

@app.route('/get-json')
def get_json():
    return send_from_directory('static', 'Data.JSON')


if __name__ == '__main__':
    app.run()
