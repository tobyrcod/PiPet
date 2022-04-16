from utils.settings import *


class IDraggable:
    def __init__(self, rect):
        self.rect = rect
        self.events = DraggableEvents()


class DraggableEvents(Events):
    __events__ = 'on_drag'
