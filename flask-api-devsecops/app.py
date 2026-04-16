from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "API Flask DevSecOps", "version": "1.0"})

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/user/<int:user_id>')
def get_user(user_id):
    return jsonify({"user_id": user_id, "name": "Test User"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
