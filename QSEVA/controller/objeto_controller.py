from QSEVA.model.models import Objeto
from QSEVA.dao.daos import ObjetoDAO


class ObjetoController:
    @staticmethod
    def inserir(descricao, data_hora_encontrado, local_encontrado):
        objeto = Objeto(descricao, data_hora_encontrado, local_encontrado)
        return ObjetoDAO.inserir(objeto)


    @staticmethod
    def listar():
        return ObjetoDAO.listar()


    @staticmethod
    def buscar(id):
        return ObjetoDAO.procurar(Objeto(id))


    @staticmethod
    def atualizar(id, descricao, data_hora_encontrado, local_encontrado):
        objeto = Objeto(descricao, data_hora_encontrado, local_encontrado, id)
        return ObjetoDAO.atualizar(objeto)


    @staticmethod
    def deletar(id):
        return ObjetoDAO.deletar(Objeto(id))
