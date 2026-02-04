from QSEVA.dao.devolucao_dao import DevolucaoDAO
from QSEVA.dao.objeto_dao import ObjetoDAO
from QSEVA.dao.solicitacao_dao import SolicitacaoDAO
from QSEVA.dao.usuario_dao import UsuarioDAO


def criar_tabelas(resetar: bool = False):
    if resetar:
        DevolucaoDAO().resetar()
        ObjetoDAO().resetar()
        SolicitacaoDAO().resetar()
        UsuarioDAO().resetar()

    DevolucaoDAO().criar_tabela()
    ObjetoDAO().criar_tabela()
    SolicitacaoDAO().criar_tabela()
    UsuarioDAO().criar_tabela()