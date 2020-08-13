from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget

from uuid import uuid4


class DataTreeWidgetItem(QTreeWidgetItem):
    """
    Each subclass must have the attribute _type that
    matches it's parent type
    """

    def __init__(self, widget_name):
        super(DataTreeWidgetItem, self).__init__([widget_name])
        self.id = uuid4().hex
        self.name = widget_name
        self._type = None





