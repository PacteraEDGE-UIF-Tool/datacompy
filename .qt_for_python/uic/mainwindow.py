# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QToolBar, QTreeView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1148, 885)
        MainWindow.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u"img/diff.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon1 = QIcon()
        icon1.addFile(u"img/new_edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon2 = QIcon()
        icon2.addFile(u"img/new_open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon3 = QIcon()
        icon3.addFile(u"img/new_save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        icon4 = QIcon()
        icon4.addFile(u"img/new_printer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrint.setIcon(icon4)
        self.actionPrint_Preview = QAction(MainWindow)
        self.actionPrint_Preview.setObjectName(u"actionPrint_Preview")
        self.actionExport_PDF = QAction(MainWindow)
        self.actionExport_PDF.setObjectName(u"actionExport_PDF")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionsetting = QAction(MainWindow)
        self.actionsetting.setObjectName(u"actionsetting")
        icon5 = QIcon()
        icon5.addFile(u"img/new_setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionsetting.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_15 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")

        self.horizontalLayout_15.addWidget(self.treeView)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout_15.addLayout(self.horizontalLayout_4)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_15.addWidget(self.line_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setBold(True)
        self.label_7.setFont(font)

        self.verticalLayout_3.addWidget(self.label_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        self.pushButton_5.setFont(font1)

        self.horizontalLayout_8.addWidget(self.pushButton_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMargin(20)

        self.horizontalLayout_10.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u"img/new_analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)

        self.horizontalLayout_9.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_4.addWidget(self.label_8)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)

        self.horizontalLayout_11.addWidget(self.pushButton_6)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font1)

        self.horizontalLayout_11.addWidget(self.pushButton_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_12.addWidget(self.label_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)

        self.horizontalLayout_7.addWidget(self.pushButton_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(9)
        self.pushButton_9.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u"img/new_document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon7)

        self.verticalLayout_2.addWidget(self.pushButton_9)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_6)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_4.addWidget(self.label_9)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u"img/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon8)

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u"img/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon9)

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pushButton_8)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(30, 0))
        self.pushButton_12.setFont(font1)
        self.pushButton_12.setIcon(icon8)

        self.horizontalLayout_14.addWidget(self.pushButton_12)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(30, 0))
        self.pushButton_13.setFont(font1)
        self.pushButton_13.setIcon(icon9)

        self.horizontalLayout_13.addWidget(self.pushButton_13)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pushButton_11)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addLayout(self.verticalLayout_8)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setBold(False)
        self.pushButton_4.setFont(font3)
        icon10 = QIcon()
        icon10.addFile(u"img/new_compare.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)

        self.verticalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout_15.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1148, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionPrint_Preview)
        self.menuFile.addAction(self.actionExport_PDF)
        self.menuFile.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.actionsetting)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
#if QT_CONFIG(shortcut)
        self.actionPrint.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrint_Preview.setText(QCoreApplication.translate("MainWindow", u"Print Preview", None))
        self.actionExport_PDF.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionsetting.setText(QCoreApplication.translate("MainWindow", u"setting", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u2022Step1", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Select original file", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate cleaned data", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u2022Step2", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Select cleaned file1", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Select  cleaned file2", None))
        self.label_5.setText("")
        self.label_2.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Select output folder", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Default is \"./splited_dataset\"", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Split cleaned_file with pattern to output floder", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u2022Step3", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Go to index number", None))
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Go to index number", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Check the splited file pair", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

