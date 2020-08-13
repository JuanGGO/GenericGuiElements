from PyQt5.QtWidgets import QMainWindow

from .ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _setupUi(self, window):
        self.setupUi(window)

        # region mainwindow slots
        self.toggleDataTreeCommandLinkButton.clicked.connect(self.toggle_data_tree_btn_clicked)

        # endregion

    # region mainwindow slots

    def toggle_data_tree_btn_clicked(self):
        if self.treeViewDockWidget.isHidden():
            self.treeViewDockWidget.setHidden(False)
        else:
            self.treeViewDockWidget.setHidden(True)

    # endregion
