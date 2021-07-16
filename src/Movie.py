import PyQt5.QtWidgets
from PyQt5 import QtWidgets


class Movie :
    def __init__(self , id , title , year , rate , description):
        self.id = id
        self.title = title
        self.year = year
        self.rate = rate
        self.description = description


    @staticmethod
    def ConvertFromMovieToItem(movie , item):
        item.setData(3 , movie.id)
        item.setData(4 , movie.title)
        item.setData(5 , movie.year)
        item.setData(6 , movie.rate)
        item.setData(7 , movie.description)


    @staticmethod
    def ConvertFromItemToMovie( item:QtWidgets.QListWidgetItem ):
        return Movie(item.data(3) , item.data(4) , item.data(5) , item.data(6) , item.data(7))

    @staticmethod
    def ConvertFromItemToMovie(item: QtWidgets.QListWidgetItem):
        return Movie(item.data(3), item.data(4), item.data(5), item.data(6), item.data(7))

    @staticmethod
    def ConvertFromTupleToMovie(movieTuple:tuple):
        return Movie(movieTuple[0] , movieTuple[1] , movieTuple[2] , movieTuple[3] , movieTuple[4])

    def __str__(self):
        return f"{self.id} , {self.title}  , {self.rate} "