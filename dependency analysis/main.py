# This Python file uses the following encoding: utf-8

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from mainwindowgui import Ui_MainWindow
from PyQt6  import QtWidgets
import pandas as pd
from ResultWindow import CResultWindow
from ResultWindowAdapter import CResultWindowAdapter
import os
from PyQt6.QtGui import QFileSystemModel, QIntValidator
from PyQt6.QtCore import QDir
from PyQt6.QtCore import QItemSelectionModel, QItemSelection
from PyQt6 import QtCore
from PyQt6 import QtGui,uic
import glob
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QMessageBox
from data_cleaner import cleanfile
from prefixspan_pattern_generator import split_data_main

FILE_PATH=r"C:\Users\sheng\experiments\Log Info\DIE_log"
class CMainWindow(QMainWindow, Ui_MainWindow):

    def actionBtnSelectCleanFile1Clicked(self):
        self.cleaned_first_fname=QFileDialog.getOpenFileName(
            self, 'Open file', 
            self.current_path,"All files (*.*)"
            )[0]
        self.label_5.setText(self.cleaned_first_fname)
        self.label_5.adjustSize()


    def actionBtnSelectCleanFile2Clicked(self):
        self.cleaned_second_fname=QFileDialog.getOpenFileName(
            self, 'Open file', 
            self.current_path,"All files (*.*)"
            )[0]
        self.label_2.setText(self.cleaned_first_fname)
        self.label_2.adjustSize()


    def actionBtnPrefixSpanClicked(self):
        split_data_main(self.cleaned_first_fname, self.cleaned_second_fname, self.current_path, self.UseSaveDataMode)
        

    def actionBtnCleanDataClicked(self):
        if self.first_fname ==None :
             QMessageBox.information(None,'Error', 'Please select file you want to clean', QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)
             return
        cleanfile(self.first_fname, self.current_path)
        


    def actionBtnGoToIndexClicked(self):
        #We initialize the validator when lineedit created, so there is only number
         parsed_index = int(self.lineEdit.text())
         self.SelectCount=parsed_index
         print(f"parsed_index:{parsed_index}")
         self.label_3.setText(str(self.SelectCount))
         self.SelectCount-=1
         self.actionBtnNextClicked()


    def actionBtnCompPairClicked(self):
        fp=os.path.join(FILE_PATH, "DIE_win10_.csv")
        table1_column_names=pd.read_csv(fp, index_col=0, nrows=0).columns.tolist()
        table2_column_names=table1_column_names
        data_left_name= os.path.join(self.OutputFloder ,str(self.SelectCount)+"_win10*")
        data_right_name=os.path.join(self.OutputFloder, str(self.SelectCount)+"_win11*")
        data_left=open(glob.glob(data_left_name)[0],"r").read()
        data_right=open(glob.glob(data_right_name)[0], "r").read()
        self.ResultWindow = QtWidgets.QWidget()
        self.ResultUI= CResultWindowAdapter(
            OutputFloder=self.OutputFloder,
            table1_column_names=table1_column_names,
            table2_column_names=table2_column_names,
            data_right=data_right,
            data_left=data_left,
            SelectCount=self.SelectCount
             )
        self.ResultUI.setupUi(self.ResultWindow)
        self.ResultUI.setupData()
        self.ResultWindow.show()
        

    def actionTreeClicked(self, Qmodelidx):
        print(self.model.filePath(Qmodelidx))
        print(self.model.fileName(Qmodelidx))
        print(self.model.fileInfo(Qmodelidx))

    def actionBtnSelectOrigFileClicked(self):
        self.first_fname=QFileDialog.getOpenFileName(
            self, 'Open file', 
            self.current_path,"All files (*.*)"
            )[0]
        self.label.setText(self.first_fname)
        self.label.adjustSize()
        


    def actionBtnNextClicked(self):
        if self.SelectCount+1>self.DataLimitCount:
            self.SelectCount=self.DataLimitCount
        else:
            self.SelectCount+=1
        print(self.SelectCount)
        

        index=self.model.index(self.SelectCount*2,0, self.model.index(self.OutputFloder))
         #programmatical selection
        self.treeView.selectionModel().select(
            index,
            QtCore.QItemSelectionModel.SelectionFlag.ClearAndSelect | QtCore.QItemSelectionModel.SelectionFlag.Rows)
        index2=self.model.index(self.SelectCount*2+1,0, self.model.index(self.OutputFloder))
        self.treeView.selectionModel().select( 
            index2,
            QtCore.QItemSelectionModel.SelectionFlag.Select | QtCore.QItemSelectionModel.SelectionFlag.Rows)
        self.label_3.setText(str(self.SelectCount))



    def actionBtnPreviousClicked(self):

        if self.SelectCount-1<0:
            self.SelectCount=0
        else:
            self.SelectCount-=1
        index=self.model.index(self.SelectCount*2,0, self.model.index(self.OutputFloder))
        self.treeView.selectionModel().select( #programmatical selection---------
            index,
            QtCore.QItemSelectionModel.SelectionFlag.ClearAndSelect | QtCore.QItemSelectionModel.SelectionFlag.Rows)
        index2=self.model.index(self.SelectCount*2+1,0, self.model.index(self.OutputFloder))
        self.treeView.selectionModel().select( 
            index2,
            QtCore.QItemSelectionModel.SelectionFlag.Select | QtCore.QItemSelectionModel.SelectionFlag.Rows)
        print(self.SelectCount)
        self.label_3.setText(str(self.SelectCount))
        

    def actionBtnOutputFloderClicked(self):
        self.OutputFloder=QFileDialog.getExistingDirectory(
            self,
        "Open a folder",
        self.current_path
    )
        print(self.OutputFloder)
        self.label_4.setText(self.OutputFloder)
        self.treeView.setRootIndex(self.model.index(self.OutputFloder))

    

    def setupUIFunctionalities(self):
        #=======================================
        #Initialize some variables
        #=======================================
        #cleaed file name
        self.cleaned_first_fname=None
        self.cleaned_second_fname=None
        # retrain or not retran, TO DO: get value from check box
        self.UseSaveDataMode=False
        self.current_path= os.path.dirname(os.path.abspath(__file__))
        self.defualt_dataset_path=os.path.join(self.current_path, "splited_dataset")
        self.OutputFloder=self.defualt_dataset_path

        #the counter for go to next button
        self.SelectCount=0
        #select count = file numbers /2
        self.DataLimitCount=499


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
        #===================================================
        #initailize the treeview select
        #===================================================
        index=self.model.index(0,0, self.model.index(self.OutputFloder))
        self.treeView.selectionModel().select(
            index,
            QtCore.QItemSelectionModel.SelectionFlag.ClearAndSelect | QtCore.QItemSelectionModel.SelectionFlag.Rows)
        index2=self.model.index(1,0, self.model.index(self.OutputFloder))
        self.treeView.selectionModel().select( 
            index2,
         QtCore.QItemSelectionModel.SelectionFlag.Select | QtCore.QItemSelectionModel.SelectionFlag.Rows)

        #===================================================
        #Initialize the line edit validation
        #===================================================
        self.lineEdit.setValidator(QIntValidator(1, 9999999, self))

        #add action to show splited file result
        self.pushButton_4.clicked.connect(self.actionBtnCompPairClicked)
        self.pushButton_5.clicked.connect(self.actionBtnSelectOrigFileClicked)
        self.pushButton_6.clicked.connect(self.actionBtnSelectCleanFile1Clicked)
        self.pushButton_10.clicked.connect(self.actionBtnSelectCleanFile2Clicked)
        self.pushButton_7.clicked.connect(self.actionBtnOutputFloderClicked)
        self.pushButton_3.clicked.connect(self.actionBtnNextClicked)
        self.pushButton_2.clicked.connect(self.actionBtnPreviousClicked)
        self.pushButton_8.clicked.connect(self.actionBtnGoToIndexClicked)
        self.pushButton.clicked.connect(self.actionBtnCleanDataClicked)
        self.pushButton_9.clicked.connect(self.actionBtnPrefixSpanClicked)

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(os.path.join(__file__, "./img/diff.png")))
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
