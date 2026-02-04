class UsuarioController(BaseController, dao=DAOS.UsuarioDAO):
    @staticmethod
    def insert(nome, email, telefone, senha, interessado, funcionario):
        usuario = Models.Usuario(nome, email, telefone, senha, interessado, funcionario)
        return DAOS.UsuarioDAO.insert(usuario)


    @staticmethod
    def get_by_id(id):
        return DAOS.UsuarioDAO.get_by_id(id)


    @staticmethod
    def list_all():
        return DAOS.UsuarioDAO.list_all()


    @staticmethod
    def update(id, nome, email, telefone, senha, interessado, funcionario):
        usuario = Models.Usuario(nome, email, telefone, senha, interessado, funcionario, id)
        return DAOS.UsuarioDAO.update(usuario)


    @staticmethod
    def delete(id):
        return DAOS.UsuarioDAO.delete(id)


    @staticmethod
    def authenticate(email, senha):
        return DAOS.UsuarioDAO.authenticate(email, senha)
