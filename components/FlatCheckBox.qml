import QtQuick 2.8
import QtQuick.Templates 2.1 as T
import ViewEnum 1.0

T.CheckBox {
    id: control

    property int objectType: ViewEnum.OBJECT_COMBOBOX_CONTROL
    property int objectId: 0
    property bool bConnectEvent: false

    property string borderNormalColor: "#75929F"
    property string borderHoverColor: "#668695"
    property string borderFocusColor: "#668695"
    property string borderPressedColor: "#617E8D"
    property string borderDisableColor: "#75929F"

    property string bgNormalColor: "#FFFFFF"
    property string bgHoverColor: "#EAEEF0"
    property string bgFocusColor: "#EAEEF0"
    property string bgPressedColor: "#617E8D"
    property string bgDisableColor: "#75929F"

    property string textNormalColor: "#2A2A2A"
    property string textHoverColor: "#2A2A2A"
    property string textFocusColor: "#2A2A2A"
    property string textPressedColor: "#2A2A2A"
    property string textDisableColor: "#ABABAB"

    property var horizontalIndicatorAlignment: control.left
    property var verticalIndicatorAlignment: control.verticalCenter

    property real horizontalAlignment: Text.AlignLeft
    property real verticalAlignment: Text.AlignVCenter
    property real elide: Text.ElideRight

    property int radius: 2

    property real indicatorimplicitWidth: 16
    property real indicatorimplicitHeight: 16

    property real contentItemMargin: 0

    property bool bReadOnly: false

    indicator: Rectangle {
            anchors.horizontalCenter: horizontalIndicatorAlignment
            anchors.verticalCenter: verticalIndicatorAlignment
            implicitWidth: control.indicatorimplicitWidth
            implicitHeight: control.indicatorimplicitHeight
            border.width: 1
            border.color: {
                if( control.down )
                {
                    borderPressedColor
                }
                else
                {
                    if( control.focus )
                    {
                        borderFocusColor
                    }
                    else
                    {
                        if( control.hovered )
                            borderHoverColor
                        else
                            borderNormalColor
                    }
                }
            }
            radius: control.radius
            color: {
                if( control.down )
                {
                    bgPressedColor
                }
                else
                {
                    if( control.focus )
                    {
                        bgFocusColor
                    }
                    else
                    {
                        if( control.hovered )
                            bgHoverColor
                        else
                            bgNormalColor
                    }
                }
            }

            Rectangle {
                anchors.fill: parent
                visible: control.checked
                border.width: 0
                radius: control.radius
                color: bgPressedColor
                anchors.margins: 4
            }
    }
    text: ""
    contentItem: Text {
        anchors.verticalCenter: control.verticalCenter
        leftPadding: control.indicatorimplicitWidth + control.contentItemMargin
        text: control.text
        font: control.font
        opacity: enabled ? 1.0 : 0.3
        color: {
            if( control.down )
            {
                textPressedColor
            }
            else
            {
                if( control.hovered )
                {
                    textHoverColor
                }
                else
                {
                    if( control.focus )
                        textFocusColor
                    else
                        textNormalColor
                }
            }
        }
        horizontalAlignment: control.horizontalAlignment
        verticalAlignment: control.verticalAlignment
        elide: control.elide
    }

    onBReadOnlyChanged: {
        if( bReadOnly )
        {
            focusPolicy = Qt.NoFocus
            _idLdrBlocker.sourceComponent = _idCmpBlocker
        }
        else
        {
            focusPolicy = Qt.WheelFocus
            _idLdrBlocker.sourceComponent = null
        }
    }

    Loader{
        id: _idLdrBlocker
        anchors.fill: parent
    }

    Component{
        id: _idCmpBlocker
        MouseArea {
            anchors.fill: parent
            hoverEnabled: false
            onClicked: {}
            onReleased: {}
            onEntered: {}
            onExited: {}
            onWheel: {}
            onHoveredChanged: {}
        }
    }
}
