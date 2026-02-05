import streamlit as st
from datetime import datetime
from QSEVA.controller.solicitacao_controller import SolicitacaoController


class RegistrarSolicitacaoUI:
    @staticmethod
    def main():
        st.header("Registrar Solicitação")

        descricao = st.text_area("O que você perdeu?")
        local_perdido = st.text_input("Onde você perdeu?")
        data_hora_perdido = st.datetime_input("Quando você perdeu?")

        if st.button("Enviar"):
            try:
                usuario = st.session_state.usuario
                SolicitacaoController.inserir(
                    id_solicitante = usuario.id,
                    descricao = descricao,
                    local_perdido = local_perdido,
                    data_hora_perdido = data_hora_perdido,
                    data_hora = datetime.now()
                )
                st.success("Enviado.")
                
            except Exception as e:
                st.error(f"Erro: {e}")
