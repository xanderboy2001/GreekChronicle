from os.path import join
import sys
from PyQt6.QtWidgets import QMainWindow, QTreeWidgetItem, QTreeWidget
from PyQt6.uic import loadUi
from envVars import DESIGNER_PATH
import MemberObject, ImageObject, DocObject, main_functions
from GUI_runners import search_ui
from GUI_runners.showPopUp import showMsg
from GUI_runners.show_member import showMemberDialog
from GUI_runners.edit_data_dialog import editDataDialog


class ResultsWindow(QMainWindow):
    def __init__(self, results=None):
        super().__init__()
        path = join(DESIGNER_PATH, 'results.ui')
        loadUi(path, self)
        self.results = results

        for result in self.results:
            if type(result) == MemberObject.MemberObject:
                attribute_list = [result.getName(), result.getBig(), str(result.getBdate()), str(result.getJoinDate())]
                item = QTreeWidgetItem(attribute_list)
                self.memberTreeWidget.addTopLevelItem(item)
            else:
                attribute_list = [result.getName(), str(result.getLocation()), str(result.getCreateDate()), str(result.getModifyDate())]
                item = QTreeWidgetItem(attribute_list)
                self.fileTreeWidget.addTopLevelItem(item)
    def treeItem_to_result(self, item):
        for result in self.results:
            if (type(result) == MemberObject.MemberObject and 
            result.getName() == item.text(0) and
            result.getBig() == item.text(1) and
            str(result.getBdate()) == item.text(2) and
            str(result.getJoinDate()) == item.text(3)):
                return result
            elif (type(result) != MemberObject.MemberObject and
            result.getName() == item.text(0) and
            str(result.getLocation()) == item.text(1) and
            str(result.getCreateDate()) == item.text(2) and
            str(result.getModifyDate()) == item.text(3)):
                return result
    def newSearch(self):
        self.returnWindow = search_ui.SearchWindow()
        self.returnWindow.show()
        self.close()
    def openItem(self, item):
        if self.fileTreeWidget.currentItem():
            item = self.fileTreeWidget.currentItem()
            main_functions.open_file(item.text(1))
            return
        else:
            item = self.memberTreeWidget.currentItem()
        item = self.treeItem_to_result(item)
        self.dialog = showMemberDialog(member=item)
        self.dialog.show()
        # this gets run when a user 'activates' an item 
        #   (depends on OS, could be single/doubleclick or selcting and pressing enter, etc)
        # item.text(#) returns data for #th attribute of item
        # e.g. item.text(0) returns the name (result.getName()) of the item.
        # main_functions.open_file(item.text(1))
        # print(item.text(1))
    def editItem(self, item):
        if self.fileTreeWidget.currentItem():
            item = self.fileTreeWidget.currentItem()
        else:
            item = self.memberTreeWidget.currentItem()
        item = self.treeItem_to_result(item)
        self.dialog = editDataDialog(item)
        self.dialog.show()
    def deleteItem(self):
        pass