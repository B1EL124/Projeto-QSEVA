import sys
sys.dont_write_bytecode = True


# # from QSEVA.controller.usuario_controller import UsuarioController

# # UsuarioController.inserir(
# #     nome="gio",
# #     email="gio@gmail.com",
# #     telefone="111111111",
# #     senha="senha123",
# #     permissao_administrador=False,
# #     permissao_funcionario=True,
# #     permissao_interessado=True
# # )


# import streamlit as st
# from QSEVA.templates.loginUI import login
# from QSEVA.templates.funcionario_dashboard import funcionario_dashboard

# def main():
#     if "usuario_logado" not in st.session_state:
#         st.session_state.usuario_logado = None

#     if "perfil" not in st.session_state:
#         st.session_state.perfil = None

#     if st.session_state.usuario_logado  is None:
#         login()
#     else:
#         match st.session_state.perfil:
#             case "Funcionario": funcionario_dashboard()

# main()

import streamlit as st
from datetime import datetime
from QSEVA.controller.objeto_controller import ObjetoController


def registrar_objeto():
    st.header("Registro de Objeto Encontrado")

    descricao = st.text_input("Descrição do objeto")
    local_encontrado = st.text_input("Local onde foi encontrado")

    data_hora_encontrado = st.date_input("Data em que o objeto foi encontrado")

    hora_encontrado = st.time_input("Hora em que o objeto foi encontrado")

    if st.button("Registrar Objeto"):
        try:
            data_hora_completa = datetime.combine(
                data_hora_encontrado,
                hora_encontrado
            )

            ObjetoController.inserir(
                descricao, data_hora_completa, local_encontrado
            )

            st.success("Objeto registrado com sucesso.")

        except Exception as e:
            st.error(f"Erro ao registrar objeto. {e}")
        
registrar_objeto()