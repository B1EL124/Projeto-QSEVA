from QSEVA.model.usuario import Usuario
from QSEVA.dao.usuario_dao import UsuarioDAO


class UsuarioController:
    def __init__(self):
        self.dao = UsuarioDAO()


    def inserir(self, nome, email, telefone, senha, interessado, funcionario) -> Usuario:
        usuario = Usuario(
            nome=nome,
            email=email,
            telefone=telefone,
            senha=senha,
            interessado=interessado,
            funcionario=funcionario
        )
        return self.dao.inserir(usuario)


    def listar(self) -> list[Usuario]:
        return self.dao.listar()


    def procurar(self, id) -> Usuario | None:
        return self.dao.procurar(id)


    def atualizar(self, id, nome, email, telefone, senha, interessado, funcionario) -> None:
        usuario = Usuario(
            id=id,
            nome=nome,
            email=email,
            telefone=telefone,
            senha=senha,
            interessado=interessado,
            funcionario=funcionario
        )
        self.dao.atualizar(usuario)


    def deletar(self, id) -> None:
        self.dao.deletar(id)


    def autenticar(self, email, senha) -> Usuario | None:
        return self.dao.autenticar(email, senha)
