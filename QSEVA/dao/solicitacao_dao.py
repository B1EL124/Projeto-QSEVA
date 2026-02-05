from QSEVA.model.solicitacao import Solicitacao
from QSEVA.dao.base_dao import BaseDAO


class SolicitacaoDAO(BaseDAO):
    def criar_tabela(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS solicitacao (
                id INTEGER PRIMARY KEY,
                id_solicitante INTEGER NOT NULL,
                descricao TEXT NOT NULL,
                local_perdido TEXT NOT NULL,
                data_hora_perdido DATETIME NOT NULL,
                data_hora DATETIME NOT NULL
            )
        """
        self.abrir()
        self.executar(sql)
        self.salvar()
        self.fechar()

    
    def resetar(self) -> None:
        sql = "DROP TABLE IF EXISTS solicitacao"
        self.abrir()
        self.executar(sql)
        self.salvar()
        self.fechar()

    
    def inserir(self, solicitacao: Solicitacao) -> Solicitacao:
        sql = """
            INSERT INTO solicitacao (
                id_solicitante, descricao, local_perdido,
                data_hora_perdido, data_hora
            )
            VALUES (?, ?, ?, ?, ?)
        """
        parameters = (
            solicitacao.id_solicitante,
            solicitacao.descricao,
            solicitacao.local_perdido,
            solicitacao.data_hora_perdido,
            solicitacao.data_hora
        )

        self.abrir()
        self.executar(sql, parameters)
        self.salvar()
        solicitacao = self.procurar(id=self.cursor.lastrowid)
        self.fechar()
        return solicitacao

    
    def listar(self) -> list[Solicitacao]:
        sql = "SELECT * FROM solicitacao"
        self.abrir()
        self.executar(sql)
        rows = self.cursor.fetchall()
        self.fechar()
        return [Solicitacao(**row) for row in rows]

    
    def procurar(self, id: int) -> Solicitacao | None:
        sql = "SELECT * FROM solicitacao WHERE id = ?"
        self.abrir()
        self.executar(sql, (id,))
        row = self.cursor.fetchone()
        self.fechar()
        return Solicitacao(**row) if row else None

    
    def atualizar(self, solicitacao: Solicitacao) -> None:
        sql = """
            UPDATE solicitacao
            SET id_solicitante = ?, descricao = ?, local_perdido = ?,
                data_hora_perdido = ?, data_hora = ?
            WHERE id = ?
        """
        parameters = (
            solicitacao.id_solicitante,
            solicitacao.descricao,
            solicitacao.local_perdido,
            solicitacao.data_hora_perdido,
            solicitacao.data_hora,
            solicitacao.id
        )

        self.abrir()
        self.executar(sql, parameters)
        self.salvar()
        self.fechar()

    
    def deletar(self, id: int) -> None:
        sql = "DELETE FROM solicitacao WHERE id = ?"
        self.abrir()
        self.executar(sql, (id,))
        self.salvar()
        self.fechar()
