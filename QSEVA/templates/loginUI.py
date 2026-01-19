import streamlit as st
from QSEVA.controller.usuario_controllers import UsuarioController


def login():
    st.header("Login Menu")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    perfil = st.radio("Entrar como:", ("Interessado", "Funcionário", "Administrador"))
    entrar = st.button("Entrar")

    if entrar:
        usuario = UsuarioController.autenticar(email, senha)

        if not usuario:
            st.error("Email ou senha incorretos.")
            return
        
        if not any( [
            perfil == "Administrador" and usuario.permissao_administrador,
            perfil == "Funcionário" and usuario.permissao_funcionario,
            perfil == "Interessado" and usuario.permissao_interessado
        ] ):
            st.error("Permissão negada para este perfil.")
            return

        st.session_state.usuario_logado = usuario
        st.session_state.perfil = perfil

        st.success(f"Bem vindo {usuario.nome}!")