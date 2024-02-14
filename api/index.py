import os, socket, json, sqlite3
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, send_from_directory, session

# Initialize Flask application
app = Flask(__name__, template_folder='.')
app.secret_key = '6738'
socket.getaddrinfo('localhost', 5000)
LOCAL_IP = '0.0.0.0'

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "An error occurred", "details": str(e)}), 500

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('../Data/usersdata.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE name = ?', (username,))
        user = cursor.fetchone()

        session['username'] = username
        return redirect(url_for('scout'))  # Redirect to Scout page

    return render_template("Login.html")
@app.route("/Scout", methods=["POST", "GET"])
def scout():
    """
    Route for the Scout page.
    If the request method is POST, it processes the form data and updates the JSON file.
    If the request method is GET, it returns the rendered template for the Scout page.
    """
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
    """
    Route for getting the JSON data.
    Returns the JSON data from the static directory.
    """
    return send_from_directory('../Data', 'Data.json')


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

@app.route('/get-json')
def get_json():
    """
    Route for getting the JSON data.
    Returns the JSON data from the static directory.
    """
    return send_from_directory('../Data', 'Data.json')


@app.route("/")
def home():
    return render_template("ScoutHomePage.html")

#hji
@app.route("/Queen-Of-Scouting")
def queen_of_scouting():
    return render_template("QueenOfScout.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)