import streamlit as st

from QSEVA.ui.login_ui import LoginUI

from QSEVA.ui.funcionario.listar_objetos_ui import ListarObjetosUI
from QSEVA.ui.funcionario.listar_solicitacoes_ui import ListarSolicitacoesUI
from QSEVA.ui.funcionario.registrar_devolucao_ui import RegistrarDevolucaoUI
from QSEVA.ui.funcionario.registrar_objeto_ui import RegistrarObjetoUI
from QSEVA.ui.funcionario.registrar_usuario_ui import RegistrarUsuarioUI

from QSEVA.ui.interessado.registrar_solicitacao_ui import RegistrarSolicitacaoUI
from QSEVA.ui.interessado.suas_solicitacoes_ui import SuasSolicitacoesUI



class IndexUI:
    @classmethod
    def main(cls):
        st.session_state.usuario = st.session_state.get("usuario", None)
        st.session_state.perfil = st.session_state.get("perfil", None)

        if st.session_state.usuario is None:
            LoginUI.main()
            ...
        
        else:
            match st.session_state.perfil:
                case "interessado": cls.interessado_main()
                case "funcionario": cls.funcionario_main()
    

    @classmethod
    def interessado_main(cls):
        paginas = [
            "Abrir solicitação",
            "Suas solicitações"
        ]

        pagina = st.sidebar.radio(
            "Menu do Interessado",
            options = paginas
        )

        match pagina:
            case "Abrir solicitação": ... # AbrirSolicitacaoUI.main()
            case "Suas solicitações": ... #SuasSolicitacoes.main()


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
            case "Registrar objeto": ... # RegistrarObjetoUI.main()
            case "Registrar devolução": ... # RegistrarDevolucao.main()
            case "Registrar usuário": ... # RegistrarUsuario.main()
            case "Listar solicitações": ... # ListarSolicitacoes.main()
            case "Listar objetos": ... # ListarObjetosUI.main()