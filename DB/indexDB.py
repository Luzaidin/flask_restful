from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

config = {
        'user': os.getenv("MYSQL_USER"),
        'password': os.getenv("MYSQL_PASSWORD"),
        'host': os.getenv("MYSQL_HOST"),
        'port': os.getenv("MYSQL_PORT"),
        'database': os.getenv("MYSQL_DATABASE"),
        'connect_timeout': 1000,
        'auth_plugin':'mysql_native_password'
}

class DB():
    def initConnection(self):
        self.connection = mysql.connector.connect(**config)

    def closeConnection(self):
        self.connection.close()

    def initCursor(self):
        self.initConnection()
        self.cursor = self.connection.cursor()

    def closeCursor(self):
        self.cursor.close()

    def commitConnection(self):
        self.connection.commit()