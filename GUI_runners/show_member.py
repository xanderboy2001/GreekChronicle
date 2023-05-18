from os.path import join
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from envVars import DESIGNER_PATH

class showMemberDialog(QDialog):
    def __init__(self, member):
        self.member = member
        super().__init__()
        path = join(DESIGNER_PATH, 'member_results.ui')
        uic.loadUi(path, self)
        self.name_field.setText(member.getName())
        self.big_field.setText(member.getBig())
        self.dob_field.setText(str(member.getBdate()))
        self.date_joined_field.setText(str(member.getJoinDate()))
        