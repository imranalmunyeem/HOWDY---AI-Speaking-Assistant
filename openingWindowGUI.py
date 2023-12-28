from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_firstWindow(object):
    def setupUi(self, firstWindow):
        firstWindow.setObjectName("firstWindow")
        firstWindow.resize(690, 550)
        firstWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.howdyIntroLabel = QtWidgets.QLabel(firstWindow)  # Updated here
        self.howdyIntroLabel.setGeometry(QtCore.QRect(-2, 67, 690, 385))
        self.howdyIntroLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.howdyIntroLabel.setText("")
        self.howdyIntroLabel.setPixmap(QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/Hero_Template.gif"))
        self.howdyIntroLabel.setScaledContents(True)
        self.howdyIntroLabel.setWordWrap(False)
        self.howdyIntroLabel.setObjectName("howdyIntroLabel")  # Updated here

        self.startButton = QtWidgets.QPushButton(firstWindow)
        self.startButton.setGeometry(QtCore.QRect(0, 450, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setStyleSheet(
            "background-color: transparent;\n"
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/start.png);")
        self.startButton.setText("")
        icon = QtGui.QIcon.fromTheme("camera-web")
        self.startButton.setIcon(icon)
        self.startButton.setObjectName("startButton")

        self.exitButton = QtWidgets.QPushButton(firstWindow)
        self.exitButton.setGeometry(QtCore.QRect(524, 490, 161, 51))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet(
            "background-color: transparent;\n"
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/exit(with border).png);")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")

        self.loginButton = QtWidgets.QPushButton(firstWindow)
        self.loginButton.setGeometry(QtCore.QRect(262, 450, 261, 91))
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setStyleSheet(
            "background-color: transparent;\n"
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/login.png);")
        self.loginButton.setText("")
        self.loginButton.setObjectName("loginButton")

        self.textView = QtWidgets.QLabel(firstWindow)
        self.textView.setGeometry(QtCore.QRect(0, 0, 690, 71))
        self.textView.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: transparent;\n"
                                    "border-color: rgb(255, 255, 255);")
        self.textView.setText("")
        self.textView.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/KartisTechnology(white).png"))
        self.textView.setScaledContents(True)
        self.textView.setObjectName("textView")

        self.retranslateUi(firstWindow)
        QtCore.QMetaObject.connectSlotsByName(firstWindow)

    def retranslateUi(self, firstWindow):
        _translate = QtCore.QCoreApplication.translate
        firstWindow.setWindowTitle(_translate("firstWindow", "HOWDY --- Main Page"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    firstWindow = QtWidgets.QDialog()
    ui = Ui_firstWindow()
    ui.setupUi(firstWindow)
    firstWindow.show()
    sys.exit(app.exec_())
