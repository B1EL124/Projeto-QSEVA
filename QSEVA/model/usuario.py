from dataclasses import dataclass
from QSEVA.model.base_model import BaseModel


@dataclass
class Usuario(BaseModel):
    id: int = None
    nome: str 
    email: str 
    telefone: str 
    senha: str 
    interessado: bool
    funcionario: bool