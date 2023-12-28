
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(1080, 720)

        loginWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.howdyTechLabel = QtWidgets.QLabel(loginWindow)
        self.howdyTechLabel.setGeometry(QtCore.QRect(220, 0, 640, 81))
        self.howdyTechLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background-color: transparent;\n"
                                           "border-color: rgb(255, 255, 255);")
        self.howdyTechLabel.setText("")
        self.howdyTechLabel.setPixmap(QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/KartisTechnology(white).png"))
        self.howdyTechLabel.setScaledContents(True)
        self.howdyTechLabel.setObjectName("howdyTechLabel")

        self.loginmainFrame = QtWidgets.QFrame(loginWindow)
        self.loginmainFrame.setGeometry(QtCore.QRect(220, 75, 640, 641))
        self.loginmainFrame.setAutoFillBackground(False)
        self.loginmainFrame.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                          "border-style: solid;\n"
                                          "border-width: 5px 5px 5px 5px;\n"
                                          "background-color: transparent;\n"
                                          "border-radius: 30px;")
        self.loginmainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginmainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginmainFrame.setObjectName("loginmainFrame")

        self.LoginButton = QtWidgets.QPushButton(self.loginmainFrame)
        self.LoginButton.setGeometry(QtCore.QRect(183, 340, 274, 101))
        self.LoginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginButton.setStyleSheet(
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/login.png);\n"
            "")
        self.LoginButton.setText("")
        self.LoginButton.setFlat(False)
        self.LoginButton.setObjectName("LoginButton")

        self.passwordEdit = QtWidgets.QLineEdit(self.loginmainFrame)
        self.passwordEdit.setGeometry(QtCore.QRect(125, 250, 391, 71))
        self.passwordEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                        "font: 30pt \"IRON MAN OF WAR 2 NCV\";\n"
                                        "border-style: solid;\n"
                                        "border-width: 1px 1px 1px 1px;\n"
                                        "border-radius: 20px;\n"
                                        "padding-left:10px;\n"
                                        "background-color: transparent;\n"
                                        "color:rgb(255, 255, 255)")
        self.passwordEdit.setObjectName("passwordEdit")

        self.usernameEdit = QtWidgets.QLineEdit(self.loginmainFrame)
        self.usernameEdit.setGeometry(QtCore.QRect(125, 150, 391, 71))
        self.usernameEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                        "font: 30pt \"IRON MAN OF WAR 2 NCV\";\n"
                                        "border-style: solid;\n"
                                        "border-width: 1px 1px 1px 1px;\n"
                                        "border-radius: 20px;\n"
                                        "padding-left:10px;\n"
                                        "background-color: transparent;\n"
                                        "color:rgb(255, 255, 255)")
        self.usernameEdit.setObjectName("usernameEdit")

        self.exitButton = QtWidgets.QPushButton(self.loginmainFrame)
        self.exitButton.setGeometry(QtCore.QRect(400, 522, 201, 91))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet(
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/exit.png);\n"
            "")
        self.exitButton.setText("")
        self.exitButton.setFlat(False)
        self.exitButton.setObjectName("exitButton")

        self.backButton = QtWidgets.QPushButton(self.loginmainFrame)
        self.backButton.setGeometry(QtCore.QRect(230, 517, 201, 91))
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet(
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/back.png);\n"
            "")
        self.backButton.setText("")
        self.backButton.setFlat(False)
        self.backButton.setObjectName("backButton")

        self.retryButton = QtWidgets.QPushButton(self.loginmainFrame)
        self.retryButton.setGeometry(QtCore.QRect(50, 525, 200, 81))
        self.retryButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retryButton.setStyleSheet(
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/retry.png);\n"
            "")
        self.retryButton.setText("")
        self.retryButton.setFlat(False)
        self.retryButton.setObjectName("retryButton")

        self.illegalentrylabel = QtWidgets.QLabel(self.loginmainFrame)
        self.illegalentrylabel.setEnabled(True)
        self.illegalentrylabel.setGeometry(QtCore.QRect(100, 90, 441, 351))
        self.illegalentrylabel.setStyleSheet("border:none;")
        self.illegalentrylabel.setText("")
        self.illegalentrylabel.setPixmap(
            QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/illegalEntry.gif"))
        self.illegalentrylabel.setScaledContents(True)
        self.illegalentrylabel.setObjectName("illegalentrylabel")

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "HOWDY - Login"))
        self.passwordEdit.setPlaceholderText(_translate("loginWindow", "Password"))
        self.usernameEdit.setPlaceholderText(_translate("loginWindow", "Username"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QDialog()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())

