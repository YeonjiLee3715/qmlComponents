import QtQuick 2.9
import QtQuick.Dialogs 1.3
import ViewEnum 1.0

FileDialog{
    property int objectType: ViewEnum.OBJECT_DIALOG
    property int objectId: 0
    property int dialogType: ViewEnum.DIALOG_FILE_DIALOG
    property bool bConnectEvent: false

    property bool bConnectShowEvent: false
    property bool bConnectHideEvent: false
    property bool bConnectOpenEvent: false
    property bool bConnectAcceptedEvent: false
    property bool bConnectRejectedEvent: false

    signal dialogShowEvent()
    signal dialogHideEvent()
    signal dialogOpenEvent()
    signal dialogAcceptedEvent()
    signal dialogRejectedEvent()

    selectExisting: true
    folder: shortcuts.home

    onVisibleChanged: {
        if( visible )
        {
            if(bConnectShowEvent)
                dialogShowEvent()
        }
        else
        {
            if(bConnectHideEvent)
                dialogHideEvent()
        }
    }

    Component.onCompleted: {
        if(bConnectOpenEvent)
            dialogOpenEvent()
    }

    onAccepted: {

        if(bConnectAcceptedEvent)
            dialogAcceptedEvent()
    }

    onRejected: {

        if(bConnectRejectedEvent)
            dialogRejectedEvent()
    }
}
