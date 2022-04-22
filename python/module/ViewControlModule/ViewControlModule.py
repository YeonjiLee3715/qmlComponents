# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore, QtGui, QtQml, QtQuick
from PyQt5.QtCore import QObject, QUrl, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.Qt import QMetaObject, Q_ARG, Q_RETURN_ARG

from python.res import rc_qml
from python.src.module.BaseModule import QBaseModule
from python.src.utils.logger import getLogger

from python.src.define.viewDefs import *
from .handler.WindowEventHandler import WindowEventHandler
from .handler.ViewEventHandler import ViewEventHandler
from .handler.ListEventHandler import ListEventHandler
from .handler.ButtonEventHandler import ButtonEventHandler
from .handler.ComboBoxEventHandler import ComboBoxEventHandler
from .handler.DialogEventHandler import DialogEventHandler
from .handler.TextEditEventHandler import TextEditEventHandler

class ViewControlModule(QBaseModule):
    _strModultName = 'ViewControlModule'
    __engine = None

    __hWindowEvent = None
    __hViewEvent = None
    __hLstEvent = None
    __hBtnCtlEvent = None
    __hCbxCtlEvent = None
    __hDlgEvent = None
    __hEdtCtlEvent = None

    def __init__(self, parent=None):
        super().__init__(parent)

    def init(self) -> None:
        if self.__initQmlEngine() == False:
            getLogger().error("Failed to init QML Engine")
            return

        if not self.__hWindowEvent:
            self.__hWindowEvent = WindowEventHandler()
        if not self.__hViewEvent:
            self.__hViewEvent = ViewEventHandler()
        if not self.__hLstEvent:
            self.__hLstEvent = ListEventHandler()
        if not self.__hBtnCtlEvent:
            self.__hBtnCtlEvent = ButtonEventHandler()
        if not self.__hCbxCtlEvent:
            self.__hCbxCtlEvent = ComboBoxEventHandler()
        if not self.__hDlgEvent:
            self.__hDlgEvent = DialogEventHandler()
        if not self.__hEdtCtlEvent:
            self.__hEdtCtlEvent = TextEditEventHandler()

        self.SetControlEventConnections()

        super().init()

    @QtCore.pyqtSlot()
    def doRun(self) -> None:
        pass

    @QtCore.pyqtSlot()
    def stopModule(self) -> None:
        self.SetControlEventDisconnections()

        if self.__engine:
            self.__engine.exit(0)
            self.__engine.deleteLater()
            self.__engine = None

        super().stopModule()
        self.__clear()

    def __initQmlEngine(self) -> bool:
        if not self.__engine:
            self.__engine = QQmlApplicationEngine()

            self.__engine.addImportPath('qrc:/')
            self.__engine.addImportPath('qrc:///BaseComponents')
            self.__engine.addImportPath('qrc:///components')

            qmlRegisterType(ViewEnum, 'ViewEnum', 1, 0, 'ViewEnum')
            self.__engine.load('qrc:/main.qml')
            if len(self.__engine.rootObjects()) <= 0:
                getLogger().error('Failed to init engine')
                return False

        return True

    def __clear(self) -> None:
        pass

    def SetControlEventConnections(self):
        objRoot = self.GetRootControlObject()
        if not objRoot:
            getLogger().error('Root object is None')
            return

        nEventConnected = objRoot.property(PROP_IS_EVENT_CONNECTED)
        if not nEventConnected:
            objRoot.sigNewControlLoaded.connect(self.HandleNewControlLoadedEvent, Qt.DirectConnection)
            objRoot.sigDestroyControlLoaded.connect(self.HandleDestroyControlLoadedEvent, Qt.DirectConnection)
            objRoot.sigAppModeChanged.connect(self.HandleAppModeChangedEvent, Qt.DirectConnection)

            appMode = objRoot.property(PROP_N_APP_MODE)
            if appMode != None:
                self.HandleAppModeChangedEvent(appMode)

            objRoot.setProperty(PROP_IS_EVENT_CONNECTED, True)

        self.SetControlEventConnection(objRoot, True)

    def SetControlEventConnection(self, obj, bRecursive):
        if not obj:
            getLogger().error('Object is null')
            return

        if bRecursive:
            self.SetControlEventConnectionRecursive(obj)
        else:
            self.connectObjectEvent(obj)

    def connectObjectEvent(self, obj):
        if not obj:
            getLogger().error('Object is null')
            return

        bConnectEvent = obj.property(PROP_B_CONNECT_EVENT)
        if not bConnectEvent:
            return

        nObjectType = obj.property('objectType')
        if not nObjectType:
            getLogger().error('Object type is null')
            return

        if nObjectType == ViewEnum.eObjectType.OBJECT_WINDOW:
            self.__hWindowEvent.connectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_VIEW:
            self.__hViewEvent.connectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_DIALOG:
            self.__hDlgEvent.connectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_BUTTON_CONTROL:
            self.__hBtnCtlEvent.connectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_COMBOBOX_CONTROL:
            self.__hCbxCtlEvent.connectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_TEXTEDIT_CONTROL:
            self.__hEdtCtlEvent.connectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_LIST_VIEW:
            self.__hLstEvent.connectObjectEvent(obj)
        else: # nObjectType == ViewEnum::OBJECT_NONE or unknown
            getLogger().error('Unknown objectType: %d', nObjectType)

    def SetControlEventDisconnections(self):
        objRoot = self.GetRootControlObject()
        if not objRoot:
            getLogger().error('Root object is None')
            return

        nEventConnected = objRoot.property(PROP_IS_EVENT_CONNECTED)
        if nEventConnected != None and nEventConnected == True:
            objRoot.newControlLoaded.disconnect(self.HandleNewControlLoadedEvent)
            objRoot.destroyControlLoaded.disconnect(self.HandleDestroyControlLoadedEvent)
            objRoot.setProperty(PROP_IS_EVENT_CONNECTED, False)

        self.SetControlEventDisconnection(objRoot, True)

    def SetControlEventDisconnection(self, obj, bRecursive):
        if not obj:
            getLogger().error('Object is null')
            return

        if bRecursive:
            self.SetControlEventDisconnectionRecursive(obj)
        else:
            self.disconnectObjectEvent(obj)

    def disconnectObjectEvent(self, obj):
        if not obj:
            getLogger().error('Object is null')
            return

        bConnectEvent = obj.property(PROP_B_CONNECT_EVENT)
        if not bConnectEvent:
            return

        nObjectType = obj.property('objectType')
        if not nObjectType:
            getLogger().error('Object type is null')
            return

        if nObjectType == ViewEnum.eObjectType.OBJECT_WINDOW:
            self.__hWindowEvent.disconnectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_VIEW:
            self.__hViewEvent.disconnectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_DIALOG:
            self.__hDlgEvent.disconnectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_BUTTON_CONTROL:
            self.__hBtnCtlEvent.disconnectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_COMBOBOX_CONTROL:
            self.__hCbxCtlEvent.disconnectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_TEXTEDIT_CONTROL:
            self.__hEdtCtlEvent.disconnectObjectEvent(obj)
        elif nObjectType == ViewEnum.eObjectType.OBJECT_LIST_VIEW:
            self.__hLstEvent.disconnectObjectEvent(obj)
        else: # nObjectType == ViewEnum::OBJECT_NONE or unknown
            getLogger().error('Unknown objectType: %d', nObjectType)

    def GetRootControlObject(self) -> QObject:
        objRoot = None

        if self.__engine == None:
            return objRoot

        lstRootObject = self.__engine.rootObjects()
        if len(lstRootObject) == 0:
            return objRoot

        for obj in lstRootObject:
            if obj != None:
                if obj.objectName() == ID_idRootWindow:
                    objRoot = obj
                    break

        return objRoot

    def FindChildObject(self, objectName:str, parent = None):
        if not objectName:
            return None

        if not parent:
            parent = self.GetRootControlObject()

        if not parent:
            return None

        if objectName == parent.objectName():
            return parent

        return parent.findChild(QtCore.QObject, objectName)

    def SetControlEventConnectionRecursive(self, obj):
        if not obj:
            getLogger().error('Object is null')
            return

        self.connectObjectEvent(obj)

        lstObjChild = obj.children()
        if len(lstObjChild) == 0:
            return

        for objChild in lstObjChild:
            if not objChild:
                continue

            self.SetControlEventConnectionRecursive(objChild)

    def SetControlEventDisconnectionRecursive(self, obj):
        if not obj:
            getLogger().error('Object is null')
            return

        self.disconnectObjectEvent(obj);

        lstObjChild = obj.children()
        if len(lstObjChild) == 0:
            return

        for objChild in lstObjChild:
            if not objChild:
                continue

            self.SetControlEventDisconnectionRecursive(objChild)

    @QtCore.pyqtSlot(str)
    def HandleNewControlLoadedEvent(self, objName:str):
        newObj = self.FindChildObject( objName )
        if not newObj:
            getLogger().error('Failed to get object: ', objName)
            return

        self.SetControlEventConnection(newObj, True)

    @QtCore.pyqtSlot(str)
    def HandleDestroyControlLoadedEvent(self, objName:str):
        newObj = self.FindChildObject( objName )
        if not newObj:
            getLogger().error('Failed to get object: ', objName)
            return

        self.SetControlEventDisconnection(newObj, True)

    @property
    def hWindowEvent(self):
        return self.__hWindowEvent

    @property
    def hViewEvent(self):
        return self.__hViewEvent

    @property
    def hLstEvent(self):
        return self.__hLstEvent

    @property
    def hBtnCtlEvent(self):
        return self.__hBtnCtlEvent

    @property
    def hCbxCtlEvent(self):
        return self.__hCbxCtlEvent

    @property
    def hDlgEvent(self):
        return self.__hDlgEvent

    @property
    def hEdtCtlEvent(self):
        return self.__hEdtCtlEvent

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
