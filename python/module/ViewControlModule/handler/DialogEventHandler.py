# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt

from python.src.define.viewDefs import *
from python.src.utils.logger import getLogger

class DialogEventHandler(QtCore.QObject):

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

        if nObjectType != int(ViewEnum.eObjectType.OBJECT_DIALOG):
            getLogger().error('This object is not a dialog. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property(PROP_B_CONNECT_SHOW_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.dialogShowEvent.connect(self.HandleDialogShowEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_HIDE_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.dialogHideEvent.connect(self.HandleDialogHideEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_OPEN_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.dialogOpenEvent.connect(self.HandleDialogOpenEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ACCEPTED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.dialogAcceptedEvent.connect(self.HandleDialogAcceptedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_REJECTED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.dialogRejectedEvent.connect(self.HandleDialogRejectedEvent, Qt.DirectConnection)

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

        if nObjectType != int( ViewEnum.eObjectType.OBJECT_DIALOG ):
            getLogger().error('This object is not a dialog. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property( PROP_B_CONNECT_SHOW_EVENT )
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.dialogShowEvent.disconnect(self.HandleDialogShowEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_HIDE_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.dialogHideEvent.disconnect(self.HandleDialogHideEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_OPEN_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.dialogOpenEvent.disconnect(self.HandleDialogOpenEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ACCEPTED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.dialogAcceptedEvent.disconnect(self.HandleDialogAcceptedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_REJECTED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.dialogRejectedEvent.disconnect(self.HandleDialogRejectedEvent)

        obj.setProperty(PROP_IS_EVENT_CONNECTED, False)

    @QtCore.pyqtSlot()
    def HandleDialogShowEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleDialogHideEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleDialogOpenEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleAcceptedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleRejectedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
