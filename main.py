import sys
sys.dont_write_bytecode = True


from QSEVA.model.models import Usuario
from QSEVA.dao.daos import UsuarioDAO


gio = Usuario(
    nome="gio",
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

# gio = UsuarioDAO.inserir(gio)
# joao = UsuarioDAO.inserir(joao)
# luis = UsuarioDAO.inserir(luis)

# for obj in UsuarioDAO.listar():
#     print(obj)

procurar_gio_por_id = Usuario(id = 1)
print(UsuarioDAO.procurar(procurar_gio_por_id))

# novo_gio = Usuario(
#     id = 1,
#     nome="Giordanni2 Funcionando",
#     email="gio2@gmail.com",
#     telefone="0000000000",
#     senha="SENHA_MUDOU",
#     permissao_administrador=True,
#     permissao_funcionario=False,
#     permissao_interessado=True
# )
# print(UsuarioDAO.atualizar(novo_gio))

# deletar_gio = Usuario(id=1)
# print(UsuarioDAO.deletar(deletar_gio))
