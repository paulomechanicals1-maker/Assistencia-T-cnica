from app.database import get_connection


class Cliente:

    @staticmethod
    def buscar_por_id(id):

        conexao = get_connection()

        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM clientes WHERE id = ?",
            (id,)
        )

        cliente = cursor.fetchone()

        conexao.close()

        return cliente

    @staticmethod
    def criar(
        nome,
        cpf,
        whatsapp,
        email,
        observacoes
    ):

        conexao = get_connection()

        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO clientes(
                nome,
                cpf,
                whatsapp,
                email,
                observacoes
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            nome,
            cpf,
            whatsapp,
            email,
            observacoes
        ))

        conexao.commit()

        conexao.close()

    @staticmethod
    def listar():

        conexao = get_connection()

        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM clientes ORDER BY id DESC"
        )

        clientes = cursor.fetchall()

        conexao.close()

        return clientes