import sys
from utility import getLangs

import qtpy.QtWidgets as qtw 
import qtpy.QtGui as qtg
from qtpy.uic import loadUi
from qtpy import QtWidgets
from qtpy.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QListWidget

# from PyQt5.uic import loadUi
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox

class ListboxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui",self)

        # load files 
        
        # Combo Box
        self.mappingOptions = getLangs()
        for lang in self.mappingOptions:
            self.comboBox.addItem(lang)

        #drag and drop List Widget
        self.upload_text_files = ListboxWidget(self)
        self.upload_text_files.setGeometry

# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
