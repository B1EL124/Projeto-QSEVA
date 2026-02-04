import sys
sys.dont_write_bytecode = True


from QSEVA.dao.criar_tabelas import criar_tabelas
criar_tabelas(resetar = True)


from QSEVA.controller.devolucao_controller import DevolucaoController
controller = DevolucaoController()
