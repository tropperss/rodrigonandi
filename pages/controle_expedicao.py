import streamlit as st
from db.db_setup import session, Order, FiscalInfo
from utils.forms import fiscal_form

def controle_expedicao():
    st.title("Controle de Expedição")

    order_id, tax_info = fiscal_form()

    if st.button("Emitir Nota Fiscal"):
        if order_id and tax_info:
            new_fiscal_info = FiscalInfo(order_id=order_id, tax_info=tax_info)
            session.add(new_fiscal_info)
            session.commit()
            st.success("Nota Fiscal emitida com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
