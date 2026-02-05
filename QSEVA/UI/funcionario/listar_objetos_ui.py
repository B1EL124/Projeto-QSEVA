import streamlit as st
from QSEVA.controller.objeto_controller import ObjetoController

class ListarObjetosUI:
    @staticmethod
    def main():
        st.header("Lista de Objetos Encontrados")
        objetos = ObjetoController.listar()
        if not objetos:
            st.info("Nenhum objeto encontrado.")
            return
        dados = []
        for obj in objetos:
            dados.append({
                "ID": obj.id,
                "Descrição": obj.descricao,
                "Local": obj.local_encontrado,
                "Data/Hora": obj.data_hora_encontrado.strftime("%d/%m/%Y %H:%M")
            })
        st.table(dados)