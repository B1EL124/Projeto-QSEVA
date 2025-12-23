#from templates.loginUI import LoginUI
from templates.criarusuarioUI import CriarUsuarioUI
import streamlit as st

class IndexUI:
        def menu_usuario():
            LoginUI.main()

        def criar_usuario():
              CriarUsuarioUI.main()

