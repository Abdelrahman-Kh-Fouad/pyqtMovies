from PyQt5 import QtCore, QtGui, QtWidgets
from src.MainWindow import *
from src.Api import *


def onCreated():
    movies = Request.GetTopMovies()
    for movie in movies:
        ui.TopMovies.addItem(movie.name)


if __name__ == "__main__":
    import sys
    global app , MainWindow , ui
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    onCreated()


    MainWindow.show()
    sys.exit(app.exec_())
