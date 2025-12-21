from QSEVA.model.models import Usuario
from QSEVA.dao.daos import BaseDAO



class UsuarioDAO(BaseDAO, model=Usuario):
   @classmethod
   def procurar(cls, objeto):
       cls.abrir()

       for obj in cls.objetos:
           if obj.id == objeto.id:
               return obj

       return None      