from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5 import QtGui

from loginWindowGUI import Ui_loginWindow


class Ui_LoginPage(QDialog):
    def __init__(self):
        super(Ui_LoginPage, self).__init__()
        self.loginui = Ui_loginWindow()
        self.loginui.setupUi(self)
        self.loginui.passwordEdit.setEchoMode(QLineEdit.Password)
        self.loginui.LoginButton.clicked.connect(self.validateLogin)
        self.loginui.exitButton.clicked.connect(self.close)

        self.loginui.illegalentrylabel.hide()
        self.loginui.retryButton.clicked.connect(self.retryFunction)
        self.loginui.illmovie = QtGui.QMovie(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/illegalEntry.gif")
        self.loginui.illegalentrylabel.setMovie(self.loginui.illmovie)

        self.loginui.backButton.clicked.connect(self.backFunction)

    def validateLogin(self):
        username = self.loginui.usernameEdit.text()
        password = self.loginui.passwordEdit.text()
        if username == "imran" and password == "imran":
            print("Login Successful")
            self.connectJarvisMainWindow()

        else:
            self.playIllegalEntry()

    def playIllegalEntry(self):
        self.loginui.illegalentrylabel.show()
        self.loginui.illmovie.start()

    def stopIllegalEntry(self):
        self.loginui.illmovie.stop()
        self.loginui.illegalentrylabel.hide()

    def retryFunction(self):
        self.loginui.usernameEdit.clear()
        self.loginui.passwordEdit.clear()
        self.stopIllegalEntry()

    def connectJarvisMainWindow(self):
        from subprocess import call
        self.close()
        call(["python", 'JARVISmainfile.py'])

    def backFunction(self):
        from secondWindow import Ui_SecondWindow
        self.secondWindow = Ui_SecondWindow()
        self.hide()
        self.secondWindow.show()
