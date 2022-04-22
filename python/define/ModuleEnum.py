# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, Q_ENUMS, QMetaEnum, QMetaObject
from typing import Tuple

class eModuleRequestCode():
    MDL_REQ_NONE = 0

class eModuleResponseCode():
    MDL_RES_NONE = 0

class eModuleErrorCode():
    MDL_ERROR_NONE = 0

class eModuleResultCode():
    MDL_RESULT_FAILED = 0
    MDL_RESULT_SUCCESSED = 1

class QModuleEnum(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    class eMODULE():
        UNKNOWN = 0
        #MAIN_CLASS = 1

        ALL = 10000

    Q_ENUMS(eMODULE)

    @staticmethod
    def isMainManager(moduleType:eMODULE) -> bool:
        if moduleType == #QModuleEnum.eMODULE.MAIN_CLASS:
            return True
        return False

    def getStringFromEnum(self, moduleType:eMODULE) -> str:
        metaObj = self.metaObject()
        metaEnum = metaObj.enumerator(metaObj.indexOfEnumerator('eMODULE'))
        if not metaEnum:
            return ''
        return metaEnum.valueTokey(moduleType)

    def getIndexFromString(self, strName: str) -> Tuple[int, bool]:
        metaObj = self.metaObject()
        metaEnum = metaObj.enumerator(metaObj.indexOfEnumerator('eMODULE'))
        if not metaEnum:
            return (-1, False)

        return metaEnum.keyToValue(strName)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
