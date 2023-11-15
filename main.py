from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        screens = QApplication.screens()
        if len(screens) < 2:
            raise Exception('You must have more than 1 monitor')
        self.web_view = QWebEngineView(self)
        self.resize(300, 300)
        self.move(QPoint(screens[1].geometry().left() + 100, screens[1].geometry().top() + 100))
        self.setWindowTitle('test')

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()