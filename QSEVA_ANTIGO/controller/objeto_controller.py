class ObjetoController(BaseController, dao=DAOS.ObjetoDAO):
    @staticmethod
    def insert(descricao, data_hora_encontrado, local_encontrado):
        objeto = Models.Objeto(descricao, data_hora_encontrado, local_encontrado)
        return DAOS.ObjetoDAO.insert(objeto)


    @staticmethod
    def get_by_id(id):
        return DAOS.ObjetoDAO.get_by_id(id)


    @staticmethod
    def list_all():
        return DAOS.ObjetoDAO.list_all()


    @staticmethod
    def update(id, descricao, data_hora_encontrado, local_encontrado):
        objeto = Models.Objeto(descricao, data_hora_encontrado, local_encontrado, id)
        return DAOS.ObjetoDAO.update(objeto)


    @staticmethod
    def delete(id):
        return DAOS.ObjetoDAO.delete(id)
