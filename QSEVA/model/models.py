from diagramas.base_model import BaseModel
from QSEVA.model.field import Field
from datetime import datetime


def nao_vazio(value):
    if not value.strip():
        raise ValueError("não pode ser vazio.")


class Usuario(BaseModel):
    id: int = Field()
    nome: str = Field(validators=[nao_vazio])
    email: str = Field(validators=[nao_vazio])
    telefone: str = Field(validators=[nao_vazio])
    senha: str = Field(validators=[nao_vazio])

    permissao_administrador: bool = Field()
    permissao_funcionario: bool = Field()
    permissao_interessado: bool = Field()

    def __init__(
        self,
        id = None,
        nome = None,
        email = None,
        telefone = None,
        senha = None,
        permissao_administrador = None,
        permissao_funcionario = None,
        permissao_interessado = None,
    ):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.permissao_administrador = permissao_administrador
        self.permissao_funcionario = permissao_funcionario
        self.permissao_interessado = permissao_interessado


class Objeto(BaseModel):
    id: int = Field()
    descricao: str = Field(validators=[nao_vazio])
    guardado_em: str = Field(validators=[nao_vazio])

    def __init__(self, id = None, descricao = None, guardado_em = None):
        self.id = id
        self.descricao = descricao
        self.guardado_em = guardado_em


class Colaboracao(BaseModel):
    id_objeto: int = Field()
    id_colaborador: int = Field()
    data_hora_encontrado: datetime = Field()
    local_encontrado: str = Field(validators=[nao_vazio])

    def __init__(
        self,
        id_objeto = None,
        id_colaborador = None,
        data_hora_encontrado = None,
        local_encontrado = None,
    ):
        self.id_objeto = id_objeto
        self.id_colaborador = id_colaborador
        self.data_hora_encontrado = data_hora_encontrado
        self.local_encontrado = local_encontrado


class Solicitacao(BaseModel):
    id: int = Field()
    id_solicitante: int = Field()
    id_autorizador: int = Field()
    descricao: str = Field(validators=[nao_vazio])
    data_hora: datetime = Field()
    foi_finalizada: bool = Field()

    def __init__(
        self,
        id = None,
        id_solicitante = None,
        descricao = None,
        data_hora = None,
        foi_finalizada = None,
    ):
        self.id = id
        self.id_solicitante = id_solicitante
        self.descricao = descricao
        self.data_hora = data_hora
        self.foi_finalizada = foi_finalizada


class Devolucao(BaseModel):
    id_objeto: int = Field()
    id_solicitante: int = Field()

    def __init__(self, id_objeto = None, id_solicitante = None):
        self.id_objeto = id_objeto
        self.id_solicitante = id_solicitante
