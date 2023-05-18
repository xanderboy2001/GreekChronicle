from os.path import join
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QFileDialog
from envVars import DESIGNER_PATH
from main_functions import add_data
from GUI_runners.add_member_dialog import addMemberDialog
import datetime
import os

class addDataDialog(QDialog):
    def __init__(self):
        super().__init__()
        path = join(DESIGNER_PATH, 'add_data_dialog.ui')
        uic.loadUi(path, self)
    def addMember(self):
        self.dialog = addMemberDialog()
        self.dialog.show()
        self.close()
    def addFile(self):
        self.filePicker = QFileDialog(self)
        self.filePicker.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.filePicker.show()
        self.close()
        if self.filePicker.exec():
            filename = self.filePicker.selectedFiles()
            if filename:
                self.new_file_path = filename
                result = str(self.new_file_path)
                result = result.replace("[", "")
                result = result.replace("]", "")
                name = os.path.basename(result)
                name = f"'{name}"
                input_type = substring_after(result, ".")
                input_type = input_type.replace("'", "")
                if input_type == "jpg" or input_type == "png":
                    current_date_time = f"'{datetime.datetime.now()}'"
                    edit_date = current_date_time
                    sql_inject = f"{name}, {result}, {current_date_time}, {edit_date}"
                    print(sql_inject)
                    add_data("image", (f"{name}, {result}, {current_date_time}, {edit_date}"))
                #add_data()
                #print(result)
                elif input_type == "docx"  or input_type == "txt" or input_type == "pdf":
                    current_date_time = f"'{datetime.datetime.now()}'"
                    edit_date = current_date_time
                    sql_inject = f"{name}, {result}, {current_date_time}, {edit_date}"
                    print(sql_inject)
                    add_data("doc", (f"{name}, {result}, {current_date_time}, {edit_date}"))
        self.close()

def substring_after(s, delim):
    return s.partition(delim)[2]