from flask import Flask, request, jsonify

app = Flask(__name__)

storage = {}

@app.route('/')
def home():
    return "Serverless Cloud Drive"

@app.route('/upload', methods=['POST'])
def upload():
    filename = request.json['filename']
    content = request.json['content']

    storage[filename] = content

    return jsonify({
        "message": "File uploaded successfully"
    })

@app.route('/files')
def files():
    return jsonify(list(storage.keys()))

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "cloud-drive"
    })

if __name__ == '__main__':
    app.run(debug=True)
