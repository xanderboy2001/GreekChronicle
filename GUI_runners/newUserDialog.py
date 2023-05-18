from os.path import join
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from GUI_runners.pinDialog import PINDialog
from GUI_runners.showPopUp import showMsg
import UserObject
from envVars import DESIGNER_PATH

class NewUserDialog(QDialog):
    def __init__(self):
        super().__init__()
        path = join(DESIGNER_PATH, 'newUser_dialog.ui')
        uic.loadUi(path, self)
                    
    # Debug button to print list of users
    def printUserList(self):
        print(UserObject.read_userList())

    def accept(self):
        # Checks if username was entered
        if self.newUname_lineEdit.text() == '':
            showMsg("ERROR: You must choose a username.")
            return
        # Checks if password was entered
        if self.newPsswd_lineEdit.text() == '':
            showMsg("ERROR: You must choose a password.")
            return
        # Checks if user already exists
        if UserObject.exists(self.newUname_lineEdit.text()):
            showMsg("ERROR: The username you have chosen already exists. Please choose a different username.")
            return
        # Checks if passwords match
        if self.newPsswd_lineEdit.text() != self.newPasswordConfirmLineEdit.text():
            showMsg("ERROR: The passwords do not match.")
            return
        # Check what permissions the user gives themselves, require PIN if r/w is selected
        if self.readWrite_radioButton.isChecked():
            newUser_PINWindow = PINDialog()
            newUser_PINWindow.exec()
        if not UserObject.authenticate('root', str(newUser_PINWindow.num)):
            showMsg("ERROR: The PIN you entered was incorrect. Please try again")
            self.accept()
        # create the user
        newUser = UserObject.UserObject(self.newUname_lineEdit.text(), self.newPsswd_lineEdit.text(), self.readWrite_radioButton.isChecked())
        self.close()
