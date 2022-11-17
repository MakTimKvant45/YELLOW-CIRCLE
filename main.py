import sys
from random import randint as rnd

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor

from ui import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.qp = QPainter()
        self.draw_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            self.qp.begin(self)
            self.draw_circle(self.qp)
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(rnd(1, 255), rnd(1, 255), rnd(1, 255)))
        circle_size = rnd(1, 300)
        rand_x = rnd(1, 725)
        rand_y = rnd(1, 554)
        qp.drawEllipse(rand_x, rand_y, rand_x + circle_size, rand_x + circle_size,)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())