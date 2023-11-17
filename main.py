from random import randint
import sys
from random import randint

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Mein_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 300, 300)
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Пожалуйста, заработай...')
        self.create_yellow: QPushButton
        self.create_yellow.clicked.connect(self.du_paint_true)
        self.do_paint = False

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        if self.do_paint:
            qp.begin(self)
            self.self_draw_circle(qp)
            self.do_paint = True
            qp.end()

    def self_draw_circle(self, qp):
        radius = randint(20, 100)
        qp.setBrush(QColor(250, 255, 87))
        qp.drawEllipse(randint(10, 300), randint(10, 300), radius, radius)

    def du_paint_true(self):
        self.update()
        self.do_paint = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mein_app()
    ex.show()
    sys.exit(app.exec_())
