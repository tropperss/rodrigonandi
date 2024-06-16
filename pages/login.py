import streamlit as st
from db.db_setup import session, User
from utils.auth import check_password, generate_token

def login():
    st.title("Login")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Login"):
        if username and password:
            user = session.query(User).filter_by(username=username).first()
            if user and check_password(password, user.password):
                token = generate_token(user.username, user.role)
                st.session_state.token = token
                st.success("Login realizado com sucesso!")
                st.experimental_rerun()
            else:
                st.error("Usuário ou senha incorretos.")
        else:
            st.error("Por favor, preencha todos os campos.")
