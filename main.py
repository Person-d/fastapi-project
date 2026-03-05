from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3
import os

app = FastAPI(title="Users API")

DB_FILE = "users.db"

# Модель користувача
class User(BaseModel):
    id: int = None
    name: str
    email: str

# Ініціалізація бази даних
def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

init_db()

# CREATE
@app.post("/users/", response_model=User)
def create_user(user: User):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user.name, user.email))
    user.id = c.lastrowid
    conn.commit()
    conn.close()
    return user

# READ all
@app.get("/users/", response_model=List[User])
def read_all_users():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, name, email FROM users")
    rows = c.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]

# READ one
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, name, email FROM users WHERE id=?", (user_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "name": row[1], "email": row[2]}
    raise HTTPException(status_code=404, detail="User not found")

# UPDATE
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE users SET name=?, email=? WHERE id=?", (user.name, user.email, user_id))
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="User not found")
    conn.commit()
    conn.close()
    user.id = user_id
    return user

# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (user_id,))
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="User not found")
    conn.commit()
    conn.close()
    return {"detail": "User deleted"}