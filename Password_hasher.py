import sys
import hashlib
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox,
    QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QToolButton
)
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
from PyQt5.QtCore import Qt, QSize

class HashingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.dark_mode = True  # Start in dark mode
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Hasher')
        self.setGeometry(100, 100, 600, 300)

        # Input Label and Field
        self.input_label = QLabel('Enter Clear Text:')
        self.input_line = QLineEdit()

        # Algorithm Selection
        self.algo_label = QLabel('Select Algorithm:')
        self.algo_combo = QComboBox()
        algorithms = [algo.upper() for algo in sorted(hashlib.algorithms_guaranteed)]
        self.algo_combo.addItems(algorithms)
        self.algo_combo.setCurrentText('MD5')  # Set MD5 as the default algorithm

        # Hash Button
        self.hash_button = QPushButton('Hash Password')
        self.hash_button.clicked.connect(self.hash_password)

        # Result Display
        self.result_label = QLabel('Hashed Password:')
        self.result_text = QLineEdit()
        self.result_text.setReadOnly(True)

        # Copy Button
        self.copy_button = QPushButton('Copy')
        self.copy_button.clicked.connect(self.copy_hash)

        # Dark Mode Toggle Switch
        self.toggle_button = QToolButton()
        self.toggle_button.setCheckable(True)
        self.toggle_button.setChecked(True)
        self.toggle_button.toggled.connect(self.toggle_mode)
        self.update_toggle_icon()

        # Make the toggle button larger
        self.toggle_button.setIconSize(QSize(32, 32))

        # Layouts
        main_layout = QVBoxLayout()
        form_layout = QGridLayout()

        # Add widgets to form layout
        form_layout.addWidget(self.input_label, 0, 0)
        form_layout.addWidget(self.input_line, 0, 1, 1, 2)

        form_layout.addWidget(self.algo_label, 1, 0)
        form_layout.addWidget(self.algo_combo, 1, 1, 1, 2)

        form_layout.addWidget(self.hash_button, 2, 0, 1, 3)

        form_layout.addWidget(self.result_label, 3, 0)
        form_layout.addWidget(self.result_text, 3, 1)
        form_layout.addWidget(self.copy_button, 3, 2)

        # Add toggle button to the top right corner
        top_layout = QHBoxLayout()
        top_layout.addStretch()
        top_layout.addWidget(self.toggle_button)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(form_layout)

        self.setLayout(main_layout)

        # Apply initial styles after widgets are created
        if self.dark_mode:
            self.apply_dark_mode_styles()
        else:
            self.apply_light_mode_styles()

    def input_style(self):
        return """
            QLineEdit {
                background-color: #3C3C3C;
                color: white;
                padding: 8px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            QLineEdit:hover {
                background-color: #444444;
            }
        """

    def combo_style(self):
        return """
            QComboBox {
                background-color: #3C3C3C;
                color: white;
                padding: 8px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #3C3C3C;
                color: white;
                selection-background-color: #555555;
                border-radius: 5px;
            }
        """

    def button_style(self):
        return """
            QPushButton {
                background-color: #5A9;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #7AB;
            }
        """

    def toggle_style(self):
        return """
            QToolButton {
                background: transparent;
                border: none;
                font-size: 24px;
                color: white;
            }
        """

    def update_toggle_icon(self):
        if self.dark_mode:
            self.toggle_button.setText('☀')  # Sun symbol
        else:
            self.toggle_button.setText('🌙')  # Moon symbol

    def hash_password(self):
        password = self.input_line.text()
        algo = self.algo_combo.currentText().lower()
        try:
            hash_func = hashlib.new(algo)
            hash_func.update(password.encode('utf-8'))
            hashed_password = hash_func.hexdigest()
            self.result_text.setText(hashed_password)
        except Exception as e:
            self.result_text.setText(f"Error: {str(e)}")

    def copy_hash(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.result_text.text())

    def toggle_mode(self):
        self.dark_mode = self.toggle_button.isChecked()
        self.update_toggle_icon()
        if self.dark_mode:
            self.apply_dark_mode_styles()
        else:
            self.apply_light_mode_styles()

    def apply_dark_mode_styles(self):
        # Set styles for dark mode
        self.setStyleSheet("background-color: #2D2D2D; color: white;")
        self.input_label.setStyleSheet("font-size: 14px; color: white;")
        self.algo_label.setStyleSheet("font-size: 14px; color: white;")
        self.result_label.setStyleSheet("font-size: 14px; color: white;")
        self.input_line.setStyleSheet(self.input_style())
        self.result_text.setStyleSheet(self.input_style())
        self.algo_combo.setStyleSheet(self.combo_style())
        self.toggle_button.setStyleSheet(self.toggle_style())
        self.hash_button.setStyleSheet(self.button_style())
        self.copy_button.setStyleSheet(self.button_style())

    def apply_light_mode_styles(self):
        # Set styles for light mode
        self.setStyleSheet("background-color: #F0F0F0; color: black;")
        self.input_label.setStyleSheet("font-size: 14px; color: black;")
        self.algo_label.setStyleSheet("font-size: 14px; color: black;")
        self.result_label.setStyleSheet("font-size: 14px; color: black;")
        self.input_line.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: black;
                padding: 8px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            QLineEdit:hover {
                background-color: #E8E8E8;
            }
        """)
        self.result_text.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: black;
                padding: 8px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            QLineEdit:hover {
                background-color: #E8E8E8;
            }
        """)
        self.algo_combo.setStyleSheet("""
            QComboBox {
                background-color: #FFFFFF;
                color: black;
                padding: 8px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #FFFFFF;
                color: black;
                selection-background-color: #DDDDDD;
                border-radius: 5px;
            }
        """)
        self.toggle_button.setStyleSheet("""
            QToolButton {
                background: transparent;
                border: none;
                font-size: 24px;
                color: black;
            }
        """)
        self.hash_button.setStyleSheet("""
            QPushButton {
                background-color: #007ACC;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005F99;
            }
        """)
        self.copy_button.setStyleSheet("""
            QPushButton {
                background-color: #007ACC;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005F99;
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = HashingApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
