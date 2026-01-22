import sys
sys.dont_write_bytecode = True
import streamlit as st
from QSEVA.controller.controllers import Controllers


class loginUI():
    def main():
        st.header("Login Menu")

        email = st.text_input("Email")
        senha = st.text_input("Senha", type = "password")
        perfil = st.radio("Entrar Como:", ("Interessado", "Funcionário"))

        if st.button("Entrar"):
            usuario = Controllers.UsuarioController.autenticar(email, senha)

            if not usuario:
                st.error("Email ou senha incorretos.")
                return
            
            st.session_state.usuario_logado = usuario
            match perfil:
                case "Interessado": st.session_state.perfil = "interessado"
                case "Funcionário": st.session_state.perfil = "funcionario"
            
            st.success(f"Bem vindo {usuario.nome}!")
            st.rerun()
