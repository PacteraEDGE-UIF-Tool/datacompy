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
import collections


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
        


    def actionBtnGoToIndex1Clicked(self):
        #We initialize the validator when lineedit created, so there is only number
         parsed_index = int(self.lineEdit.text())
         self.SelectCount1=parsed_index
         print(f"parsed_index:{parsed_index}")
         self.label_3.setText(str(self.SelectCount))
         #just a workaround to show select
         self.SelectCount1-=1
         self.actionBtnNext1Clicked()


    def actionBtnGoToIndex2Clicked(self):
        #We initialize the validator when lineedit created, so there is only number
         parsed_index = int(self.lineEdit_2.text())
         self.SelectCount2=parsed_index
         print(f"parsed_index:{parsed_index}")
         self.label_6.setText(str(self.SelectCount))
         #just a workaround to show select
         self.SelectCount2-=1
         self.actionBtnNext2Clicked()


    def actionBtnCompPairClicked(self):
        
        #!TO DO setup columns
        fp=os.path.join(FILE_PATH, "DIE_win10_.csv")
        table1_column_names=pd.read_csv(fp, index_col=0, nrows=0).columns.tolist()
        table2_column_names=table1_column_names
        

        self.absfile1=os.path.join(self.OutputFloder, self.SelectedFile1)
        self.absfile2=os.path.join(self.OutputFloder, self.SelectedFile2)
        data_left=open(self.absfile1,"r").read()
        data_right=open(self.absfile2, "r").read()
        self.ResultWindow = QtWidgets.QWidget()
        self.ResultUI= CResultWindowAdapter(
            OutputFloder=self.OutputFloder,
            table1_column_names=table1_column_names,
            table2_column_names=table2_column_names,
            data_right=data_right,
            data_left=data_left,
            absfile1=self.absfile1,
            absfile2=self.absfile2
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
        
    def actionBtnNext2Clicked(self):
        if self.SelectCount2+1>self.DataLimitCount:
            self.SelectCount2=self.DataLimitCount
        else:
            self.SelectCount2+=1
        print(self.SelectCount2)
        self.showSelect()
        self.label_6.setText(str(self.SelectCount2))


    def actionBtnPrevious2Clicked(self):
        if self.SelectCount2-1<0:
            self.SelectCount2=0
        else:
            self.SelectCount2-=1
        self.showSelect()
        print(self.SelectCount2)
        self.label_6.setText(str(self.SelectCount2))
        

    def showSelect(self):
        #row , columns ...
        index1=self.model.index(self.SelectCount1,0, self.model.index(self.OutputFloder))
         #programmatical selection
        self.treeView.selectionModel().select(
            index1,
            QtCore.QItemSelectionModel.SelectionFlag.ClearAndSelect | QtCore.QItemSelectionModel.SelectionFlag.Rows)
        index2=self.model.index(self.SelectCount2,0, self.model.index(self.OutputFloder))
         #programmatical selection
        self.treeView.selectionModel().select(
            index2,
            QtCore.QItemSelectionModel.SelectionFlag.Select | QtCore.QItemSelectionModel.SelectionFlag.Rows)


        
        self.SelectedFile1= self.model.itemData(index1)[0]
        self.SelectedFile2=self.model.itemData(index2)[0]
        print(self.SelectedFile1, self.SelectedFile2)
        print("=======================================")



    def actionBtnNext1Clicked(self):
        if self.SelectCount1+1>self.DataLimitCount:
            self.SelectCount1=self.DataLimitCount
        else:
            self.SelectCount1+=1
        print(self.SelectCount1)
        
        self.showSelect()
        self.label_3.setText(str(self.SelectCount1))


    def actionBtnPrevious1Clicked(self):
        if self.SelectCount1-1<0:
            self.SelectCount1=0
        else:
            self.SelectCount1-=1
        self.showSelect()
        print(self.SelectCount1)
        self.label_3.setText(str(self.SelectCount1))
        

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
        self.SelectCount1=0
        self.SelectCount2=0
        #select count = file numbers /2
        self.DataLimitCount=499

        #select file queue
        self.SelectFileQueue=collections.deque(["",""],2)

        #selected file by selected count
        self.SelectedFile1=''
        self.SeletedFile2=''

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
        self.pushButton_3.clicked.connect(self.actionBtnNext1Clicked)
        self.pushButton_2.clicked.connect(self.actionBtnPrevious1Clicked)
        self.pushButton_8.clicked.connect(self.actionBtnGoToIndex1Clicked)
        self.pushButton.clicked.connect(self.actionBtnCleanDataClicked)
        self.pushButton_9.clicked.connect(self.actionBtnPrefixSpanClicked)
        self.pushButton_13.clicked.connect(self.actionBtnNext2Clicked)
        self.pushButton_12.clicked.connect(self.actionBtnPrevious2Clicked)
        self.pushButton_11.clicked.connect(self.actionBtnGoToIndex2Clicked)

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
