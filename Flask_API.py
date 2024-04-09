from flask import Flask, jsonify, request
from detection import detectBarcode
from convert_Image import base64_to_image
import base64
from PIL import Image
from io import BytesIO
import os
from flask_cors import CORS
# Create a Flask app
app = Flask(__name__)
CORS(app)
# Define a simple route
@app.route('/')
def hello():
    return 'Hello, World!'

# Define a route that returns JSON data
@app.route('/api/data')
def get_data():
    data = {'message': 'This is JSON data from the Flask API'}
    return jsonify(data)

# Define a route that accepts a parameter
@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.json
    name = data.args.get('name', 'Guest')  # Get the 'name' parameter from the query string, default to 'Guest'
    greeting = f'Hello, {name}!'
    return jsonify({'greeting': greeting})

@app.route('/api/detectbarcode', methods=['POST'])
async def startDetect():
    data = request.json
    base64 = data.get('image')  # Get the 'name' parameter from the query string, default to 'Guest'
    # print(base64)
    await base64_to_image(base64,'images')
    data = await detectBarcode(1)
    return data

if __name__ == '__main__':
    # Run the app in debug mode on port 5000
    app.run(host='0.0.0.0',debug=True, port=8080)
