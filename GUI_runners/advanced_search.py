from os.path import join
from PyQt6.QtWidgets import QMainWindow, QFormLayout, QPushButton, QHBoxLayout, QWidget
from PyQt6 import QtCore, QtGui
from PyQt6.uic import loadUi
from envVars import DESIGNER_PATH, member_attrs, file_attrs

class AdvancedSearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        path = join(DESIGNER_PATH, 'advancedSearch.ui')
        loadUi(path, self)
        self.setAttrs()
    def setAttrs(self):
        comboBoxes = [self.comboBox, self.comboBox_2, self.comboBox_3]
        for box in comboBoxes: box.clear()
        if self.file_checkBox.isChecked():
            for box in comboBoxes: box.addItems(file_attrs)
        if self.member_checkBox.isChecked():
            for box in comboBoxes: box.addItems(member_attrs)
    def accept(self):

        ''' Attributes are the tags we're searching by, queries are the text in the text boxes
        andOrFlags correspond to the which button is pressed'''

        attribute1 = self.comboBox.currentText()
        attribute2 = self.comboBox_2.currentText()
        attribute3 = self.comboBox_3.currentText()
        query1 = self.lineEdit.text()
        query2 = self.lineEdit_2.text()
        query3 = self.lineEdit_3.text()
        if self.andBtn.isDown():
            andOrFlag1 = 'AND'
        else:
            andOrFlag1 = 'OR'
        if self.andBtn_2.isDown():
            andOrFlag2 = 'AND'
        else:
            andOrFlag2 = 'OR'

        self.close()