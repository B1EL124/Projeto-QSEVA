from QSEVA.controller.base_controller import BaseController
from QSEVA.model.base_model import BaseModel
from QSEVA.model.models import Models
from QSEVA.dao.daos import DAOS
from typing import Optional


class ObjetoController(BaseController, dao = DAOS.ObjetoDAO):
    @staticmethod
    def inserir(descricao, data_hora_encontrado, local_encontrado) :
        objeto = Models.Objeto(descricao, data_hora_encontrado, local_encontrado)
        return DAOS.ObjetoDAO.inserir(objeto)

    @staticmethod
    def buscar(id) :
        return DAOS.ObjetoDAO.procurar(Models.Objeto(id))

    @staticmethod
    def atualizar(id, descricao, data_hora_encontrado, local_encontrado):
        objeto = Models.Objeto(descricao, data_hora_encontrado, local_encontrado, id)
        return DAOS.ObjetoDAO.atualizar(objeto)

    @staticmethod
    def deletar(id):
        return DAOS.ObjetoDAO.deletar(Models.Objeto(id))


class UsuarioController(BaseController, dao = DAOS.UsuarioDAO):
    @staticmethod
    def inserir(nome, email, telefone, senha, interessado, funcionario):
        usuario = Models.Usuario(nome, email, telefone, senha, interessado, funcionario)
        return DAOS.UsuarioDAO.inserir(usuario)

    @staticmethod
    def buscar(id) -> Optional[BaseModel]:
        return DAOS.UsuarioDAO.procurar(Models.Usuario(id))

    @staticmethod
    def atualizar(id, nome, email, telefone, senha):
        usuario = Models.Usuario(nome, email, telefone, senha, id)
        return DAOS.UsuarioDAO.atualizar(usuario)

    @staticmethod
    def deletar(id):
        return DAOS.UsuarioDAO.deletar(Models.Usuario(id))

    @staticmethod
    def autenticar(email, senha) -> Models.Usuario:
        for usuario in DAOS.UsuarioDAO.listar():
            if usuario.email == email and usuario.senha == senha:
                return usuario
        return None


class DevolucaoController(BaseController, dao = DAOS.DevolucaoDAO):
    @staticmethod
    def inserir(id_objeto, id_solicitante) :
        devolucao = Models.Devolucao(id_objeto, id_solicitante)
        return DAOS.DevolucaoDAO.inserir(devolucao)

    @staticmethod
    def buscar(id_objeto, id_solicitacao):
        return DAOS.DevolucaoDAO.procurar(Models.Devolucao(id_objeto, id_solicitacao))

    @staticmethod
    def deletar(id_objeto, id_solicitante):
        return DAOS.DevolucaoDAO.deletar(Models.Devolucao(id_objeto, id_solicitante))


class SolicitacaoController(BaseController, dao = DAOS.SolicitacaoDAO):
    @staticmethod
    def inserir(id_solicitante, descricao, data_hora) :
        Solicitacao = Models.Solicitacao(id_solicitante, descricao, data_hora)
        return DAOS.SolicitacaoDAO.inserir(Solicitacao)

    @staticmethod
    def buscar(id) :
        return DAOS.SolicitacaoDAO.procurar(Models.Solicitacao(id))

    @staticmethod
    def atualizar(id, id_solicitante, descricao, data_hora):
        Solicitacao = Models.Solicitacao(id_solicitante, descricao, data_hora, id)
        return DAOS.SolicitacaoDAO.atualizar(Solicitacao)

    @staticmethod
    def deletar(id):
        return DAOS.SolicitacaoDAO.deletar(Models.Solicitacao(id))


class Controllers:
    ObjetoController = ObjetoController
    SolicitacaoController = SolicitacaoController
    DevolucaoController = DevolucaoController
    UsuarioController = UsuarioController
