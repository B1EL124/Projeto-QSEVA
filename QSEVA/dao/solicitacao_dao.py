from QSEVA.model.solicitacao import Solicitacao
from QSEVA.dao.base_dao import BaseDAO


class SolicitacaoDAO(BaseDAO):
    def criar_tabela(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS solicitacao (
                id INTEGER NOT NULL,
                id_solicitante INTEGER NOT NULL,
                descricao TEXT NOT NULL,
                data_hora DATETIME NOT NULL,
                PRIMARY KEY (id)
            )
        """
        
        self.executar(sql, abrir=True, salvar=True, fechar=True)


    def resetar(self) -> None:
        sql = "DROP TABLE IF EXISTS solicitacao"
        self.executar(sql, abrir=True, salvar=True, fechar=True)


    def inserir(self, solicitacao: Solicitacao) -> Solicitacao:
        sql = """
            INSERT INTO solicitacao (id_solicitante, descricao, data_hora)
            VALUES (?, ?, ?)
        """
        parameters = (
            solicitacao.id_solicitante,
            solicitacao.descricao,
            solicitacao.data_hora
        )

        self.executar(sql, parameters, abrir=True, salvar=True, fechar=True)

        return self.procurar(id=self.cursor.lastrowid)


    def listar(self) -> list[Solicitacao]:
        sql = "SELECT * FROM solicitacao"

        self.abrir()
        self.executar(sql)
        rows = self.cursor.fetchall()
        self.fechar()
        
        return [Solicitacao(**row) for row in rows]


    def procurar(self, id: int) -> Solicitacao | None:
        sql = """
            SELECT * FROM solicitacao
            WHERE id = ?
        """
        parameters = (id,)

        self.abrir()
        self.executar(sql, parameters)
        row = self.cursor.fetchone()
        self.fechar()

        return Solicitacao(**row) if row else None


    def atualizar(self, solicitacao: Solicitacao) -> None:
        sql = """
            UPDATE solicitacao
            SET id_solicitante = ?, descricao = ?, data_hora = ?
            WHERE id = ?
        """
        parameters = (
            solicitacao.id_solicitante,
            solicitacao.descricao,
            solicitacao.data_hora,
            solicitacao.id
        )

        self.executar(sql, parameters, abrir=True, salvar=True, fechar=True)


    def deletar(self, id: int) -> None:
        sql = """
            DELETE FROM solicitacao
            WHERE id = ?
        """
        parameters = (id,)
        
        self.executar(sql, parameters, abrir=True, salvar=True, fechar=True)
