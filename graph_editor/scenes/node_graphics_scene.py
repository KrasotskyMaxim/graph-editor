from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QDMGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # settings
        self._color_background = QColor("#393939")
        self._color_light = QColor("#2f2f2f")
        
        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        
        self.scene_width, self.scene_height = 64000, 64000
        self.setSceneRect(-self.scene_width//2, -self.scene_height//2, self.scene_width, self.scene_height)
        
        self.setBackgroundBrush(self._color_background)
        
    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)
        
        # here we create our grid
        
        # compute all lines to be drawn
        lines_light = []
        lines_light.append(QLine(0, 0, 100, 100))
        
        # draw the lines
        painter.setPen(self._pen_light)
        painter.drawLines(*lines_light)