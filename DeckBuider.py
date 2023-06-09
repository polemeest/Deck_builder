
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QRadioButton, QFrame, QHBoxLayout, QGroupBox, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
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
        self.CreatureEntry = self.findChild(QTextEdit, 'CreatureEntry')
        # Buttons
        self.BlackBt = self.findChild(QPushButton, 'BlackBt')
        self.BlueBt = self.findChild(QPushButton, 'BlueBt')
        self.GreyBt = self.findChild(QPushButton, 'GreyBt')
        self.YellowkBt = self.findChild(QPushButton, 'YellowBt')
        self.RedBt = self.findChild(QPushButton, 'RedBt')
        self.WhiteBt = self.findChild(QPushButton, 'WhiteBt')
        self.VioletBt = self.findChild(QPushButton, 'VioletBt')
        self.Backspace = self.findChild(QPushButton, 'Backspace')
        self.SaveButton = self.findChild(QPushButton, 'SaveButton')
        self.CloseButton = self.findChild(QPushButton, 'CloseButton')
        self.ImageButton = self.findChild(QPushButton, 'ImageButton')
        # Radiobuttons
        self.BlackRadio = self.findChild(QRadioButton, 'BlackRadio')
        self.BlueRadio = self.findChild(QRadioButton, 'BlueRadio')
        self.GreyRadio = self.findChild(QRadioButton, 'GreyRadio')
        self.YellowRadio = self.findChild(QRadioButton, 'YellowRadio')
        self.RedRadio = self.findChild(QRadioButton, 'RedRadio')
        self.WhiteRadio = self.findChild(QRadioButton, 'WhiteRadio')
        self.VioletRadio = self.findChild(QRadioButton, 'VioletRadio')
        # Labels
        self.MainTextLabel = self.findChild(QLabel, 'MainTextLabel')
        self.FlavorTextLabel = self.findChild(QLabel, 'FlavorTextLabel')
        self.PowerHitLabel = self.findChild(QLabel, 'PowerHitLabel')
        self.MainTextLabel = self.findChild(QLabel, 'MainTextLabel')
        self.TopImage = self.findChild(QLabel, 'TopImage')
        self.BottomImage = self.findChild(QLabel, 'BottomImage')
        self.CreatureLabel = self.findChild(QLabel, 'CreatureLabel')
        # Frame
        self.Frame = self.findChild(QFrame, 'frame')
        # Layout
        self.HLayout = self.findChild(QHBoxLayout, 'horizontalLayout')
        # Group Box
        self.GroupBox = self.findChild(QGroupBox, 'GroupBox')
        self.GroupBox.setLayout(self.HLayout)

        # connect entrys
        self.MainTextEntry.textChanged.connect(lambda: self.input_text(self.MainTextEntry, self.MainTextLabel))
        self.FlavorTextEntry.textChanged.connect(lambda: self.input_text(self.FlavorTextEntry, self.FlavorTextLabel))
        self.PowerHitEntry.textChanged.connect(lambda: self.input_text(self.PowerHitEntry, self.PowerHitLabel))
        self.CreatureEntry.textChanged.connect(lambda: self.input_text(self.CreatureEntry, self.CreatureLabel))

        # connect btns
        self.CloseButton.clicked.connect(self.close)
        self.SaveButton.clicked.connect(self.close)
        self.ImageButton.clicked.connect(self.insert_creature)

        self.BlackBt.clicked.connect(lambda: self.add_cost(self.BlackBt))
        self.BlueBt.clicked.connect(lambda: self.add_cost(self.BlueBt))
        self.GreyBt.clicked.connect(lambda: self.add_cost(self.GreyBt))
        self.YellowkBt.clicked.connect(lambda: self.add_cost(self.YellowkBt))
        self.RedBt.clicked.connect(lambda: self.add_cost(self.RedBt))
        self.WhiteBt.clicked.connect(lambda: self.add_cost(self.WhiteBt))
        self.VioletBt.clicked.connect(lambda: self.add_cost(self.VioletBt))
        self.Backspace.clicked.connect(self.del_cost)

        # connect radios
        self.BlackRadio.clicked.connect(lambda: self.choose_color(self.BlackRadio))
        self.BlueRadio.clicked.connect(lambda: self.choose_color(self.BlueRadio))
        self.GreyRadio.clicked.connect(lambda: self.choose_color(self.GreyRadio))
        self.YellowRadio.clicked.connect(lambda: self.choose_color(self.YellowRadio))
        self.RedRadio.clicked.connect(lambda: self.choose_color(self.RedRadio))
        self.WhiteRadio.clicked.connect(lambda: self.choose_color(self.WhiteRadio))
        self.VioletRadio.clicked.connect(lambda: self.choose_color(self.VioletRadio))


        # special vars
        self.cur_pixmap = ''
        self.cur_color = ''


        self.show()


    def choose_color(self, radio: QRadioButton):
        self.cur_color = f'images/{radio.objectName()}.png'
        self.TopImage.setPixmap(QPixmap(f'images/{radio.objectName()}.png'))


    def insert_creature(self):
        self.cur_pixmap = QFileDialog.getOpenFileName()[0]
        pic = QPixmap(self.cur_pixmap)
        self.BottomImage.setPixmap(pic)


    def add_cost(self, button: QPushButton):
        self.cur_pixmap = f'images\{button.objectName()}.png'
        pixmap = QPixmap(f'images\{button.objectName()}.png')
        pixmap = pixmap.scaled(20, 20)
        label = QLabel(pixmap=pixmap)
        print(button.objectName())

        self.HLayout.addWidget(label)
        for child in self.GroupBox.children():
            if isinstance(child, QLabel):
                print(child.__getattribute__('pixmap'))


    def del_cost(self):
        for child in self.GroupBox.children():
            if isinstance(child, QLabel):
                child.deleteLater()


    def input_text(self, entry: QTextEdit, label: QLabel):
        label.setWordWrap(True)
        label.setText(entry.toPlainText())

myapp = QApplication(sys.argv)
UIwindow = UI()
myapp.exec()
