from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JARVISmainUI(object):
    def setupUi(self, JARVISmain):
        JARVISmain.setObjectName("JARVISmain")
        JARVISmain.resize(1080, 720)
        JARVISmain.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.kartisTechLabel = QtWidgets.QLabel(JARVISmain)
        self.kartisTechLabel.setGeometry(QtCore.QRect(300, 10, 640, 81))
        self.kartisTechLabel.setStyleSheet("\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-color: rgb(255, 255, 255);\n"
                                           "\n"
                                           "background-color: transparent;")
        self.kartisTechLabel.setText("")
        self.kartisTechLabel.setPixmap(QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/KartisTechnology(white).png"))
        self.kartisTechLabel.setScaledContents(True)
        self.kartisTechLabel.setObjectName("kartisTechLabel")

        self.terminalFrame = QtWidgets.QFrame(JARVISmain)
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


        self.listeningLabel = QtWidgets.QLabel(JARVISmain)
        self.listeningLabel.setGeometry(QtCore.QRect(20, 160, 250, 300))
        self.listeningLabel.setStyleSheet("border-radius: 200px;\n"
                                          "background: transparent;")
        self.listeningLabel.setText("")
        self.listeningLabel.setPixmap(QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/listening.gif"))
        self.listeningLabel.setScaledContents(True)
        self.listeningLabel.setObjectName("listeningLabel")

        self.sleepingLabel = QtWidgets.QLabel(JARVISmain)
        self.sleepingLabel.setGeometry(QtCore.QRect(50, 230, 201, 185))
        self.sleepingLabel.setStyleSheet("border-radius: 200px;\n"
                                          "background: transparent;")
        self.sleepingLabel.setText("")
        self.sleepingLabel.setPixmap(
            QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/sleepmode.gif"))
        self.sleepingLabel.setScaledContents(True)
        self.sleepingLabel.setObjectName("sleepingLabel")


        self.arcLabel = QtWidgets.QLabel(JARVISmain)
        self.arcLabel.setGeometry(QtCore.QRect(340, 80, 411, 391))
        self.arcLabel.setStyleSheet("border-radius: 200px;\n"
                                    "background: transparent;")
        self.arcLabel.setText("")
        self.arcLabel.setPixmap(QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/techcircle.gif"))
        self.arcLabel.setScaledContents(True)
        self.arcLabel.setObjectName("arcLabel")


        self.backgroundgifLabel = QtWidgets.QLabel(JARVISmain)
        self.backgroundgifLabel.setGeometry(QtCore.QRect(0, 600, 1091, 121))
        self.backgroundgifLabel.setStyleSheet("border-radius: 200px;\n"
                                              "background: transparent;")
        self.backgroundgifLabel.setText("")
        self.backgroundgifLabel.setPixmap(QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/background-cropped.gif"))
        self.backgroundgifLabel.setScaledContents(True)
        self.backgroundgifLabel.setObjectName("backgroundgifLabel")



        self.ironmanLabel = QtWidgets.QLabel(JARVISmain)
        self.ironmanLabel.setGeometry(QtCore.QRect(730, -40, 481, 761))
        self.ironmanLabel.setStyleSheet("border-radius: 200px;\n"
                                              "background: transparent;")
        self.ironmanLabel.setText("")
        self.ironmanLabel.setPixmap(QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/howdy-portrait.png"))
        self.ironmanLabel.setScaledContents(True)
        self.ironmanLabel.setObjectName("ironmanLabel")








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





        self.jarvisSpeakingLabel = QtWidgets.QLabel(JARVISmain)
        self.jarvisSpeakingLabel.setEnabled(True)
        self.jarvisSpeakingLabel.setGeometry(QtCore.QRect(0, 160, 311, 291))
        self.jarvisSpeakingLabel.setStyleSheet("border-radius: 200px;\n"
                                               "background: transparent;")
        self.jarvisSpeakingLabel.setText("")
        self.jarvisSpeakingLabel.setPixmap(QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/speaking.gif"))
        self.jarvisSpeakingLabel.setScaledContents(True)
        self.jarvisSpeakingLabel.setObjectName("jarvisSpeakingLabel")



        self.jarvisLoadingLabel = QtWidgets.QLabel(JARVISmain)
        self.jarvisLoadingLabel.setEnabled(True)
        self.jarvisLoadingLabel.setGeometry(QtCore.QRect(20, 170, 271, 261))
        self.jarvisSpeakingLabel.setStyleSheet("border-radius: 200px;\n"
                                               "background: transparent;")
        self.jarvisLoadingLabel.setText("")
        self.jarvisLoadingLabel.setPixmap(
            QtGui.QPixmap("D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/tech loading-cropped.gif"))
        self.jarvisLoadingLabel.setScaledContents(True)
        self.jarvisLoadingLabel.setObjectName("jarvisLoadingLabel")

        # FRAME
        self.smartHomeFrame = QtWidgets.QFrame(JARVISmain)
        self.smartHomeFrame.setGeometry(QtCore.QRect(3, 3, 311, 171))
        self.smartHomeFrame.setStyleSheet("border-color:rgb(255, 255, 255);\n"
                                          "background: transparent;\n"
                                          "border-style: solid;\n"
                                          "border-width: 2px 2px 2px 2px;")
        self.smartHomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.smartHomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.smartHomeFrame.setObjectName("smartHomeFrame")
        # REACTOR GIF
        self.ironHomeReactorLabel = QtWidgets.QLabel(JARVISmain)
        self.ironHomeReactorLabel.setEnabled(True)
        self.ironHomeReactorLabel.setGeometry(QtCore.QRect(-43, -4, 221, 131))
        self.ironHomeReactorLabel.setText("")
        self.ironHomeReactorLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/smarthomereactor.gif"))
        self.ironHomeReactorLabel.setScaledContents(True)
        self.ironHomeReactorLabel.setObjectName("IronHomeReactorLabel")
        # IRON HOME LABEL
        self.ironHomeLabel = QtWidgets.QLabel(JARVISmain)
        self.ironHomeLabel.setEnabled(True)
        self.ironHomeLabel.setGeometry(QtCore.QRect(19, 125, 101, 31))
        self.ironHomeLabel.setText("")
        self.ironHomeLabel.setStyleSheet("background: transparent;")
        self.ironHomeLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/IRON HOME_.png"))
        self.ironHomeLabel.setScaledContents(True)
        self.ironHomeLabel.setObjectName("IronHomeLabel")
        # ONLINE LABEL
        self.IHOnlineLabel = QtWidgets.QLabel(JARVISmain)
        self.IHOnlineLabel.setEnabled(True)
        self.IHOnlineLabel.setGeometry(QtCore.QRect(159, 20, 101, 21))
        self.IHOnlineLabel.setText("")
        self.IHOnlineLabel.setStyleSheet("background: transparent;")
        self.IHOnlineLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/ONLINE_.png"))
        self.IHOnlineLabel.setScaledContents(True)
        self.IHOnlineLabel.setObjectName("IHOnlineLabel")
        # OFFLINE LABEL
        self.IHOfflineLabel = QtWidgets.QLabel(JARVISmain)
        self.IHOfflineLabel.setEnabled(True)
        self.IHOfflineLabel.setGeometry(QtCore.QRect(159, 20, 101, 21))
        self.IHOfflineLabel.setText("")
        self.IHOfflineLabel.setStyleSheet("background: transparent;")
        self.IHOfflineLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/OFFLINE_.png"))
        self.IHOfflineLabel.setScaledContents(True)
        self.IHOfflineLabel.setObjectName("IHOfflineLabel")

        # LIGHT ON
        self.IHLightsON = QtWidgets.QLabel(JARVISmain)
        self.IHLightsON.setEnabled(True)
        self.IHLightsON.setGeometry(QtCore.QRect(148, 70, 51, 45))
        self.IHLightsON.setText("")
        self.IHLightsON.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/lightON.png"))
        self.IHLightsON.setScaledContents(True)
        self.IHLightsON.setObjectName("IHLightsONLabel")
        # FAN ON
        self.IHFanON = QtWidgets.QLabel(JARVISmain)
        self.IHFanON.setEnabled(True)
        self.IHFanON.setGeometry(QtCore.QRect(210, 70, 81, 51))
        self.IHFanON.setText("")
        self.IHFanON.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/fanON.png"))
        self.IHFanON.setScaledContents(True)
        self.IHFanON.setObjectName("IHFanON")

        # LIGHT OFF
        self.IHLightsOFF = QtWidgets.QLabel(JARVISmain)
        self.IHLightsOFF.setEnabled(True)
        self.IHLightsOFF.setGeometry(QtCore.QRect(148, 70, 51, 45))
        self.IHLightsOFF.setText("")
        self.IHLightsOFF.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/lightOFF.png"))
        self.IHLightsOFF.setScaledContents(True)
        self.IHLightsOFF.setObjectName("IHLightsOFF")
        # FAN OFF
        self.IHFanOFF = QtWidgets.QLabel(JARVISmain)
        self.IHFanOFF.setEnabled(True)
        self.IHFanOFF.setGeometry(QtCore.QRect(210, 70, 81, 51))
        self.IHFanOFF.setText("")
        self.IHFanOFF.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/fanOFF.png"))
        self.IHFanOFF.setScaledContents(True)
        self.IHFanOFF.setObjectName("IHLightsONLabel")

        # FAN ON LABEL
        self.IHFanONLabel = QtWidgets.QLabel(JARVISmain)
        self.IHFanONLabel.setEnabled(True)
        self.IHFanONLabel.setGeometry(QtCore.QRect(235, 140, 31, 20))
        self.IHFanONLabel.setText("")
        self.IHFanONLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/ON.png"))
        self.IHFanONLabel.setScaledContents(True)
        self.IHFanONLabel.setObjectName("IHFanONLabel")

        # LIGHT ON LABEL
        self.IHLightsONLabel = QtWidgets.QLabel(JARVISmain)
        self.IHLightsONLabel.setEnabled(True)
        self.IHLightsONLabel.setGeometry(QtCore.QRect(150, 140, 31, 20))
        self.IHLightsONLabel.setText("")
        self.IHLightsONLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/ON.png"))
        self.IHLightsONLabel.setScaledContents(True)
        self.IHLightsONLabel.setObjectName("IHLightsONLabel")

        # FAN OFF LABEL
        self.IHFanOFFLabel = QtWidgets.QLabel(JARVISmain)
        self.IHFanOFFLabel.setEnabled(True)
        self.IHFanOFFLabel.setGeometry(QtCore.QRect(235, 140, 31, 20))
        self.IHFanOFFLabel.setText("")
        self.IHFanOFFLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/OFF.png"))
        self.IHFanOFFLabel.setScaledContents(True)
        self.IHFanOFFLabel.setObjectName("IHFanOFFLabel")

        # LIGHT OFF LABEL
        self.IHLightsOFFLabel = QtWidgets.QLabel(JARVISmain)
        self.IHLightsOFFLabel.setEnabled(True)
        self.IHLightsOFFLabel.setGeometry(QtCore.QRect(150, 140, 31, 20))
        self.IHLightsOFFLabel.setText("")
        self.IHLightsOFFLabel.setPixmap(QtGui.QPixmap(
            "D:/Python Projects/Python-AI-Projects/HOWDY - AI Speaking Assistant/gui_tools/OFF.png"))
        self.IHLightsOFFLabel.setScaledContents(True)
        self.IHLightsOFFLabel.setObjectName("IHLightsOFFLabel")



        self.ironmanLabel.raise_()
        self.jarvisSpeakingLabel.raise_()
        self.jarvisLoadingLabel.raise_()
        self.listeningLabel.raise_()
        self.sleepingLabel.raise_()
        self.backgroundgifLabel.raise_()
        self.exitButton.raise_()
        self.terminalFrame.raise_()
        self.enterButton.raise_()
        self.arcLabel.raise_()
        self.kartisTechLabel.raise_()
        self.smartHomeFrame.raise_()

        self.retranslateUi(JARVISmain)
        QtCore.QMetaObject.connectSlotsByName(JARVISmain)

    def retranslateUi(self, JARVISmain):
        _translate = QtCore.QCoreApplication.translate
        JARVISmain.setWindowTitle(_translate("JARVISmain", "JARVIS Main Window"))
        self.terminalInputBox.setPlaceholderText(_translate("JARVISmain", "Enter your command"))
        self.terminalOutputBox.setPlaceholderText(_translate("JARVISmain", "Terminal Output goes here"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    JARVISmain = QtWidgets.QMainWindow()
    ui = Ui_JARVISmainUI()
    ui.setupUi(JARVISmain)
    JARVISmain.show()
    sys.exit(app.exec_())
