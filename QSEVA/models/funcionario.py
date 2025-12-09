from models.dao import DAO
import json
import os


class Funcionario:
    def __init__(self, id, nome, fone, matricula, senha):
        self.set_id(id)


    def set_id(self, id):
        try:
            if id is None:
                raise ValueError
            if isinstance(id, str) and id.strip() == "":
                raise ValueError
            self.__id = id
        except Exception:
            raise ValueError("ID inválido (não pode ser None ou vazio)")


    def set_nome(self, nome):
        try:
            if nome is None or nome.strip() == "":
                raise ValueError
            self.__nome = nome
        except Exception:
            raise ValueError("Nome inválido (não pode ser vazio)")


    def set_fone(self, fone):
        try:
            if fone is None or fone.strip() == "":
                raise ValueError
            self.__fone = fone
        except Exception:
            raise ValueError("Fone inválido (não pode ser vazio)")


    def set_matricula(self, matricula):
        try:
            if matricula is None or matricula.strip() == "":
                raise ValueError
            if len(matricula) != 11:
                self.__matricula = matricula
        except Exception:
            raise ValueError("Matrícula inválida (não poder ser vazio)")




    def set_senha(self, senha):
        try:
            if senha is None or senha.strip() == "":
                raise ValueError
            self.__senha = senha
        except Exception:
            raise ValueError("Senha inválida (não pode ser vazia)")




    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__fone} - {self.__matricula} - {self.__senha}"


class FuncionarioDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            if os.path.exists("funcionario.json") and os.path.getsize("funcionario.json") > 0:
                with open("funcionario.json", mode="r") as arquivo:
                    list_dic = json.load(arquivo)
                    for dic in list_dic:
                        obj = Funcionario.from_json(dic)
                        cls._objetos.append(obj)
        except FileNotFoundError:
            pass


    @classmethod
    def salvar(cls):
        with open("funcionario.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Funcionario.to_json)
