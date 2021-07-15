from PyQt5 import QtCore, QtGui, QtWidgets
from src.MainWindow import *
from src.Api import *
from src.DataBase import *
from src.MovieWidget import *

import threading

def BackgroundSearch(searchQuery , lastSearchQuery):
    ui.SearchMovies.clear()
    searchResult = Request.GetSearchMovie(searchQuery)
    lastSearchQuery = searchQuery

    for movie in searchResult:
        ui.SearchMovies.addItem(QtWidgets.QListWidgetItem(MovieWidget(Form=ui.SearchMovies, movie=movie)))


def Search(lastSearchQuery):

    searchQuery = ui.lineEdit.text()
    if lastSearchQuery == searchQuery:
        return

    searchThread = threading.Thread(target=BackgroundSearch , args=(searchQuery , lastSearchQuery))
    searchThread.run()



def AddToDatabase(item :QtWidgets.QListWidgetItem ):
    movie = Movie.ConvertFromItemToMovie(item)
    dataBase.InsertMovie(movie)



def UpdateDatabase():
    pass




def OnCreated():
    movies = Request.GetTopMovies()
    for movie in movies:
        print(movie.title)
        movieItem = MovieWidget(movie)
        movieListItem = QtWidgets.QListWidgetItem(ui.TopMovies)
        movieListItem.setSizeHint(movieItem.sizeHint())

        Movie.ConvertFromMovieToItem(movie , movieListItem)

        ui.TopMovies.addItem(movieListItem)
        ui.TopMovies.setItemWidget(movieListItem , movieItem)




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

    MainWindow.show()
    sys.exit(app.exec_())
