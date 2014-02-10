# -*- coding: UTF-8 -*-

from PySide.QtCore import QRegExp
from PySide.QtGui import QValidator


class UppercaseValidator(QValidator):
    """
        Forces uppercase input
    """

    def __init__(self, parent=None):
        super(UppercaseValidator, self).__init__(parent)

    def validate(self, input, pos):
        input = input.replace(input, input.upper())
        return QValidator.Acceptable, input, pos

class EmailValidator(QValidator):
    """
        Validates an e-mail address
    """

    def __init__(self, parent=None):
        super(EmailValidator, self).__init__(parent)
        self.intermediateRegExp = QRegExp("[a-z0-9._%+-]*@?[a-z0-9.-]*\\.?[a-z]*")
        self.validRegExp = QRegExp("[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}")

    def validate(self, input, pos):
        input = input.replace(input, input.lower())
        if self.validRegExp.exactMatch(input):
            return QValidator.Acceptable, input, pos
        elif self.intermediateRegExp.exactMatch(input):
            return QValidator.Intermediate, input, pos
        else:
            return QValidator.Invalid, input, pos

class AlphaNumericValidator(QValidator):
    """
        Forces alphabetic/numbers input
    """

    def __init__(self, parent=None):
        super(AlphaNumericValidator, self).__init__(parent)
        self.regex = QRegExp("[A-Za-z0-9_]*")

    def validate(self, input, pos):
        if self.regex.exactMatch(input):
            return QValidator.Acceptable, input, pos
        else:
            return QValidator.Invalid