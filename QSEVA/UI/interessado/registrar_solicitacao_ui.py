import streamlit as st
from datetime import datetime
from QSEVA.controller.solicitacao_controller import SolicitacaoController

class RegistrarSolicitacaoUI:
    @staticmethod
    def main():
        st.header("Nova Solicitação")
        descricao = st.text_area("O que você perdeu?")
        if st.button("Enviar"):
            try:
                usuario = st.session_state.usuario_logado
                SolicitacaoController.inserir(usuario.id, descricao, datetime.now())
                st.success("Enviado.")
            except Exception as e:
                st.error(f"Erro: {e}")