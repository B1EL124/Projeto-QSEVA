import sys
sys.dont_write_bytecode = True


from QSEVA.dao.criar_tabelas import criar_tabelas
from QSEVA.UI.index_ui import IndexUI
from QSEVA.controller.usuario_controller import UsuarioController


def iniciar_db():
    criar_tabelas(resetar = True)

    UsuarioController.inserir(
        nome = "Giordanni",
        email = "gio@gmail.com",
        telefone = "99999999",
        senha = "gio",
        interessado = True,
        funcionario = True
    )

# iniciar_db()
IndexUI.main()