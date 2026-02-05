from dataclasses import dataclass, field
from QSEVA.model.base_model import BaseModel
from model.validacao import nao_vazio


@dataclass
class Usuario(BaseModel):
    nome: str = field(metadata = {'validators':[nao_vazio]})
    email: str = field(metadata = {'validators':[nao_vazio]})
    telefone: str = field(metadata = {'validators':[nao_vazio]})
    senha: str = field(metadata = {'validators':[nao_vazio]})
    interessado: bool
    funcionario: bool
    id: int = None