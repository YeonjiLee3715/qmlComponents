# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QMetaObject, QReadWriteLock, QGenericArgument, QGenericReturnArgument, QThread, QReadLocker, QWriteLocker
from PyQt5.QtCore import Qt

from python.src.define.ModuleEnum import *
from python.src.module.BaseModule import QBaseModule
from python.src.utils.logger import getLogger

class QModuleManager(QtCore.QObject):
    __instance = None

    __mapIdToPtr = {}
    __mapIdToThread = {}
    __lck = QReadWriteLock()

    def __init__(self, parent=None):
        if not QModuleManager.__instance:
            super().__init__(parent)
        else:
            self.getInstance()

    def init(self) -> bool:
        return True

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, parent=None):
        cls.__instance = cls(parent)
        cls.instance = cls.__getInstance
        return cls.__instance

    def runIndependentModules(self) -> bool:
        for nModuleId, thModule in self.__mapIdToThread.items():
            objModule = self.getModuleById(nModuleId)
            if not objModule or issubclass( objModule.__class__, QBaseModule) == False:
                getLogger().error(f'Module: {nModuleId} is None')
                return False
            thModule.start()

        return True

    def getModuleById(self, nModuleId:int) -> QBaseModule:
        lck = QReadLocker(self.__lck)
        return self.__mapIdToPtr.get(nModuleId, None)

    def getModuleByName(self, strName:str) -> QBaseModule:
        lck = QReadLocker(self.__lck)
        moduleEnum = QModuleEnum()
        nModuleId, isModule = moduleEnum.getIndexFromString(strName)
        if isModule:
            return self.__mapIdToPtr.get(nModuleId, None)
        return None

    def stopIndependentModules(self) -> bool:
        for nModuleId, thModule in self.__mapIdToThread:
            if thModule is not None and thModule.isRunning():
                thModule.quit()
                thModule.wait()

        return True

    def stopIndependentModule(self, nModuleId:int) -> bool:
        thModule = self.__mapIdToThread.get( nModuleId, None )
        if thModule is not None and thModule.isRunning():
            thModule.quit()
            thModule.wait()

        return True

    def getRequest(self, reqCode:int, sender:int, response:bool, reqPacket:dict ):
        if self.m_isSet == False or self.m_isStop:
            return

        functionName = self.getFunctionNameFromReqCode(reqCode)
        if not functionName:
            getLogger().error('Function %s is not registed' % functionName)
            return

        QMetaObject.invokeMethod(self, functionName, QtCore.Qt.DirectConnection
                                  , QtCore.QGenericArgument('int',sender)
                                  , QtCore.QGenericArgument('bool',response)
                                  , QtCore.QGenericArgument('QVariantMap',reqPacket))

    def getResponse( self, resCode:int, sender:int, resPacket:dict ):
        if self.m_isSet == False or self.m_isStop:
            return

        functionName = self.getFunctionNameFromResCode(resCode)
        if not functionName:
            getLogger().error('Function %s is not registed' % functionName )
            return

        QMetaObject.invokeMethod(self, functionName, QtCore.Qt.DirectConnection
                                  , QtCore.QGenericArgument('int',sender)
                                  , QtCore.QGenericArgument('QVariantMap',resPacket))

    def registDependentModule(self, module, nModuleId:int ):
        if not module:
            self._printError(nModuleId, 'is nullptr')
            return False

        self.__lck.lockForRead()
        if nModuleId in self.__mapIdToPtr.keys():
            self._printError(nModuleId, 'is already exist')
            return False
        self.__lck.unlock()

        self.__lck.lockForWrite()
        self.__mapIdToPtr[nModuleId] = module
        self.__lck.unlock()

    def registIndependentModule(self, module, nModuleId:int):
        if not module:
            self._printError(nModuleId, 'is nullptr')
            return False

        self.__lck.lockForRead()
        if nModuleId in self.__mapIdToPtr.keys():
            self._printError(nModuleId, 'is already exist')
            return False
        self.__lck.unlock()

        thModule = QThread()

        module.moveToThread( thModule )
        thModule.started.connect(module.doRun, Qt.QueuedConnection)
        thModule.finished.connect(module.stopModule, Qt.QueuedConnection)

        module.isIndependentModule = True

        self.__lck.lockForWrite()
        self.__mapIdToPtr[nModuleId] = module
        self.__mapIdToThread[nModuleId] = thModule
        self.__lck.unlock()

        return True

    def _printError(self, nModuleId, errorMessage):
        moduleEnum = QModuleEnum()
        getLogger().error('Module: %s (ID: %d) %s' % moduleEnum.getStringFromEnum(nModuleId), nModuleId, errorMessage )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
