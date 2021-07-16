from PyQt5 import QtCore, QtGui, QtWidgets
from src.MainWindow import *
from src.Api import *
from src.DataBase import *
from src.MovieWidget import *
from src.DescriptionDialog import *

import threading



def FillList(movies :list , QList:QtWidgets.QListWidget ):
    for movie in movies:
        movieItem = MovieWidget(movie)
        movieListItem = QtWidgets.QListWidgetItem(QList)
        movieListItem.setSizeHint(movieItem.sizeHint())
        Movie.ConvertFromMovieToItem(movie , movieListItem)
        QList.addItem(movieListItem)
        QList.setItemWidget(movieListItem , movieItem)



def BackgroundSearch(searchQuery , lastSearchQuery):
    ui.SearchMovies.clear()
    searchResult = Request.GetSearchMovie(searchQuery)
    lastSearchQuery = searchQuery
    FillList(searchResult , ui.SearchMovies )

def Search(lastSearchQuery):

    searchQuery = ui.lineEdit.text()
    if lastSearchQuery == searchQuery:
        return
    searchThread = threading.Thread(target=BackgroundSearch , args=(searchQuery , lastSearchQuery))
    searchThread.run()



def AddToDatabase(item :QtWidgets.QListWidgetItem ):

    movie = Movie.ConvertFromItemToMovie(item)
    dataBase.InsertMovie(movie)
    UpdateDatabase()


def UpdateDatabase():
    ui.favoritMovies.clear()
    FillList(dataBase.GetAll() , ui.favoritMovies)


def ShowDescription(item : QtWidgets.QListWidgetItem):
    movie = Movie.ConvertFromItemToMovie(item)
    discription = MovieDiscrestion(movie)
    discription.show()


def OnCreated():
    movies = Request.GetTopMovies()
    FillList(movies , ui.TopMovies)
    FillList(dataBase.GetAll() , ui.favoritMovies)



if __name__ == "__main__":
    import sys
    global app , MainWindow , ui
    global dataBase
    dataBase = DataBase()
    lastSearchQuery=""

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    OnCreated()

    ui.searchButton.clicked.connect(lambda : Search(lastSearchQuery))
    ui.TopMovies.itemClicked.connect(AddToDatabase)
    ui.SearchMovies.itemClicked.connect(AddToDatabase)
    ui.TopMovies.itemDoubleClicked.connect(ShowDescription)
    ui.SearchMovies.itemDoubleClicked.connect(ShowDescription)
    MainWindow.show()
    sys.exit(app.exec_())
