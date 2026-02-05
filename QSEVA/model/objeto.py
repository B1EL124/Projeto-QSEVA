from dataclasses import dataclass
from QSEVA.model.base_model import BaseModel
from datetime import datetime


@dataclass
class Objeto(BaseModel):
    descricao: str 
    data_hora_encontrado: datetime
    local_encontrado: str 
    id: int = None