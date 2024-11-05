# gui/dialogs.py

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from converters.audio_converter import AudioConverter
from converters.document_converter import DocumentConverter
from converters.ebook_converter import EbookConverter
from converters.gif_converter import GIFConverter

class ConversationOptionsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Escolha o que quer formatar")
        self.setGeometry(250, 250, 400, 300)

        layout = QVBoxLayout()

        # Botões para cada tipo de conversão
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
        
        try:
            converter = AudioConverter(file_path)
            output_file = converter.convert('wav')  
            QMessageBox.information(self, "Sucesso", f"Arquivo convertido para {output_file}")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao converter o arquivo: {str(e)}")

    def convert_document(self): # falta
        pass

    def convert_ebook(self):# falta

        pass

    def convert_gif(self): # falta

        pass

    def convert_image(self): # falta
       
        pass
