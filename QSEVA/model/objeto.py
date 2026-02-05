from dataclasses import dataclass, field
from QSEVA.model.base_model import BaseModel
from QSEVA.model.validacao import nao_futuro, nao_vazio
from datetime import datetime


@dataclass
class Objeto(BaseModel):
    descricao: str 
    data_hora_encontrado: datetime = field(metadata={'validators': [nao_futuro]})
    local_encontrado: str = field(metadata = {'validators':[nao_vazio]})
    id: int = None