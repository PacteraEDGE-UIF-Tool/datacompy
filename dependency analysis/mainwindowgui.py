# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1148, 724)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout_15.addWidget(self.treeView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_15.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_8.addWidget(self.pushButton_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_11.addWidget(self.pushButton_6)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_11.addWidget(self.pushButton_10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_12.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_12.addWidget(self.label_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_7.addWidget(self.pushButton_7)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\img/up.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\img/down.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setMinimumSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_12.setFont(font)
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_14.addWidget(self.pushButton_12)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setMinimumSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_13.setFont(font)
        self.pushButton_13.setText("")
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_13.addWidget(self.pushButton_13)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_6.addWidget(self.pushButton_11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.horizontalLayout_15.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\img/new_edit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNew.setIcon(icon2)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\img/new_open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon3)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\img/new_save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSave.setIcon(icon4)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\img/new_printer.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPrint.setIcon(icon5)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint_Preview = QtGui.QAction(MainWindow)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.actionExport_PDF = QtGui.QAction(MainWindow)
        self.actionExport_PDF.setObjectName("actionExport_PDF")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionPrint_Preview)
        self.menuFile.addAction(self.actionExport_PDF)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionPrint)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "Select file Origin"))
        self.label.setText(_translate("MainWindow", "file name 1"))
        self.pushButton.setText(_translate("MainWindow", "Generate cleaned data"))
        self.pushButton_6.setText(_translate("MainWindow", "Select cleaned file1"))
        self.pushButton_10.setText(_translate("MainWindow", "Select  cleaned file2"))
        self.label_5.setText(_translate("MainWindow", "cleaned file name 1"))
        self.label_2.setText(_translate("MainWindow", "cleaned file name2"))
        self.pushButton_7.setText(_translate("MainWindow", "Select output folder"))
        self.label_4.setText(_translate("MainWindow", "Default is \"./splited_dataset\""))
        self.checkBox.setText(_translate("MainWindow", "Use pattern from saved record"))
        self.pushButton_9.setText(_translate("MainWindow", "Split cleaned_file with pattern to output floder"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.pushButton_8.setText(_translate("MainWindow", "Go to index number"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "Go to index number"))
        self.pushButton_4.setText(_translate("MainWindow", "Check the splited file pair"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPrint_Preview.setText(_translate("MainWindow", "Print Preview"))
        self.actionExport_PDF.setText(_translate("MainWindow", "Export PDF"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
