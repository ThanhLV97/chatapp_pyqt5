from enum import Enum
from enum import unique
from collections import namedtuple


class CustomEnum(Enum):
    def __get__(self, *args):
        return self.value


class Icon(CustomEnum):
    avatar1 = "ui/assets/icons/avatar_1.jpg"
    avatar2 = "ui/assets/icons/avatar_2.jpg"
    menu    = 'ui/assets/icons/menu.png'
    add     = 'ui/assets/icons/add.png'
    chat     = 'ui/assets/icons/chat.png'
    people  = 'ui/assets/icons/people.png'
    dog     = 'ui/assets/icons/dog.png'

class Style(CustomEnum):
    border = "border: 2px solid blue"


class Tittle(CustomEnum):
    name = "ChatApp"

class Tab(CustomEnum):
    chats = 'Chats'
    people = 'people'

class Size(CustomEnum):
    pass
