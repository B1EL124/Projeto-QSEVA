from typing import Optional, Type, Callable, get_type_hints
import copy

from .errors import TypeCastError, MissingFieldDefaultError


Default = object()
Unchanged = object()


class Field:
    def __init__(
        self,
        default_value: Optional[object] = None,
        default_factory: Optional[Callable[[], object]] = None,
        validators: list[Callable[[object], None]] = None,
        is_primary_key: bool = False,
        is_nullable: bool = False,
        is_immutable: bool = False,
        is_auto_generated: bool = False,
    ):
        self.validators = validators if validators is not None else []

        # ------------------------- DEFAULT ATTRIBUTES -------------------------
        self.default_value = default_value if default_factory is None else None
        self.default_factory = default_factory

        self.has_default_value = default_factory is None and (
            default_value is not None or is_nullable
        )
        self.has_default_factory = default_factory is not None
        self.has_default = default_factory is not None or (
            default_value is not None or is_nullable
        )

        # ------------------------- FLAG ATTRIBUTES -------------------------
        self.is_primary_key = is_primary_key
        self.is_nullable = is_nullable and not is_primary_key
        self.is_immutable = is_immutable or is_primary_key
        self.is_auto_generated = is_auto_generated

    
    # ------------------------- DESCRIPTOR METHODS -------------------------
    def __set_name__(self, owner: Type, name: str):
        self.owner = owner
        self.name = name

        if not hasattr(self, "type_"):
            self.type_ = get_type_hints(owner).get(name)


    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if value is Unchanged:
            return

        if self.is_immutable and self.name in instance.__dict__:
            raise AttributeError(f"Field '{self.name}' is immutable.")

        if value is Default:
            value = self.__default__()

        value = self.__type_caster__(value)
        self.__validator__(value)


        instance.__dict__[self.name] = value

    
    # ------------------------- FRAMEWORK METHODS -------------------------
    def __type_caster__(self, value):
        if self.is_nullable and value is None:
            return None

        if not isinstance(value, self.type_):
            try:
                value = self.type_(value)
            except Exception:
                raise TypeCastError(value, self.type_)

        return value


    def __validator__(self, value) -> None:
        if self.is_nullable and value is None:
            return

        for validator in self.validators:
            validator(value)


    def __default__(self):
        if self.has_default_factory:
            return self.default_factory()

        if self.has_default_value:
            return copy.copy(self.default_value)

        raise MissingFieldDefaultError(self.name)