from PyQt5 import QtCore, QtGui, QtWidgets
from src.MainWindow import *






if __name__ == "__main__":
    import sys
    global app , MainWindow , ui
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.TopMovies.addItem("ad")
    


    MainWindow.show()
    sys.exit(app.exec_())
