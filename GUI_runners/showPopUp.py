from PyQt6.QtWidgets import QMessageBox
# Simple function to show a popup message with a given message
def showMsg(msg):
    errorMsgBox = QMessageBox()
    errorMsgBox.setText(msg)
    errorMsgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
    errorMsgBox.exec()
