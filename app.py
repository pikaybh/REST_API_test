from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def home():
    data = {"message": "Hello, World!"}
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
