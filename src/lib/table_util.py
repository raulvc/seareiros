from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem
from src.lib import constants

class WeekdayTableWidgetItem(QTableWidgetItem):
    """ Overloading TableWidgetItem for custom sorting weekdays """
    def __lt__(self, other):
        if ( isinstance(other, QTableWidgetItem) ):
            left_value = constants.days_of_the_week.index(self.data(Qt.EditRole))
            right_value = constants.days_of_the_week.index(other.data(Qt.EditRole))

            return left_value < right_value
        return super(WeekdayTableWidgetItem, self).__lt__(other)