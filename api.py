from flask import Flask, request, jsonify
from app import app

@app.route('/api', methods=['POST'])
def api():
    data = request.json  # Get JSON data from the request
    # Process the request and return a response
    return jsonify({'message': 'Data received'})

if __name__ == '__main__':
    app.run()
