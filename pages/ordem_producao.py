import streamlit as st
from db.db_setup import session, Order, Reference
from utils.forms import order_form

def ordem_producao():
    st.title("Gerenciamento de Ordem de Produção")

    reference_ids = [ref.id for ref in session.query(Reference).all()]
    reference_id, status = order_form(reference_ids)

    if st.button("Criar Ordem de Produção"):
        if reference_id and status:
            new_order = Order(reference_id=reference_id, status=status)
            session.add(new_order)
            session.commit()
            st.success("Ordem de Produção criada com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
