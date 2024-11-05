from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget
from GUI.dialogs import ConversationOptionsDialog  
from GUI.styles import apply_stylesheet 

class FileTransmute(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FileTransmute")
        self.setGeometry(200, 200, 800, 400)

        layout = QVBoxLayout()

        button = QPushButton("Transmute a file!", self) # botao prinipal
        button.clicked.connect(self.show_conversion_options)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        apply_stylesheet(self) # aplica estilo

    def show_conversion_options(self):
        options_dialog = ConversationOptionsDialog(self)
        options_dialog.exec_()
