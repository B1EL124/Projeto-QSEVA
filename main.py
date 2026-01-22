import sys
sys.dont_write_bytecode = True


from QSEVA.controller.controllers import UsuarioController

UsuarioController.inserir(
    nome = "gio",
    email = "gio@gmail.com",
    telefone = "111111111",
    senha = "senha123",
    interessado = True,
    funcionario = True
)


from QSEVA.UI.index_ui import IndexUI
IndexUI.main()