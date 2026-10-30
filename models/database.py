
import mysql.connector as mc
from mysql.connector import Error


class Database:
    """Classe que gerencia conexões e operações com um banco de dados MySQL.
    """
    def __init__(self):
        self.host = 'localhost'
        self.username = 'root'
        self.password = 'admin'
        self.database = 'biblioteca'
        self.connection = None
        self.cursor = None

    def conectar(self) -> None:
        """Estabelece uma conexão com o banco de dados MySQL"""
        try:
            self.connection = mc.connect(
                host=self.host,
                database=self.database,
                user=self.username,
                password=self.password
            )

            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print('Conexão ao banco de dados realizada!')

                return True

        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None
            return False

    def desconectar(self):
        """Encerra a conexão com banco de dados e o cursor, se existirem."""
        if self.cursor is not None:
            self.cursor.close()

        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print('Conexão encerrada com sucesso!')


# Teste da conexão
db = Database()


"""Área 51
Tudo o que for escrito dessa área
será lido e executado como string.
""" 
if db.conectar():
    db.desconectar()
