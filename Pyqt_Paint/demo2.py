from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtGui import QPixmap, QMouseEvent, QPainter, QPen
from PyQt6.QtCore import Qt, QPoint, QRect
import sys


class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap(400, 400)  # Set the size of the canvas
        self.pixmap.fill(Qt.GlobalColor.white)  # Fill the canvas with white color
        self.setPixmap(self.pixmap)  # Properly set the pixmap
        self.setMouseTracking(True)
        self.drawing = False
        self.last_mouse_position = QPoint()

    def mouseMoveEvent(self, event):
        mouse_position = event.pos()
        if (event.buttons() & Qt.MouseButton.LeftButton) and self.drawing:
            self.draw(mouse_position)
        print(mouse_position)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_mouse_position = event.pos()  # Initialize the last mouse position
            print("Left Click Position: " + str(event.pos()))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
            print("Mouse released at Position: " + str(event.pos()))

    def draw(self, points):
        painter = QPainter(self.pixmap)
        pen = QPen(Qt.GlobalColor.black, 5)  # Set pen color and width
        painter.setPen(pen)
        painter.drawLine(self.last_mouse_position, points)  # Draw a line from the last position to the current position
        self.last_mouse_position = points  # Update the last mouse position
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        target_rect = event.rect()
        painter.drawPixmap(target_rect, self.pixmap, target_rect)  # Draw the pixmap on the canvas
        painter.end()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("Paint App")
        canvas = Canvas()
        self.setCentralWidget(canvas)


app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()