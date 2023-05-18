from os.path import join
from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi
from envVars import DESIGNER_PATH

# This dialog is a simple input screen where the user inputs a 4-digit PIN.
class PINDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        path = join(DESIGNER_PATH, 'PIN.ui')
        loadUi(path, self)

    def edit2(self):
        # moves cursor to the next box
        self.lineEdit_3.setFocus()

    def edit3(self):
        self.lineEdit_2.setFocus()

    def edit4(self):
        self.lineEdit.setFocus()

    def accept(self):
        # Combines all 4 numbers into single 4-digit int
        PIN = self.lineEdit_4.text() + self.lineEdit_3.text() + self.lineEdit_2.text() + self.lineEdit.text()
        self.num = PIN
        self.close()
