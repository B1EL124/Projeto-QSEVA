import streamlit as st
from datetime import datetime
from QSEVA.controller.devolucao_controller import DevolucaoController

class RegistrarDevolucaoUI:
    @staticmethod
    def main():
        st.header("Registrar Devolução")
        id_objeto = st.number_input("ID do Objeto", min_value=1, step=1)
        id_solicitante = st.number_input("ID do Solicitante", min_value=1, step=1)
        if st.button("Confirmar"):
            try:
                DevolucaoController.inserir(id_objeto, id_solicitante, datetime.now())
                st.success("Devolução realizada.")
            except Exception as e:
                st.error(f"Erro: {e}")