from QSEVA.model.usuario import Usuario
from QSEVA.dao.base_dao import BaseDAO


class UsuarioDAO(BaseDAO):
    def criar_tabela(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL,
                senha TEXT NOT NULL,
                interessado BOOLEAN NOT NULL,
                funcionario BOOLEAN NOT NULL,

                PRIMARY KEY (id),
                UNIQUE (email)
            )
        """
        
        self.executar(sql, abrir=True, salvar=True, fechar=True)


    def resetar(self) -> None:
        sql = "DROP TABLE IF EXISTS usuario"
        self.executar(sql, abrir=True, salvar=True, fechar=True)


    def inserir(self, usuario: Usuario) -> Usuario:
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
            usuario.funcionario
        )

        self.executar(sql, parameters, abrir=True, salvar=True, fechar=True)

        return self.procurar(id = self.cursor.lastrowid)


    def listar(self) -> list[Usuario]:
        sql = "SELECT * FROM usuario"

        self.abrir()
        self.executar(sql)
        rows = self.cursor.fetchall()
        self.fechar()
        
        return [Usuario(**row) for row in rows]


    def procurar(self, id: int) -> Usuario | None:
        sql = """
            SELECT * FROM usuario
            WHERE id = ?
        """
        parameters = (id,)

        self.abrir()
        self.executar(sql, parameters)
        row = self.cursor.fetchone()
        self.fechar()

        return Usuario(**row) if row else None


    def autenticar(self, email: str, senha: str) -> Usuario | None:
        sql = """
            SELECT * FROM usuario
            WHERE email = ? AND senha = ?
        """
        parameters = (email, senha)

        self.abrir()
        self.executar(sql, parameters)
        row = self.cursor.fetchone()
        self.fechar()

        return Usuario(**row) if row else None


    def atualizar(self, usuario: Usuario) -> None:
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
            usuario.id
        )

        self.executar(sql, parameters, abrir=True, salvar=True, fechar=True)


    def deletar(self, id: int) -> None:
        sql = """
            DELETE FROM usuario
            WHERE id = ?
        """
        parameters = (id,)
        
        self.executar(sql, parameters, abrir=True, salvar=True, fechar=True)
