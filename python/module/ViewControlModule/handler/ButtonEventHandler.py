# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt

from python.src.define.viewDefs import *
from python.src.utils.logger import getLogger

class ButtonEventHandler(QtCore.QObject):
    sigSrcRefresh = pyqtSignal()
    sigDstRefresh = pyqtSignal()

    sigConvert = pyqtSignal()
    sigReset = pyqtSignal()

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

        if nObjectType != int(ViewEnum.eObjectType.OBJECT_BUTTON_CONTROL):
            getLogger().error('This object is not a button control. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLICKED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlClickedEvent.connect(self.HandleControlClickedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DOUBLE_CLICKED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDoubleClickedEvent.connect(self.HandleControlDoubleClickedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_PRESS_AND_HOLD_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlPressAndHoldEvent.connect(self.HandleControlPressAndHoldEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_PRESSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlPressedEvent.connect(self.HandleControlPressedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_RELEASED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlReleasedEvent.connect(self.HandleControlReleasedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CANCELED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlCanceledEvent.connect(self.HandleControlCanceledEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_TOGGLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlToggledEvent.connect(self.HandleControlToggledEvent, Qt.DirectConnection)

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

        if nObjectType != int(ViewEnum.eObjectType.OBJECT_BUTTON_CONTROL):
            getLogger().error('This object is not a button control. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLICKED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlClickedEvent.disconnect(self.HandleControlClickedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DOUBLE_CLICKED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDoubleClickedEvent.disconnect(self.HandleControlDoubleClickedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_PRESS_AND_HOLD_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlPressAndHoldEvent.disconnect(self.HandleControlPressAndHoldEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_PRESSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlPressedEvent.disconnect(self.HandleControlPressedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_RELEASED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlReleasedEvent.disconnect(self.HandleControlReleasedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CANCELED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlCanceledEvent.disconnect(self.HandleControlCanceledEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_TOGGLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlToggledEvent.disconnect(self.HandleControlToggledEvent)

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

        obj.setProperty(PROP_IS_EVENT_CONNECTED, False)

    @QtCore.pyqtSlot()
    def HandleControlClickedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlDoubleClickedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlPressAndHoldEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlPressedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlReleasedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

        nObjectId = obj.property('objectId')
        if not nObjectId:
            getLogger().error('Object id is null')
            return

    @QtCore.pyqtSlot()
    def HandleControlCanceledEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlToggledEvent(self):
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
