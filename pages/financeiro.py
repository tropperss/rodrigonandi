import streamlit as st
from utils.auth import login_required, verify_token

@login_required
def financeiro():
    token = st.session_state.get('token')
    user = verify_token(token)
    
    if user and user['role'] == 'admin':
        st.title("Área Financeira")
        st.write("Acesso permitido apenas para administradores.")
        # Adicione as funcionalidades financeiras aqui
    else:
        st.error("Acesso negado. Esta área é restrita aos administradores.")
