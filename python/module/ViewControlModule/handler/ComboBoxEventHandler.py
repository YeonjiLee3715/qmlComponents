# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt

from python.src.define.viewDefs import *
from python.src.utils.logger import getLogger

class ComboBoxEventHandler(QtCore.QObject):

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

        if nObjectType != int(ViewEnum.eObjectType.OBJECT_COMBOBOX_CONTROL):
            getLogger().error('This object is not a combobox control. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property(PROP_B_CONNECT_PRESSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlPressedEvent.connect(self.HandleControlPressedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_HOVERED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlHoveredEvent.connect(self.HandleControlHoveredEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_FOCUSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlFocusedEvent.connect(self.HandleControlFocusedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_FOCUS_OUT_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlFocusOutEvent.connect(self.HandleControlFocusOutEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ENABLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlEnabledEvent.connect(self.HandleControlEnabledEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DISABLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDisabledEvent.connect(self.HandleControlDisabledEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_OPEN_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlOpenEvent.connect(self.HandleControlOpenEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLOSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlClosedEvent.connect(self.HandleControlClosedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_SELECTED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlSelectedEvent.connect(self.HandleControlSelectedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ACCEPTED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlAcceptedEvent.connect(self.HandleControlAcceptedEvent, Qt.DirectConnection)

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

        if nObjectType != int( ViewEnum.eObjectType.OBJECT_COMBOBOX_CONTROL ):
            getLogger().error('This object is not a combobox control. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property( PROP_B_CONNECT_PRESSED_EVENT )
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlPressedEvent.disconnect(self.HandleControlPressedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_HOVERED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlHoveredEvent.disconnect(self.HandleControlHoveredEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_FOCUSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlFocusedEvent.disconnect(self.HandleControlFocusedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_FOCUS_OUT_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlFocusOutEvent.disconnect(self.HandleControlFocusOutEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ENABLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlEnabledEvent.disconnect(self.HandleControlEnabledEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DISABLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDisabledEvent.disconnect(self.HandleControlDisabledEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_OPEN_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlOpenEvent.disconnect(self.HandleControlOpenEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLOSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlClosedEvent.disconnect(self.HandleControlClosedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_SELECTED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlSelectedEvent.disconnect(self.HandleControlSelectedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ACCEPTED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlAcceptedEvent.disconnect(self.HandleControlAcceptedEvent)

        obj.setProperty(PROP_IS_EVENT_CONNECTED, False)

    @QtCore.pyqtSlot(bool)
    def HandleControlPressedEvent(self, bPressed):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(bool)
    def HandleControlHoveredEvent(self, bHovered):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlFocusedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlFocusOutEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlEnabledEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlDisabledEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlOpenEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlClosedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int)
    def HandleControlSelectedEvent(self, idx):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlAccepted(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
