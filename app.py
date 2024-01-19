import requests
from flask import (Flask, jsonify, redirect, render_template, request,
                   send_from_directory, url_for)

from utils.extractUtils import extract_followers_features, extract_user_features

app = Flask(__name__)

@app.route('/extract-user-features', methods=['GET'])
def route_extract_user_features():
    try:
        #data = request.get_json()
        username = request.args.get('username')
        print(username)
        api_url = f'https://userinfoms.azurewebsites.net/get-user-info?username={username}'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            features = extract_user_features(data)
            return jsonify(features)
        else:
            return jsonify({'error': f'API Error: {response.status_code}'})
        
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/extract-followers-features', methods=['GET'])
def route_extract_followers_features():
    try:
        #data = request.get_json()
        username = request.args.get('username')
        api_url = f'https://userinfoms.azurewebsites.net/get-user-followers-info?username={username}'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            features = extract_followers_features(data)
            return jsonify(features)
        else:
            return jsonify({'error': f'API Error: {response.status_code}'})
        
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)