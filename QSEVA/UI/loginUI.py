import sys
sys.dont_write_bytecode = True
import streamlit as st
from QSEVA.controller.controllers import Controllers


class loginUI():
    def main():
        st.header("Login Menu")

        email = st.text_input("Email")
        senha = st.text_input("Senha", type = "password")

        if st.button("Entrar"):
            usuario = Controllers.UsuarioController.autenticar(email, senha)

            if not usuario:
                st.error("Email ou senha incorretos.")
                return
            
            st.session_state.usuario_logado = usuario
            st.success(f"Bem vindo {usuario.nome}!")
        


# import streamlit as st
# from datetime import datetime
# from QSEVA.controller.objeto_controller import ObjetoController


# def registrar_objeto():
#     st.header("Registro de Objeto Encontrado")

#     descricao = st.text_input("Descrição do objeto")
#     local_encontrado = st.text_input("Local onde foi encontrado")

#     data_hora_encontrado = st.date_input("Data em que o objeto foi encontrado")

#     hora_encontrado = st.time_input("Hora em que o objeto foi encontrado")

#     if st.button("Registrar Objeto"):
#         try:
#             data_hora_completa = datetime.combine(
#                 data_hora_encontrado,
#                 hora_encontrado
#             )

#             ObjetoController.inserir(
#                 descricao, data_hora_completa, local_encontrado
#             )

#             st.success("Objeto registrado com sucesso.")

#         except Exception as e:
#             st.error(f"Erro ao registrar objeto. {e}")
        
# registrar_objeto()