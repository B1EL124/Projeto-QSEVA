from dataclasses import dataclass
from QSEVA.model.base_model import BaseModel
from datetime import datetime


@dataclass
class Solicitacao(BaseModel):
    id: int = None
    id_solicitante: int
    descricao: str 
    data_hora: datetime