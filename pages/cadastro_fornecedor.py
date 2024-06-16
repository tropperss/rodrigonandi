import streamlit as st
from db.db_setup import session, Supplier
from utils.forms import supplier_form

def cadastro_fornecedor():
    st.title("Cadastro de Fornecedor")

    name, cnpj, address, contact = supplier_form()

    if st.button("Cadastrar"):
        if name and cnpj and address and contact:
            new_supplier = Supplier(name=name, cnpj=cnpj, address=address, contact=contact)
            session.add(new_supplier)
            session.commit()
            st.success("Fornecedor cadastrado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
