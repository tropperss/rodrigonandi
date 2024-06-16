import streamlit as st
from utils.auth import login_required

st.set_page_config(page_title="Sistema de Produção Têxtil", layout="wide")

def main():
    st.markdown("<style>{}</style>".format(open("assets/styles.css").read()), unsafe_allow_html=True)
    st.title("Sistema de Produção Têxtil")

    if 'token' not in st.session_state:
        st.session_state.token = None

    menu = ["Home", "Cadastrar Usuário", "Cadastrar Fornecedor", "Cadastrar Referência", 
            "Cadastrar Fiscal", "Ordem de Produção", "Controle de Expedição", "Financeiro", "Login"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Bem-vindo ao Sistema de Produção Têxtil")
        st.markdown(
            """
            <div class='nav-button'><button onclick="window.location.href='Cadastrar Usuário'">Cadastrar Usuário</button></div>
            <div class='nav-button'><button onclick="window.location.href='Cadastrar Fornecedor'">Cadastrar Fornecedor</button></div>
            <div class='nav-button'><button onclick="window.location.href='Cadastrar Referência'">Cadastrar Referência</button></div>
            <div class='nav-button'><button onclick="window.location.href='Cadastrar Fiscal'">Cadastrar Fiscal</button></div>
            <div class='nav-button'><button onclick="window.location.href='Ordem de Produção'">Ordem de Produção</button></div>
            <div class='nav-button'><button onclick="window.location.href='Controle de Expedição'">Controle de Expedição</button></div>
            <div class='nav-button'><button onclick="window.location.href='Financeiro'">Financeiro</button></div>
            """, unsafe_allow_html=True)
    elif choice == "Cadastrar Usuário":
        from pages.cadastro_usuario import cadastro_usuario
        cadastro_usuario()
    elif choice == "Cadastrar Fornecedor":
        from pages.cadastro_fornecedor import cadastro_fornecedor
        cadastro_fornecedor()
    elif choice == "Cadastrar Referência":
        from pages.cadastro_referencia import cadastro_referencia
        cadastro_referencia()
    elif choice == "Cadastrar Fiscal":
        from pages.cadastro_fiscal import cadastro_fiscal
        cadastro_fiscal()
    elif choice == "Ordem de Produção":
        from pages.ordem_producao import ordem_producao
        ordem_producao()
    elif choice == "Controle de Expedição":
        from pages.controle_expedicao import controle_expedicao
        controle_expedicao()
    elif choice == "Financeiro":
        from pages.financeiro import financeiro
        financeiro()
    elif choice == "Login":
        from pages.login import login
        login()

if __name__ == '__main__':
    main()
