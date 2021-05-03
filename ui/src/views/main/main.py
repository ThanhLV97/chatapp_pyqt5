from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFont
from ...utils import round_corners, set_icon
from ...configs import Tittle, Icon, Tab


class MainUI(object):
    def setup_ui(self, MainWindow):
        MainWindow.resize(800, 600)
        # size policy
        size_pp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # Main Window
        size_policy = MainWindow.sizePolicy().hasHeightForWidth()
        size_pp.setHeightForWidth(size_policy)
        MainWindow.setSizePolicy(size_pp)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setFixedSize(800, 600)
        self.central_widget.setStyleSheet("background:rgb(0, 204, 204)")
        self.v_central_layout = QVBoxLayout(self.central_widget)
        self.v_central_layout.setContentsMargins(0, 0, 0, 0)
        self.v_central_layout.setSpacing(0)
        # Topbar
        # background
        self.background = QWidget()
        self.h_background = QVBoxLayout(self.background)
        self.h_background.setContentsMargins(0, 0, 0, 0)
        self.h_background.setSpacing(0)
        # add to layout
        self.topbar = Topbar()
        self.window = Window()
        self.h_background.addWidget(self.topbar)
        self.h_background.addWidget(self.window)
        self.v_central_layout.addWidget(self.background)
        MainWindow.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

class Topbar(QWidget):
    def __init__(self):
        super().__init__()
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        # self.setStyleSheet("border: 1px solid black;")
        self.h_central_layout = QHBoxLayout(self)
        self.h_central_layout.setContentsMargins(0, 0, 0, 0)
        self.h_central_layout.setSpacing(5)
        # Menu
        self.menu_button = QPushButton()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy)
        self.menu_button.setMaximumSize(50, 50)
        self.menu_button.setFlat(True)
        rounded = round_corners(Icon.menu)
        set_icon(self.menu_button, rounded)
        # App Name
        self.app_name = QLabel()
        self.app_name.setText(Tittle.name.value)
        self.app_name.setAlignment(Qt.AlignCenter)
        # Add to layout
        self.h_central_layout.addWidget(self.menu_button)
        self.h_central_layout.addWidget(self.app_name)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        self.setStyleSheet("background:rgb(255, 51, 255)")
        self.h_central_layout = QHBoxLayout(self)
        self.h_central_layout.setContentsMargins(0, 0, 0, 0)
        self.h_central_layout.setSpacing(0)
        # background
        self.bg = QWidget()
        self.h_bg = QHBoxLayout(self.bg)
        self.h_bg.setContentsMargins(0, 0, 0, 0)
        self.h_bg.setSpacing(0)
        self.app_name = QLabel()
        self.app_name.setText(Tittle.name.value)

        # add leftbar
        left_bar = LeftBar()
        self.h_bg.addWidget(left_bar)
        self.h_bg.addWidget(self.app_name)
        self.h_central_layout.addWidget(self.bg)

class LeftBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(200, 640)
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        # self.setStyleSheet("background:rgb(255, 255, 255)")
        self.v_central_layout = QVBoxLayout(self)
        self.v_central_layout.setContentsMargins(0, 0, 0, 0)
        self.v_central_layout.setSpacing(0)
        # Add background
        self.bg = QWidget()
        self.v_bg = QVBoxLayout(self.bg)
        self.v_bg.setContentsMargins(0, 0, 0, 0)
        self.v_bg.setSpacing(0)
        # add top, middle, bottom
        topleft = TopLeft()
        middleleft = MiddleLeft()
        bottomleft = BottomLeft()
        # add layout
        self.v_bg.addWidget(topleft)
        self.v_bg.addWidget(middleleft)
        self.v_bg.addWidget(bottomleft)
        self.v_central_layout.addWidget(self.bg)


class TopLeft(QWidget):
    def __init__(self):
        super().__init__()
        # self.setMaximumSize(, 50)
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        self.setStyleSheet("background:rgb(204, 0, 204)")
        self.h_top = QHBoxLayout(self)
        self.h_top.setContentsMargins(0, 0, 0, 0)
        self.h_top.setSpacing(0)
        # self.setStyleSheet('border: 1px solid black;')
        # add background
        self.bg = QWidget()
        self.h_bg = QHBoxLayout(self.bg)
        self.h_bg.setContentsMargins(0, 0 ,0, 0)
        self.h_bg.setSpacing(5)
        # logo
        self.logo = QPushButton()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(50, 50)
        self.logo.setFlat(True)
        rounded = round_corners(Icon.avatar1)
        set_icon(self.logo, rounded)
        # status box text
        self._tab = QLabel(self)
        self._tab.setText(Tab.chats)
        self._tab.setAlignment(Qt.AlignCenter)
        # add button
        self.add_btn = QPushButton()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)
        self.add_btn.setMaximumSize(50, 50)
        self.add_btn.setFlat(True)
        rounded = round_corners(Icon.add)
        set_icon(self.add_btn, rounded)
        # add into layout
        self.h_bg.addWidget(self.logo)
        self.h_bg.addWidget(self._tab)
        self.h_bg.addWidget(self.add_btn)
        self.h_top.addWidget(self.bg)

    @property
    def tab(self):
        return self._tab
    @tab.setter
    def tab(self, tab_name):
        self._tab.setText(tab_name)

