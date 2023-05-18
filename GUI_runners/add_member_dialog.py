from os.path import join
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from envVars import DESIGNER_PATH
from main_functions import add_data
import datetime

class addMemberDialog(QDialog):
    def __init__(self):
        super().__init__()
        path = join(DESIGNER_PATH, 'add_member_dialog.ui')
        uic.loadUi(path, self)
    def accept(self):
        name = self.name_field.text()
        big_name = self.big_field.text()
        dob = self.dob_field.date().toString('dd.MM.yyyy')
        date_joined = self.date_joined_field.date().toString('dd.MM.yyyy')
        """idk how to add this to the db. i think you need to lookup the big by their name to get the id. but idk how that works
        but the variable names are self-explanatory. They're all strings. I sent a screenshot in discord showing how to format the dates
        (you just edit that little string argument)"""
        self.close()