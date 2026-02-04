from QSEVA.model.solicitacao import Solicitacao
from QSEVA.dao.solicitacao_dao import SolicitacaoDAO


class SolicitacaoController:
    @staticmethod
    def inserir(id_solicitante, descricao, data_hora) -> Solicitacao:
        solicitacao = Solicitacao(
            id_solicitante=id_solicitante,
            descricao=descricao,
            data_hora=data_hora
        )
        return SolicitacaoDAO().inserir(solicitacao)


    @staticmethod
    def listar() -> list[Solicitacao]:
        return SolicitacaoDAO().listar()


    @staticmethod
    def procurar(id) -> Solicitacao | None:
        return SolicitacaoDAO().procurar(id)


    @staticmethod
    def atualizar(id, id_solicitante, descricao, data_hora) -> None:
        solicitacao = Solicitacao(
            id=id,
            id_solicitante=id_solicitante,
            descricao=descricao,
            data_hora=data_hora
        )
        SolicitacaoDAO().atualizar(solicitacao)


    @staticmethod
    def deletar(id) -> None:
        SolicitacaoDAO().deletar(id)
