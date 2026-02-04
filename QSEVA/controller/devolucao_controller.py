from QSEVA.model.devolucao import Devolucao
from QSEVA.dao.devolucao_dao import DevolucaoDAO


class DevolucaoController:
    def __init__(self):
        self.dao = DevolucaoDAO()


    def inserir(self, id_objeto, id_solicitante, data_hora) -> Devolucao:
        devolucao = Devolucao(
            id_objeto = id_objeto, 
            id_solicitante = id_solicitante,
            data_hora = data_hora
        )
        return self.dao.inserir(devolucao)
        

    def listar(self) -> list[Devolucao]:
        return self.dao.listar()


    def procurar(self, id_objeto, id_solicitante) -> Devolucao | None:
        return self.dao.procurar(id_objeto, id_solicitante)


    def deletar(self, id_objeto, id_solicitante) -> None:
        return self.dao.deletar(id_objeto, id_solicitante)