from utils.settings import *


class IClickable:
    def __init__(self, rect):
        self.rect = rect
        self.events = ClickableEvents()


class ClickableEvents(Events):
    __events__ = 'on_clicked'
