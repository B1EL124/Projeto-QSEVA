from typing import get_type_hints
from QSEVA.errors import TypeCastError
from datetime import datetime, date, time


Padrao = object()
Indefinido = object()


class Field:
    def __init__(
            self, 
            valor_padrao = None, 
            fabrica_padrao = None,
            validadores: list = [],
            chave_primaria: bool = False, 
            permitir_nulo: bool = False, 
    ):
        self.valor_padrao = valor_padrao
        self.fabrica_padrao = fabrica_padrao
        self.validadores = list(validadores)
        self.chave_primaria = chave_primaria
        self.permitir_nulo = permitir_nulo


    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name
        self.type = get_type_hints(owner).get(name)


    def __set__(self, instance, value):
        if value is Padrao:
            value = self.Padrao()
        
        if value is not Indefinido:
            value = self.conversar_tipo(value)
            self.validator(value)

        instance.__dict__[self.name] = value


    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        return instance.__dict__[self.name]


    def conversar_tipo(self, value):
        if isinstance(value, self.type) or (self.permitir_nulo and value is None):
            return value        

        try:
            match self.type:
                case int(): value = int(float(value))
                case datetime(): value = datetime.fromisoformat(value)
                case date(): value = date.fromisoformat(value)
                case time(): value = time.fromisoformat(value)
                case _: value = self.type(value)
        except:
            raise TypeCastError(value, self.type)

        return value


    def validator(self, value):
        if self.permitir_nulo and value is None:
            return
        
        for validator in self.validadores:
            validator(value)


    def Padrao(self):
        if self.fabrica_padrao is not None:
            return self.fabrica_padrao()
        
        if self.valor_padrao is not None or self.permitir_nulo:
            return self.valor_padrao