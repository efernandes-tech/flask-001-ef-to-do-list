from flask import Flask, jsonify
from todos_api import todos_bp
from users_api import users_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(todos_bp)
app.register_blueprint(users_bp)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the To-Do API"})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
