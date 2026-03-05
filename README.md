# FastAPI Users CRUD Project

Simple API built with **FastAPI** and **SQLite** that supports CRUD operations for users.

## Features

- **Create**: POST `/users/` – add a new user  
- **Read All**: GET `/users/` – list all users  
- **Read One**: GET `/users/{user_id}` – get a user by ID  
- **Update**: PUT `/users/{user_id}` – update a user  
- **Delete**: DELETE `/users/{user_id}` – remove a user  
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

## Tech Stack

- Python 3.9+  
- FastAPI  
- SQLite  
- Pydantic  
- Uvicorn  

## Setup & Run

1. Clone the repo:

```bash
git clone <your-repo-url>
cd <project-folder>

2. Create & activate virtual environment:
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3.Install dependencies:
pip install fastapi uvicorn pydantic

4. Start the server
uvicorn main:app --reload

5. Open Swagger UI 
http://127.0.0.1:8000/docs

6. Exemple curl Requests 
Example curl Requests

Get all users:
curl http://127.0.0.1:8000/users/

Create a user:
curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d '{"name":"Mikita","email":"mikita@example.com"}'

Update a user:
curl -X PUT "http://127.0.0.1:8000/users/1" -H "Content-Type: application/json" -d '{"name":"Mikita Updated","email":"new@example.com"}'

Delete a user:
curl -X DELETE "http://127.0.0.1:8000/users/
