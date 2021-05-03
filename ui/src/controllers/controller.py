from PyQt5.QtWidgets import QMainWindow
from ..views import MainUI


class MainController(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainUI()
        self.ui.setup_ui(self)
        self.show()
