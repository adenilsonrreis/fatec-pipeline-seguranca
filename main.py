import sqlite3


def saudacao(nome: str) -> str:
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string")
    return f"Olá, {nome}!"


def calcular_media(notas: list) -> float:
    if not notas:
        return 0
    return sum(notas) / len(notas)


def buscar_usuario_vulneravel(user_id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")

    return cursor.fetchone()


if __name__ == "__main__":
    print(saudacao("Aluno"))
    print(calcular_media([10, 8, 6]))