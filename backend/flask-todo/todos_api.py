from flask import Blueprint, jsonify, request
from datetime import datetime

todos_bp = Blueprint('todos', __name__, url_prefix='/api')

# In-memory storage (use a database in production)
todos = []
next_id = 1

@todos_bp.route('/todos', methods=['POST'])
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

@todos_bp.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@todos_bp.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)

    if todo is None:
        return jsonify({"error": "To-do not found"}), 404

    return jsonify(todo)

@todos_bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)

    if todo is None:
        return jsonify({"error": "To-do not found"}), 404

    data = request.get_json()

    todo['title'] = data.get('title', todo['title'])
    todo['description'] = data.get('description', todo['description'])
    todo['completed'] = data.get('completed', todo['completed'])

    return jsonify(todo)

@todos_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todo = next((t for t in todos if t['id'] == todo_id), None)

    if todo is None:
        return jsonify({"error": "To-do not found"}), 404

    todos = [t for t in todos if t['id'] != todo_id]

    return jsonify({"message": "To-do deleted successfully"})
