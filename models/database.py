
import mysql.connector as mc
from mysql.connector import Error


class Database:
    def __init__(self):
        self.host = 'localhost'
        self.username = 'root'
        self.password = 'admin'
        self.database = 'app_viagens'
        self.connection = None
        self.cursor = None

    def conectar(self):
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
        if self.cursor is not None:
            self.cursor.close()

        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print('Conexão encerrada com sucesso!')


# Teste da conexão
db = Database()

if db.conectar():
    db.desconectar()