class MiddleLeft(QWidget):
    def __init__(self):
        super().__init__()
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        self.setStyleSheet("background:rgb(204, 0, 204)")
        # self.setStyleSheet('border: 1px solid black;')
        self.h_top = QVBoxLayout(self)
        self.h_top.setContentsMargins(0, 0, 0, 0)
        self.h_top.setSpacing(5)
        # add background
        self.bg = QWidget()
        self.h_bg = QVBoxLayout(self.bg)
        self.h_bg.setContentsMargins(0, 0 ,0, 0)
        self.h_bg.setSpacing(0)
        # add userbox
        userbox1 = UserBox()
        userbox2 = UserBox()
        userbox3 = UserBox()
        # add into layout
        self.h_bg.addWidget(userbox1)
        self.h_bg.addWidget(userbox2)
        self.h_bg.addWidget(userbox3)
        self.h_top.addWidget(self.bg)


class UserBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(50, 50)
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        # self.setStyleSheet("background:rgb(204, 0, 204)")
        self.setStyleSheet('border: 1px solid black;')
        self.h_user = QHBoxLayout(self)
        self.h_user.setContentsMargins(0, 0, 0, 0)
        self.h_user.setSpacing(5)
        # add background
        self.bg = QWidget()
        self.h_bg = QHBoxLayout(self.bg)
        self.h_bg.setContentsMargins(0, 0 ,0, 0)
        self.h_bg.setSpacing(0)
        # avatar
        self.avatar = QPushButton()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.avatar.sizePolicy().hasHeightForWidth())
        self.avatar.setSizePolicy(sizePolicy)
        self.avatar.setMaximumSize(50, 50)
        self.avatar.setFlat(True)
        rounded = round_corners(Icon.avatar2)
        set_icon(self.avatar, rounded)
        # info box
        self.info_box = QLabel()
        self.info_box.setText('Covid-19')
        # add to layout
        self.h_bg.addWidget(self.avatar)
        self.h_bg.addWidget(self.info_box)
        self.h_user.addWidget(self.bg)
    
    def update_status(self):
        pass
    
    def update_avatar(self):
        pass


class BottomLeft(QWidget):
    def __init__(self):
        super().__init__()
        size_pf = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        policy = self.sizePolicy().hasHeightForWidth()
        size_pf.setHeightForWidth(policy)
        self.setSizePolicy(size_pf)
        self.setStyleSheet("background:rgb(128, 0, 128)")
        self.h_bottom_left = QHBoxLayout(self)
        self.h_bottom_left.setContentsMargins(0, 0, 0, 0)
        self.h_bottom_left.setSpacing(0)

        # add background
        self.bg = QWidget()
        self.h_bg = QHBoxLayout(self.bg)
        self.h_bg.setContentsMargins(0, 0 ,0, 0)
        self.h_bg.setSpacing(0)
        # chats
        self.chat_btn = QPushButton()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.chat_btn.sizePolicy().hasHeightForWidth())
        self.chat_btn.setSizePolicy(sizePolicy)
        self.chat_btn.setMaximumSize(50, 50)
        self.chat_btn.setFlat(True)
        rounded = round_corners(Icon.chat)
        set_icon(self.chat_btn, rounded)
        # people 
        self.people_btn = QPushButton()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.people_btn.sizePolicy().hasHeightForWidth())
        self.people_btn.setSizePolicy(sizePolicy)
        self.people_btn.setMaximumSize(50, 50)
        self.people_btn.setFlat(True)
        rounded = round_corners(Icon.people, radius=50)
        set_icon(self.people_btn, rounded)
        # add to layout
        self.h_bg.addWidget(self.chat_btn)
        self.h_bg.addWidget(self.people_btn)
        self.h_bottom_left.addWidget(self.bg)
