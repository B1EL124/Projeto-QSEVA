from datetime import datetime
from QSEVA.controller.objeto_controller import ObjetoController
import streamlit as st


class RegistrarObjetoUI():        
    def main():
        st.header("Registro de Objeto Encontrado")
        descricao = st.text_input("Descrição do objeto")
        local_encontrado = st.text_input("Local onde foi encontrado")
        data_hora_encontrado = st.date_input("Data em que o objeto foi encontrado")
        hora_encontrado = st.time_input("Hora em que o objeto foi encontrado")

        if st.button("Registrar Objeto"):
            try:
                data_hora_encontrado = datetime.combine(
                    data_hora_encontrado,
                    hora_encontrado
                )
                ObjetoController.inserir(
                    descricao, data_hora_encontrado, local_encontrado
                )
                st.success("Objeto registrado com sucesso.")

            except Exception as e:
                st.error(f"Erro ao registrar objeto. {e}")
