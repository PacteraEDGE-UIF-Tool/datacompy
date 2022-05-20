
# Welcome to PyShine
# This is part 12 of the PyQt5 learning series
# Start and Stop Qthreads
# Source code available: www.pyshine.com
from locale import currency
from PyQt6 import QtCore, QtWidgets,QtGui
from PyQt6 import uic
import sys, time
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QProgressBar
from PyQt6.QtWidgets import QVBoxLayout
import multiprocessing
from data_cleaner import cleanfile
import os


class CProgressBarDialog(QDialog):
    def __init__(self, Original_file):
        super(CProgressBarDialog, self).__init__()
        self.InputFilename=Original_file


        self.resize(350,100)
        self.setWindowTitle(self.tr("Processing progress"))
    
        self.Label = QLabel("Proccessing the data, be patient ...")
        self.ProgressBar = QProgressBar(self)
        self.ProgressBar.setValue(0)
        self.pushButton = QPushButton('Close window')
        self.vbox = QVBoxLayout()

        self.vbox.addWidget(self.Label)
        self.vbox.addWidget(self.ProgressBar)
        self.vbox.addWidget(self.pushButton)


        self.setLayout(self.vbox)
        self.resize(888, 200)

        self.thread={}
        self.pushButton.clicked.connect(self.closeWindow)
        self.start_worker_1()
    def closeWindow(self):
        self.close()

    def start_worker_1(self):
        self.thread[0] = ThreadClass(InputFileName=self.InputFilename,parent=None,index=0)
        self.thread[0].start()
        self.thread[0].any_signal.connect(self.SetProgressBarValue)
        self.pushButton.setEnabled(False)
		
		

    def SetProgressBarValue(self, counter):	
        cnt=counter
        #print(cnt)
        index = self.sender().index
        #if index==1:
        self.ProgressBar.setValue(cnt)
        if cnt==100:
            self.pushButton.setEnabled(True)
            self.Label.setText("Job finished.")
            self.thread[0].stop()

	
class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)
    def __init__(self, InputFileName, parent=None,index=0):
        super(ThreadClass, self).__init__(parent)
        self.current_step=multiprocessing.Value('i' ,0)
        self.old_step=self.current_step.value

        sub_proccess=multiprocessing.Process(target=cleanfile, args=(InputFileName, self.current_step,os.path.dirname(__file__)))
        sub_proccess.start()
        #no wait
        #sub_proccess.join() 
        self.index=index
        self.is_running = True


    def run(self):
        print('Starting thread...',self.index)
        #cnt=0
        while (True):
            if self.old_step==0:
                self.current_step.value+=1
            if self.old_step!= self.current_step.value:
                self.any_signal.emit(self.current_step.value)
                #print(self.current_step.value)
                self.old_step=self.current_step.value

    def stop(self):
        self.is_running = False
        print('Stopping thread...',self.index)
        self.terminate()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = CProgressBarDialog()
    mainWindow.start_worker_1()
    mainWindow.show()
    sys.exit(app.exec())
