import streamlit as st


class HomeUI:
    def main():
        st.write(f"Bem vindo de volta {st.session_state.usuario_logado.nome}")