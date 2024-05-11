from flask import Flask, jsonify

app = Flask(__name__)

# Cache to store the data from the external API
data_cache = {}

# Endpoint to fetch data from the external API
@app.route('/api/poedata/fetch', methods=['GET'])
def fetch_data():
    # Check if data is already cached
    if 'data' in data_cache:
        return jsonify({'message': 'Data fetched from cache test', 'data': data_cache['data']})

    data_cache['data'] = 'test'
    return jsonify({'message': 'Data fetched from external API', 'data': data_cache['data']})