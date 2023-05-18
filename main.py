import sys
from PyQt6.QtWidgets import (
    QApplication
)
from GUI_runners.showPopUp import showMsg
import GUI_runners.login
from GUI_runners.pinDialog import PINDialog
import UserObject
import highest_level_calling as dbmain

# Runs only on first run
def first_run():
    msg = "Welcome to Greek Chronical! In order to get started, \
    we're going to set up an admin account. \
    This will most likely be the president of the organization, \
    as their permission will be needed to add/remove users or delete documents."
    showMsg(msg)
    # Allow user to set PIN, then create root account with PIN as password
    set_pin_dialog = PINDialog()
    set_pin_dialog.exec()
    admin_user = UserObject.UserObject('root', set_pin_dialog.num, 1)

def mainmain():
    # Initializes Qt6 App
    app = QApplication(sys.argv)
    #Enables our window and shows our app
    login_screen = GUI_runners.login.LoginDialog()
    login_screen.show()
    # adv_search = GUI_runners.advanced_search.AdvancedSearchWindow()
    # adv_search.show()
    app.exec()

if __name__ == '__main__':
    dbmain.main()
