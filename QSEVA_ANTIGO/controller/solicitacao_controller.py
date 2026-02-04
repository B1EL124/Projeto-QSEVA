class SolicitacaoController(BaseController, dao=DAOS.SolicitacaoDAO):
    @staticmethod
    def insert(id_solicitante, descricao, data_hora):
        solicitacao = Models.Solicitacao(id_solicitante, descricao, data_hora)
        return DAOS.SolicitacaoDAO.insert(solicitacao)

    @staticmethod
    def get_by_id(id):
        return DAOS.SolicitacaoDAO.get_by_id(id)

    @staticmethod
    def list_all():
        return DAOS.SolicitacaoDAO.list_all()

    @staticmethod
    def update(id, id_solicitante, descricao, data_hora):
        solicitacao = Models.Solicitacao(id_solicitante, descricao, data_hora, id)
        return DAOS.SolicitacaoDAO.update(solicitacao)

    @staticmethod
    def delete(id):
        return DAOS.SolicitacaoDAO.delete(id)
