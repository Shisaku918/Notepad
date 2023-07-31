import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QFileDialog, QFontDialog
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: black; color: white;")
        
        self.setWindowTitle("Notepad in Python")
        self.setGeometry(300, 300, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.text_edit = QTextEdit(self.central_widget)
        self.text_edit.setStyleSheet("border: none;")  # Supprime les bordures du QTextEdit
        self.text_edit.setFont(QFont("Poppins sans serif", 13))

        self.layout.addWidget(self.text_edit)

        self.button_save_as = QPushButton("Save as", self.central_widget)
        self.button_save_as.clicked.connect(self.save_as)
        self.button_save_as.setStyleSheet("border-style: solid; border-width: 2px; border-radius: 10px; border-image: linear-gradient(to right, red, purple);")

        self.layout.addWidget(self.button_save_as)

    def save_as(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getSaveFileName(self, "Save as", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_edit.toPlainText())

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
