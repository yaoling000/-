from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

stored_prompt = {"value": None}

@app.route('/save_prompt', methods=['POST'])
def save_prompt():
    data = request.json
    prompt = data.get('prompt')
    if stored_prompt["value"] is None:
        stored_prompt["value"] = prompt
        return jsonify({"message": "Prompt saved successfully."}), 200
    else:
        return jsonify({"message": "Prompt already exists."}), 200

@app.route('/get_prompt', methods=['GET'])
def get_prompt():
    if stored_prompt["value"]:
        return jsonify({"prompt": stored_prompt["value"]}), 200
    else:
        return jsonify({"prompt": None}), 200

@app.route('/', methods=['GET'])
def home():
    return "Prompt Store is running!", 200

if __name__ == '__main__':
    from gunicorn.app.base import BaseApplication
    app.run(debug=True)
