import sqlite3
from QSEVA.model.models import Solicitacao


class SolicitacaoDAO(BaseDAO):
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS solicitacao (
                id INTEGER NOT NULL,
                id_solicitante INTEGER NOT NULL,
                descricao TEXT NOT NULL,
                data_hora TEXT NOT NULL,

                PRIMARY KEY (id)
            )
        """
        self.execute(sql, open=True, commit=True, close=True)


    def insert(self, solicitacao: Solicitacao):
        sql = """
            INSERT INTO solicitacao (id_solicitante, descricao, data_hora)
            VALUES (?, ?, ?)
        """
        parameters = (
            solicitacao.id_solicitante,
            solicitacao.descricao,
            solicitacao.data_hora.isoformat(),
        )
        self.execute(sql, parameters, open=True, commit=True, close=True)


    def list_all(self) -> list[Solicitacao]:
        sql = "SELECT * FROM solicitacao"
        self.cursor.execute(sql, open=True)
        rows = self.cursor.fetchall()
        self.close()
        return [Solicitacao(**row) for row in rows]


    def get_by_id(self, id: int) -> Solicitacao | None:
        sql = "SELECT * FROM solicitacao WHERE id = ?"
        self.cursor.execute(sql, (id,), open=True)
        row = self.cursor.fetchone()
        self.close()
        return Solicitacao(**row) if row else None


    def update(self, solicitacao: Solicitacao):
        sql = """
            UPDATE solicitacao
            SET id_solicitante = ?, descricao = ?, data_hora = ?
            WHERE id = ?
        """
        parameters = (
            solicitacao.id_solicitante,
            solicitacao.descricao,
            solicitacao.data_hora.isoformat(),
            solicitacao.id,
        )
        self.execute(sql, parameters, open=True, commit=True, close=True)


    def delete(self, id: int):
        sql = "DELETE FROM solicitacao WHERE id = ?"
        self.execute(sql, (id,), open=True, commit=True, close=True)



