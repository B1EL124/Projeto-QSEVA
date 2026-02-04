from QSEVA.model.objeto import Objeto
from QSEVA.dao.objeto_dao import ObjetoDAO


class ObjetoController:
    def __init__(self):
        self.dao = ObjetoDAO()


    def inserir(self, descricao, data_hora_encontrado, local_encontrado) -> Objeto:
        objeto = Objeto(
            descricao=descricao,
            data_hora_encontrado=data_hora_encontrado,
            local_encontrado=local_encontrado
        )
        return self.dao.inserir(objeto)


    def listar(self) -> list[Objeto]:
        return self.dao.listar()


    def procurar(self, id) -> Objeto | None:
        return self.dao.procurar(id)


    def atualizar(self, id, descricao, data_hora_encontrado, local_encontrado) -> None:
        objeto = Objeto(
            id=id,
            descricao=descricao,
            data_hora_encontrado=data_hora_encontrado,
            local_encontrado=local_encontrado
        )
        self.dao.atualizar(objeto)


    def deletar(self, id) -> None:
        self.dao.deletar(id)
