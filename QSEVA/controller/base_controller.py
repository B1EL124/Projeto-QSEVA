from QSEVA.model.models import BaseModel


class BaseController:
    # Não precisa colocar no diagrama
    def __init_subclass__(cls, *, dao):
        cls.dao = dao


    @classmethod
    def listar(cls) -> list[BaseModel]:
        return cls.dao.listar()