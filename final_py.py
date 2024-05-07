import os, json
from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
@login_required
def home():
    return render_template("new.html")

@app.route("/Scout", methods=["POST", "GET"])
@login_required
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
            except OSError as e:
                print(f"An OSError occurred while writing to the file: {e}")
                return "An error occurred while saving your data. Please try again later.", 500

            return "Thanks For Submmiting - Exclaibur Scouting System Dev Team" + username
    except Exception as e:
        print(f"An error occurred: {e}")
    return render_template("Scout.html")


@app.route('/getdata')
@login_required
def get_json_data():
    return send_from_directory('Data', '/home/yehudarothstein/mysite/static/Data.JSON')

@app.route("/process_form", methods=["POST"])
@login_required
def process_form():
    return "Form processed successfully"

@app.route("/home")
@login_required
def test():
    return render_template('test.html')

@app.route("/snake")
@login_required
def test_new():
    return render_template("snake.html")

@app.route("/ReportBugs", methods=["POST", "GET"])
@login_required
def ReportBug():
    return render_template("Report.html")

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route("/<usr>")
@login_required
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/Autonomous", methods=["POST", "GET"])
@login_required
def Autonomus():
    return render_template("autonomous.html")

@app.route('/get-json')
@login_required
def get_json():
    return send_from_directory('static', 'Data.JSON')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another.', 'danger')
            return redirect(url_for('register'))
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
