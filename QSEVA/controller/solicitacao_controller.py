from QSEVA.model.models import Solicitacao
from QSEVA.dao.daos import SolicitacaoDAO


# class Solicitacao(BaseModel):
#     id: int = Field()
#     id_solicitante: int = Field()
#     descricao: str = Field(validators=[nao_vazio])
#     data_hora: datetime = Field()

#     def __init__(self, id_solicitante, descricao, data_hora, id = None):
#         self.id_solicitante = id_solicitante
#         self.descricao = descricao
#         self.data_hora = data_hora
#         self.id = id


# class Devolucao(BaseModel):
#     id_objeto: int = Field()
#     id_solicitante: int = Field()

#     def __init__(self, id_objeto = None, id_solicitante = None):
#         self.id_objeto = id_objeto
#         self.id_solicitante = id_solicitante


class SolicitacaoController:
    def inserir(id_solicitante, descricao, data_hora):
        solicitacao = Solicitacao(id_solicitante, descricao, data_hora)
        SolicitacaoDAO.inserir(solicitacao)


    @staticmethod
    def listar():
        return UsuarioDAO.listar()


class UsuarioController:
    @staticmethod
    def inserir(nome, email, telefone, senha):
        usuario = Usuario(nome, email, telefone, senha)
        return UsuarioDAO.inserir(usuario)


    @staticmethod
    def listar():
        return UsuarioDAO.listar()


    @staticmethod
    def buscar(id):
        return UsuarioDAO.procurar(Usuario(id))


    @staticmethod
    def atualizar(id, nome, email, telefone, senha):
        usuario = Usuario(nome, email, telefone, senha, id)
        return UsuarioDAO.atualizar(usuario)


    @staticmethod
    def deletar(id):
        return UsuarioDAO.deletar(Usuario(id))


    @staticmethod
    def autenticar(email, senha):
        for usuario in UsuarioDAO.listar():
            if usuario.email == email and usuario.senha == senha:
                return usuario
        return None