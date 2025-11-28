from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated


class Colaboradores(BaseModel):
    nome: Annotated[str, StringConstraints(min_length=3)]
    matricula: Annotated[str, StringConstraints(min_length=14, max_length=14)]
    email: EmailStr
    fone: Annotated[str, StringConstraints(pattern=r"^\d{11}$")]
    senha: Annotated[str, StringConstraints(min_length=8)]