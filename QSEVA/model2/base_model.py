from typing import Any
from dataclasses import dataclass, Field, fields
from datetime import datetime, date, time
from decimal import Decimal


def type_cast(field: Field, value: Any) -> object:
    if value is None:
        return value

    try:
        if isinstance(value, field.type):
            return value

        if field.type is int:
            value = int(float(value))
        elif field.type in (datetime, date, time) and isinstance(value, str):
            value = field.type.fromisoformat(value)
        else:
            value = field.type(value)

    except Exception:
        if field.type in (int, float, Decimal):
            raise ValueError(f"Erro em {field.name}: deve ser um número.")
        raise

    return value


def validate(field: Field, value: Any) -> None:
    try: 
        for validator in field.metadata.get("validators", []): 
            validator(value) 

    except Exception as e: 
        raise ValueError(f"Erro em {field.name}: {e}")


def normalize(field: Field, value: Any) -> object:
    if value is None:
        return value

    value = type_cast(field, value)
    validate(field, value)

    return value


@dataclass
class BaseModel:
    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            
            value = normalize(field, value)
            setattr(self, field.name, value)
