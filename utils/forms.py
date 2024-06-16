import streamlit as st

def user_form():
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    role = st.selectbox("Papel", ["admin", "user"])
    return username, password, role

def supplier_form():
    name = st.text_input("Nome")
    cnpj = st.text_input("CNPJ")
    address = st.text_area("Endereço")
    contact = st.text_input("Contato")
    return name, cnpj, address, contact

def reference_form():
    description = st.text_input("Descrição")
    cost = st.number_input("Custo", min_value=0.0, format="%.2f")
    return description, cost

def fiscal_form():
    order_id = st.number_input("ID da Ordem de Produção", min_value=1)
    tax_info = st.text_area("Informações Fiscais")
    return order_id, tax_info

def order_form(reference_ids):
    reference_id = st.selectbox("Referência", reference_ids)
    status = st.selectbox("Status", ["MPR", "Corte", "Pré-Costura", "Costura", "Revisão", "Acabamento", "Expedição"])
    return reference_id, status
