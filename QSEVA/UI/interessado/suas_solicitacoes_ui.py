import streamlit as st
from QSEVA.controller.solicitacao_controller import SolicitacaoController


class SuasSolicitacoesUI:
    @staticmethod
    def main():
        st.header("Minhas Solicitações")

        usuario = st.session_state.usuario
        todas = SolicitacaoController.listar()
        minhas = [s for s in todas if s.id_solicitante == usuario.id]

        if not minhas:
            st.info("Nenhuma solicitação.")
            return

        dados = []
        for s in minhas:
            dados.append({
                "ID": s.id,
                "ID Solicitante": s.id_solicitante,
                "Descrição": s.descricao,
                "Local Perdido": s.local_perdido,
                "Data do Ocorrido": s.data_hora_perdido.strftime("%d/%m/%Y %H:%M"),
                "Registrado em": s.data_hora.strftime("%d/%m/%Y %H:%M")
            })

        st.table(dados)
