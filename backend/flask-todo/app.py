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

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)

    if todo is None:
        return jsonify({"error": "To-do not found"}), 404

    return jsonify(todo)

if __name__ == '__main__':
    app.run(debug=True)
