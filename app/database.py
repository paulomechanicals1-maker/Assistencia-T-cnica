import sqlite3

DATABASE = "instance/banco.db"


def get_connection():

    conexao = sqlite3.connect(DATABASE)

    conexao.row_factory = sqlite3.Row

    return conexao


def criar_tabelas():

    conexao = get_connection()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT,
            whatsapp TEXT,
            email TEXT,
            observacoes TEXT
        )
    """)

    conexao.commit()

    conexao.close()