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

class NumericValidator(QValidator):
    """
        Forces numbers on input (where I can't use an QIntegerValidator due to maxlength)
    """

    def __init__(self, parent=None):
        super(NumericValidator, self).__init__(parent)
        self.regex = QRegExp("[0-9_]*")

    def validate(self, input, pos):
        if self.regex.exactMatch(input):
            return QValidator.Acceptable, input, pos
        else:
            return QValidator.Invalid

class CurrencyValidator(QValidator):
    # Workaround for PySide's bugs
    # see http://stackoverflow.com/questions/16067893/how-does-qvalidator-fixup-works-in-pyside
    def __init__(self, parent):
        super(CurrencyValidator, self).__init__(parent)
        self.regex = QRegExp("[0-9]{1,4}[,][0-9]{2}")
        self.inter_regex = QRegExp("^(?:[\d-]{0,4},?[\d-]{0,2})$")
        self.zeroes_regex = QRegExp("[0]+")
        self.line_edit = parent

    def validate(self, input, pos):
        if self.regex.exactMatch(input):
            input = input.replace(input, self.remove_zeroes(input))
            return QValidator.Acceptable, input, pos
        elif self.inter_regex.exactMatch(input):
            return QValidator.Intermediate
        else:
            return QValidator.Invalid

    def remove_zeroes(self, txt):
        # removes leading zeros
        if len(txt.split(',')[0]) > 1:
            # remove leading zeroes
            if self.zeroes_regex.exactMatch(txt.split(',')[0]):
                # all leading numbers are zeroes
                return '0' + txt.lstrip('0')
            else:
                return txt.lstrip('0')
        else:
            return txt

    def fixup(self, input):
        if input == '':
            input = input.replace(input, '0,00')
        else:
            temp = input.split(',')
            if temp[-1] == '':
                # input ends with ','
                input = input.replace(input, input + '00')
            if temp[0] == '':
                # input starts with ','
                input = input.replace(input, '0' + input)
            if len(input.split(',')) == 1:
                # no decimal separator
                input = input.replace(input, input + ',00')
            elif len(input.split(',')[1]) < 2:
                # only 1 decimal
                input = input.replace(input, input + '0')
            input = input.replace(input, self.remove_zeroes(input))
        self.line_edit.setText(input)
        self.line_edit.focusNextChild()