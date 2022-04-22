# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QMetaObject, QGenericArgument, QGenericReturnArgument
from typing import Dict

from python.src.utils.logger import getLogger

class QBaseModule(QtCore.QObject):
    _strModultName = ''

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__isSet = False
        self.__isStop = False
        self.__isIndependentModule = False
        self.__mapReqCodeToFuncName = Dict[int, str]
        self.__mapResCodeToFuncName = Dict[int, str]

    def init(self) -> None:
        self.__isSet = True

    @QtCore.pyqtSlot()
    def doRun(self) -> None:
        pass

    @classmethod
    def getModuleName(cls) -> str:
        return cls._strModultName

    @property
    def isSet(self) -> bool:
        return self.__isSet

    @isSet.setter
    def isSet(self, isSet) -> None:
        self.__isSet = isSet

    @property
    def isStop(self) -> bool:
        return self.__isStop

    @isStop.setter
    def isStop(self, isStop) -> None:
        self.__isStop = isStop

    @property
    def isIndependentModule(self) -> bool:
        return self.__isIndependentModule

    @isIndependentModule.setter
    def isIndependentModule(self, isIndependentModule) -> None:
        self.__isIndependentModule = isIndependentModule

    @QtCore.pyqtSlot()
    def stopModule(self) -> None:
        self.__isStop = True
        self.__isSet = False

    def getFunctionNameFromReqCode(self, reqCode:int) -> str:
        return self.__mapReqCodeToFuncName.get(reqCode, '')

    def getFunctionNameFromResCode(self, resCode:int) -> str:
        return self.__mapResCodeToFuncName.get(resCode, '')

    @QtCore.pyqtSlot(int, int, bool, dict)
    def getRequest(self, reqCode:int, sender:int, response:bool, reqPacket:dict ) -> None:
        if self.__isSet == False or self.__isStop:
            return

        functionName = self.getFunctionNameFromReqCode(reqCode)
        if not functionName:
            getLogger().error( "Function %s is not registed" % functionName )
            return

        QMetaObject.invokeMethod(self, functionName, QtCore.Qt.DirectConnection
                                  , QtCore.QGenericArgument('int',sender)
                                  , QtCore.QGenericArgument('bool',response)
                                  , QtCore.QGenericArgument('QVariantMap',reqPacket))

    @QtCore.pyqtSlot(int, int, dict)
    def getResponse( self, resCode:int, sender:int, resPacket:dict ) -> None:
        if self.__isSet == False or self.__isStop:
            return

        functionName = self.getFunctionNameFromResCode(resCode)
        if not functionName:
            getLogger().error( "Function %s is not registed" % functionName )
            return

        QMetaObject.invokeMethod(self, functionName, QtCore.Qt.DirectConnection
                                  , QtCore.QGenericArgument('int',sender)
                                  , QtCore.QGenericArgument('QVariantMap',resPacket))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
