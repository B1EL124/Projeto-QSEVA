from QSEVA.model.models import Usuario
from QSEVA.dao.daos import UsuarioDAO


class UsuarioController:
    @staticmethod
    def inserir(nome, email, telefone, senha,
              permissao_administrador,
              permissao_funcionario,
              permissao_interessado):
        
        return UsuarioDAO.inserir(
            Usuario(
                None,
                nome,
                email,
                telefone,
                senha,
                permissao_administrador,
                permissao_funcionario,
                permissao_interessado
            )
        )


    @staticmethod
    def listar():
        return UsuarioDAO.listar()


    @staticmethod
    def buscar(id):
        return UsuarioDAO.procurar(Usuario(id))


    @staticmethod
    def atualizar(id, nome, email, telefone, senha,
                  permissao_administrador,
                  permissao_funcionario,
                  permissao_interessado):
        return UsuarioDAO.atualizar(
            Usuario(
                id,
                nome,
                email,
                telefone,
                senha,
                permissao_administrador,
                permissao_funcionario,
                permissao_interessado
            )
        )


    @staticmethod
    def deletar(id):
        return UsuarioDAO.deletar(Usuario(id))


    @staticmethod
    def autenticar(email, senha):
        for usuario in UsuarioDAO.listar():
            if usuario.email == email and usuario.senha == senha:
                return usuario
        return None