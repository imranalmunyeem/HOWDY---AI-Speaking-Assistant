from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HOWDYmainUI(object):
    def setupUi(self, HOWDYmain):
        HOWDYmain.setObjectName("HOWDYmain")
        HOWDYmain.resize(1080, 720)
        HOWDYmain.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.howdyTechLabel = QtWidgets.QLabel(HOWDYmain)
        self.howdyTechLabel.setGeometry(QtCore.QRect(300, 10, 640, 81))
        self.howdyTechLabel.setStyleSheet("\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-color: rgb(255, 255, 255);\n"
                                           "\n"
                                           "background-color: transparent;")
        self.howdyTechLabel.setText("")
        self.howdyTechLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/KartisTechnology(white).png"))
        self.howdyTechLabel.setScaledContents(True)
        self.howdyTechLabel.setObjectName("howdyTechLabel")

        self.terminalFrame = QtWidgets.QFrame(HOWDYmain)
        self.terminalFrame.setGeometry(QtCore.QRect(10, 480, 1061, 231))
        self.terminalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.terminalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.terminalFrame.setStyleSheet(
            "background-color: transparent;\n"
            "border-color: rgb(255, 255, 255);\n"
            "border-style: solid;\n"
            "border-left: 5px;\n"
            "")
        self.terminalFrame.setObjectName("terminalFrame")

        self.enterButton = QtWidgets.QPushButton(self.terminalFrame)
        self.enterButton.setGeometry(QtCore.QRect(852, 200, 71, 31))
        self.enterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterButton.setStyleSheet(
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/enter.png);\n"
            "background-color: transparent;\n"
            "border-color: rgb(255, 255, 255);\n"
            "border-style: solid;\n"
            "border-left: 5px;\n"
            "")
        self.enterButton.setText("")
        self.enterButton.setFlat(False)
        self.enterButton.setObjectName("enterButton")

        self.exitButton = QtWidgets.QPushButton(self.terminalFrame)
        self.exitButton.setGeometry(QtCore.QRect(931, 160, 130, 71))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet(
            "border-image: url(D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/exit(with border).png);\n"
            "background-color: transparent;\n"
            "border-color: rgb(255, 255, 255);\n"
            "border-style: solid;\n"
            "border-width: 5px 5px 5px 5px;\n"
            "")
        self.exitButton.setText("")
        self.exitButton.setFlat(False)
        self.exitButton.setObjectName("exitButton")

        self.listeningLabel = QtWidgets.QLabel(HOWDYmain)
        self.listeningLabel.setGeometry(QtCore.QRect(20, 160, 250, 300))
        self.listeningLabel.setStyleSheet("border-radius: 200px;\n"
                                          "background: transparent;")
        self.listeningLabel.setText("")
        self.listeningLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/listening.gif"))
        self.listeningLabel.setScaledContents(True)
        self.listeningLabel.setObjectName("listeningLabel")

        self.sleepingLabel = QtWidgets.QLabel(HOWDYmain)
        self.sleepingLabel.setGeometry(QtCore.QRect(50, 230, 201, 185))
        self.sleepingLabel.setStyleSheet("border-radius: 200px;\n"
                                         "background: transparent;")
        self.sleepingLabel.setText("")
        self.sleepingLabel.setPixmap(
            QtGui.QPixmap(
                "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/sleepmode.gif"))
        self.sleepingLabel.setScaledContents(True)
        self.sleepingLabel.setObjectName("sleepingLabel")

        self.arcLabel = QtWidgets.QLabel(HOWDYmain)
        self.arcLabel.setGeometry(QtCore.QRect(340, 80, 411, 391))
        self.arcLabel.setStyleSheet("border-radius: 200px;\n"
                                    "background: transparent;")
        self.arcLabel.setText("")
        self.arcLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/techcircle.gif"))
        self.arcLabel.setScaledContents(True)
        self.arcLabel.setObjectName("arcLabel")

        self.backgroundgifLabel = QtWidgets.QLabel(HOWDYmain)
        self.backgroundgifLabel.setGeometry(QtCore.QRect(0, 600, 1091, 121))
        self.backgroundgifLabel.setStyleSheet("border-radius: 200px;\n"
                                              "background: transparent;")
        self.backgroundgifLabel.setText("")
        self.backgroundgifLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/background-cropped.gif"))
        self.backgroundgifLabel.setScaledContents(True)
        self.backgroundgifLabel.setObjectName("backgroundgifLabel")

        self.ironmanLabel = QtWidgets.QLabel(HOWDYmain)
        self.ironmanLabel.setGeometry(QtCore.QRect(730, -40, 481, 761))
        self.ironmanLabel.setStyleSheet("border-radius: 200px;\n"
                                        "background: transparent;")
        self.ironmanLabel.setText("")
        self.ironmanLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/howdy-portrait.png"))
        self.ironmanLabel.setScaledContents(True)
        self.ironmanLabel.setObjectName("ironmanLabel")



