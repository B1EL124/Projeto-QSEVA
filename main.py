import sys
sys.dont_write_bytecode = True


from QSEVA.model.models import Usuario
from QSEVA.dao.daos import UsuarioDAO


gio = Usuario(
    nome="Giordanni",
    email="gio@gmail.com",
    telefone="111111111",
    senha="senha123",
    permissao_administrador=True,
    permissao_funcionario=False,
    permissao_interessado=True
)

joao = Usuario(
    nome="João Gustavo",
    email="joão@gmail.com",
    telefone="222222222",
    senha="senha456",
    permissao_administrador=False,
    permissao_funcionario=True,
    permissao_interessado=False
)

luis = Usuario(
    nome="Luis Benício",
    email="luis@gmail.com",
    telefone="333333333",
    senha="senha789",
    permissao_administrador=False,
    permissao_funcionario=False,
    permissao_interessado=True
)

UsuarioDAO.inserir(gio)
UsuarioDAO.inserir(joao)
UsuarioDAO.inserir(luis)
