from os.path import join
from PyQt6 import uic, QtGui
from PyQt6 import QtWidgets
from envVars import DESIGNER_PATH, member_attrs, file_attrs
from MemberObject import MemberObject

class editDataDialog(QtWidgets.QDialog):
    def __init__(self, item):
        super().__init__()
        path = join(DESIGNER_PATH, 'edit_data.ui')
        uic.loadUi(path, self)
        print(type(item))
        if type(item) == MemberObject:
            for tag in member_attrs:
                self.newLabel = QtGui.QLabel(tag)
                self.newField = QtGui.QLineEdit()
                self.formLayout.addRow(newLabel, newField)
                print(tag)
        else:
            for tag in file_attrs:
                self.newLabel = QtGui.QLabel(tag)
                self.newField = QtGui.QLineEdit()
                print(tag)
# class formRow(QtGui.QWidget, labelText):
#     def __init__(self, parent=None):
#         super(formRow, self).__init__(parent)
#         self.label = QtGui.QLabel(labelText)
