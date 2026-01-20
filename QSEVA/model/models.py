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

    def __init__(
        self, nome, email, telefone, senha, id = None
    ):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.id = id


class Objeto(BaseModel):
    id: int = Field()
    descricao: str = Field(validators=[nao_vazio])
    data_hora_encontrado: datetime = Field()
    local_encontrado: str = Field(validators=[nao_vazio])

    def __init__(self, descricao, data_hora_encontrado, local_encontrado, id = None):
        self.descricao = descricao
        self.data_hora_encontrado = data_hora_encontrado
        self.local_encontrado = local_encontrado
        self.id = id


class Solicitacao(BaseModel):
    id: int = Field()
    id_solicitante: int = Field()
    descricao: str = Field(validators=[nao_vazio])
    data_hora: datetime = Field()

    def __init__(self, id_solicitante, descricao, data_hora, id = None):
        self.id_solicitante = id_solicitante
        self.descricao = descricao
        self.data_hora = data_hora
        self.id = id


class Devolucao(BaseModel):
    id_objeto: int = Field()
    id_solicitante: int = Field()

    def __init__(self, id_objeto = None, id_solicitante = None):
        self.id_objeto = id_objeto
        self.id_solicitante = id_solicitante


class Models:
    Usuario = Usuario
    Solicitacao = Solicitacao
    Devolucao = Devolucao
    Objeto = Objeto