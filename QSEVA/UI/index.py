import sys
sys.dont_write_bytecode = True
from QSEVA.UI.loginUI import loginUI
from QSEVA.UI.registrarobjetoUI import RegistrarObjetoUI
import streamlit as st


class IndexUI:
    @staticmethod
    def main():
        if "usuario_logado" not in st.session_state:
            st.session_state.usuario_logado = None

        if st.session_state.usuario_logado is None:
            loginUI.main()
            st.write("Tela de login")  # debug visível no navegador
        else:
            RegistrarObjetoUI.main()
            st.write("Tela principal")  # debug visível no navegador
