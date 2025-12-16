from .field import Field


class IdField(Field):
    def __set_name__(self, owner, name):
        super().__set_name__(owner, name)
        self.counter = 0


    def next_id(self):
        self.counter += 1
        return self.counter


    def __init__(self, is_primary_key = False):
        super().__init__(
            default_value = None,
            default_factory = self.next_id,
            validators = None,
            is_primary_key = is_primary_key,
            is_nullable = False,
            is_immutable = True,
            is_auto_generated = True,
        )
        self.type_ = int
