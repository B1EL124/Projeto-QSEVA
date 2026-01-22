import sys
sys.dont_write_bytecode = True
import streamlit as st

from QSEVA.UI.abrir_solicitacao_ui import AbrirSolicitacaoUI
from QSEVA.UI.home_ui import HomeUI
from QSEVA.UI.login_ui import loginUI
from QSEVA.UI.registrar_solicitação_ui import RegistrarSolicitacaoUI
from QSEVA.UI.registrar_objeto_ui import RegistrarObjetoUI


class IndexUI:
    @classmethod
    def main(cls):
        if "usuario_logado" not in st.session_state:
            st.session_state.usuario_logado = None
        if "perfil_usuario" not in st.session_state:
            st.session_state.perfil_usuario = None

        if st.session_state.usuario_logado is None:
            loginUI.main()
            st.write("Faça o seu Login")
        
        else:
            match st.session_state.perfil_usuario:
                case "interessado": cls.interessado_main()
                case "funcionario": cls.funcionario_main() 
    
    
    @classmethod
    def interessado_main(cls):
        paginas = [
            "Home",
            "Abrir Solicitação"
        ]
        pagina = st.sidebar.radio(options = paginas)

        match pagina:
            case "Home": HomeUI.main()
            case "Abrir Solicitação": AbrirSolicitacaoUI.main()


    @classmethod
    def funcionario_main(cls):
        paginas = [
            "Home", 
            "Registrar Objeto", 
            "Registrar Solicitação"
        ]
        pagina = st.sidebar.radio(options = paginas)

        match pagina:
            case "Home": HomeUI.main()
            case "Registrar Objeto": RegistrarObjetoUI.main()
            case "Registrar Solicitação": RegistrarSolicitacaoUI.main()   