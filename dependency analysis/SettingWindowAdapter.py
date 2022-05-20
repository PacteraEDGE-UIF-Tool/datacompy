from xmlrpc.client import Boolean
from SettingWindowgui import CSettingWindow
import configparser
from PyQt6.QtWidgets import QMessageBox 

class CSettingWindowAdapter(CSettingWindow):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')


    def read_config_and_set_checkbox_status(self):

        if  self.config.has_section("Settings"):
            status1= Boolean( self.config.getboolean("Settings", "checkbox"))
            status2=Boolean( self.config.getboolean("Settings", "checkbox_2"))
            status3=Boolean( self.config.getboolean("Settings", "checkbox_3"))
            status4=Boolean( self.config.getboolean("Settings", "checkbox_4"))
            self.checkBox.setChecked(status1)
            self.checkBox_2.setChecked(status2)
            self.checkBox_3.setChecked(status3)
            self.checkBox_4.setChecked(status4)

            print(status1, status2, status3, status4)

        else:
            self.checkBox.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_4.setChecked(False)




    def actionBtnSaveConfigClicked(self):
        self.config["Settings"]={
            "checkbox": self.checkBox.isChecked(),
            "checkbox_2": self.checkBox_2.isChecked(),
            "checkbox_3": self.checkBox_3.isChecked(),
            "checkbox_4": self.checkBox_4.isChecked()
        }
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
            QMessageBox.information(
                None,
                'Info',
                'Config had been saved.',
                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close        
        )
    def setupData(self):
        self.read_config_and_set_checkbox_status()
        self.pushButton.clicked.connect(self.actionBtnSaveConfigClicked)