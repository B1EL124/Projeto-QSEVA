import sqlite3
from pathlib import Path

from QSEVA.model.base_model import BaseModel


DB_PATH = str(Path(__file__).parents[1] / "db.sqlite")


class BaseDAO:
    connection: sqlite3.Connection | None
    cursor: sqlite3.Cursor | None


    def __init__(self):
        self.connection = None
        self.cursor = None


    def abrir(self):
        if self.connection is not None:
            return
    
        self.connection = sqlite3.connect(
            DB_PATH,
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()


    def fechar(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        
        self.cursor = None
        self.connection = None


    def salvar(self):
        if self.connection:
            self.connection.commit()


    def executar(
        self, sql: str, parameters: tuple = (),
        *, abrir: bool = False, salvar: bool = False, fechar: bool = False,
    ):
        try: 
            if abrir: self.abrir()
            self.cursor.execute(sql, parameters)
            if salvar: self.salvar()
        
        finally:
            if fechar: self.fechar()


    def criar_tabela(self) -> None:
        raise NotImplementedError()


    def inserir(self) -> BaseModel:
        raise NotImplementedError()


    def listar(self) -> list[BaseModel]:
        raise NotImplementedError()


    def procurar(self) -> BaseModel | None:
        raise NotImplementedError()


    def atualizar(self) -> None:
        raise NotImplementedError()


    def deletar(self) -> None:
        raise NotImplementedError()
