# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QModelIndex

from python.src.utils.logger import getLogger

class BaseListItemModel(QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def FindByRoleItem(self, role, value, column=0):
        matchItem = None

        if not value:
            getLogger().error(f'Wrong value role: {role}')
            return matchItem

        maxRow = self.rowCount()
        for idx in range(0, maxRow):
            item = self.item(idx, column)
            itemData = item.data(role)
            if type(value) == type(itemData) \
                    and value == itemData:
                matchItem = item
                break

        return matchItem

    def SetListItems(self, lstItems)->bool:
        isSuccess = False
        if self.rowCount() > 0:
            self.removeRows(0, self.rowCount(), QModelIndex())

        if lstItems and len(lstItems) > 0:
            for lstColumnItems in lstItems:
                if lstColumnItems and len(lstColumnItems) > 0:
                    self.appendRow(lstColumnItems)
            isSuccess = True

        return isSuccess

    def ResetModel(self):
        self.beginResetModel()
        self.endResetModel()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/