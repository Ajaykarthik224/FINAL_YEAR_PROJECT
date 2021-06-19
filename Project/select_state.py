import sys
from home import Home
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import annual_rainfall as annual_rainfall
from PyQt5.QtWidgets import QMessageBox
import get_local_weather
import prepare_data_graph as prepare_data_graph
state_list = [
    "Please Select State",
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
    "Please Select Month": "Please Select Month",
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

        screen = QApplication.primaryScreen()
        width = screen.size().width()
        height = screen.size().height()
        self.setWindowTitle("Select State")
        self.resize(width, height)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setMaximumSize(width, height)
        self.setMinimumSize(width, height)
        # self.setStyleSheet("background-color:#FFFFFF;")

        # Set Label for Displaying Select State
        self.label1 = QLabel(self)
        self.label1.setText("Want to know if there is flood in your area?")
        self.label1.move(int(width/4), 60)
        self.label1.setStyleSheet(
            "font:20pt \"Courier New\", monospace; color:#344fa1;")

        self.label3 = QLabel(self)
        self.label3.setText("Please select your state and month below...")
        self.label3.move(int(width/4), 100)
        self.label3.setStyleSheet(
            "font:20pt \"Courier New\", monospace; color:#344fa1;")

        # add a Label that displays the application name
        self.label2 = QLabel(self)
        self.label2.setText("Global Flood Predictor")
        self.label2.move(int(width/2)-180, 10)
        # self.label2.resize(300, 40)
        self.label2.setStyleSheet(
            "color:MidnightBlue;font:30pt \"Georgia\";font-weight:bold;padding-left:20px;")

        # add a combobox to choose states
        self.comboboxState = QComboBox(self)
        self.comboboxState.addItems(state_list)
        self.comboboxState.move(int(width/4), 140)
        self.comboboxState.resize(200, 30)
        self.comboboxState.activated.connect(self.selectionchange)

        # add a combobox to choose time of year
        self.comboboxMonth = QComboBox(self)
        self.comboboxMonth.addItems(month_options)
        self.comboboxMonth.move(int(width/3)+75, 140)
        self.comboboxMonth.resize(200, 30)
        self.comboboxMonth.activated.connect(self.selectionchange)

        # add a push button
        self.go_btn = QPushButton(self)
        self.go_btn.setText("GO")
        self.go_btn.resize(80, 30)
        self.go_btn.move(int(width/2), 140)
        self.go_btn.clicked.connect(self.on_go_btn_clicked)

        self.image1 = QLabel(self)
        self.image1.setGeometry(QRect(int(width/4), 200, 500, 400))
        pixmap = QPixmap('flood_input.jpg')
        self.image1.setScaledContents(True)
        self.image1.setPixmap(pixmap)

        self.image2 = QLabel(self)
        self.image2.setGeometry(QRect(100, 400, 300, 500))
        pixmap = QPixmap('flood_input3.jpg')
        self.image2.setScaledContents(True)
        self.image2.setPixmap(pixmap)

        self.image3 = QLabel(self)
        self.image3.setGeometry(QRect(int(width/4), 600, 500, 400))
        pixmap = QPixmap('flood_input2.jpg')
        self.image3.setScaledContents(True)
        self.image3.setPixmap(pixmap)

        weather_info = get_local_weather.get_weather()
        self.weatherlabel1 = QLabel(self)
        self.weatherlabel1.setText(
            f"Current Weather in {weather_info['name']}:")
        self.weatherlabel1.move(int(width/2)+100, 200)
        self.weatherlabel1.setStyleSheet(
            "font:15pt \"Courier New\", monospace; color:#344fa1;")

        self.weatherlabel2 = QLabel(self)
        self.weatherlabel2.setText(
            f"{weather_info['weather'][0]['main']}")
        self.weatherlabel2.move(int(width/2)+100, 220)
        self.weatherlabel2.setStyleSheet(
            "font:15pt \"Courier New\", monospace; color:#344fa1; font-weight:bold;")

        self.weatherlabel3 = QLabel(self)
        self.weatherlabel3.setText(
            f"Temperature:{weather_info['main']['temp']}" + u"\N{DEGREE SIGN}"+"C")
        self.weatherlabel3.move(int(width/2)+100, 240)
        self.weatherlabel3.setStyleSheet(
            "font:15pt \"Courier New\", monospace; color:#344fa1; font-weight:bold;")

        self.weatherlabel4 = QLabel(self)
        self.weatherlabel4.setText(
            f"Humididy:{weather_info['main']['humidity']}%")
        self.weatherlabel4.move(int(width/2)+100, 260)
        self.weatherlabel4.setStyleSheet(
            "font:15pt \"Courier New\", monospace; color:#344fa1; font-weight:bold;")

        self.image4 = QLabel(self)
        self.image4.setGeometry(QRect(int(width/2)+100, 400, 600, 400))
        pixmap = QPixmap('flood_input4.jpg')
        self.image4.setScaledContents(True)
        self.image4.setPixmap(pixmap)

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
        # print(self.comboboxMonth.currentText()).
        if(self.comboboxState.currentText() == 'Please Select State'):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("State cannot be 'Please Select'")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        elif(self.comboboxMonth.currentText() == 'Please Select Month'):
            msg2 = QMessageBox()
            msg2.setWindowTitle("Error")
            msg2.setText("Month cannot be 'Please Select'")
            msg2.setIcon(QMessageBox.Critical)
            x = msg2.exec_()
        else:
            annual_rainfall.show_graph(self.comboboxState.currentText())
            prepare_data_graph.prepare()
            self.w = Home(self.comboboxState.currentText(),
                          month_options[self.comboboxMonth.currentText()])
            self.w.show()
            self.close()


app = QApplication(sys.argv)
w = Window2()
sys.exit(app.exec_())
