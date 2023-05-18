from os.path import join
from PyQt6.QtWidgets import QDialog
from GUI_runners.newUserDialog import NewUserDialog
from GUI_runners.showPopUp import showMsg
from GUI_runners.search_ui import SearchWindow
from PyQt6.uic import loadUi
from envVars import DESIGNER_PATH
import UserObject

def checkRoot():
    # Checks for root account
    if not UserObject.exists("root"):
        first_run()

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        path = join(DESIGNER_PATH, 'login.ui')
        loadUi(path, self)
        self.auth_flag = False
        checkRoot()

    # Hides the main window and pops up a new window
    def new_user(self):
        self.hide()
        dialog = NewUserDialog()
        dialog.exec()
        self.show()

    def accept(self):
        # Checks if user is trying to login as root
        #if self.uname_lineEdit.text() == 'root':
        #    showMsg("ERROR: You cannot login to the root account.")
        #    return
        # checks if user exists
        if not UserObject.exists(self.uname_lineEdit.text()):
            showMsg("ERROR: User does not exist!")
            return
        # Sets self.authFlag and checks if passwd is correct
        self.auth_flag = UserObject.authenticate(self.uname_lineEdit.text(), self.psswd_lineEdit.text())
        if not self.auth_flag:
            showMsg("ERROR: Incorrect password")
            return
        # Open search_window and close login_window if login was successful
        self.search_window = SearchWindow()
        self.search_window.show()
        self.close()
