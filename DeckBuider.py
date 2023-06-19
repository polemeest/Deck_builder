
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QRadioButton, QFrame, QHBoxLayout, QGroupBox, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
import sys, os
from PIL import Image, ImageDraw, ImageFont


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
        self.CreatureNameEntry = self.findChild(QTextEdit, 'CreatureNameEntry')
        self.CreatureTypeEntry = self.findChild(QTextEdit, 'CreatureTypeEntry')
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
        self.CreatureNameLabel = self.findChild(QLabel, 'CreatureNameLabel')
        self.CreatureTypeLabel = self.findChild(QLabel, 'CreatureTypeLabel')
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
        self.CreatureNameEntry.textChanged.connect(lambda: self.input_text(self.CreatureNameEntry, self.CreatureNameLabel))
        self.CreatureTypeEntry.textChanged.connect(lambda: self.input_text(self.CreatureTypeEntry, self.CreatureTypeLabel))

        # connect btns
        self.CloseButton.clicked.connect(self.close)
        self.SaveButton.clicked.connect(self.save)
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
        self.cur_color = 'images/BlackRadio.png'
        self.cur_cost = []


        self.show()


    def choose_color(self, radio: QRadioButton):
        self.cur_color = f'images/{radio.objectName()}.png'
        self.TopImage.setPixmap(QPixmap(f'images/{radio.objectName()}.png'))


    def insert_creature(self):
        self.cur_pixmap = QFileDialog.getOpenFileName(directory='./images/characters')[0]
        pic = QPixmap(self.cur_pixmap)
        self.BottomImage.setPixmap(pic)


    def add_cost(self, button: QPushButton):
        self.cur_cost.append(f'images\{button.objectName()}.jpg')
        pixmap = QPixmap(f'images\{button.objectName()}.jpg')
        pixmap = pixmap.scaled(20, 20)
        label = QLabel(pixmap=pixmap)
        self.HLayout.addWidget(label)


    def del_cost(self):
        for child in self.GroupBox.children():
            if isinstance(child, QLabel):
                child.deleteLater()
                self.cur_cost.pop()


    def input_text(self, entry: QTextEdit, label: QLabel):
        label.setWordWrap(True)
        label.setText(entry.toPlainText())


    def clear_all(self):
        self.del_cost()
        for child in self.__dict__.values():
            if isinstance(child, QTextEdit):
                child.clear()
        self.cur_pixmap = ''
        self.BottomImage.setPixmap(QPixmap())


    def paste_images(self):
        # init a colored border
        with Image.open(self.cur_color) as bor:
            border = bor.copy().convert(mode='RGBA')
        # pasting central image
        with Image.open(self.cur_pixmap) as mai:
            main = mai.copy().resize((808, 593))
        with Image.open('images\mask.png') as mask:
            mask = mask.resize((50, 50)).convert('L')
        border.paste(main, (35, 113))
        # pasting cost
        for index, item in enumerate(self.cur_cost):
            temp = Image.open(item)
            cost = temp.resize((50, 50)).copy()
            border.paste(cost, ((border.width - 85) - 60 * index, 40), mask)
            temp.close()
            cost.close()
        return border


    def draw_text(self, image):
        # pasting text
        texts = ImageDraw.Draw(image)
        main_font = ImageFont.truetype(r'C:\Windows\Fonts\Gabriola.ttf', 65)
        flavor_font = ImageFont.truetype(r'C:\Windows\Fonts\Crimson-Italic.ttf', 40)
        pwrhit_font = ImageFont.truetype(r'C:\Windows\Fonts\Crimson-Italic.ttf', 55)
        # main block
        texts.text((55, 810), f'''{self.MainTextEntry.toPlainText()}''', (0,0,0), font=main_font)
        texts.line((80, 1050, 800, 1050), fill=(2, 2, 2), width=1)
        texts.text((55, 1070), f'''{self.FlavorTextEntry.toPlainText()}''', (0,0,0), font=flavor_font)
        # stats and creature type
        texts.text((700, 1172), f'''{self.PowerHitEntry.toPlainText()}''', (0,0,0), font=pwrhit_font, align='center')
        texts.text((50, 35), f'''{self.CreatureNameEntry.toPlainText()}''', (0,0,0), font=main_font)
        texts.text((50, 720), f'''{self.CreatureTypeEntry.toPlainText()}''', (0,0,0), font=main_font)


    def save(self):
        # init a destination
        location = QFileDialog.getSaveFileName(self, 'Save As', './images/characters', filter='*.png')
        # call for pillow
        image = self.paste_images()
        self.draw_text(image)
        # saving and checking file
        image.save(location[0], quality=95)
        if os.path.isfile(location[0]):
            dlg = QMessageBox.information(self, 'Success', 'Your file has been successfully saved!', QMessageBox.StandardButton.Ok)
            self.clear_all()
        else:
            dlg = QMessageBox.critical(self, 'Failure', "Your file can't be saved!", QMessageBox.StandardButton.Retry | QMessageBox.StandardButton.Cancel)
            if dlg == QMessageBox.StandardButton.Cancel:
                self.clear_all()



if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    UIwindow = UI()
    myapp.exec()
