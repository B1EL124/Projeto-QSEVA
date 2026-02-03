import sqlite3
from QSEVA.sql_dao.base_dao import BaseDAO
from QSEVA.model.models import Usuario


class UsuarioDAO(BaseDAO):
    def create_table(self):
        sql = (
            "CREATE TABLE IF NOT EXISTS usuario (" \
            "id INTEGER;" \
            "nome TEXT;"
            "email TEXT" \
            "telefone TEXT;" \
            "senha TEXT;" \
            "interessado BOOLEAN;" \
            "funcionario BOOLEAN;" \
            
            "PRIMARY KEY id" \
            "UNIQUE email" \
            ")" 
        )
        self.execute(sql, open=True, commit=True, close=True)


    def insert(usuario: Usuario):
        ...