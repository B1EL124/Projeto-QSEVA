from typing import get_type_hints
from QSEVA.errors import TypeCastError


Default = object()
NotSet = object()


class Field:
    def __init__(
            self, 
            default_value = None, 
            default_factory = None,
            validators: list = [],
            is_pk: bool = False, 
            is_nullable: bool = False, 
    ):
        self.default_value = default_value
        self.default_factory = default_factory
        self.validators = list(validators)
        self.is_pk = is_pk
        self.is_nullable = is_nullable


    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name
        self.type = get_type_hints(owner).get(name)


    def __set__(self, instance, value):
        if value is Default:
            value = self.default()
        
        if value is not NotSet:
            value = self.type_caster(value)
            self.validator(value)

        instance.__dict__[self.name] = value



    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        return instance.__dict__[self.name]


    def type_caster(self, value):
        if self.is_nullable and value is None:
            return value
        
        if not isinstance(value, self.type):
            try:
                value = self.type(value)
            except:
                raise TypeCastError(value, self.type)

        return value


    def validator(self, value):
        if self.is_nullable and value is None:
            return
        
        for validator in self.validators:
            validator(value)


    def default(self):
        if self.default_factory is not None:
            return self.default_factory()
        
        if self.default_value is not None or self.is_nullable:
            return self.default_value