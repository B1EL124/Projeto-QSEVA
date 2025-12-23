from decimal import Decimal


number_types = [int, float, Decimal]


class TypeCastError(Exception):
    def __init__(self, value, target_type):
        self.value = value
        self.origin_type = type(value)
        self.target_type = target_type
    
    def __str__(self):
        if self.origin_type is int and self.target_type in number_types:
            return "deve ser um número."
        else:
            return f"{self.origin_type.__name__} -> {self.target_type.__name__}"


class NormalizationError(Exception):
    def __init__(self, field, error):
        self.field = field
        self.error = error
    
    def __str__(self):
        return f"{self.field.name} de {self.field.owner.__name__}: {self.error}"
