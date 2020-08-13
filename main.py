import sys
from PyQt5.QtWidgets import QApplication

from Uis.MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window._setupUi(window)
    window.show()
    sys.exit(app.exec_())
