# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt

from python.src.define.viewDefs import *
from python.src.utils.logger import getLogger

class TextEditEventHandler(QtCore.QObject):

    def __init__(self, parent=None):
        super().__init__(parent)

    def connectObjectEvent(self, obj:QtCore.QObject):
        if not obj:
            getLogger().error('object is null')

        bConnectEvent = obj.property(PROP_B_CONNECT_EVENT)
        if not bConnectEvent:
            return

        bEventConnected = obj.property(PROP_IS_EVENT_CONNECTED)
        if bEventConnected != None and bEventConnected == True:
            return

        nObjectType = obj.property('objectType')
        if not nObjectType:
            getLogger().error('Object type is null')
            return

        if nObjectType != int(ViewEnum.eObjectType.OBJECT_TEXTEDIT_CONTROL):
            getLogger().error('This object is not a text control. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property( PROP_B_CONNECT_ACCEPTED_EVENT )
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlAcceptedEvent.connect(self.HandleControlAcceptedEvent,Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_EDITING_FINISHED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlEditingFinishedEvent.connect(self.HandleControlEditingFinishedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_TEXT_EDITED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlTextEditedEvent.connect(self.HandleControlTextEditedEvent,Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_FOCUSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlFocusedEvent.connect(self.HandleControlFocusedEvent,Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_FOCUS_OUT_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlFocusOutEvent.connect(self.HandleControlFocusOutEvent,Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ENABLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlEnabledEvent.connect(self.HandleControlEnabledEvent,Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_DISABLED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlDisabledEvent.connect(self.HandleControlDisabledEvent,Qt.DirectConnection)

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

        if nObjectType != int( ViewEnum.eObjectType.OBJECT_TEXTEDIT_CONTROL ):
            getLogger().error('This object is not a text control. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property( PROP_B_CONNECT_ACCEPTED_EVENT )
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlAcceptedEvent.disconnect(self.HandleControlAcceptedEvent())

        bEventConnectFlag = obj.property(PROP_B_CONNECT_EDITING_FINISHED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlEditingFinishedEvent.disconnect(self.HandleControlEditingFinishedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_TEXT_EDITED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.controlTextEditedEvent.disconnect(self.HandleControlTextEditedEvent)

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
    def HandleControlAcceptedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleControlEditingFinishedEvent(self):
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

        text = obj.property('text')
        if not text:
            getLogger().error('text is null')
            return

    @QtCore.pyqtSlot()
    def HandleControlTextEditedEvent(self):
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
