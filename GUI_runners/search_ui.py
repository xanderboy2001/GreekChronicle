from os.path import join
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.uic import loadUi
#from GUI_runners.advanced_search import AdvancedSearchWindow
from GUI_runners import advanced_search, resultsWindow, add_data_dialog
from envVars import DESIGNER_PATH
from search_service import search

class SearchWindow(QMainWindow):

    # self.searchBox.text() returns text inside search box
    # filetype_checkBox_docs.isChecked() returns T/F based on status (T for checked, F for not)
    # filetype_checkBox_pics.isChecked() returns T/F based on status
    # filetype_checkBox_members.isChecked() returns T/F based on status
    # each function corresponds to a button (should be self-explanatory)

    def __init__(self):
        super().__init__()
        path = join(DESIGNER_PATH, 'search.ui')
        loadUi(path, self)
    def addData(self):
        self.new_item_dialog = add_data_dialog.addDataDialog()
        self.new_item_dialog.show()
    def presentData(self):
        pass
    def advancedSearch(self):
        self.newWindow = advanced_search.AdvancedSearchWindow()
        self.newWindow.show()
    def search(self):
        search_results = search(self.searchBox.text())
        self.newWindow = resultsWindow.ResultsWindow(results=search_results)
        self.newWindow.show()
        self.close()