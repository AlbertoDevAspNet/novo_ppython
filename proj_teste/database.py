
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = "localhost"
        self.user = "prof"
        self.password = "dev_mysql"
        self.database = "proj_teste"
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexão bem-sucedida ao banco de dados")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão ao banco de dados fechada")

    def execute_query(self, query):
        if not self.connection or not self.connection.is_connected():
            print("Conexão ao banco de dados não estabelecida")
            return None
        
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
        finally:
            cursor.close()