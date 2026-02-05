from QSEVA.model.objeto import Objeto
from QSEVA.dao.objeto_dao import ObjetoDAO

class ObjetoController:
    @staticmethod
    def inserir(descricao, data_hora_encontrado, local_encontrado) -> Objeto:
        objeto = Objeto(
            descricao=descricao,
            data_hora_encontrado=data_hora_encontrado,
            local_encontrado=local_encontrado
        )
        return ObjetoDAO().inserir(objeto)

    @staticmethod
    def listar() -> list[Objeto]:
        return ObjetoDAO().listar()

    @staticmethod
    def procurar(id) -> Objeto | None:
        return ObjetoDAO().procurar(id)

    @staticmethod
    def atualizar(id, descricao, data_hora_encontrado, local_encontrado) -> None:
        objeto = Objeto(
            id=id,
            descricao=descricao,
            data_hora_encontrado=data_hora_encontrado,
            local_encontrado=local_encontrado
        )
        ObjetoDAO().atualizar(objeto)

    @staticmethod
    def deletar(id) -> None:
        ObjetoDAO().deletar(id)