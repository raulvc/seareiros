# -*- coding: UTF-8 -*-
from PySide.QtGui import QDialog, QMovie, QIcon
from src.lib.ui.ui_loading import Ui_Dialog


class Loading(QDialog, Ui_Dialog):
    """Loading dialog utility"""

    def __init__(self, parent=None):
        super(Loading, self).__init__(parent)
        self.setupUi(self)
        # setting min and max to 0 turns the progressbar into a 'busy' state, before setting it up
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self._load_icon = QMovie(":icons/loading.gif")
        self._load_icon.frameChanged.connect(self._set_loading_icon)
        self._load_icon.start()

    def setMaxRows(self, rowCount):
        self.progressBar.setMaximum(rowCount)

    def clear(self):
        self.progressBar.reset()

    def incrementReadRows(self):
        current_row = self.progressBar.value()
        self.progressBar.setValue(current_row + 1)

    def setMessage(self, message):
        self.label.setText(message)

    def _set_loading_icon(self, frame=None):
        self.loadingButton.setIcon(QIcon(self._load_icon.currentPixmap()))

    def closeEvent(self, event):
        # prevents window manager from closing it
        event.ignore()