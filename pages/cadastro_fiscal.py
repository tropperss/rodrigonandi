import streamlit as st
from db.db_setup import session, FiscalInfo
from utils.forms import fiscal_form

def cadastro_fiscal():
    st.title("Cadastro Fiscal")

    order_id, tax_info = fiscal_form()

    if st.button("Cadastrar"):
        if order_id and tax_info:
            new_fiscal_info = FiscalInfo(order_id=order_id, tax_info=tax_info)
            session.add(new_fiscal_info)
            session.commit()
            st.success("Informações fiscais cadastradas com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
