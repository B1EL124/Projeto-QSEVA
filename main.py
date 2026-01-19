import sys
sys.dont_write_bytecode = True


# from QSEVA.controller.usuario_controller import UsuarioController

# UsuarioController.inserir(
#     nome="gio",
#     email="gio@gmail.com",
#     telefone="111111111",
#     senha="senha123",
#     permissao_administrador=False,
#     permissao_funcionario=True,
#     permissao_interessado=True
# )


import streamlit as st
from QSEVA.templates.loginUI import login
from QSEVA.templates.funcionario_dashboard import funcionario_dashboard

def main():
    if "usuario_logado" not in st.session_state:
        st.session_state.usuario_logado = None

    if "perfil" not in st.session_state:
        st.session_state.perfil = None

    if st.session_state.usuario_logado  is None:
        login()
    else:
        match st.session_state.perfil:
            case "Funcionario": funcionario_dashboard()

main()