from QSEVA.dao.base_dao import BaseDAO
from QSEVA.model.models import *


class UsuarioDAO(BaseDAO, model = Usuario):
    @classmethod
    def procurar(cls, objeto):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == objeto.id:
                return obj
        return None
    

class ObjetoDAO(BaseDAO, model = Objeto):
    @classmethod
    def procurar(cls, objeto):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == objeto.id:
                return 
        return None
    


class ColaboracaoDAO(BaseDAO, model = Colaboracao):
    @classmethod
    def procurar(cls, objeto):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id_objeto == objeto.id_objeto and obj.id_colaborador == objeto.id_colaborador:
                return obj
        return None
    

class SolicitacaoDAO(BaseDAO, model = Solicitacao):
    @classmethod
    def procurar(cls, objeto):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == objeto.id:
                return obj
        return None


class DevolucaoDAO(BaseDAO, model = Devolucao):
    @classmethod
    def procurar(cls, objeto):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id_objeto == objeto.id_objeto and obj.id_solicitante == objeto.id_solicitante:
                return obj
        return None
    
