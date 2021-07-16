import sqlite3
import sqlite3
from sqlite3 import Error
from src.Const import *
from src.Movie import *

class DataBase:

    def __init__(self):
        self.dbConnection = self.CreateConnection(PATH)
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute('CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title TEXT , year TEXT , rate TEXT , description TEXT);')


    def CreateConnection(self , path)->sqlite3.Connection:
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection


    def InsertMovie(self , movie):

        self.dbCursor.execute(f"SELECT * FROM movies WHERE id = {int(movie.id)}")
        if len(self.dbCursor.fetchall())!=0 :
            self.DeleteMovie(movie)
        else :
            self.dbCursor.execute('INSERT INTO movies (id, title , year , rate , description) VALUES (?, ? , ? , ? , ?)',
                        (int(movie.id), movie.title , movie.year , movie.rate , movie.description))
            self.dbConnection.commit()

    def DeleteMovie(self ,movie):
        self.dbCursor.execute(f"DELETE FROM movies WHERE id = {int(movie.id)}")


    def GetAll(self)->list:
        self.dbCursor.execute('SELECT * FROM movies')
        resultList = []
        for movieTuple in self.dbCursor.fetchall():
            resultList.append(Movie.ConvertFromTupleToMovie(movieTuple))
        return resultList
