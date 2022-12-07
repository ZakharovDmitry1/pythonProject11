import sys
from random import choice, randint
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'untitled.ui', self)
        self.do_paint = False
        self.run()

    def run(self):
        self.btn.clicked.connect(self.hello)

    def hello(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event) -> None:
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.paintRect(qp)
            qp.end()

    def paintRect(self, qp: QPainter) -> None:
        qp.fillRect(0, 0, 500, 700, QColor(255 - 17, 255 - 17, 255 - 17))
        qp.setPen(QColor(255, 0, 0))
        size = int(self.edit1.text())
        for i in range(int(self.edit3.text())):
            qp.drawRect(250 - size, 400 - size, size * 2, size * 2)
            r = float(self.edit2.text())
            size = int(r * size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
