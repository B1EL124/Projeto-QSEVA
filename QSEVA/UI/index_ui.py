import streamlit as st

from QSEVA.UI.login_ui import LoginUI

from QSEVA.UI.funcionario.listar_objetos_ui import ListarObjetosUI
from QSEVA.UI.funcionario.listar_solicitacoes_ui import ListarSolicitacoesUI
from QSEVA.UI.funcionario.registrar_devolucao_ui import RegistrarDevolucaoUI
from QSEVA.UI.funcionario.registrar_objeto_ui import RegistrarObjetoUI
from QSEVA.UI.funcionario.registrar_usuario_ui import RegistrarUsuarioUI

from QSEVA.UI.interessado.registrar_solicitacao_ui import RegistrarSolicitacaoUI
from QSEVA.UI.interessado.suas_solicitacoes_ui import SuasSolicitacoesUI



class IndexUI:
    @classmethod
    def main(cls):
        if "usuario" not in st.session_state:
            st.session_state.usuario = None
            
        if "perfil" not in st.session_state:
            st.session_state.perfil = None

        if st.session_state.usuario is None:
            LoginUI.main()
        
        else:
            match st.session_state.perfil:
                case "interessado": cls.interessado_main()
                case "funcionario": cls.funcionario_main()
    

    @classmethod
    def interessado_main(cls):
        print("Interessado")

        paginas = [
            "Abrir solicitação",
            "Suas solicitações"
        ]

        pagina = st.sidebar.radio(
            "Menu do Interessado",
            options = paginas
        )

        print(f"Página: {pagina}")

        match pagina:
            case "Abrir solicitação": RegistrarSolicitacaoUI.main()
            case "Suas solicitações": SuasSolicitacoesUI.main()


    @classmethod
    def funcionario_main(cls):
        paginas = [
            "Registrar objeto",
            "Registrar devolução",
            "Registrar usuário",
            "Listar solicitações",
            "Listar objetos"
        ]

        pagina = st.sidebar.radio(
            "Menu do Funcionário",
            options = paginas
        )

        match pagina:
            case "Registrar objeto": RegistrarObjetoUI.main()
            case "Registrar devolução": RegistrarDevolucaoUI.main()
            case "Registrar usuário": RegistrarUsuarioUI.main()
            case "Listar solicitações": ListarSolicitacoesUI.main()
            case "Listar objetos": ListarObjetosUI.main()