import sqlite3
from QSEVA.model.models import Devolucao


class DevolucaoDAO(BaseDAO):
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS devolucao (
                id_objeto INTEGER NOT NULL,
                id_solicitante INTEGER NOT NULL,

                PRIMARY KEY (id_objeto, id_solicitante)
            )
        """
        self.execute(sql, open=True, commit=True, close=True)


    def insert(self, devolucao: Devolucao):
        sql = """
            INSERT INTO devolucao (id_objeto, id_solicitante)
            VALUES (?, ?)
        """
        parameters = (
            devolucao.id_objeto,
            devolucao.id_solicitante,
        )
        self.execute(sql, parameters, open=True, commit=True, close=True)


    def list_all(self) -> list[Devolucao]:
        sql = "SELECT * FROM devolucao"
        self.cursor.execute(sql, open=True)
        rows = self.cursor.fetchall()
        self.close()
        return [Devolucao(**row) for row in rows]


    def get_by_id(self, id_objeto: int, id_solicitante: int) -> Devolucao | None:
        sql = """
            SELECT * FROM devolucao
            WHERE id_objeto = ? AND id_solicitante = ?
        """
        self.cursor.execute(sql, (id_objeto, id_solicitante), open=True)
        row = self.cursor.fetchone()
        self.close()
        return Devolucao(**row) if row else None


    def delete(self, id_objeto: int, id_solicitante: int):
        sql = """
            DELETE FROM devolucao
            WHERE id_objeto = ? AND id_solicitante = ?
        """
        self.execute(sql, (id_objeto, id_solicitante), open=True, commit=True, close=True)
