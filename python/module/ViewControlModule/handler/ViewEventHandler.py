# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt

from python.src.define.viewDefs import *
from python.src.utils.logger import getLogger

class ViewEventHandler(QtCore.QObject):

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

        if nObjectType != int(ViewEnum.eObjectType.OBJECT_VIEW):
            getLogger().error('This object is not a view. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property(PROP_B_CONNECT_SHOW_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewShowEvent.connect(self.HandleViewShowEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_HIDE_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewHideEvent.connect(self.HandleViewHideEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_OPEN_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewOpenEvent.connect(self.HandleViewOpenEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLOSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewClosedEvent.connect(self.HandleViewClosedEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ACTIVEFOCUS_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewActiveFocusEvent.connect(self.HandleViewActiveFocusEvent, Qt.DirectConnection)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_INACTIVEFOCUS_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewInactiveFocusEvent.connect(self.HandleViewInactiveFocusEvent, Qt.DirectConnection)

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

        if nObjectType != int(ViewEnum.eObjectType.OBJECT_VIEW):
            getLogger().error('This object is not a view. objectType: %d' % nObjectType)
            return

        bEventConnectFlag = obj.property(PROP_B_CONNECT_SHOW_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewShowEvent.disconnect(self.HandleViewShowEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_HIDE_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewHideEvent.disconnect(self.HandleViewHideEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_OPEN_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewOpenEvent.disconnect(self.HandleViewOpenEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_CLOSED_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewClosedEvent.disconnect(self.HandleViewClosedEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_ACTIVEFOCUS_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewActiveFocusEvent.disconnect(self.HandleViewActiveFocusEvent)

        bEventConnectFlag = obj.property(PROP_B_CONNECT_INACTIVEFOCUS_EVENT)
        if bEventConnectFlag != None and bEventConnectFlag == True:
            obj.viewInactiveFocusEvent.disconnect(self.HandleViewInactiveFocusEvent)

        obj.setProperty(PROP_IS_EVENT_CONNECTED, False)

    @QtCore.pyqtSlot()
    def HandleViewShowEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleViewHideEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleViewOpenEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleViewClosedEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleViewActiveFocusEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

    @QtCore.pyqtSlot()
    def HandleViewInactiveFocusEvent(self):
        obj = self.sender()
        if not obj:
            getLogger().error('obj is Null')
            return

        strObjName = obj.objectName()
        getLogger().debug(f'strObjName: {strObjName}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
