from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory storage (use a database in production)
todos = []
next_id = 1

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the To-Do API"})

@app.route('/todos', methods=['POST'])
def create_todo():
    global next_id
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400

    todo = {
        "id": next_id,
        "title": data['title'],
        "description": data.get('description', ''),
        "completed": False,
        "created_at": datetime.now().isoformat()
    }

    todos.append(todo)
    next_id += 1

    return jsonify(todo), 201

if __name__ == '__main__':
    app.run(debug=True)
