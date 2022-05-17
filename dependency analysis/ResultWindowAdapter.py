from ResultWindow import CResultWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
import os
import pandas as pd
import glob
from PyQt6.QtWidgets import QMessageBox
import datacompy
class CResultWindowAdapter(CResultWindow):
    def setColortoRow(table, rowIndex, color):
        for j in range(table.columnCount()):
            #QtGui.QColor(125,125,125)
            table.item(rowIndex, j).setBackground(color)
    def actionBtnCompareClicked(self):
        _notimportant_col_name="a"
        file_name_left=os.path.join(self.OutputFloder, str(self.SelectCount)+"_win10*")
        file_name_right=os.path.join(self.OutputFloder, str(self.SelectCount)+"_win11*")
        data_left= pd.read_csv(glob.glob(file_name_left)[0], delimiter=r'\n',  header=None, names=list(_notimportant_col_name))
        data_right= pd.read_csv(glob.glob(file_name_right)[0], delimiter=r'\n',  header=None, names=list(_notimportant_col_name))
        print(f"data left: {data_left}")
        print(f"data_right: {data_right}")
        result_left_df=None
        result_right_df=None
        NoDifferntFlag=True

        compare = datacompy.Compare(data_left, data_right, join_columns=_notimportant_col_name)
        compare.matches(ignore_extra_columns=False)

        report=compare.customized_report()
        result_left_df=report[0]
        result_right_df=report[1]
        result_outer_merged=report[2]
        if not result_left_df.empty:
            NoDifferntFlag=False
            indexies_left=list(result_left_df.index)
            # Get the ID(index) by the name of the different dataset
            #the left or right might be non exist, so we conduct operation in try excep zone.
            try:
                set1=set()
                real_left_index_list=list()
                real_left_index_list=result_left_df.index
                for row_index in real_left_index_list:
                    #for i in range(self.tableWidget.columnCount()):
                    #================================================
                    #!important
                    #===============================================
                    #Qt TABLE start from 1, so we need to add 1
                    item=self.tableWidget.item(row_index, 3)
                    if item !=None:
                        #print(row_index, i)
                        item.setBackground(QtGui.QColor(107,142,35))
            except KeyError:
                indexies_left=None
        if not result_right_df.empty:
            NoDifferntFlag=False
            indexies_right=list(result_right_df.index)
            print(f"right_indexies :{indexies_right}")
            set1=set()
            real_right_index_list=list()
            try:
                for i in indexies_right:
                    data=result_outer_merged.loc[i, _notimportant_col_name]
                    set1.add(data)
                for i in set1:
                    tl1=data_right.index[data_right[_notimportant_col_name]==i].tolist()
                    #print(tl1)
                    real_right_index_list=[*real_right_index_list, *tl1]
                print(f"real_right_index {real_right_index_list}")
                for row_index in real_right_index_list:
                    item=self.tableWidget_2.item(row_index,3)
                    if item !=None:
                    #for i in range(self.tableWidget_2.columnCount()):
                        item.setBackground(QtGui.QColor(107,142,35))
            except KeyError:
                indexies_right=None


        if NoDifferntFlag:
            QMessageBox.information(None,'Compelete the processing', 'These two files seems like the same', QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)


    def __init__(self, **kargvs):
        self.table1_column_names=kargvs["table1_column_names"]
        self.table2_column_names=kargvs["table2_column_names"]
        self.data_right=kargvs["data_right"].split("\n")
        self.data_left=kargvs["data_left"].split("\n")
        self.SelectCount=kargvs["SelectCount"]
        self.OutputFloder=kargvs["OutputFloder"]
        self.CompareColName="Prototype"
        
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
        self.pushButton.clicked.connect(self.actionBtnCompareClicked)
       