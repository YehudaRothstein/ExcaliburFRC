from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):  # Change the parameter name to match the route
    return render_template("index.html", content=name)  # Adjust the parameter name here as well

if __name__ == '__main__':
    app.run()
