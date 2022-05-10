from PyQt5.QtWidgets import QApplication

from graph_editor.graph_editor import GraphEditor

import sys 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphEditor()
    
    sys.exit(app.exec_())