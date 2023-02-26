import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from widgets.craft import Craft


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.tab1.layout = QVBoxLayout(self.tab1)
        # TODO craft page widgets
        self.tab1.layout.addWidget(Craft())
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QVBoxLayout(self.tab2)
        self.tab2.layout.addWidget(QLabel("Sockets"))
        self.tab2.setLayout(self.tab2.layout)

        self.tab3.layout = QVBoxLayout(self.tab3)
        self.tab3.layout.addWidget(QLabel("Maps"))
        self.tab3.setLayout(self.tab3.layout)

        self.tab4.layout = QVBoxLayout(self.tab4)
        self.tab4.layout.addWidget(QLabel("Settings"))
        self.tab4.setLayout(self.tab4.layout)

        self.tabs.addTab(self.tab1, "Craft")
        self.tabs.addTab(self.tab2, "Sockets")
        self.tabs.addTab(self.tab3, "Maps")
        self.tabs.addTab(self.tab4, "Settings")

        self.setCentralWidget(self.tabs)

        self.setGeometry(300, 200, 300, 600)
        self.setWindowTitle("Edgar crafter")

        ###


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
