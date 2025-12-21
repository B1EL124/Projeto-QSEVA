import typing
from datetime import datetime, date, time
from QSEVA.errors import NormalizationError,TypeCastError


class Field:
    def __init__(self, validators = []):
        self.validators = list(validators)
    

    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name
        self.type = typing.get_type_hints(owner).get(name)


    def __set__(self, instance, value):
        try:
            value = self.type_caster(value)
            self.validator(value)
        except Exception as e:
            raise NormalizationError(self, e)

        instance.__dict__[self.name] = value
    

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        return instance.__dict__[self.name]
    

    def type_caster(self, value):
        if value is None or isinstance(value, self.type):
            return value
        
        try:
            if self.type in (datetime, date, time):
                value = self.type.fromisoformat(value)
            else:
                value = self.type(value)
        except Exception:
            raise TypeCastError(value, self.type)

        return value


    def validator(self, value):
        if value is None:
            return
        
        for validator in self.validators:
            validator(value)