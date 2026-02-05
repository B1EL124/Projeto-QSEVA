from dataclasses import dataclass
from QSEVA.model.base_model import BaseModel


@dataclass
class Usuario(BaseModel):
    nome: str 
    email: str 
    telefone: str 
    senha: str 
    interessado: bool
    funcionario: bool
    id: int = None