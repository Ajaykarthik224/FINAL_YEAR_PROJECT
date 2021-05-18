from select_state import Window2
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
counter = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window()

    def main_window(self):
        # Setting the widget or window
        self.resize(400, 300)
        self.setWindowTitle("Test Window")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 300)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:#7579e7;")
        # setting the label for displaying welcome to flood prediction model
        self.label = QLabel(self)
        self.label.setText("Welcome to Flood Prediction Model")
        self.label.setGeometry(QRect(10, 30, 371, 71))
        self.label.setStyleSheet("font: 14pt \"Sans serif\";\n"
                                 "font-weight:bold;\n"
                                 "color:#FFFFFF;\n"
                                 "background-color:#344fa1;\n"
                                 "padding-left:10px;")
        # label2 to set a image below label1
        self.label2 = QLabel(self)
        self.label2.setGeometry(QRect(20, 110, 350, 170))
        pixmap = QPixmap('bg_image_flood.jpg')
        self.label2.setScaledContents(True)
        self.label2.setPixmap(pixmap)
        # label3 which displays loading data below the flood image
        self.label3 = QLabel(self)
        self.label3.setText("Loading Data....")
        self.label3.move(10, 285)
        self.label3.setStyleSheet("font-weight:bold;color:#FFFFFF;")

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.window2)
        self.timer.start(10)
        self.show()

    def window2(self):
        global counter

        if counter > 100:
            self.timer.stop()
            self.w = Window2()
            self.w.show()
            self.close()
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
