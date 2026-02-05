from datetime import datetime


def nao_vazio(valor: str):
    if not valor.strip():
        raise ValueError("não pode ser vazio.")


def nao_futuro(valor: datetime):
    if valor > datetime.now():
        raise ValueError("A data/hora não pode ser no futuro.")