def nao_vazio(valor: str):
    if not valor.strip():
        raise ValueError("não pode ser vazio.")