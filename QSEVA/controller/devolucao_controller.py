from QSEVA.model.devolucao import Devolucao
from QSEVA.dao.devolucao_dao import DevolucaoDAO


class DevolucaoController:
    @staticmethod
    def inserir(id_objeto, id_solicitante, data_hora) -> Devolucao:
        devolucao = Devolucao(
            id_objeto = id_objeto, 
            id_solicitante = id_solicitante,
            data_hora = data_hora
        )
        return DevolucaoDAO().inserir(devolucao)
        

    @staticmethod
    def listar() -> list[Devolucao]:
        return DevolucaoDAO().listar()


    @staticmethod
    def procurar(id_objeto, id_solicitante) -> Devolucao | None:
        return DevolucaoDAO().procurar(id_objeto, id_solicitante)


    @staticmethod
    def deletar(id_objeto, id_solicitante) -> None:
        return DevolucaoDAO().deletar(id_objeto, id_solicitante)