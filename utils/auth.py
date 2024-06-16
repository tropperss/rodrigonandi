import bcrypt
import jwt
import streamlit as st
from datetime import datetime, timedelta

SECRET_KEY = 'sua_chave_secreta'

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def generate_token(username, role):
    payload = {
        'username': username,
        'role': role,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def login_required(func):
    def wrapper(*args, **kwargs):
        token = st.session_state.get('token')
        if token:
            user = verify_token(token)
            if user:
                return func(*args, **kwargs)
        st.error("Você precisa estar logado para acessar esta página.")
    return wrapper
