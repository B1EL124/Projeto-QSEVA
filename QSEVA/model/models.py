from QSEVA.model.base_model import BaseModel
from datetime import datetime, date, time


class SAP:
    id: int
    nome: str
    horario_abrir: time
    horario_fechar: time


class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str
    senha: str


class PapelDeUsuario:
    id_usuario: int


class Interessado(PapelDeUsuario):
    ...


class Funcionario(PapelDeUsuario):
    id_sap: int


class Administrador(PapelDeUsuario):
    ...


class Objeto:
    id: int
    descricao: str    
    status: str


class Colaboracao:
    id_objeto: int
    id_interessado: int
    


class Solicitacao:
    id_objeto: int
    id_interessado: int
    status: str


