from QSEVA.model.models import Usuario
from QSEVA.dao.daos import UsuarioDAO


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