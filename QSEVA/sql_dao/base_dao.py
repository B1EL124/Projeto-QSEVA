import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / ".db"


class BaseDAO:
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor


    def __init__(self):
        self.connection: sqlite3.Connection = None
        self.cursor: sqlite3.Cursor = None


    def open(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()


    def close(self):
        self.cursor.close()
        self.connection.close()
        
        self.cursor = None
        self.connection = None


    def commit(self):
        self.connection.commit()


    def execute(
        self, sql: str, parameters: tuple = (),
        *,
        open: bool = False, commit: bool = False, close: bool = False,
    ):
        if open: self.open()
        self.cursor.execute(sql, parameters)
        if commit: self.commit()
        if close: self.close()


    def create_table():
        raise NotImplementedError()