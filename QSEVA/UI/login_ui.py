import streamlit as st
from QSEVA.controller.usuario_controller import UsuarioController


class LoginUI():
    def main():
        st.header("Login Menu")

        email = st.text_input("Email")
        senha = st.text_input("Senha", type = "password")
        perfil = st.radio("Entrar Como:", ("Interessado", "Funcionário"))

        if st.button("Entrar"):
            usuario = UsuarioController.autenticar(email, senha)

            if not usuario:
                st.error("Email ou senha incorretos.")
                return
            
            if perfil == "Interessado" and usuario.interessado:
                st.session_state.perfil = "interessado"
            elif perfil == "Funcionário" and usuario.funcionario:
                st.session_state.perfil = "funcionario"
            else:
                st.error("Você não tem permissão para entrar com este perfil.")
                return
            
            st.session_state.usuario = usuario
            match perfil:
                case "Interessado": st.session_state.perfil = "interessado"
                case "Funcionário": st.session_state.perfil = "funcionario"
            
            st.success(f"Bem vindo {usuario.nome}!")
            st.rerun()
