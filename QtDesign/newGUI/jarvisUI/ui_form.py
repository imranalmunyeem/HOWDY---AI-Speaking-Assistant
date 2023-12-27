# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_JARVISmain(object):
    def setupUi(self, JARVISmain):
        if not JARVISmain.objectName():
            JARVISmain.setObjectName(u"JARVISmain")
        JARVISmain.resize(1080, 720)
        JARVISmain.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.kartisTechLabel = QLabel(JARVISmain)
        self.kartisTechLabel.setObjectName(u"kartisTechLabel")
        self.kartisTechLabel.setGeometry(QRect(240, 10, 640, 81))
        self.kartisTechLabel.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"background-color: transparent;")
        self.kartisTechLabel.setPixmap(QPixmap(u"../../../gui_tools/KartisTechnology(white).png"))
        self.kartisTechLabel.setScaledContents(True)
        self.listeningLabel = QLabel(JARVISmain)
        self.listeningLabel.setObjectName(u"listeningLabel")
        self.listeningLabel.setGeometry(QRect(20, 170, 271, 261))
        self.listeningLabel.setStyleSheet(u"border-radius: 200px;\n"
"background: transparent;")
        self.listeningLabel.setPixmap(QPixmap(u"../../../gui_tools/tech loading-cropped.gif"))
        self.listeningLabel.setScaledContents(True)
        self.arcLabel = QLabel(JARVISmain)
        self.arcLabel.setObjectName(u"arcLabel")
        self.arcLabel.setGeometry(QRect(340, 80, 411, 391))
        self.arcLabel.setStyleSheet(u"border-radius: 200px;\n"
"background: transparent;")
        self.arcLabel.setPixmap(QPixmap(u"../../../gui_tools/techcircle.gif"))
        self.arcLabel.setScaledContents(True)
        self.backgroundgifLabel = QLabel(JARVISmain)
        self.backgroundgifLabel.setObjectName(u"backgroundgifLabel")
        self.backgroundgifLabel.setGeometry(QRect(0, 600, 1091, 121))
        self.backgroundgifLabel.setStyleSheet(u"border-radius: 200px;\n"
"background: transparent;")
        self.backgroundgifLabel.setPixmap(QPixmap(u"../../../gui_tools/background-cropped.gif"))
        self.backgroundgifLabel.setScaledContents(True)
        self.codingLabel = QLabel(JARVISmain)
        self.codingLabel.setObjectName(u"codingLabel")
        self.codingLabel.setGeometry(QRect(0, 0, 251, 151))
        self.codingLabel.setStyleSheet(u"border:none;\n"
"border-radius: 200px;\n"
"background: transparent;")
        self.codingLabel.setPixmap(QPixmap(u"../../../gui_tools/B.G_Template_1.gif"))
        self.codingLabel.setScaledContents(True)
        self.ironmanLabel = QLabel(JARVISmain)
        self.ironmanLabel.setObjectName(u"ironmanLabel")
        self.ironmanLabel.setGeometry(QRect(730, -40, 481, 761))
        self.ironmanLabel.setStyleSheet(u"border-radius: 200px;\n"
"background: transparent;")
        self.ironmanLabel.setPixmap(QPixmap(u"../../../gui_tools/ironman-portrait.webp"))
        self.ironmanLabel.setScaledContents(True)
        self.frame = QFrame(JARVISmain)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 480, 1061, 231))
        self.frame.setStyleSheet(u"background:none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.terminalInputBox = QLineEdit(self.frame)
        self.terminalInputBox.setObjectName(u"terminalInputBox")
        self.terminalInputBox.setGeometry(QRect(0, 200, 923, 31))
        self.terminalInputBox.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"background:transparent;\n"
"font: 16pt \"Karisma\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 3px 3px 3px 3px;\n"
"padding-left:5px;")
        self.enterButton = QPushButton(self.frame)
        self.enterButton.setObjectName(u"enterButton")
        self.enterButton.setGeometry(QRect(852, 200, 71, 31))
        self.enterButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.enterButton.setStyleSheet(u"border-image: url(E:/CODING/Artificial_Intelligence/FacialRecogByJARVIS/with GUI/gui_tools/enter.png);\n"
"background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-left: 5px;\n"
"")
        self.enterButton.setFlat(False)
        self.terminalOutputBox = QPlainTextEdit(self.frame)
        self.terminalOutputBox.setObjectName(u"terminalOutputBox")
        self.terminalOutputBox.setGeometry(QRect(0, 0, 923, 200))
        self.terminalOutputBox.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.terminalOutputBox.setMouseTracking(True)
        self.terminalOutputBox.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font:14pt \"Karisma\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 1px 1px 1px 1px;\n"
