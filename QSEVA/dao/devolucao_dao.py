from QSEVA.model.devolucao import Devolucao
from QSEVA.dao.base_dao import BaseDAO


class DevolucaoDAO(BaseDAO):
    def criar_tabela(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS devolucao (
                id_objeto INTEGER NOT NULL,
                id_solicitante INTEGER NOT NULL,
                data_hora DATETIME, 
                
                PRIMARY KEY (id_objeto, id_solicitante)
            )
        """

        self.abrir()
        self.executar(sql)
        self.salvar()
        self.fechar()


    def resetar(self) -> None:
        sql = "DROP TABLE IF EXISTS devolucao"

        self.abrir()
        self.executar(sql)
        self.salvar()
        self.fechar()


    def inserir(self, devolucao: Devolucao) -> Devolucao:
        sql = """
            INSERT INTO devolucao (id_objeto, id_solicitante, data_hora)
            VALUES (?, ?, ?)
        """
        parameters = (
            devolucao.id_objeto,
            devolucao.id_solicitante,
            devolucao.data_hora
        )

        self.abrir()
        self.executar(sql, parameters)
        self.salvar()
        self.fechar()

        return self.procurar(
            id_objeto = devolucao.id_objeto, 
            id_solicitante = devolucao.id_solicitante
        )

    
    def listar(self) -> list[Devolucao]:
        sql = "SELECT * FROM devolucao"

        self.abrir()
        self.executar(sql)
        rows = self.cursor.fetchall()
        self.fechar()
        
        return [Devolucao(**row) for row in rows]

    
    def procurar(self, id_objeto: int, id_solicitante: int) -> Devolucao | None:
        sql = """
            SELECT * FROM devolucao
            WHERE id_objeto = ? AND id_solicitante = ?
        """
        parameters = (
            id_objeto, 
            id_solicitante
        )

        self.abrir()
        self.executar(sql, parameters)
        row = self.cursor.fetchone()
        self.fechar()

        return Devolucao(**row) if row else None

    
    def deletar(self, id_objeto: int, id_solicitante: int) -> None:
        sql = """
            DELETE FROM devolucao
            WHERE id_objeto = ? AND id_solicitante = ?
        """
        parameters = (
            id_objeto, 
            id_solicitante
        )

        self.abrir()
        self.executar(sql, parameters)
        self.salvar()
        self.fechar()
