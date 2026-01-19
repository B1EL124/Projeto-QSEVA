from QSEVA.model.models import Objeto
from QSEVA.dao.daos import ObjetoDAO
from datetime import datetime
from typing import List, Optional


class ObjetoController:
    @staticmethod
    def inserir(descricao: str, guardado_em: str,
                id_colaborador: int, data_hora_encontrado: datetime, local_encontrado: str) -> Objeto:
        return ObjetoDAO.inserir(
            Objeto(
                None,
                descricao,
                guardado_em,
                id_colaborador,
                data_hora_encontrado,
                local_encontrado
            )
        )


    @staticmethod
    def listar() -> List[Objeto]:
        return ObjetoDAO.listar()


    @staticmethod
    def buscar(id: int) -> Optional[Objeto]:
        return ObjetoDAO.procurar(Objeto(id))


    @staticmethod
    def atualizar(id: int, descricao: str, guardado_em: str,
                   id_colaborador: int, data_hora_encontrado: datetime, local_encontrado: str) -> Objeto:
        return ObjetoDAO.atualizar(
            Objeto(
                id,
                descricao,
                guardado_em,
                id_colaborador,
                data_hora_encontrado,
                local_encontrado
            )
        )


    @staticmethod
    def deletar(id: int) -> bool:
        return ObjetoDAO.deletar(Objeto(id))
