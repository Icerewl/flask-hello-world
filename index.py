import csv
from flask import Flask, jsonify, request, abort
import os
app = Flask(__name__)

# Get the absolute path to the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), 'ToyotaCorolla.csv')

# Load the CSV data into a list of dictionaries
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    car_data = list(csv_reader)

@app.route('/', methods=['GET'])  # Add this route
def hello_world():
    return "Hello, World!"

@app.route('/data', methods=['GET'])
def get_data():
    index = request.args.get('index', default=None, type=int)
    if index is not None:
        try:
            return jsonify(car_data[index])
        except IndexError:
            abort(404)  # Not found if index is out of range
    return jsonify(car_data)  # Return all data if no index provided

@app.route('/data/search', methods=['GET'])
def search_data():
    query = request.args.get('model', default=None, type=str)
    if query:
        result = [car for car in car_data if query.lower() in car['Model'].lower()]
        if result:
            return jsonify(result)
        else:
            abort(404)  # Not found if no match
    return jsonify(car_data)  # Return all data if no query provided

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get port from environment variable or default to 5000
    app.run(host='0.0.0.0', port=port)

