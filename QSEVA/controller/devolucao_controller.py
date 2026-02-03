# from QSEVA.model.models import Devolucao
# from QSEVA.sql_dao.


class DevolucaoController(BaseController, dao=DevolucaoDAO):
    @staticmethod
    def insert(id_objeto, id_solicitante):
        devolucao = Devolucao(id_objeto, id_solicitante)
        return DevolucaoDAO.insert(devolucao)


    @staticmethod
    def get_by_id(id_objeto, id_solicitante):
        return DevolucaoDAO.get_by_id(id_objeto, id_solicitante)


    @staticmethod
    def list_all():
        return DevolucaoDAO.list_all()


    @staticmethod
    def delete(id_objeto, id_solicitante):
        return DevolucaoDAO.delete(id_objeto, id_solicitante)
