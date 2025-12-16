from framework import Model, Field, ValidationError


def validate_str_not_empty(value: str):
    if not value.strip():
        raise ValidationError("não pode ser vazio.")


class Usuario(Model):
    nome: str = Field(validators = [validate_str_not_empty])
    telefone: str = Field(validators = [validate_str_not_empty])
    email: str = Field(validators = [validate_str_not_empty])
    senha: str = Field(validators = [validate_str_not_empty])


