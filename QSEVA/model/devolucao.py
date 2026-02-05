from dataclasses import dataclass, field
from QSEVA.model.base_model import BaseModel
from datetime import datetime

from QSEVA.model.validacao import nao_futuro


@dataclass
class Devolucao(BaseModel):
    id_objeto: int
    id_solicitante: int
    data_hora: datetime = field(metadata={'validators': [nao_futuro]})