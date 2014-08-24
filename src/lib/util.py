'''
    Some general useful stuff I couldn't really categorize
'''
from PySide.QtCore import Qt, QObject, QEvent, Signal, QBuffer, QByteArray, QIODevice
from PySide.QtGui import QSpinBox, QImage, QCompleter
from src.lib.constants import access_table

import sys
import PySide
sys.modules['PyQt4'] = PySide

def bin(s):
    """ returns a binary number (str format) based on an integer (not really needed on python3) """
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def check_access(access_level, target):
    try:
        bit_representation = bin(access_level)
        bit_target = access_table.index(target) + 1
        return bool(int(bit_representation[-bit_target]))
    except IndexError:
        # undefined permission'
        return False
    except ValueError:
        # target not in permission table (will happen to some stuff I don't want to control)
        return True

def iterate_model(model):
    # returns records associated with a QSqlTableModel or QSqlQueryModel
    record_list = []
    i = 0
    while 1:
        record = model.record(i)
        if record.value(0):
            # valid record
            record_list.append(record)
        else:
            # reached an invalid/empty record
            break
        i += 1
    return record_list

class ReturnKeySpinBox(QSpinBox):
    def __init__(self, parent=None):
        super(ReturnKeySpinBox, self).__init__(parent)
    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            self.focusNextChild()
        else:
            super(ReturnKeySpinBox, self).keyPressEvent(event)

def clickable(widget):
    """ Makes non-clickable widgets clickable
        usage: clickable(widget).connect(slot)
    """
    class Filter(QObject):

        clicked = Signal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True

            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

def qpixmap_to_qbytearray(pix):
    img = pix.toImage()
    ba = QByteArray()
    buffer = QBuffer(ba)
    buffer.open(QIODevice.WriteOnly)
    img.save(buffer, "PNG") # writes image into ba in PNG format
    return ba

def qbytearray_to_qimage(ba):
    img = QImage()
    img.loadFromData(ba, "PNG")
    return img

def config_completer(line_edit, model, field):
    # sets up a completer based on a QSqlTableModel for the specified field on a QLineEdit
    completer = QCompleter()
    completer.setModel(model)
    completer.setCompletionColumn(model.fieldIndex(field))
    completer.setCompletionMode(QCompleter.PopupCompletion)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    completer.activated.connect(line_edit.returnPressed)
    line_edit.setCompleter(completer)