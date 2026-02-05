import streamlit as st
from QSEVA.controller.usuario_controller import UsuarioController

class RegistrarUsuarioUI:
    @staticmethod
    def main():
        st.header("Registrar Usuário")
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        senha = st.text_input("Senha", type="password")
        interessado = st.checkbox("Interessado", value=True)
        funcionario = st.checkbox("Funcionário")
        if st.button("Salvar"):
            try:
                UsuarioController.inserir(nome, email, telefone, senha, interessado, funcionario)
                st.success("Salvo com sucesso.")
            except Exception as e:
                st.error(f"Erro: {e}")