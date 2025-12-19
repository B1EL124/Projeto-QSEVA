from pathlib import Path
import json
from QSEVA.model.base_model import BaseModel


DB_DIRECTORY_PATH = Path(__file__).parents[1] / "db"
DB_DIRECTORY_PATH.mkdir(exist_ok = True)


class BaseDAO:
    def __init_subclass__(cls, model: BaseModel):
        cls.model = model
        cls.DB_PATH = DB_DIRECTORY_PATH / f"{model.__name__}.json"

        cls.objetos = []
        cls.contador_id = 0
        
        if not cls.DB_PATH.exists():
            cls.salvar()


    @classmethod
    def abrir(cls):
        with cls.DB_PATH.open("r") as file:
            dados_json = json.load(file)

        cls.objetos = [cls.model.from_json(objeto_json) for objeto_json in dados_json]
        
        if hasattr(cls.model, "id"):
            cls.contador_id = max([objeto.id for objeto in cls.objetos])


    @classmethod
    def salvar(cls):
        dados_json = [objeto.to_json() for objeto in cls.objetos]

        with cls.DB_PATH.open("w") as file:
            json.dump(dados_json, file)
    

    @classmethod
    def inserir(cls, objeto: BaseModel):
        cls.abrir()

        if hasattr(cls.model, "id"):
            cls.contador_id += 1
            objeto.id = cls.contador_id
        cls.objetos.append(objeto)

        cls.salvar()

    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    

    @classmethod
    def procurar(cls, objeto_procurado: BaseModel):
        raise NotImplementedError()


    @classmethod
    def atualizar(cls, objeto_procurado: BaseModel, objeto_novo: BaseModel) -> bool:
        cls.abrir()
        
        objeto_antigo = cls.procurar(objeto_procurado)
        
        if objeto_antigo is None:
            return False
        
        cls.objetos.remove(objeto_antigo)
        cls.objetos.append(objeto_novo)

        cls.salvar()


    @classmethod
    def deletar(cls):
        cls.abrir()



        cls.salvar()