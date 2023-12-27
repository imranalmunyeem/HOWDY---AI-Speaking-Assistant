from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loading(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1080, 720)
        self.loadingimg = QtWidgets.QLabel(Widget)
        self.loadingimg.setGeometry(QtCore.QRect(0, 0, 1080, 720))
        self.loadingimg.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.loadingimg.setText("")
        self.loadingimg.setPixmap(QtGui.QPixmap("E:\\CODING\\Artificial_Intelligence\\FacialRecogByJARVIS\\with GUI\\gui_tools\\program_load.gif"))
        self.loadingimg.setScaledContents(True)
        self.loadingimg.setObjectName("loadingimg")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QDialog()
    ui = Ui_loading()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
