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
        item.setData(0 , movie.id)
        item.setData(1 , movie.title)
        item.setData(2 , movie.year)
        item.setData(3 , movie.rate)
        item.setData(4 , movie.description)


    @staticmethod
    def ConvertFromItemToMovie( item:QtWidgets.QListWidgetItem ):
        return Movie(item.data(0) , item.data(1) , item.data(2) , item.data(3) , item.data(4))



    def __str__(self):
        return f"{self.title} , {self.year}  , {self.rate} "