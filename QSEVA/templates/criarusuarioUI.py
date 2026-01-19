import streamlit as st

class CriarUsuarioUI():
    def main():
        st.header("Criar usuário")
        st.text_input("nome")
        st.text_input("email")
        st.text_input("telefone")
        st.text_input("senha", type="password")
        st.write("Permissões:")

        interessado = st.checkbox("Interessado")
        funcionario = st.checkbox("Funcionário")
        administrador = st.checkbox("Administrador")

        st.button("Criar Usuário")
