from pathlib import Path
import json
from diagramas.base_model import BaseModel



class BaseDAO:
    def __init_subclass__(cls, model: BaseModel):
        cls.model = model

        DB_DIRECTORY = Path(__file__).parents[1] / "db"
        DB_DIRECTORY.mkdir(exist_ok = True)

        cls.DB_PATH = DB_DIRECTORY / f"{model.__name__}.json"
        cls.objetos = []
        
        if not cls.DB_PATH.exists():
            cls.salvar()


    @classmethod
    def abrir(cls):
        with cls.DB_PATH.open("r", encoding = "utf-8") as file:
            dados_json = json.load(file)

        cls.objetos = [cls.model.from_json(objeto_json) for objeto_json in dados_json]


    @classmethod
    def salvar(cls):
        dados_json = [objeto.to_json() for objeto in cls.objetos]

        with cls.DB_PATH.open("w", encoding="utf-8") as file:
            json.dump(dados_json, file, indent=4, ensure_ascii=False)


    @classmethod
    def gerar_id(cls) -> int:
        return max([objeto.id for objeto in cls.objetos], default = 0) + 1


    @classmethod
    def inserir(cls, objeto: BaseModel):
        cls.abrir()

        if hasattr(cls.model, "id"):
            objeto.id = cls.gerar_id()
            
        cls.objetos.append(objeto)

        cls.salvar()
        return objeto

    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos


    @classmethod
    def procurar(cls, objeto: BaseModel):
        ...


    @classmethod
    def atualizar(cls, objeto: BaseModel) -> bool:
        cls.abrir()
        
        objeto_antigo = cls.procurar(objeto)
        if objeto_antigo is None:
            return False
        
        cls.objetos.remove(objeto_antigo)
        cls.objetos.append(objeto)

        cls.salvar()
        return True


    @classmethod
    def deletar(cls, objeto: BaseModel) -> bool:
        cls.abrir()

        objeto = cls.procurar(objeto)
        if objeto is None:
            return False

        cls.objetos.remove(objeto)

        cls.salvar()
        return True