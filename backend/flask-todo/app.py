from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory storage (use a database in production)
todos = []
next_id = 1

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the To-Do API"})

if __name__ == '__main__':
    app.run(debug=True)
