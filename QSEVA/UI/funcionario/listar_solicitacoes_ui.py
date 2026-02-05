import streamlit as st
from QSEVA.controller.solicitacao_controller import SolicitacaoController

class ListarSolicitacoesUI:
    @staticmethod
    def main():
        st.header("Solicitações Pendentes")
        solicitacoes = SolicitacaoController.listar()
        if not solicitacoes:
            st.info("Não há solicitações.")
            return
        dados = []
        for s in solicitacoes:
            dados.append({
                "ID": s.id,
                "ID Solicitante": s.id_solicitante,
                "Descrição": s.descricao,
                "Data": s.data_hora.strftime("%d/%m/%Y %H:%M")
            })
        st.table(dados)