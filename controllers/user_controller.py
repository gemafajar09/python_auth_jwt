import bcrypt
from db import get_connection
from models.user_model import UserModel

def create_user(user: UserModel):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",(user.name, user.email, hashed_password.decode('utf-8')))
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return user_id

def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def get_user(user: UserModel):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user.id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def update_user(user: UserModel):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s", (user.name, user.email, hashed_password.decode('utf-8'), user.id))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected

def delete_user(user: UserModel):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user.id))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected
