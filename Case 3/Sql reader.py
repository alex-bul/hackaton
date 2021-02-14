import sqlite3
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.Qt import QImage
from PyQt5.Qt import QSize
from PyQt5.Qt import QPalette
from PyQt5.Qt import QBrush
from PyQt5.Qt import QIcon
from PyQt5.QtGui import QColor


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI1.ui', self)
        self.setWindowTitle('Reader')
        self.connection = sqlite3.connect("Res\\logs.db")
        self.pushButton.clicked.connect(self.select_data)
        self.horizontalSlider.valueChanged[int].connect(self.changeValue)
        self.comboBox.addItems(["White", "Dark"])
        self.comboBox.activated[str].connect(self.themes)
        self.themes('White')
        self.error = 0

    def select_data(self):
        res = []
        with open('readable.txt', 'r') as f:
            data = f.read().split('\n')
            for i in data:
                res.append(i.split())

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Название', 'Широта', 'Долгота', 'Интенсивность', 'Энергия'])
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(4, 190)
        if self.error != 1:
            self.tableWidget.setColumnWidth(2, 150)
        else:
            self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setRowCount(0)
        try:
            self.error = 0
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))
            self.error = 0
        except:
            self.error = 1
            self.label_3.setText('Sql request Error')

    def themes(self, text):
        if text == "Dark":
            self.label_3.setStyleSheet("color: rgb(235, 235, 235);")
            self.label_5.setStyleSheet("color: rgb(235, 235, 235);")
            self.pushButton.setStyleSheet("background-color: white;border-radius: 10px;")
            self.palette = QPalette()
            self.palette.setBrush(10, QBrush(QColor(27, 27, 27)))
            self.setPalette(self.palette)
            stylesheet = """
                                QTableWidget {color: rgb(235, 235, 235); background-color: rgb(50, 50, 50)}
                                QTableWidget QHeaderView::section {background-color: rgb(50, 50, 50); border: none; border-style: none;}
                                QTableWidget QHeaderView {color: rgb(235, 235, 235);background-color: rgb(50, 50, 50); border: none; border-style: none;}
                                QTableWidget QTableCornerButton::section {background-color: rgb(50, 50, 50);  border: 0px}
                                """
            self.tableWidget.setStyleSheet(stylesheet)

        elif text == "White":
            self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
            self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 10px;")
            self.palette = QPalette()
            self.palette.setBrush(10, QBrush(QColor(240, 240, 240)))
            self.setPalette(self.palette)
            stylesheet = """
                            QTableWidget {background-color: rgb(255, 255, 255)}
                            QTableWidget QHeaderView::section {background-color: rgb(255, 255, 255); border: none; border-style: none;}
                            QTableWidget QHeaderView {background-color: rgb(255, 255, 255); border: none; border-style: none;}
                            QTableWidget QTableCornerButton::section {background-color: rgb(255, 255, 255);  border: 0px}
                            """
            self.tableWidget.setStyleSheet(stylesheet)

    def changeValue(self, value):
        self.setWindowOpacity(value / 100)

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
