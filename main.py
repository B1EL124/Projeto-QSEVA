import sys
sys.dont_write_bytecode = True

from QSEVA.models import Usuario

import inspect
print(inspect.signature(Usuario.__init__))

Joao = Usuario(
    nome="João",
    telefone="99999-9999",
    email="joao@email.com",
    senha="123"
)