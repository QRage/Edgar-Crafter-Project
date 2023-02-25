from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QRadioButton, QCheckBox


class Craft(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(300, 200)

        self.groupBox = QGroupBox('Craft method')
        self.groupBox.setGeometry(20, 20, 300, 100)
        self.grid = QGridLayout()

        radio1 = QRadioButton('Alteration')
        radio2 = QRadioButton('Alt+Regal')
        radio3 = QRadioButton('Alchemy')
        radio4 = QRadioButton('Chaos')

        self.grid.addWidget(radio1, 0, 0)
        self.grid.addWidget(radio2, 1, 0)
        self.grid.addWidget(radio3, 2, 0)
        self.grid.addWidget(radio4, 3, 0)

        self.setFixedSize(150, 130)

        self.groupBox.setLayout(self.grid)

        layout = QGridLayout()
        layout.addWidget(self.groupBox)
        self.setLayout(layout)
