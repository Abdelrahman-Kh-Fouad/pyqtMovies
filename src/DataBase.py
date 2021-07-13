import sqlite3
import sqlite3
from sqlite3 import Error

class DataBase:

    @classmethod
    def init(cls , path):
        cls.dbConnection = cls.createConnection(path)
        cls.dbCursor = cls.dbConnection.cursor()

        cls.dbCursor.execute('DROP TABLE IF EXISTS movies')


    @classmethod
    def CreateConnection(path)->sqlite3.Connection:
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

