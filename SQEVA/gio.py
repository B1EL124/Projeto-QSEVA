from typing import Type
from abc import ABC, abstractmethod
import json
from pathlib import Path


DATA_BASE_DIRECTORY_PATH = Path(__file__).parents[1]


class DAO(ABC):
    _objetos = []

    def __init_subclass__(cls, model_class: Type):
        cls.model_class = model_class
        cls.DB_PATH: Path = DATA_BASE_DIRECTORY_PATH / model_class.__name__ + ".json"
        cls.id_counter: int = 0

    @classmethod
    @abstractmethod
    def abrir(cls):
        with cls.DB_PATH.open("r") as file:
            dados_json = json.load(file)
        
        for objeto_json in dados_json:
            
    #boa sorte meu mano! --Samuel
    @classmethod
    @abstractmethod
    def salvar(cls):
        json_data = []

        for objeto in cls._objetos:
            json_data.append(objeto.to_json())

    @classmethod
    def inserir(cls, obj):
        cls.abrir()

        if hasattr(obj, "id"):
            cls.id_counter += 1
            obj.id = id

        cls._objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls._objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls._objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls._objetos.remove(aux)
            cls._objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls._objetos.remove(aux)
            cls.salvar()

    
