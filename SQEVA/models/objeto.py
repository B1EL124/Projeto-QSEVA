import json

class Objeto:
    def __init__(self, id, local, data, descricao):
        self.set_id(id)
        self.set_local(local)
        self.set_data(data)
        self.set_descricao(descricao)

    def __str__(self):
        return f"{self.__id} - {self.__local} - {self.__data} – {self.__descricao}"
    
# ---sets---
        def set_id(self, id):
            try:
                if id is None:
                    raise ValueError("Id inválido")
                if isinstance(id, str) and id.strip() == "":
                    raise ValueError
                self.__id = id
            except Exception:
                raise ValueError("ID inválido (O ID não pode estar vazio)")

        def set_local(self, local):
            try:
                if local is None or local.strip() == "":
                    raise ValueError
                self.__local = local
            except Exception:
                raise ValueError("Local inválido (O local não pode estar vazio)")

        def set_data(self, data):
            if data is None:
                raise ValueError("Data inválida")
            if isinstance(data, str):
                data = datetime.fromisoformat(data)
            if data.year > 2025:
                raise ValueError("Ano deve ser antes de 2026.")
            self.__data = data    
            #s O melhor copia e cola do mundo está nesse set

        def set_descricao(self, descricao):
            try:
                if descricao is None or descricao.strip() == "":
                    raise ValueError
                self.__descricao = descricao
            except Exception:
                raise ValueError("Descrição inválida (A descrição não pode estar vazia)")
