# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DescriptionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from src.Movie import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MovieDiscrestion(QtWidgets.QDialog ):
    def __init__(self , movie :Movie):
        QtWidgets.QDialog.__init__(self)


        self.setWindowTitle(f"{movie.title}")
        self.resize(451, 241)
        self.MovieDiscription = QtWidgets.QTextBrowser(self)
        self.MovieDiscription.setGeometry(QtCore.QRect(0, 0, 451, 201))
        self.MovieDiscription.setObjectName("MovieDiscription")
        self.CloseButton = QtWidgets.QPushButton(self)
        self.CloseButton.setGeometry(QtCore.QRect(350, 210, 80, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setText("Close")


        self.CloseButton.clicked.connect(self.close)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = MovieDiscrestion(Movie(23,'23' ,'df' ,'df' , 'df'))
    Dialog.show()
    sys.exit(app.exec_())
