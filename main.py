def saudacao(nome: str) -> str:
    dif not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string")
    return f"Olá, {nome}!"


def calcular_media(notas: list) -> float:
    if not notas:
        return 0
    return sum(notas) / len(notas)


if __name__ == "__main__":
    print(saudacao("Aluno"))
    print(calcular_media([10, 8, 6]))
