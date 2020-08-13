from PyQt5.QtWidgets import QTreeWidget, QAction, QFileDialog
from PyQt5.QtCore import pyqtSignal

from .data_tree import DataTreeWidgetItem


class DataTreeWidget(QTreeWidget):

    # signals
    add_item_to_tree_from_file_signal = pyqtSignal(str, object)  # filename, tree object
    item_added_to_tree_signal = pyqtSignal(object)
    item_deleted_from_tree_signal = pyqtSignal(object)
    item_hidden_from_tree_signal = pyqtSignal(object)

    def __init__(self, parent=None):
        super(DataTreeWidget, self).__init__(parent)
        self.items = {}

    def add_child_from_file(self, item_placeholder: DataTreeWidgetItem, extensions: str) -> DataTreeWidgetItem:
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", filter=extensions)
        if filename != '':
            item_name = filename
            item_placeholder.name = item_name
            if not item_placeholder._type in self.items.keys():
                self.items[item_placeholder._type] = {}
            self.items[item_placeholder._type][item_placeholder.id] = item_placeholder
            self.add_item_to_tree_from_file_signal(filename, item_placeholder)
        else:
            return

    def add_child_from_instance(self, item: DataTreeWidgetItem):
        if not item._type in self.items.keys():
            self.items[item._type] = {}
        self.items[item._type][item.id] = item
        self.item_added_to_tree_signal.emit(item)



