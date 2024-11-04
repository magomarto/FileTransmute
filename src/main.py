import sys
import subprocess
import os
from converters import audio
from converters import documents
from converters import ebook
from converters import gif
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QMessageBox, QWidget, QDialog, QHBoxLayout
)
class FileTransmute(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FileTransmute")
        self.setGeometry(200, 200, 800, 400)

        layout = QVBoxLayout()

        button = QPushButton("Oque deseja converter?", self)
        button.clicked.connect(self.show_conversion_options)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_conversion_options(self):
        options_dialog = ConversationOptionsDialog(self)
        options_dialog.exec_()

    def choose(self):
        pass

'''    def convert_odt_to_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Escolha um arquivo ODT", "", "ODT files (*.odt)")
        
        if not file_path:
            return 

        output_path = os.path.splitext(file_path)[0] + ".pdf"

        try:
            subprocess.run(['pandoc', file_path, '-o', output_path], check=True)
            QMessageBox.information(self, "Sucesso", f"Arquivo convertido para {output_path}")
        except subprocess.CalledProcessError:
            QMessageBox.critical(self, "Erro", "Falha na conversão do arquivo.")'''

class ConversationOptionsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Escolha o quer formatar")
        self.setGeometry(250, 250, 400, 200)

        layout = QVBoxLayout()

        audio_button = QPushButton("Áudio", self)
        audio_button.clicked.connect(self.convert_audio)
        layout.addWidget(audio_button)

        document_button = QPushButton("Document", self)
        document_button.clicked.connect(self.convert_document)
        layout.addWidget(document_button)

        ebook_button = QPushButton("Ebook", self)
        ebook_button.clicked.connect(self.convert_ebook)
        layout.addWidget(ebook_button)

        gif_button = QPushButton("GIF", self)
        gif_button.clicked.connect(self.convert_gif)
        layout.addWidget(gif_button)

        image_button = QPushButton("Image", self)
        image_button.clicked.connect(self.convert_image)
        layout.addWidget(image_button)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileTransmute()
    window.show()
    sys.exit(app.exec_())
