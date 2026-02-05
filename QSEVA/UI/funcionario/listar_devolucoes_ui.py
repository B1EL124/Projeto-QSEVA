import streamlit as st
from QSEVA.controller.devolucao_controller import DevolucaoController  


class ListarDevolucoesUI:
    @staticmethod
    def main():
        st.header("Devoluções Registradas")

        devolucoes = DevolucaoController.listar() 
        if not devolucoes:
            st.info("Não há devoluções registradas.")
            return

        dados = []
        for d in devolucoes:
            dados.append({
                "ID Objeto": d.id_objeto,
                "ID Solicitante": d.id_solicitante,
                "Data/Hora": d.data_hora.strftime("%d/%m/%Y %H:%M")
            })

        st.table(dados)
