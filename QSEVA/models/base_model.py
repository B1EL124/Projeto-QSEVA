from typing import Any
from pydantic import BaseModel as PydanticBaseModel, Field as PydanticField
from pydantic.fields import FieldInfo


def Field(
    *args,
    is_primary_key: bool = False,
    is_foreign_key: bool = False,
    **kwargs
) -> Any:
    field = PydanticField(*args, **kwargs)
    field.extra["is_primary_key"] = is_primary_key
    field.extra["is_foreign_key"] = is_foreign_key
    return field


class BaseModel(PydanticBaseModel):
    @classmethod
    def next_id():
        self.id_counter += 1
        return id_counter

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls.__primary_key_fields__: dict[str, Field] = {
            name: field
            for name, field in cls.model_fields.items()
            if field.field_info.extra.get("is_primary_key", False)
        }

        cls.__foreign_key_fields__: dict[str, Field] = {
            name: field
            for name, field in cls.model_fields.items()
            if field.field_info.extra.get("is_foreign_key", False)
        }

        if not cls.__primary_key_fields__:
            cls.id_counter = 0

            cls.__annotations__["id"] = int

            cls.model_fields["id"] = FieldInfo(
                annotation = int,
                default_factory = cls.next_id
            )