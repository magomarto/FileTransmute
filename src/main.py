import sys
import subprocess
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog, QVBoxLayout

class FileTransmute(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FileTransmute")
        self.setGeometry(200, 200, 800, 400)

        layout = QVBoxLayout()

        button = QPushButton("Converter ODT para PDF", self)
        button.clicked.connect(self.convert_odt_to_pdf)
        layout.addWidget(button)

        self.setLayout(layout)

    def convert_odt_to_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Escolha um arquivo ODT", "", "ODT files (*.odt)")
        
        if not file_path:
            return 

        output_path = os.path.splitext(file_path)[0] + ".pdf"

        try:
            subprocess.run(['pandoc', file_path, '-o', output_path], check=True)
            QMessageBox.information(self, "Sucesso", f"Arquivo convertido para {output_path}")
        except subprocess.CalledProcessError:
            QMessageBox.critical(self, "Erro", "Falha na conversão do arquivo.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileTransmute()
    window.show()
    sys.exit(app.exec_())
