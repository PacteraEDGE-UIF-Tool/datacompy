# This Python file uses the following encoding: utf-8

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from mainwindowgui import Ui_MainWindow
from PyQt6  import QtWidgets
import pandas as pd
from ResultWindow import CResultWindow
import os
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QDir
from PyQt6.QtCore import QItemSelectionModel, QItemSelection
from PyQt6 import QtCore
from PyQt6 import QtGui
FILE_PATH=r"C:\Users\sheng\experiments\Log Info\DIE_log"
class CMainWindow(QMainWindow, Ui_MainWindow):
    def actionButton1Clicked(self):
        fp=os.path.join(FILE_PATH, "DIE_win10_.csv")
        table1_column_names=pd.read_csv(fp, index_col=0, nrows=0).columns.tolist()

        self.ResultWindow = QtWidgets.QWidget()
        self.ResultUI = CResultWindow(
            table1_column_names=table1_column_names)
        self.ResultUI.setupUi(self.ResultWindow)
        self.ResultWindow.show()
    def actionTreeClicked(self, Qmodelidx):
        print(self.model.filePath(Qmodelidx))
        print(self.model.fileName(Qmodelidx))
        print(self.model.fileInfo(Qmodelidx))

    def actionBtnSelectFile1Clicked(self):
        self.first_fname = QFileDialog.getOpenFileName(
            self, 'Open file', 
            self.current_path,"All files (*.*)")[0]
        self.label.setText(self.first_fname)
        self.label.adjustSize()
        

    def actionBtnSelectFile2Clicked(self):
        self.second_fname = QFileDialog.getOpenFileName(
            self, 'Open file', 
            self.current_path,"All files (*.*)")[0]
        self.label_2.setText(self.second_fname)
        self.label_2.adjustSize()




    def actionBtnNextClicked(self):

        if self.SelectCount>self.DataLimitCount:
            self.SelectCount=self.DataLimitCount
        index=self.model.index(self.SelectCount*2,0, self.model.index(self.OutputFloder))
         #programmatical selection
        self.treeView.selectionModel().select(
            index,
            QtCore.QItemSelectionModel.SelectionFlag.ClearAndSelect | QtCore.QItemSelectionModel.SelectionFlag.Rows)
        index2=self.model.index(self.SelectCount*2+1,0, self.model.index(self.OutputFloder))
        self.treeView.selectionModel().select( 
            index2,
            QtCore.QItemSelectionModel.SelectionFlag.Select | QtCore.QItemSelectionModel.SelectionFlag.Rows)
        self.SelectCount+=1


    def actionBtnPreviousClicked(self):
        if self.SelectCount<0:
            self.SelectCount=0
        index=self.model.index(self.SelectCount*2,0, self.model.index(self.OutputFloder))
        self.treeView.selectionModel().select( #programmatical selection---------
            index,
            QtCore.QItemSelectionModel.SelectionFlag.ClearAndSelect | QtCore.QItemSelectionModel.SelectionFlag.Rows)
        index2=self.model.index(self.SelectCount*2+1,0, self.model.index(self.OutputFloder))
        self.treeView.selectionModel().select( 
            index2,
            QtCore.QItemSelectionModel.SelectionFlag.Select | QtCore.QItemSelectionModel.SelectionFlag.Rows)
        self.SelectCount-=1
        

    def actionBtnOutputFloderClicked(self):
        self.OutputFloder=QFileDialog.getExistingDirectory(
            self,
        "Open a folder",
        self.current_path
    )
        self.label_4.setText(self.OutputFloder)
        self.treeView.setRootIndex(self.model.index(self.OutputFloder))

    

    def setupUIFunctionalities(self):
        #=======================================
        #Initialize some variables
        #=======================================
        self.current_path= os.path.dirname(os.path.abspath(__file__))
        self.defualt_dataset_path=os.path.join(self.current_path, "splited_dataset")
        self.OutputFloder=self.defualt_dataset_path

        #the counter for go to next button
        self.SelectCount=0
        self.DataLimitCount=100


        #check whether the output folder exists
        if not os.path.isdir(self.defualt_dataset_path):
            os.mkdir(self.defualt_dataset_path)


        #setup tree view
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        self.model.setNameFilters(['*.txt'])
        self.model.setNameFilterDisables(False)
        self.treeView.setModel(self.model)
        self.treeView.doubleClicked.connect(self.actionTreeClicked)
        self.treeView.setIndentation(10)
        self.treeView.setRootIndex(self.model.index(self.defualt_dataset_path))
        self.treeView.setWindowTitle("Splited file dataset")
        

        

        #add action to show splited file result
        self.pushButton.clicked.connect(self.actionButton1Clicked)
        self.pushButton_5.clicked.connect(self.actionBtnSelectFile1Clicked)
        self.pushButton_6.clicked.connect(self.actionBtnSelectFile2Clicked)
        self.pushButton_7.clicked.connect(self.actionBtnOutputFloderClicked)
        self.pushButton_3.clicked.connect(self.actionBtnNextClicked)
        self.pushButton_2.clicked.connect(self.actionBtnPreviousClicked)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupUIFunctionalities()
        self.show()
        #QMainWindow.__init__(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=CMainWindow()
    qss_str=open("main.qss").read()
    app.setStyleSheet(qss_str)
    sys.exit(app.exec())
