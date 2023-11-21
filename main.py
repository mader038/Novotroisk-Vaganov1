import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView, QVBoxLayout, QGraphicsEllipseItem
from PyQt5 import uic
import random

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.setWindowTitle('Круги')
        self.btnDrawCircles.clicked.connect(self.draw_circles)
        
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

    def draw_circles(self):
        diameter = random.randint(10, 100)
        ellipse = QGraphicsEllipseItem(0, 0, diameter, diameter)
        ellipse.setBrush(Qt.yellow)
        self.scene.addItem(ellipse)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
