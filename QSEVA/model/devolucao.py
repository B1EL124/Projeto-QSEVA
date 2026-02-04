from dataclasses import dataclass
from QSEVA.model.base_model import BaseModel
from datetime import datetime


@dataclass
class Devolucao(BaseModel):
    id_objeto: int
    id_solicitante: int
    data_hora: datetime