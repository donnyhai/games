import game
from PyQt5 import QtWidgets

class MyDialog(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400, 300)
        self.groupbox = QtWidgets.QGroupBox(self)
        self.pushbutton1 = QtWidgets.QPushButton(self.groupbox)
        self.textedit = QtWidgets.QTextEdit(self.groupbox)
        self.label = QtWidgets.QLabel(self.groupbox)
        self.hlayout = QtWidgets.QHBoxLayout()
        self.hlayout.addWidget(self.label)
        self.hlayout.addWidget(self.textedit)
        self.vlayout = QtWidgets.QVBoxLayout(self.groupbox)
        self.vlayout.addLayout(self.hlayout)
        self.vlayout.addWidget(self.pushbutton1)
        self.pushbutton_ok = QtWidgets.QPushButton(self)
        spaceritem = QtWidgets.QSpacerItem(40,20)
        self.hlayout2 = QtWidgets.QHBoxLayout()
        self.hlayout2.addItem(spaceritem)
        self.hlayout2.addWidget(self.pushbutton_ok)
        self.vlayout2 = QtWidgets.QVBoxLayout(self)
        self.vlayout2.addWidget(self.groupbox)
        self.vlayout2.addLayout(self.hlayout2)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_()) 