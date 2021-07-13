from PyQt5 import QtCore, QtGui, QtWidgets
from src.MainWindow import *
from src.Api import *

import threading

def BackgroundSearch(searchQuery , lastSearchQuery):
    ui.SearchMovies.clear()
    searchResult = Request.GetSearchMovie(searchQuery)
    lastSearchQuery = searchQuery

    for movie in searchResult:
        ui.SearchMovies.addItem(movie.name)


def Search(lastSearchQuery):

    searchQuery = ui.lineEdit.text()
    if lastSearchQuery == searchQuery:
        return

    searchThread = threading.Thread(target=BackgroundSearch , args=(searchQuery , lastSearchQuery))
    searchThread.run()



def OnCreated():
    movies = Request.GetTopMovies()
    for movie in movies:
        ui.TopMovies.addItem(movie.name)


if __name__ == "__main__":
    import sys
    global app , MainWindow , ui

    lastSearchQuery=""

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    OnCreated()

    ui.searchButton.clicked.connect(lambda : Search(lastSearchQuery))

    MainWindow.show()
    sys.exit(app.exec_())
