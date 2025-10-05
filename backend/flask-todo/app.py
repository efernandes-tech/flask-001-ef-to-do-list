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

if __name__ == '__main__':
    app.run(debug=True)
