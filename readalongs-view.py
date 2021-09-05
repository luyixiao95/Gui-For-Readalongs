#Readalongs gui

import qtpy.QtWidgets as qtw 
import qtpy.QtGui as qtg
import sys
class SecondWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Readalong Studio")
        self.layout = qtw.QGridLayout()
        self.setLayout(self.layout)
        msgs1 = qtw.QLabel("""
        <h2> Step 1: Upload data to start creating your ReadAlong </h2>""")
        msgs2 =qtw.QLabel( 'Choose a plain text file (.txt) or XML file(.xml)')
        msgs3 = qtw.QLabel('Choose an Audio file (.mp3 or .wav)')
        msgs4 = qtw.QLabel("Mapping language")
        msgs5 = qtw.QLabel("""
        <h2> Step 2 (Optional): Set some configuration options </h2>""")
        self.layout.addWidget(msgs1, 0, 0, 1, 4)
        self.layout.addWidget(msgs2, 1, 0)
        self.layout.addWidget(msgs3, 2, 0)
        self.layout.addWidget(msgs4, 3, 0)
        self.layout.addWidget(msgs5, 6, 0, 1, 4)
        
        ChooseFileButton1 = qtw.QPushButton("Choose File")
        self.layout.addWidget(ChooseFileButton1, 1, 2)
        ChooseFileButton2 = qtw.QPushButton("Choose File")
        self.layout.addWidget(ChooseFileButton2, 2, 2)

        my_combo = qtw.QComboBox(self, insertPolicy=qtw.QComboBox.InsertAtBottom)

        my_combo.addItem("Fr")
        my_combo.addItem("En")
        my_combo.addItem("De")

        self.layout.addWidget(my_combo, 4, 0, 1, 2)

        SubmitButton = qtw.QPushButton("Submit")
        self.layout.addWidget(SubmitButton, 4, 2, 1, 1)
        checkBox = {"Save Temporary Files": 0, "Closed Captioning": 1, 
        "Save Text Grids" :2, "Show Log":3}
        check1 = qtw.QCheckBox("Save Temporary Files")
        self.layout.addWidget(check1, 9, 0)
        check2 = qtw.QCheckBox("Closed Captioning")
        check3 = qtw.QCheckBox("Save Text Grids")
        check4 = qtw.QCheckBox("Show Log")

        self.layout.addWidget(check2, 9, 1)
        self.layout.addWidget(check3, 10, 0)
        self.layout.addWidget(check4, 10, 1)
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Readalong Studio")
        self.layout = qtw.QGridLayout()
        self.setLayout(self.layout)
        
        self._firstDisplays()
        self._firstButton()

    
    def _firstDisplays(self):
        helloMsg = qtw.QLabel("""
        <h1> Welcome to Readalongs</h1>
        <p>  Welcome! Readalong Studio is an end audio/text aligner </p>
        <p>  where you can visualize the alignment of your audio </p>
        <p>  and text files for a specific language.</p>
        """)

        self.layout.addWidget(helloMsg, 0, 0, 1, 2)
        

    def _firstButton(self):
        getStartedButton = qtw.QPushButton("Get Started!")
        self.layout.addWidget(getStartedButton, 3, 3 ,1, 1)
        getStartedButton.clicked.connect(self.window2)
    

    
    def window2(self):
        self.w = SecondWindow()
        self.w.show()
        self.hide()

        





app = qtw.QApplication(sys.argv)

view = MainWindow()
view.show()
sys.exit(app.exec_())
