from flask import Flask, jsonify, request, redirect, url_for
from whisper_transcribe_fn import whisper_transcribe_fn
import os

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Replace with a specific domain in production environments
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET,PUT,POST,DELETE"
    return response

@app.route('/', methods=['GET'])
def get_data():
    # Example data response
    print('hello')
    return jsonify({"message": "Hello from API on port 5678!"})

@app.route('/upload', methods=['POST'])
def upload_file():
    print("request", request.files)
    file = request.files['file']
    # Upload the file
    if file:
        filename = file.filename
        
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        # # Ensure uploads folder exists
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        
        # # Save the file to disk securely
        file.save(filepath)

    return whisper_transcribe_fn(f"./uploads/{filename}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678)