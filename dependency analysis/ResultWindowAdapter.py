from ResultWindow import CResultWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem



class CResultWindowAdapter(CResultWindow):
    def __init__(self, **kargvs):
        self.table1_column_names=kargvs["table1_column_names"]
        self.table2_column_names=kargvs["table2_column_names"]
        self.data_right=kargvs["data_right"].split("\n")
        self.data_left=kargvs["data_left"].split("\n")
    def setupData(self):
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(len(self.table2_column_names))
        self.tableWidget.setColumnCount(len(self.table1_column_names))
        self.tableWidget.setRowCount(len(self.data_left))
        self.tableWidget_2.setRowCount(len(self.data_right))
        

        self.tableWidget.setHorizontalHeaderLabels(self.table1_column_names)
        for i, data in enumerate(self.data_left):
           # print(data)
            item=QTableWidgetItem(data)
            self.tableWidget.setItem(i, 3, item)
        #print(self.table1_column_names)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


        #print(self.data_right)
        self.tableWidget_2.setHorizontalHeaderLabels(self.table2_column_names)
        for i, data in enumerate(self.data_right):
           # print(data)
            item=QTableWidgetItem(data)
            self.tableWidget_2.setItem(i, 3, item)
        print(self.table2_column_names)
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.resizeRowsToContents()