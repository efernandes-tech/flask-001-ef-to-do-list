<h1 align="center">
    <a href="#" alt="Flask To-Do List API">Flask To-Do List API</a>
</h1>

<h3 align="center">
    A RESTful API for managing to-do items and users built with Flask
</h3>

<p align="center">
    <a href="https://github.com/efernandes-tech/flask-001-ef-to-do-list/commits/main">
        <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/efernandes-tech/flask-001-ef-to-do-list" />
    </a>
    <img alt="Repository size" src="https://img.shields.io/github/repo-size/efernandes-tech/flask-001-ef-to-do-list">
    <a href="https://edersonfernandes.com.br">
        <img alt="made by @efernandes-tech" src="https://img.shields.io/badge/Made_by-@efernandes%E2%80%93tech-blue">
    </a>

</p>

<h4 align="center">
    Status: In progress | Finished
</h4>

<p align="center">
    <a href="#about">About</a> •
    <a href="#features">Features</a> •
    <a href="#how-it-works">How it works</a> •
    <a href="#tech-stack">Tech Stack</a> •
    <a href="#author">Author</a>
</p>

## About

A Flask-based RESTful API for managing to-do items and users. This project demonstrates building a complete CRUD API with Flask using blueprints for modular organization.

---

## Features

-   [x] Create, read, update, and delete to-do items
-   [x] User management API endpoints
-   [x] RESTful API design with JSON responses
-   [x] Modular architecture using Flask Blueprints
-   [x] Error handling with custom error handlers

---

## How it works

### Pre-requisites

Before you begin, you will need to have the following tools installed:
[Git](https://git-scm.com), [Python 3.x](https://www.python.org/)

#### Running the project

```bash
# Clone this repository
git clone https://github.com/efernandes-tech/flask-001-ef-to-do-list.git

# Access the project folder
cd flask-001-ef-to-do-list/backend/flask-todo

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
source venv/Scripts/activate
# On macOS/Linux:
# source venv/bin/activate

# Install dependencies
pip install Flask

# Run the application
python app.py

# The server will start at port: 5000 - go to http://localhost:5000
```

### API Endpoints

**To-Do Items:**
- `POST /api/todos` - Create a new to-do
- `GET /api/todos` - Get all to-dos
- `GET /api/todos/<id>` - Get a specific to-do
- `PUT /api/todos/<id>` - Update a to-do
- `DELETE /api/todos/<id>` - Delete a to-do

**Users:**
- `GET /api/users` - Get all users
- `GET /api/users/<id>` - Get a specific user

---

## Tech Stack

**Backend:**

-   [Python](https://www.python.org/)
-   [Flask](https://flask.palletsprojects.com/)
-   In-memory storage (for demonstration purposes)

**Tools:**

-   [Visual Studio Code](https://code.visualstudio.com/)
-   [Postman](https://www.postman.com/) or [curl](https://curl.se/) for API testing

---

## Author

<a href="https://github.com/efernandes-tech">
    <img style="border-radius: 50%;" src="https://github.com/efernandes-tech.png" width="100px;" alt="Your Name" />
    <br />
    <sub><b>Your Name</b></sub>
</a>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/efernandes-tech)
[![Email](https://img.shields.io/badge/Email-Contact-red?logo=gmail)](mailto:efernandes.tech@gmail.com)
