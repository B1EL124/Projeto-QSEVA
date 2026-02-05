from dataclasses import dataclass, field
from QSEVA.model.base_model import BaseModel
from model.validacao import nao_vazio
from datetime import datetime


@dataclass
class Solicitacao(BaseModel):
    id_solicitante: int
    descricao: str = field(metadata = {'validators':[nao_vazio]})
    data_hora: datetime
    id: int = None