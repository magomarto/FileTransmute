import sys
from PyQt5.QtWidgets import QApplication
from GUI.main_window import FileTransmute

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileTransmute()
    window.show()
    sys.exit(app.exec_())
