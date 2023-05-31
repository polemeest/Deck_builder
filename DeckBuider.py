
from PyQt6.QtWidgets import QWidget, QApplication, QDial, QMainWindow, QLabel, QTextEdit, QPushButton, QRadioButton, QFrame, QHBoxLayout
from PyQt6 import uic
import sys, os

def resource(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class UI(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        uic.load_ui.loadUi(resource('DeckBuilder.ui'), self)

        # Entrys
        self.MainTextEntry = self.findChild(QTextEdit, 'MainTextEntry')
        self.FlavorTextEntry = self.findChild(QTextEdit, 'FlavorTextEntry')
        self.PowerHitEntry = self.findChild(QTextEdit, 'PowerHitEntry')
        # Buttons
        self.BlackBt = self.findChild(QPushButton, 'BlackBt')
        self.BlueBt = self.findChild(QPushButton, 'BlueBt')
        self.GreyBt = self.findChild(QPushButton, 'GreyBt')
        self.YellowkBt = self.findChild(QPushButton, 'YellowBt')
        self.RedBt = self.findChild(QPushButton, 'RedBt')
        self.WhiteBt = self.findChild(QPushButton, 'WhiteBt')
        self.VioletBt = self.findChild(QPushButton, 'VioletBt')
        self.SaveButton = self.findChild(QPushButton, 'SaveButton')
        self.CloseButton = self.findChild(QPushButton, 'CloseButton')
        self.ImageButton = self.findChild(QPushButton, 'ImageButton')
        # Radiobuttons
        self.BlackRadio = self.findChild(QRadioButton, 'BlackRadio')
        self.BlueRadio = self.findChild(QRadioButton, 'BlueRadio')
        self.GreyRadio = self.findChild(QRadioButton, 'GreyRadio')
        self.YellowkRadio = self.findChild(QRadioButton, 'YellowRadio')
        self.RedRadio = self.findChild(QRadioButton, 'RedRadio')
        self.WhiteRadio = self.findChild(QRadioButton, 'WhiteRadio')
        self.VioletRadio = self.findChild(QRadioButton, 'VioletRadio')
        # Labels
        self.MainTextLabel = self.findChild(QLabel, 'MainTextLabel')
        self.FlavorTextLabel = self.findChild(QLabel, 'FlavorTextLabel')
        self.PowerHitLabel = self.findChild(QLabel, 'PowerHitLabel')
        self.MainTextLabel = self.findChild(QLabel, 'MainTextLabel')
        # Frame
        self.Frame = self.findChild(QFrame, 'frame')
        # Layout
        self.HLayout = self.findChild(QHBoxLayout, 'horizontalLayout')

        # connect entrys
        self.MainTextEntry.textChanged.connect(lambda: self.inputtext(self.MainTextEntry))

        # connect btns
        self.CloseButton.clicked.connect(self.close)





        self.show()

        QTextEdit.toPlainText
    def inputtext(self, b):
        self.MainTextLabel.setText(b.toPlainText())

myapp = QApplication(sys.argv)
UIwindow = UI()
myapp.exec()
