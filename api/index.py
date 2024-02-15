import os, socket, json, sqlite3, werkzeug
from werkzeug.routing import url_quote
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, send_from_directory, session
import traceback


# Initialize Flask application
app = Flask(__name__, template_folder='templates')
app.secret_key = '6738'
socket.getaddrinfo('localhost', 5000)
LOCAL_IP = '0.0.0.0'

DATA_DIR = "/tmp/Data"
json_file_path = os.path.join(DATA_DIR, 'Data.JSON')

DATA_DIR = "/tmp/Data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


@app.route("/Login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Use context manager to ensure database connection is closed
        with sqlite3.connect('../Data/usersdata.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE name = ?', (username,))
            user = cursor.fetchone()

        if user is None or user[1] != password:
            flash('Invalid username or password')
            return redirect(url_for('login'))

        session['username'] = username
        return redirect(url_for('scout'))
    return render_template("Login.html")

@app.route("/Scout", methods=["POST", "GET"])
def scout():
    try:
        if request.method == 'POST':
            data = request.get_json()
            existing_data = {}
            json_file_path = "../Data/Data.JSON"
            if os.path.exists(json_file_path) and os.path.getsize(json_file_path) > 0:
                with open(json_file_path, "r") as file:
                    try:
                        existing_data = json.load(file)
                    except json.JSONDecodeError:
                        return jsonify({"error": "JSON Decode Error"}), 500

            key = data['team']
            existing_data.setdefault(key, []).append(data)

            with open(json_file_path, "w") as file:
                json.dump(existing_data, file, indent=4)

            return "Data saved successfully"
    except Exception as e:
        app.logger.error(f"An error occurred in /Scout: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

    return render_template("Scout.html")

#@app.route('/get-json-data')
#def get_json_data():
  #  if os.path.exists('../Data/Data.json'):
   #     return send_from_directory('../Data', 'Data.json')
  #  else:
  #      return jsonify({"error": "File not found"}), 404

@app.route('/get-json')
def get_json():
    if os.path.exists('../Data/Data.json'):
        return send_from_directory('../Data', 'Data.json')
    else:
        return jsonify({"error": "File not found"}), 404

@app.route("/process_form", methods=["POST"])
def process_form():
    """
    Route for processing the form.
    Returns a success message.
    """
    return "Form processed successfully"


@app.route("/home")
def test():
    """
    Route for the test page.
    Returns the rendered template for the test page.
    """
    return render_template("new.html", local_ip=LOCAL_IP)


@app.route("/test_new")
def test_new():
    """
    Route for the new test page.
    Returns the rendered template for the new test page.
    """
    return render_template("new.html", local_ip=LOCAL_IP)


@app.route("/ReportBugs", methods=["POST", "GET"])
def ReportBug():
    """
    Route for the ReportBugs page.
    Returns the rendered template for the ReportBugs page.
    """
    return render_template("Report.html", local_ip=LOCAL_IP)


@app.route('/Data/<path:path>')
def send_js(path):
    """
    Route for serving static files.
    Returns the requested static file.
    """
    return send_from_directory('../Data', path)


@app.route("/<usr>")
def user(usr):
    """
    Route for user pages.
    Returns a personalized greeting for the user.
    """
    return f"<h1>{usr}</h1>"


@app.route("/Autonomous", methods=["POST", "GET"])
def Autonomus():
    """
    Route for the Autonomous page.
    Returns the rendered template for the Autonomous page.
    """
    return render_template("autonomous.html", local_ip=LOCAL_IP)

@app.route("/ScoutHomePage")
def ScoutHomePage ():
    return render_template("ScoutHomePage.html", local_ip=LOCAL_IP)
@app.route("/ScoutGuest")
def ScoutGuest ():
    return render_template("ScoutGuest.html", local_ip=LOCAL_IP)



@app.route("/")
def home():
    return render_template("Scout.html")

#hji
@app.route("/Queen-Of-Scouting")
def queen_of_scouting():
    return render_template("QueenOfScout.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)