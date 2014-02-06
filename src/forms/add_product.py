# -*- coding: UTF-8 -*-
from PySide.QtGui import QDockWidget
from src.lib.ui.ui_add_product import Ui_Dock


class AddProductDock(QDockWidget, Ui_Dock):
    """ Interface for book input """

    def __init__(self, parent=None):
        super(AddProductDock, self).__init__(parent)
        self.setupUi(self)
        self.visibilityChanged.connect(self.toggle_visibility)

    def clear(self):
        pass

    def toggle_visibility(self, visible):
        actionAddProduct = self.parent().parent().actionAddProduct
        if visible:
            actionAddProduct.setEnabled(False)
        else:
            actionAddProduct.setEnabled(True)

    def closeEvent(self, sender):
        self.toggle_visibility(False)
        grandparent = self.parent().parent()
        grandparent.remove_instance(self)