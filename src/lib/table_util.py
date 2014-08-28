from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem, QSortFilterProxyModel
from src.lib import constants
from src.lib.constants import days_of_the_week


class WeekdayTableWidgetItem(QTableWidgetItem):
    """ Overloading TableWidgetItem for custom sorting weekdays """
    def __lt__(self, other):
        if ( isinstance(other, QTableWidgetItem) ):
            left_value = constants.days_of_the_week.index(self.data(Qt.EditRole))
            right_value = constants.days_of_the_week.index(other.data(Qt.EditRole))

            return left_value < right_value
        return super(WeekdayTableWidgetItem, self).__lt__(other)

class CustomSortFilterProxyModel(QSortFilterProxyModel):
    """ I'm overriding the default sorting to make it less stupid on numbers and allow weekday sorting """
    def lessThan(self, left_index, right_index):
        left_var = left_index.data(Qt.DisplayRole)
        right_var = right_index.data(Qt.DisplayRole)

        # numeric values
        try:
            return float(left_var) < float(right_var)
        except (ValueError, TypeError):
            pass

        # weekdays
        try:
            return days_of_the_week.index(left_var) < days_of_the_week.index(right_var)
        except:
            pass

        return left_var < right_var

    def set_filter_columns(self, key_list):
        """ turns out the overhead of filtering all columns is impossible to handle so I had to select a few """
        self._key_columns = key_list

    def filterAcceptsRow(self, row_num, parent):
        """ implements multiple column search """
        for col in self._key_columns:
            index = self.sourceModel().index(row_num, col, parent)
            regexp = self.filterRegExp()
            # trying to match regexp, -1 means not found
            txt = unicode(index.data())
            if regexp.indexIn(txt) != -1:
                return True
        return False
