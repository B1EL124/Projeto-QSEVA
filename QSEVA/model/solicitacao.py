from dataclasses import dataclass, field
from QSEVA.model.base_model import BaseModel
from QSEVA.model.validacao import nao_vazio
from datetime import datetime


@dataclass
class Solicitacao(BaseModel):
    id_solicitante: int
    descricao: str = field(metadata = {'validators':[nao_vazio]})
    local_perdido: str = field(metadata = {'validators':[nao_vazio]})
    data_hora_perdido: datetime
    data_hora: datetime
    id: int = None