import sqlite3
from QSEVA.model.models import Objeto


class ObjetoDAO(BaseDAO):
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS objeto (
                id INTEGER NOT NULL,
                descricao TEXT NOT NULL,
                data_hora_encontrado TEXT NOT NULL,
                local_encontrado TEXT NOT NULL,

                PRIMARY KEY (id)
            )
        """
        self.execute(sql, open=True, commit=True, close=True)


    def insert(self, objeto: Objeto):
        sql = """
            INSERT INTO objeto (descricao, data_hora_encontrado, local_encontrado)
            VALUES (?, ?, ?)
        """
        parameters = (
            objeto.descricao,
            objeto.data_hora_encontrado.isoformat(),
            objeto.local_encontrado,
        )
        self.execute(sql, parameters, open=True, commit=True, close=True)


    def list_all(self) -> list[Objeto]:
        sql = "SELECT * FROM objeto"
        self.cursor.execute(sql, open=True)
        rows = self.cursor.fetchall()
        self.close()
        return [Objeto(**row) for row in rows]


    def get_by_id(self, id: int) -> Objeto | None:
        sql = "SELECT * FROM objeto WHERE id = ?"
        self.cursor.execute(sql, (id,), open=True)

        row = self.cursor.fetchone()
        self.close()
        return Objeto(**row) if row else None


    def update(self, objeto: Objeto):
        sql = """
            UPDATE objeto
            SET descricao = ?, data_hora_encontrado = ?, local_encontrado = ?
            WHERE id = ?
        """
        parameters = (
            objeto.descricao,
            objeto.data_hora_encontrado.isoformat(),
            objeto.local_encontrado,
            objeto.id,
        )
        self.execute(sql, parameters, open=True, commit=True, close=True)


    def delete(self, id: int):
        sql = "DELETE FROM objeto WHERE id = ?"
        self.execute(sql, (id,), open=True, commit=True, close=True)
