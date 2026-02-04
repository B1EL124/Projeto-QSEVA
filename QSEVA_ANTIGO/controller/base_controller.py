from QSEVA.model.models import BaseModel
from typing import Optional


class BaseController:
    def __init_subclass__(cls, *, dao):
        cls.dao = dao


    @classmethod
    def inserir(nome, email, telefone, senha) -> BaseModel:
        raise NotImplementedError


    @classmethod
    def listar(cls) -> list[BaseModel]:
        return cls.dao.listar()


    @classmethod
    def buscar(id) -> Optional[BaseModel]:
        raise NotImplementedError


    @classmethod
    def atualizar(id, nome, email, telefone, senha) -> bool:
        raise NotImplementedError


    @classmethod
    def deletar(id) -> bool:
        raise NotImplementedError