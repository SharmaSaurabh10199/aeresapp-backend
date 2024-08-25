from flask import Flask, request, jsonify
from business import get_data
from flask_cors import CORS

app= Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/data')
def data():
    return jsonify(get_data())

if __name__ == '__main__':
    app.run( port=8000, host='0.0.0.0', debug=True)