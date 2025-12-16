from inspect import Parameter
from .field import Field, Default
from .id_field import IdField
from .helpers import generate_function
from .errors import ModelErrors


class ModelMeta(type):
    def __new__(mcls, name, bases, namespace, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)

        # inherit metadata
        cls.__annotations__ = {}
        cls.__fields__ = {}
        cls.__primary_key_fields__ = {}

        for base in bases:
            cls.__annotations__.update(getattr(base, "__annotations__", {}))
            cls.__fields__.update(getattr(base, "__fields__", {}))
            cls.__primary_key_fields__.update(
                getattr(base, "__primary_key_fields__", {})
            )

        # collect fields from class body
        for attr_name, attr_value in namespace.items():
            if isinstance(attr_value, Field):
                attr_value.__set_name__(cls, attr_name)
                cls.__fields__[attr_name] = attr_value
                cls.__annotations__[attr_name] = attr_value.type_
                if attr_value.is_primary_key:
                    cls.__primary_key_fields__[attr_name] = attr_value

        # auto id
        if "id" not in cls.__fields__:
            cls.id = IdField(is_primary_key=True)
            cls.id.__set_name__(cls, "id")
            cls.__fields__["id"] = cls.id
            cls.__annotations__["id"] = cls.id.type_
            cls.__primary_key_fields__["id"] = cls.id

        # generate __init__ AFTER fields exist
        cls.__generate_init__()

        return cls


class Model(metaclass=ModelMeta):
    __errors__: dict[str, Exception]

    @classmethod
    def __generate_init__(cls):
        namespace = {"Default": Default}
        parameters = [Parameter("self", Parameter.POSITIONAL_OR_KEYWORD)]
        body_lines = ["self.__errors__ = {}"]

        for name, field in cls.__fields__.items():
            if field.is_auto_generated:
                continue

            parameters.append(
                Parameter(
                    name=name,
                    kind=Parameter.POSITIONAL_OR_KEYWORD,
                    default=Default if field.has_default else Parameter.empty,
                    annotation=field.type_,
                )
            )
            body_lines.append(f"self.{name} = {name}")

        for name, field in cls.__fields__.items():
            if field.is_auto_generated:
                body_lines.append(f"self.{name} = Default")

        cls.__init__ = generate_function(
            "__init__", parameters, body_lines, namespace
        )

    def __setattr__(self, name, value):
        if name in self.__fields__:
            try:
                self.__fields__[name].__set__(self, value)
            except Exception as exc:
                self.__errors__[name] = exc
        else:
            super().__setattr__(name, value)

    def __raise_errors_if_any__(self):
        if self.__errors__:
            raise ModelErrors(self.__class__, self.__errors__)
