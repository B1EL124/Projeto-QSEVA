import sqlite3
from QSEVA.model.models import Usuario


class UsuarioDAO(BaseDAO):
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL,
                senha TEXT NOT NULL,
                interessado INTEGER NOT NULL,
                funcionario INTEGER NOT NULL,

                PRIMARY KEY (id)
                UNIQUE (email)
            )
        """
        self.execute(sql, open=True, commit=True, close=True)


    def insert(self, usuario: Usuario):
        sql = """
            INSERT INTO usuario (nome, email, telefone, senha, interessado, funcionario)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        parameters = (
                usuario.nome,
                usuario.email,
                usuario.telefone,
                usuario.senha,
                usuario.interessado,
                usuario.funcionario,
        )
        self.execute(sql, parameters, open=True, commit=True, close=True,)


    def list_all(self) -> list[Usuario]:
        sql = "SELECT * FROM usuario"
        self.cursor.execute(sql, open=True)
        rows = self.cursor.fetchall()
        self.close()
        return [Usuario(**row) for row in rows]


    def get_by_id(self, id: int) -> Usuario | None:
        sql = "SELECT * FROM usuario WHERE id = ?"
        self.cursor.execute(sql, (id,), open = True)

        row = self.cursor.fetchone()
        self.close()
        
        return Usuario(**row) if row else None


    def update(self, usuario: Usuario):
        sql = """
            UPDATE usuario
            SET nome = ?, email = ?, telefone = ?, senha = ?, interessado = ?, funcionario = ?
            WHERE id = ?
        """
        parameters = (
            usuario.nome,
            usuario.email,
            usuario.telefone,
            usuario.senha,
            usuario.interessado,
            usuario.funcionario,
            usuario.id,
        )
        self.execute(sql, parameters, open=True, commit=True, close=True)


    def delete(self, id: int):
        sql = "DELETE FROM usuario WHERE id = ?"
        self.execute(sql, (id,), open=True, commit=True, close=True)


    def authenticate(self, email: str, senha: str) -> Usuario | None:
        sql = "SELECT * FROM usuario WHERE email = ? AND senha = ?"
        self.cursor.execute(sql, (email, senha), open=True)

        row = self.cursor.fetchone()
        self.close()
        return Usuario(**row) if row else None
