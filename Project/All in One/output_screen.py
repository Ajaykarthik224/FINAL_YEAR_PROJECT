import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import get_local_weather
import all_in_one
import json

selected_state = ''


def run_algorithms(state, month):
    all_in_one.knn_algorithm(state, month)
    # all_in_one.logistic_regression(state, month)
    # all_in_one.support_vector_algorithm(state, month)
    # all_in_one.decision_tree(state, month)


class Home(QWidget):
    def __init__(self, state, month):
        super().__init__()
        selected_state = state
        selected_month = month

        self.setWindowTitle("Main Window")
        self.resize(800, 400)
        self.setMaximumSize(800, 400)
        self.setMinimumSize(800, 400)
        self.setStyleSheet("background-color:#243665;")
        # add a label for displaying state
        self.label = QLabel(self)
        self.label.resize(50, 20)
        self.label.move(10, 5)
        self.label.setText("State:")
        self.label.setStyleSheet(
            "color:#8BD8BD;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")
        # add a label for state
        self.label1 = QLabel(self)
        self.label1.resize(250, 20)
        self.label1.move(60, 5)
        self.label1.setText(selected_state)
        self.label1.setStyleSheet(
            "color:#8BD8BD;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        # add a label to display weather
        self.label4 = QLabel(self)
        self.label4.resize(80, 20)
        self.label4.move(550, 5)
        self.label4.setText("Weather:")
        self.label4.setStyleSheet(
            "color:#8BD8BD;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")
        # add label to display value of weather
        self.label5 = QLabel(self)
        self.label5.resize(100, 20)
        self.label5.move(650, 5)
        # instead of 'data' add weather data
        weather_info = get_local_weather.get_weather()
        self.label5.setText(str(weather_info['temp'])+u"\N{DEGREE SIGN}"+"C")
        self.label5.setStyleSheet(
            "color:#8BD8BD;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        # add labels
        self.label6 = QLabel(self)
        self.label6.resize(100, 30)
        self.label6.move(250, 100)

        # reading the results from the file for output
        run_algorithms(selected_state, selected_month)
        results = open('output.json', 'r')
        results = json.load(results)
        self.label6.setText("Algorithm")
        self.label6.setStyleSheet(
            "color:#FFFFFF;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;border:2px solid white;padding-left:10px;")

        self.label7 = QLabel(self)
        self.label7.resize(200, 30)
        self.label7.move(450, 100)
        # instead of 'data' add weather data
        self.label7.setText("Accuracy ( in % )")
        self.label7.setStyleSheet(
            "color:#FFFFFF;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;border:2px solid white;padding-left:30px;")

        self.label8 = QLabel(self)
        self.label8.resize(150, 30)
        self.label8.move(250, 150)
        # instead of 'data' add weather data
        self.label8.setText(results['scores'][0]['algorithm'])
        self.label8.setStyleSheet(
            "color:#FFFFFF;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        self.label9 = QLabel(self)
        self.label9.resize(150, 30)
        self.label9.move(250, 190)
        # instead of 'data' add weather data
        self.label9.setText(results['scores'][1]['algorithm'])
        self.label9.setStyleSheet(
            "color:#FFFFFF;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        self.label10 = QLabel(self)
        self.label10.resize(150, 30)
        self.label10.move(250, 230)
        # instead of 'data' add weather data
        self.label10.setText(results['scores'][2]['algorithm'])
        self.label10.setStyleSheet(
            "color:#FFFFFF;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        self.label11 = QLabel(self)
        self.label11.resize(150, 30)
        self.label11.move(250, 270)
        # instead of 'data' add weather data
        self.label11.setText(results['scores'][3]['algorithm'])
        self.label11.setStyleSheet(
            "color:#FFFFFF;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        self.label8 = QLabel(self)
        self.label8.resize(150, 30)
        self.label8.move(450, 150)
        # instead of 'data' add weather data
        self.label8.setText(str(results['scores'][0]['accuracy']))
        self.label8.setStyleSheet(
            "color:#FFFFFF;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        self.label9 = QLabel(self)
        self.label9.resize(150, 30)
        self.label9.move(450, 190)
        # instead of 'data' add weather data
        self.label9.setText(str(results['scores'][1]['accuracy']))
        self.label9.setStyleSheet(
            "color:#FFFFFF;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        self.label10 = QLabel(self)
        self.label10.resize(150, 30)
        self.label10.move(450, 230)
        # instead of 'data' add weather data
        self.label10.setText(str(results['scores'][2]['accuracy']))
        self.label10.setStyleSheet(
            "color:#FFFFFF;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        self.label11 = QLabel(self)
        self.label11.resize(150, 30)
        self.label11.move(450, 270)
        # instead of 'data' add weather data
        self.label11.setText(str(results['scores'][3]['accuracy']))
        self.label11.setStyleSheet(
            "color:#FFFFFF;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        # add a label to display prediction
        self.label2 = QLabel(self)
        self.label2.resize(100, 20)
        self.label2.move(350, 320)
        self.label2.setText("Prediction:")
        self.label2.setStyleSheet(
            "color:#8BD8BD;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")

        # # add a label for prediction value
        self.label3 = QLabel(self)
        self.label3.resize(50, 20)
        self.label3.move(450, 320)
        self.label3.setText(results['scores'][3]['prediction'])
        self.label3.setStyleSheet(
            "color:#8BD8BD;font:15px \"Gill Sans Extrabold\",sans-serif;font-weight:bold;")
        self.show()


# app = QApplication(sys.argv)
# w = Home('Hello')
# sys.exit(app.exec_())
