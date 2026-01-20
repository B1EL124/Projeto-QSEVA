# import sys
# sys.dont_write_bytecode = True


# from QSEVA.controller.controllers import UsuarioController

# UsuarioController.inserir(
#     nome = "gio",
#     email = "gio@gmail.com",
#     telefone = "111111111",
#     senha = "senha123"
# )


# import streamlit as st
# from QSEVA.templates.loginUI import login

# def main():
#     if "usuario_logado" not in st.session_state:
#         st.session_state.usuario_logado = None

#     while st.session_state.usuario_logado is None:
#         login()

# main()

from QSEVA.model.models import Models

print(Models.Objeto)