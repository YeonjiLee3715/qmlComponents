# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt

from python.src.define.viewDefs import *
from python.src.utils.logger import getLogger

class ListEventHandler(QtCore.QObject):

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

        if nObjectType != int(ViewEnum.eObjectType.OBJECT_LIST_VIEW):
            getLogger().error('This object is not a list control. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLICKED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlClickedEvent.connect(self.HandleControlClickedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DOUBLE_CLICKED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDoubleClickedEvent.connect(self.HandleControlDoubleClickedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ENTERED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlEnteredEvent.connect(self.HandleControlEnteredEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_EXITED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlExitedEvent.connect(self.HandleControlExitedEvent, Qt.DirectConnection)

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

        bEventConnectFlag = obj.property(PROP_B_CONNECT_WHEEL_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlWheelEvent.connect(self.HandleControlWheelEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_HOVERED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlHoveredEvent.connect(self.HandleControlHoveredEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_FOCUSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlFocusedEvent.connect(self.HandleControlFocusedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_FOCUS_OUT_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlFocusOutEvent.connect(self.HandleControlFocusOutEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_OPEN_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlOpenEvent.connect(self.HandleControlOpenEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLOSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlClosedEvent.connect(self.HandleControlClosedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DRAG_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDragEvent.connect(self.HandleControlDragEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ENABLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlEnabledEvent.connect(self.HandleControlEnabledEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DISABLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDisabledEvent.connect(self.HandleControlDisabledEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_SELECTED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlSelectedEvent.connect(self.HandleControlSelectedEvent, Qt.DirectConnection)

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

        if nObjectType != int( ViewEnum.eObjectType.OBJECT_LIST_VIEW ):
            getLogger().error('This object is not a list control. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property( PROP_B_CONNECT_CLICKED_EVENT )
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlClickedEvent.disconnect(self.HandleControlClickedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DOUBLE_CLICKED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDoubleClickedEvent.disconnect(self.HandleControlDoubleClickedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ENTERED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlEnteredEvent.disconnect(self.HandleControlEnteredEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_EXITED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlExitedEvent.disconnect(self.HandleControlExitedEvent)

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

        bEventConnectFlag = obj.property(PROP_B_CONNECT_WHEEL_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlWheelEvent.disconnect(self.HandleControlWheelEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_HOVERED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlHoveredEvent.disconnect(self.HandleControlHoveredEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_FOCUSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlFocusedEvent.disconnect(self.HandleControlFocusedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_FOCUS_OUT_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlFocusOutEvent.disconnect(self.HandleControlFocusOutEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_OPEN_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlOpenEvent.disconnect(self.HandleControlOpenEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLOSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlClosedEvent.disconnect(self.HandleControlClosedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DRAG_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDragEvent.disconnect(self.HandleControlDragEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ENABLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlEnabledEvent.disconnect(self.HandleControlEnabledEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DISABLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDisabledEvent.disconnect(self.HandleControlDisabledEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_SELECTED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlSelectedEvent.disconnect(self.HandleControlSelectedEvent)

        obj.setProperty(PROP_IS_EVENT_CONNECTED, False)

    @QtCore.pyqtSlot(int, int)
    def HandleControlClickedEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlDoubleClickedEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlEnteredEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlExitedEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlPressAndHoldEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlPressedEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlReleasedEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlCanceledEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int, int, int)
    def HandleControlWheelEvent(self, row, col, x, y):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlHoveredEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlFocusedEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlFocusOutEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlOpenEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlClosedEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int, int ,int)
    def HandleControlDragEvent(self, row, col, x, y):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlEnabledEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlDisabledEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot(int, int)
    def HandleControlSelectedEvent(self, row, col):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
