# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from PyQt5 import QtGui

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.firstui.movie = QtGui.QMovie("E:\\CODING\\Artificial_Intelligence\\FacialRecogByJARVIS\\with GUI\\gui_tools\\program_load.gif")
        self.firstui.loadingimg.setMovie(self.firstui.movie)
        self.firstui.movie.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
