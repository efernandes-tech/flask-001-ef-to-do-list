# Commands:

```cmd
cd ./backend
python hello/app.py
```

```cmd
cd ./backend
mkdir flask-todo
cd flask-todo
python -m venv venv
source venv/bin/activate  # On Windows: source venv/Scripts/activate
pip install Flask
python app.py
```

```cmd
cd ./backend/flask-todo
python app.py
```

```cmd
curl -X POST http://127.0.0.1:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Build awesome web apps"}'

curl http://127.0.0.1:5000/api/todos

curl http://127.0.0.1:5000/api/todos/1

curl -X PUT http://127.0.0.1:5000/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

curl -X DELETE http://127.0.0.1:5000/api/todos/1
```

```cmd
curl http://127.0.0.1:5000/api/users
```

```cmd

```

```cmd

```

```cmd

```

```cmd

```

```cmd

```
