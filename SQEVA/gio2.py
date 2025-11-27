BaseModel = type()


class Pessoa(BaseModel):
    nome: str
    email: str
    id: int

samuel = Pessoa("samuel", "gyuiasdf", 235)
samuel.id = 9724354

class Funcionario(BaseModel):
    id: int
    nome: str
    fone: str
