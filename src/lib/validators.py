# -*- coding: UTF-8 -*-

from PySide.QtGui import QValidator

class UppercaseValidator(QValidator):
    """
        Forces uppercase upon a line edit
    """

    def __init__(self, parent=None):
        super(UppercaseValidator, self).__init__(parent)

    def validate(self, input, pos):
        input = input.replace(input, input.upper())
        return QValidator.Acceptable, input, pos

