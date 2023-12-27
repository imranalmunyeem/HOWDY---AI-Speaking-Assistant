from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")


        self.videoLabel = QtWidgets.QLabel(MainWindow)
        self.videoLabel.setGeometry(QtCore.QRect(5, 70, 640, 480))
        self.videoLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                      "font:18pt \"Karisma\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "border-style: solid;\n"
                                      "border-width: 1px 1px 1px 1px;")
        self.videoLabel.setText("If you read this, then there is something wrong with your Web Camera!")
        self.videoLabel.setObjectName("videoLabel")


        self.kartisTechLabel = QtWidgets.QLabel(MainWindow)
        self.kartisTechLabel.setGeometry(QtCore.QRect(220, 0, 640, 71))
        self.kartisTechLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background: transparent;")
        self.kartisTechLabel.setText("")
        self.kartisTechLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/KartisTechnology(white).png"))
        self.kartisTechLabel.setScaledContents(True)
        self.kartisTechLabel.setObjectName("kartisTechLabel")

        self.ironmanLabel = QtWidgets.QLabel(MainWindow)
        self.ironmanLabel.setGeometry(QtCore.QRect(730, -40, 481, 761))
        self.ironmanLabel.setStyleSheet("border-radius: 200px;\n"
                                        "background: transparent;")
        self.ironmanLabel.setText("")
        self.ironmanLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/ironman-portrait.webp"))
        self.ironmanLabel.setScaledContents(True)
        self.ironmanLabel.setObjectName("ironmanLabel")





        self.loginButton = QtWidgets.QPushButton(MainWindow)
        self.loginButton.setGeometry(QtCore.QRect(89, 600, 231, 101))
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setStyleSheet(
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/login-empty.png);\n"
            "")
        self.loginButton.setText("")
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName("loginButton")



        self.exitButton = QtWidgets.QPushButton(MainWindow)
        self.exitButton.setGeometry(QtCore.QRect(320, 602, 231, 101))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet(
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/exit.png);\n"
            "")
        self.exitButton.setText("")
        self.exitButton.setFlat(False)
        self.exitButton.setObjectName("exitButton")


        self.ironmanLabel.raise_()
        self.kartisTechLabel.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HOWDY Face Recognition"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