##################################################

        self.terminalOutputBox = QtWidgets.QPlainTextEdit(self.terminalFrame)
        self.terminalOutputBox.setGeometry(QtCore.QRect(0, 0, 923, 200))
        self.terminalOutputBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.terminalOutputBox.setMouseTracking(True)
        self.terminalOutputBox.setOverwriteMode(True)
        self.terminalOutputBox.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                     "font:14pt \"Karisma\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-style: solid;\n"
                                     "border-width: 1px 1px 1px 1px;\n"
                                     "padding-left:5px;")
        self.terminalOutputBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.terminalOutputBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.terminalOutputBox.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.terminalOutputBox.setReadOnly(True)
        self.terminalOutputBox.setPlainText(

    "                                                     FUTURE IS HERE\n"
    "                                                               Developed by Imran\n"
    "************************************************************"

)
# self.terminalOutputBox.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.terminalOutputBox.setCenterOnScroll(False)
        self.terminalOutputBox.setObjectName("terminalOutputBox")

        self.terminalInputBox = QtWidgets.QLineEdit(self.terminalFrame)
        self.terminalInputBox.setGeometry(QtCore.QRect(0, 200, 923, 31))
        self.terminalInputBox.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                    "font: 16pt \"Karisma\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 3px 3px 3px 3px;\n"
                                    "padding-left:5px;")
        self.terminalInputBox.setText("")
        self.terminalInputBox.setObjectName("terminalInputBox")

        self.howdySpeakingLabel = QtWidgets.QLabel(HOWDYmain)
        self.howdySpeakingLabel.setEnabled(True)
        self.howdySpeakingLabel.setGeometry(QtCore.QRect(0, 160, 311, 291))
        self.howdySpeakingLabel.setStyleSheet("border-radius: 200px;\n"
                                      "background: transparent;")
        self.howdySpeakingLabel.setText("")
        self.howdySpeakingLabel.setPixmap(
        QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/speaking.gif"))
        self.howdySpeakingLabel.setScaledContents(True)
        self.howdySpeakingLabel.setObjectName("howdySpeakingLabel")

        self.howdyLoadingLabel = QtWidgets.QLabel(HOWDYmain)
        self.howdyLoadingLabel.setEnabled(True)
        self.howdyLoadingLabel.setGeometry(QtCore.QRect(20, 170, 271, 261))
        self.howdySpeakingLabel.setStyleSheet("border-radius: 200px;\n"
                                      "background: transparent;")
        self.howdyLoadingLabel.setText("")
        self.howdyLoadingLabel.setPixmap(
    QtGui.QPixmap(
        "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/tech loading-cropped.gif"))
        self.howdyLoadingLabel.setScaledContents(True)
        self.howdyLoadingLabel.setObjectName("howdyLoadingLabel")

# FRAME
        self.smartHomeFrame = QtWidgets.QFrame(HOWDYmain)
        self.smartHomeFrame.setGeometry(QtCore.QRect(3, 3, 311, 171))
        self.smartHomeFrame.setStyleSheet("border-color:rgb(255, 255, 255);\n"
                                  "background: transparent;\n"
                                  "border-style: solid;\n"
                                  "border-width: 2px 2px 2px 2px;")
        self.smartHomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.smartHomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.smartHomeFrame.setObjectName("smartHomeFrame")
# REACTOR GIF
        self.ironHomeReactorLabel = QtWidgets.QLabel(HOWDYmain)
        self.ironHomeReactorLabel.setEnabled(True)
        self.ironHomeReactorLabel.setGeometry(QtCore.QRect(-43, -4, 221, 131))
        self.ironHomeReactorLabel.setText("")
        self.ironHomeReactorLabel.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/smarthomereactor.gif"))
        self.ironHomeReactorLabel.setScaledContents(True)
        self.ironHomeReactorLabel.setObjectName("IronHomeReactorLabel")
# IRON HOME LABEL
        self.ironHomeLabel = QtWidgets.QLabel(HOWDYmain)
        self.ironHomeLabel.setEnabled(True)
        self.ironHomeLabel.setGeometry(QtCore.QRect(19, 125, 101, 31))
        self.ironHomeLabel.setText("")
        self.ironHomeLabel.setStyleSheet("background: transparent;")
        self.ironHomeLabel.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/IRON HOME_.png"))
        self.ironHomeLabel.setScaledContents(True)
        self.ironHomeLabel.setObjectName("IronHomeLabel")
# ONLINE LABEL
        self.IHOnlineLabel = QtWidgets.QLabel(HOWDYmain)
        self.IHOnlineLabel.setEnabled(True)
        self.IHOnlineLabel.setGeometry(QtCore.QRect(159, 20, 101, 21))
        self.IHOnlineLabel.setText("")
        self.IHOnlineLabel.setStyleSheet("background: transparent;")
        self.IHOnlineLabel.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/ONLINE_.png"))
        self.IHOnlineLabel.setScaledContents(True)
        self.IHOnlineLabel.setObjectName("IHOnlineLabel")
# OFFLINE LABEL
        self.IHOfflineLabel = QtWidgets.QLabel(HOWDYmain)
        self.IHOfflineLabel.setEnabled(True)
        self.IHOfflineLabel.setGeometry(QtCore.QRect(159, 20, 101, 21))
        self.IHOfflineLabel.setText("")
        self.IHOfflineLabel.setStyleSheet("background: transparent;")
        self.IHOfflineLabel.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/OFFLINE_.png"))
        self.IHOfflineLabel.setScaledContents(True)
        self.IHOfflineLabel.setObjectName("IHOfflineLabel")

# LIGHT ON
        self.IHLightsON = QtWidgets.QLabel(HOWDYmain)
        self.IHLightsON.setEnabled(True)
        self.IHLightsON.setGeometry(QtCore.QRect(148, 70, 51, 45))
        self.IHLightsON.setText("")
        self.IHLightsON.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/lightON.png"))
        self.IHLightsON.setScaledContents(True)
        self.IHLightsON.setObjectName("IHLightsONLabel")
# FAN ON
        self.IHFanON = QtWidgets.QLabel(HOWDYmain)
        self.IHFanON.setEnabled(True)
        self.IHFanON.setGeometry(QtCore.QRect(210, 70, 81, 51))
        self.IHFanON.setText("")
        self.IHFanON.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/fanON.png"))
        self.IHFanON.setScaledContents(True)
        self.IHFanON.setObjectName("IHFanON")

# LIGHT OFF
        self.IHLightsOFF = QtWidgets.QLabel(HOWDYmain)
        self.IHLightsOFF.setEnabled(True)
        self.IHLightsOFF.setGeometry(QtCore.QRect(148, 70, 51, 45))
        self.IHLightsOFF.setText("")
        self.IHLightsOFF.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/lightOFF.png"))
        self.IHLightsOFF.setScaledContents(True)
        self.IHLightsOFF.setObjectName("IHLightsOFF")
# FAN OFF
        self.IHFanOFF = QtWidgets.QLabel(HOWDYmain)
        self.IHFanOFF.setEnabled(True)
        self.IHFanOFF.setGeometry(QtCore.QRect(210, 70, 81, 51))
        self.IHFanOFF.setText("")
        self.IHFanOFF.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/fanOFF.png"))
        self.IHFanOFF.setScaledContents(True)
        self.IHFanOFF.setObjectName("IHLightsONLabel")

# FAN ON LABEL
        self.IHFanONLabel = QtWidgets.QLabel(HOWDYmain)
        self.IHFanONLabel.setEnabled(True)
        self.IHFanONLabel.setGeometry(QtCore.QRect(235, 140, 31, 20))
        self.IHFanONLabel.setText("")
        self.IHFanONLabel.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/ON.png"))
        self.IHFanONLabel.setScaledContents(True)
        self.IHFanONLabel.setObjectName("IHFanONLabel")

# LIGHT ON LABEL
        self.IHLightsONLabel = QtWidgets.QLabel(HOWDYmain)
        self.IHLightsONLabel.setEnabled(True)
        self.IHLightsONLabel.setGeometry(QtCore.QRect(150, 140, 31, 20))
        self.IHLightsONLabel.setText("")
        self.IHLightsONLabel.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/ON.png"))
        self.IHLightsONLabel.setScaledContents(True)
        self.IHLightsONLabel.setObjectName("IHLightsONLabel")

# FAN OFF LABEL
        self.IHFanOFFLabel = QtWidgets.QLabel(HOWDYmain)
        self.IHFanOFFLabel.setEnabled(True)
        self.IHFanOFFLabel.setGeometry(QtCore.QRect(235, 140, 31, 20))
        self.IHFanOFFLabel.setText("")
        self.IHFanOFFLabel.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/OFF.png"))
        self.IHFanOFFLabel.setScaledContents(True)
        self.IHFanOFFLabel.setObjectName("IHFanOFFLabel")

# LIGHT OFF LABEL
        self.IHLightsOFFLabel = QtWidgets.QLabel(HOWDYmain)
        self.IHLightsOFFLabel.setEnabled(True)
        self.IHLightsOFFLabel.setGeometry(QtCore.QRect(150, 140, 31, 20))
        self.IHLightsOFFLabel.setText("")
        self.IHLightsOFFLabel.setPixmap(QtGui.QPixmap(
    "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/OFF.png"))
        self.IHLightsOFFLabel.setScaledContents(True)
        self.IHLightsOFFLabel.setObjectName("IHLightsOFFLabel")

        self.ironmanLabel.raise_()
        self.howdySpeakingLabel.raise_()
        self.howdyLoadingLabel.raise_()
        self.listeningLabel.raise_()
        self.sleepingLabel.raise_()
        self.backgroundgifLabel.raise_()
        self.exitButton.raise_()
        self.terminalFrame.raise_()
        self.enterButton.raise_()
        self.arcLabel.raise_()
        self.howdyTechLabel.raise_()
        self.smartHomeFrame.raise_()

        self.retranslateUi(HOWDYmain)
        QtCore.QMetaObject.connectSlotsByName(HOWDYmain)


    def retranslateUi(self, HOWDYmain):
        _translate = QtCore.QCoreApplication.translate
        HOWDYmain.setWindowTitle(_translate("HOWDYmain", "HOWDY Main Window"))
        self.terminalInputBox.setPlaceholderText(_translate("HOWDYmain", "Enter your command"))
        self.terminalOutputBox.setPlaceholderText(_translate("HOWDYmain", "Terminal Output goes here"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    HOWDYmain = QtWidgets.QMainWindow()
    ui = Ui_HOWDYmainUI()
    ui.setupUi(HOWDYmain)
    HOWDYmain.show()
    sys.exit(app.exec_())
