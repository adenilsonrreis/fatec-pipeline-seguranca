import sqlite3


def saudacao(nome: str) -> str:
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string")
    return f"Olá, {nome}!"


def calcular_media(notas: list) -> float:
    if not notas:
        return 0
    return sum(notas) / len(notas)


import sqlite3


def conectar_banco():
    return sqlite3.connect("banco.db")


def buscar_usuario_vulneravel(user_id):
    conn = conectar_banco()
    cursor = conn.cursor()

    consulta = (
        f"SELECT id, nome, email "
        f"FROM usuarios "
        f"WHERE id = {user_id}"
    )

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    conn.close()

    return resultado


def buscar_por_nome_vulneravel(nome):
    conn = conectar_banco()
    cursor = conn.cursor()

    consulta = (
        f"SELECT * "
        f"FROM usuarios "
        f"WHERE nome = '{nome}'"
    )

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    conn.close()

    return resultado


def listar_pedidos_vulneravel(cliente):
    conn = conectar_banco()
    cursor = conn.cursor()

    consulta = (
        f"SELECT * "
        f"FROM pedidos "
        f"WHERE cliente = '{cliente}'"
    )

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    conn.close()

    return resultado


def buscar_produto_vulneravel(produto):
    conn = conectar_banco()
    cursor = conn.cursor()

    consulta = (
        f"SELECT * "
        f"FROM produtos "
        f"WHERE descricao LIKE '%{produto}%'"
    )

    cursor.execute(consulta)

    resultado = cursor.fetchall()

    conn.close()

    return resultado


def executar_busca():
    entrada_usuario = input("Digite um valor: ")

    usuarios = buscar_por_nome_vulneravel(
        entrada_usuario
    )

    pedidos = listar_pedidos_vulneravel(
        entrada_usuario
    )

    produtos = buscar_produto_vulneravel(
        entrada_usuario
    )

    return {
        "usuarios": usuarios,
        "pedidos": pedidos,
        "produtos": produtos,
    }
