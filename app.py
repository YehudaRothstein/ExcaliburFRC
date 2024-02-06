from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = '6738'

# Your routes and functions here

if __name__ == '__main__':
    app.run()
