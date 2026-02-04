from QSEVA.model.usuario import Usuario
from QSEVA.dao.usuario_dao import UsuarioDAO


class UsuarioController:
    @staticmethod
    def inserir(nome, email, telefone, senha, interessado, funcionario) -> Usuario:
        usuario = Usuario(
            nome = nome,
            email = email,
            telefone = telefone,
            senha = senha,
            interessado = interessado,
            funcionario = funcionario
        )
        return UsuarioDAO().inserir(usuario)


    @staticmethod
    def listar() -> list[Usuario]:
        return UsuarioDAO().listar()


    @staticmethod
    def procurar(id) -> Usuario | None:
        return UsuarioDAO().procurar(id)


    @staticmethod
    def atualizar(id, nome, email, telefone, senha, interessado, funcionario) -> None:
        usuario = Usuario(
            id = id,
            nome = nome,
            email = email,
            telefone = telefone,
            senha = senha,
            interessado = interessado,
            funcionario = funcionario
        )
        UsuarioDAO().atualizar(usuario)


    @staticmethod
    def deletar(id) -> None:
        UsuarioDAO().deletar(id)


    @staticmethod
    def autenticar(email, senha) -> Usuario | None:
        return UsuarioDAO().autenticar(email, senha)
