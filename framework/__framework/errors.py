class FrameworkError(Exception):
    ...


class ValidationError(FrameworkError):
    ...


class TypeCastError(FrameworkError):
    def __init__(self, value, target_type):
        self.value = value
        self.origin_type = type(value)
        self.target_type = target_type


class MissingFieldDefaultError(FrameworkError):
    def __init__(self, name):
        self.name = name


class ModelErrors(FrameworkError):
    def __init__(self, model, errors):
        self.mode = model
        self.errors = errors