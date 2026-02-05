import streamlit as st
from QSEVA.controller.solicitacao_controller import SolicitacaoController

class SuasSolicitacoesUI:
    @staticmethod
    def main():
        st.header("Minhas Solicitações")
        usuario = st.session_state.usuario_logado
        todas = SolicitacaoController.listar()
        minhas = [s for s in todas if s.id_solicitante == usuario.id]
        if not minhas:
            st.info("Nenhuma solicitação.")
            return
        for s in minhas:
            with st.expander(f"Solicitação #{s.id}"):
                st.write(f"Descrição: {s.descricao}")
                st.write(f"Data: {s.data_hora.strftime('%d/%m/%Y %H:%M')}")