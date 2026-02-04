from QSEVA.model.solicitacao import Solicitacao
from QSEVA.dao.solicitacao_dao import SolicitacaoDAO


class SolicitacaoController:
    def __init__(self):
        self.dao = SolicitacaoDAO()


    def inserir(self, id_solicitante, descricao, data_hora) -> Solicitacao:
        solicitacao = Solicitacao(
            id_solicitante=id_solicitante,
            descricao=descricao,
            data_hora=data_hora
        )
        return self.dao.inserir(solicitacao)


    def listar(self) -> list[Solicitacao]:
        return self.dao.listar()


    def procurar(self, id) -> Solicitacao | None:
        return self.dao.procurar(id)


    def atualizar(self, id, id_solicitante, descricao, data_hora) -> None:
        solicitacao = Solicitacao(
            id=id,
            id_solicitante=id_solicitante,
            descricao=descricao,
            data_hora=data_hora
        )
        self.dao.atualizar(solicitacao)


    def deletar(self, id) -> None:
        self.dao.deletar(id)
