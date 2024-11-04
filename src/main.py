import sys
import os
from converters.audio_converter import AudioConverter
from converters.document_converter import DocumentConverter
from converters.ebook_converter import EbookConverter
from converters.gif_converter import GIFConverter
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QMessageBox, QWidget, QDialog,QFileDialog
)

class FileTransmute(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FileTransmute")
        self.setGeometry(200, 200, 800, 400)

        layout = QVBoxLayout()

        button = QPushButton("O que deseja converter?", self)
        button.clicked.connect(self.show_conversion_options)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_conversion_options(self):
        options_dialog = ConversationOptionsDialog(self)
        options_dialog.exec_()

class ConversationOptionsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Escolha o que quer formatar")
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

    def convert_audio(self):

        file_path, _ = QFileDialog.getOpenFileName(self, "Escolha um arquivo de áudio", "", "Audio files (*.mp3 *.wav *.ogg)")
        if not file_path:
            return
        
        converter = AudioConverter(file_path)
        output_file = converter.convert('wav')  
        QMessageBox.information(self, "Sucesso", f"Arquivo convertido para {output_file}")

    def convert_document(self):
        pass

    def convert_ebook(self):
        pass

    def convert_gif(self):
        pass

    def convert_image(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileTransmute()
    window.show()
    sys.exit(app.exec_())
