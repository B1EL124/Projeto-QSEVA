from QSEVA.model.objeto import Objeto
from QSEVA.dao.base_dao import BaseDAO


class ObjetoDAO(BaseDAO):
    def criar_tabela(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS objeto (
                id INTEGER PRIMARY KEY,
                descricao TEXT NOT NULL,
                data_hora_encontrado DATETIME NOT NULL,
                local_encontrado TEXT NOT NULL
            )
        """
        
        self.abrir()
        self.executar(sql)
        self.salvar()
        self.fechar()


    def resetar(self) -> None:
        sql = "DROP TABLE IF EXISTS objeto"
        self.abrir()
        self.executar(sql)
        self.salvar()
        self.fechar()


    def inserir(self, objeto: Objeto) -> Objeto:
        sql = """
            INSERT INTO objeto (descricao, data_hora_encontrado, local_encontrado)
            VALUES (?, ?, ?)
        """
        parameters = (
            objeto.descricao,
            objeto.data_hora_encontrado,
            objeto.local_encontrado
        )

        self.abrir()
        self.executar(sql, parameters)
        self.salvar()
        objeto = self.procurar(id=self.cursor.lastrowid)
        self.fechar()

        return objeto


    def listar(self) -> list[Objeto]:
        sql = "SELECT * FROM objeto"

        self.abrir()
        self.executar(sql)
        rows = self.cursor.fetchall()
        self.fechar()
        
        return [Objeto(**row) for row in rows]


    def procurar(self, id: int) -> Objeto | None:
        sql = """
            SELECT * FROM objeto
            WHERE id = ?
        """
        parameters = (id,)

        self.abrir()
        self.executar(sql, parameters)
        row = self.cursor.fetchone()
        self.fechar()

        return Objeto(**row) if row else None


    def atualizar(self, objeto: Objeto) -> None:
        sql = """
            UPDATE objeto
            SET descricao = ?, data_hora_encontrado = ?, local_encontrado = ?
            WHERE id = ?
        """
        parameters = (
            objeto.descricao,
            objeto.data_hora_encontrado,
            objeto.local_encontrado,
            objeto.id
        )

        self.abrir()
        self.executar(sql, parameters)
        self.salvar()
        self.fechar()


    def deletar(self, id: int) -> None:
        sql = """
            DELETE FROM objeto
            WHERE id = ?
        """
        parameters = (id,)
        
        self.abrir()
        self.executar(sql, parameters)
        self.salvar()
        self.fechar()