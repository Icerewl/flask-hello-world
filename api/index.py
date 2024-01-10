from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple route to return a "Hello World" message
@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

# A route to return data based on a GET request
@app.route('/data', methods=['GET'])
def get_data():
    sample_data = {'key': 'value'}
    return jsonify(sample_data)

# A route to receive data based on a POST request
@app.route('/data', methods=['POST'])
def post_data():
    data = request.json
    # Do something with the data
    return jsonify(received=True, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
