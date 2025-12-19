from typing import Any
from decimal import Decimal
from datetime import datetime, date, time


class BaseModel:
    def to_json(self) -> dict[str, Any]:
        dados_json = {}

        for nome, valor in vars(self).items():
            if type(valor) in (Decimal, datetime, date, time):
                valor = str(valor)
            
            dados_json[nome] = valor
        
        return dados_json

    @classmethod
    def from_json(cls, dados_json) -> "BaseModel":
        return cls(**dados_json)


