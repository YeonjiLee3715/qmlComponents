# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt

from python.src.define.viewDefs import *
from python.src.utils.logger import getLogger

class WindowEventHandler(QtCore.QObject):

    def __init__(self, parent=None):
        super().__init__(parent)

    def connectObjectEvent(self, obj:QtCore.QObject):
        if not obj:
            getLogger().error('object is null')

        bConnectEvent = obj.property(PROP_B_CONNECT_EVENT)
        if not bConnectEvent:
            return

        nEventConnected = obj.property(PROP_IS_EVENT_CONNECTED)
        if nEventConnected != None and nEventConnected == True:
            return

        nObjectType = obj.property('objectType')
        if not nObjectType:
            getLogger().error('Object type is null')
            return

        if nObjectType != int(ViewEnum.eObjectType.OBJECT_WINDOW):
            getLogger().error('This object is not a window. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property(PROP_B_CONNECT_SHOW_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowShowEvent.connect(self.HandleWindowShowEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_HIDE_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowHideEvent.connect(self.HandleWindowHideEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_OPEN_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowOpenEvent.connect(self.HandleWindowOpenEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLOSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowClosedEvent.connect(self.HandleWindowClosedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ACTIVE_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowActiveEvent.connect(self.HandleWindowActiveEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_INACTIVE_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowInactiveEvent.connect(self.HandleWindowInactiveEvent, Qt.DirectConnection)

        obj.setProperty(PROP_IS_EVENT_CONNECTED, True)

    def disconnectObjectEvent(self, obj:QtCore.QObject):
        if not obj:
            getLogger().error('object is null')

        bConnectEvent = obj.property(PROP_B_CONNECT_EVENT)
        if not bConnectEvent:
            return

        nEventConnected = obj.property(PROP_IS_EVENT_CONNECTED)
        if not nEventConnected:
            return

        nObjectType = obj.property('objectType')
        if not nObjectType:
            getLogger().error('Object type is null')
            return

        if nObjectType != int(ViewEnum.eObjectType.OBJECT_WINDOW):
            getLogger().error('This object is not a window. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property(PROP_B_CONNECT_SHOW_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowShowEvent.disconnect(self.HandleWindowShowEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_HIDE_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowHideEvent.disconnect(self.HandleWindowHideEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_OPEN_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowOpenEvent.disconnect(self.HandleWindowOpenEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLOSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowClosedEvent.disconnect(self.HandleWindowClosedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ACTIVE_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowActiveEvent.disconnect(self.HandleWindowActiveEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_INACTIVE_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.windowInactiveEvent.disconnect(self.HandleWindowInactiveEvent)

        obj.setProperty(PROP_IS_EVENT_CONNECTED, False)

    @QtCore.pyqtSlot()
    def HandleWindowShowEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleWindowHideEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleWindowOpenEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleWindowClosedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleWindowActiveEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleWindowInactiveEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
