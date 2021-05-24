import sys
from home import Home
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import annual_rainfall as annual_rainfall

state_list = [
    "Andaman & Nicobar Islands",
    "Arunachal Pradesh",
    "Assam & Meghalaya",
    "Bihar",
    "Chhattisgarh",
    "Coastal Andhra Pradesh",
    "Coastal Karnataka",
    "East Madhya Pradesh",
    "East Rajasthan",
    "East Uttar Pradesh",
    "Gangetic West Bengal",
    "Gujarat Region",
    "Haryana Delhi & Chandigarh",
    "Himachal Pradesh",
    "Jammu & Kashmir",
    "Jharkhand",
    "Kerala",
    "Konkan & Goa",
    "Lakshadweep",
    "Madhya Maharashtra",
    "Matathwada",
    "Naga Mani Mizo Tripura",
    "North Interior Karnataka",
    "Orissa",
    "Punjab",
    "Rayalseema",
    "Saurashtra & Kutch",
    "South Interior Karnataka",
    "Sub Himalayan West Bengal & Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Uttarakhand",
    "Vidarbha",
    "West Madhya Pradesh",
    "West Rajasthan",
    "West Uttar Pradesh"
]

month_options = {
    "January": "jan",
    "February": "feb",
    "March": "mar",
    "April": "apr",
    "May": "may",
    "June": "jun",
    "July": "jul",
    "August": "aug",
    "September": "sep",
    "October": "oct",
    "November": "nov",
    "December": "dec",
    "Annual": "annual",
    "January - February": "jf",
    "March - April - May": "mam",
    "June - July - August - September": "jjas",
    "October - November - December": "ond"
}

selected_state = ''


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        # Set Window Properties
        self.setWindowTitle("Select State")
        self.resize(500, 200)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setMaximumSize(800, 300)
        self.setMinimumSize(800, 300)
        # self.setStyleSheet("background-color:#FFFFFF;")

        # Set Label for Displaying Select State
        self.label1 = QLabel(self)
        self.label1.setText("Want to know if there is flood in your area?")
        self.label1.move(10, 40)
        self.label1.setStyleSheet(
            "font:12pt \"Courier New\", monospace; color:#344fa1;")

        self.label3 = QLabel(self)
        self.label3.setText("Please Select your state below..")
        self.label3.move(10, 70)
        self.label3.setStyleSheet(
            "font:12pt \"Courier New\", monospace; color:#344fa1;")

        # add a Label that displays the application name
        self.label2 = QLabel(self)
        self.label2.setText("Global Flood Predictor")
        self.label2.move(130, 10)
        self.label2.resize(240, 25)
        self.label2.setStyleSheet(
            "color:MidnightBlue;font:12pt \"Georgia\";font-weight:bold;padding-left:20px;")

        # add a combobox to choose states
        self.comboboxState = QComboBox(self)
        self.comboboxState.addItems(state_list)
        self.comboboxState.move(10, 120)
        self.comboboxState.resize(200, 30)
        self.comboboxState.activated.connect(self.selectionchange)

        # add a combobox to choose time of year
        self.comboboxMonth = QComboBox(self)
        self.comboboxMonth.addItems(month_options)
        self.comboboxMonth.move(220, 120)
        self.comboboxMonth.resize(200, 30)
        self.comboboxMonth.activated.connect(self.selectionchange)

        # add a push button
        self.go_btn = QPushButton(self)
        self.go_btn.setText("GO")
        self.go_btn.resize(80, 30)
        self.go_btn.move(450, 120)
        self.go_btn.clicked.connect(self.on_go_btn_clicked)
        self.show()

    def close_btn_onclick(self):
        self.close()

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.HoverMove:
            self.btn_close.setIcon(QIcon('close_btn1_red.png'))
            return True
        return False

    def selectionchange(self, i):
        global selected_state
        selected_state = self.comboboxState.currentText()

    def on_go_btn_clicked(self):
        # print(self.comboboxState.currentText())
        # print(self.comboboxMonth.currentText())
        annual_rainfall.show_graph(self.comboboxState.currentText())
        self.w = Home(self.comboboxState.currentText(),
                      month_options[self.comboboxMonth.currentText()])
        self.w.show()
        self.close()


# app = QApplication(sys.argv)
# w = Window2()
# sys.exit(app.exec_())
