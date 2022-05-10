from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from graph_editor.scenes.node_graphics_scene import QDMGraphicsScene


class GraphEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 100, 1000, 800)
        
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        
        # create graphics scene
        self.grScene = QDMGraphicsScene()
        
        # create graphics view
        self.view = QGraphicsView(self)
        self.view.setScene(self.grScene)
        self.layout.addWidget(self.view)
        
        
        self.setWindowTitle("Graph Editor")
        self.show()