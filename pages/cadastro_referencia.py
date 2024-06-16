import streamlit as st
from db.db_setup import session, Reference
from utils.forms import reference_form

def cadastro_referencia():
    st.title("Cadastro de Referência")

    description, cost = reference_form()

    if st.button("Cadastrar"):
        if description and cost >= 0:
            new_reference = Reference(description=description, cost=cost)
            session.add(new_reference)
            session.commit()
            st.success("Referência cadastrada com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")
