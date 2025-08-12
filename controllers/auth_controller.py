from models.user_model import UserModel
from flask import jsonify
from flask_jwt_extended import create_access_token
from db import get_connection
import bcrypt

def login(user: UserModel):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (user.email,))
    db_user = cursor.fetchone()
    cursor.close()
    conn.close()

    if db_user and bcrypt.checkpw(user.password.encode('utf-8'), db_user['password'].encode('utf-8')):
        access_token = create_access_token(identity=db_user['email'])
        return access_token
    else:
        return None

def register(user: UserModel):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",(user.name, user.email, hashed_password.decode('utf-8')))
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return user
