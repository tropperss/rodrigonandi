import streamlit as st
from db.db_setup import session, User
from utils.auth import hash_password
from utils.forms import user_form

def cadastro_usuario():
    st.title("Cadastro de Usuário")

    username, password, role = user_form()

    if st.button("Cadastrar"):
        if username and password:
            hashed_password = hash_password(password)
            new_user = User(username=username, password=hashed_password, role=role)
            session.add(new_user)
            session.commit()
            st.success("Usuário cadastrado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