"padding-left:5px;")
        self.terminalOutputBox.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.terminalOutputBox.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.terminalOutputBox.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.terminalOutputBox.setReadOnly(True)
        self.terminalOutputBox.setOverwriteMode(True)
        self.terminalOutputBox.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.terminalOutputBox.setCenterOnScroll(True)
        self.exitButton = QPushButton(self.frame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(931, 160, 130, 71))
        self.exitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitButton.setStyleSheet(u"border-image: url(E:/CODING/Artificial_Intelligence/FacialRecogByJARVIS/with GUI/gui_tools/exit(with border).png);\n"
"background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 5px 5px 5px 5px;\n"
"")
        self.exitButton.setFlat(False)
        self.jarvisSpeakingLabel = QLabel(JARVISmain)
        self.jarvisSpeakingLabel.setObjectName(u"jarvisSpeakingLabel")
        self.jarvisSpeakingLabel.setEnabled(True)
        self.jarvisSpeakingLabel.setGeometry(QRect(0, 160, 311, 291))
        self.jarvisSpeakingLabel.setStyleSheet(u"border-radius: 200px;\n"
"background: transparent;")
        self.jarvisSpeakingLabel.setPixmap(QPixmap(u"../../../gui_tools/speaking.gif"))
        self.jarvisSpeakingLabel.setScaledContents(True)
        self.loadingLabel = QLabel(JARVISmain)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setGeometry(QRect(50, 200, 201, 201))
        self.loadingLabel.setStyleSheet(u"border-radius: 200px;\n"
"background: transparent;")
        self.loadingLabel.setPixmap(QPixmap(u"../../../gui_tools/loading.gif"))
        self.loadingLabel.setScaledContents(False)
        self.ironmanLabel.raise_()
        self.jarvisSpeakingLabel.raise_()
        self.loadingLabel.raise_()
        self.listeningLabel.raise_()
        self.arcLabel.raise_()
        self.backgroundgifLabel.raise_()
        self.frame.raise_()
        self.codingLabel.raise_()
        self.kartisTechLabel.raise_()

        self.retranslateUi(JARVISmain)

        QMetaObject.connectSlotsByName(JARVISmain)
    # setupUi

    def retranslateUi(self, JARVISmain):
        JARVISmain.setWindowTitle(QCoreApplication.translate("JARVISmain", u"JARVIS Main Window", None))
        self.kartisTechLabel.setText("")
        self.listeningLabel.setText("")
        self.arcLabel.setText("")
        self.backgroundgifLabel.setText("")
        self.codingLabel.setText("")
        self.ironmanLabel.setText("")
        self.terminalInputBox.setText("")
        self.terminalInputBox.setPlaceholderText(QCoreApplication.translate("JARVISmain", u"Enter your command", None))
        self.enterButton.setText("")
        self.terminalOutputBox.setPlainText("")
        self.terminalOutputBox.setPlaceholderText(QCoreApplication.translate("JARVISmain", u"Terminal Output goes here", None))
        self.exitButton.setText("")
        self.jarvisSpeakingLabel.setText("")
        self.loadingLabel.setText("")
    # retranslateUi

