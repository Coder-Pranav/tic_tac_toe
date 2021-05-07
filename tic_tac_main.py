import os.path
import sys
import os
from PySide2.QtGui import QPixmap, QFont
from PySide2.QtWidgets import *

icon_path = os.path.dirname(__file__)

class Panel(QWidget):
    count = 0

    def __init__(self):
        super(Panel, self).__init__()
        new_font = QFont("Arial", 30, QFont.Bold)
        self.table = QTableWidget()
        self.warning_label = QLabel()
        self.warning_label.setFont(new_font)
        self.new_game_button = QPushButton('Reset')
        self.new_game_button.setMinimumSize(10, 50)
        self.new_game_button.setFont(new_font)
        self.warning_label.setText(self.get_info_icon_and_text()[1])
        self.q_msg_box = QMessageBox()
        self.q_msg_box.setWindowTitle('Message')
        self.q_msg_box.setInformativeText("Do you want to start a new game?")
        self.q_msg_box.addButton('New Game', QMessageBox.AcceptRole)
        self.q_msg_box.addButton("I'm Done", QMessageBox.RejectRole)
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.cellClicked.connect(self.tic_clicked)
        self.table.setFrameStyle(QFrame.NoFrame)
        self.new_game_button.clicked.connect(self.clear_everything)
        label_button_lay = QHBoxLayout()
        label_button_lay.addWidget(self.warning_label)
        label_button_lay.addWidget(self.new_game_button)
        master_lay = QVBoxLayout()
        master_lay.addLayout(label_button_lay)
        master_lay.addWidget(self.table)
        self.setLayout(master_lay)
        self.setWindowTitle('Tic Tac Toe')
        self.setMinimumSize(900, 900)

    def tic_clicked(self, row, column):
        info = self.get_info_icon_and_text()
        icon = info[0]
        player = info[2]
        pix = QPixmap(icon)
        item = QLabel()
        item.setObjectName(player)
        item.setPixmap(pix)
        item.setScaledContents(True)
        if self.table.cellWidget(row, column) is None:
            self.table.setCellWidget(row, column, item)
            self.count = self.count + 1
            self.warning_label.setText(self.get_info_icon_and_text()[1])
            self.logic_tic()

    def get_info_icon_and_text(self):
        if self.count % 2:
            player = 'Player O'
            icon = os.path.join(icon_path, 'icons/icon1.png').replace('\\', '/')
            text_warning = '<P style="color:#8EF5FF;">Player O turn!</p>'
        else:
            player = 'Player X'
            icon = os.path.join(icon_path, 'icons/icon2.png').replace('\\', '/')
            text_warning = '<P style="color:#f7e778;">Player X turn!</p>'
        return icon, text_warning, player

    def logic_tic(self):
        message = " Won"
        if self.count >= 5:
            if self.get_object_name(0, 0) == \
                    self.get_object_name(0, 1) == self.get_object_name(0, 2) != ' ':  # across the top
                self.msg_box(self.get_object_name(0, 0) + message)
            elif self.get_object_name(1, 0) == \
                    self.get_object_name(1, 1) == self.get_object_name(1, 2) != ' ':  # across the middle
                self.msg_box(self.get_object_name(1, 0) + message)
            elif self.get_object_name(2, 0) == \
                    self.get_object_name(2, 1) == self.get_object_name(2, 2) is not None:  # across the bottom
                self.msg_box(self.get_object_name(2, 0) + message)
            elif self.get_object_name(0, 0) == \
                    self.get_object_name(1, 0) == self.get_object_name(2, 0) is not None:  # down the left side
                self.msg_box(self.get_object_name(0, 0) + message)
            elif self.get_object_name(0, 1) == \
                    self.get_object_name(1, 1) == self.get_object_name(2, 1) is not None:  # down the middle
                self.msg_box(self.get_object_name(0, 1) + message)
            elif self.get_object_name(0, 2) == \
                    self.get_object_name(1, 2) == self.get_object_name(2, 2) is not None:  # down the right side
                self.msg_box(self.get_object_name(0, 2) + message)
            elif self.get_object_name(0, 0) == \
                    self.get_object_name(1, 1) == self.get_object_name(2, 2) is not None:  # diagonal
                self.msg_box(self.get_object_name(0, 0) + message)
            elif self.get_object_name(2, 0) == \
                    self.get_object_name(1, 1) == self.get_object_name(0, 2) is not None:  # diagonal
                self.msg_box(self.get_object_name(2, 0) + message)

            if self.count == 9:
                self.msg_box("It's a Tie!!")

    def get_object_name(self, row, column):
        try:
            return self.table.cellWidget(row, column).objectName()
        except:
            return None

    def msg_box(self, message):
        """
        This method creates and shows messages box
        @param message: message to show in the message box
        """
        self.q_msg_box.setText(message)
        ret = self.q_msg_box.exec_()
        self.clear_everything(ret)

    def clear_everything(self, ret):
        if not ret:
            self.table.clear()
            self.count = 0
            self.warning_label.setText(self.get_info_icon_and_text()[1])
            self.q_msg_box.close()
        else:
            self.close()
            self.q_msg_box.close()


style = '''
QWidget{background-color: #50514f;
color:white;
}
QPushButton{background-color:#6b7fd7;
color:white;
min-height:25px;
min-width:100px;
border-radius : 5px;
}
'''


def tic_tac_run():
    tic_tac_run.panel = Panel()
    tic_tac_run.panel.show()


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(style)
    panel = Panel()
    panel.show()
    sys.exit(app.exec_())
