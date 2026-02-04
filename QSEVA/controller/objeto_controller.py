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
        return ObjetoController().inserir(objeto)


    @staticmethod
    def listar() -> list[Objeto]:
        return ObjetoController().listar()


    @staticmethod
    def procurar(id) -> Objeto | None:
        return ObjetoController().procurar(id)


    @staticmethod
    def atualizar(id, descricao, data_hora_encontrado, local_encontrado) -> None:
        objeto = Objeto(
            id=id,
            descricao=descricao,
            data_hora_encontrado=data_hora_encontrado,
            local_encontrado=local_encontrado
        )
        ObjetoController().atualizar(objeto)


    @staticmethod
    def deletar(id) -> None:
        ObjetoController().deletar(id)
