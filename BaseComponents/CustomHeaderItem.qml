import QtQuick 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.4
import ViewEnum 1.0

Item {
    id: headerItem

    property string borderNormalColor: "#75929F"
    property string borderHoverColor: "#668695"
    property string borderFocusColor: "#668695"
    property string borderPressedColor: "#617E8D"
    property string borderDisableColor: "#75929F"

    property string bgNormalColor: "#FFFFFF"
    property string bgHoverColor: "#EAEEF0"
    property string bgFocusColor: "#EAEEF0"
    property string bgPressedColor: "#D3DCE0"
    property string bgDisableColor: "#FFFFFF"

    property string textNormalColor: "#2A2A2A"
    property string textHoverColor: "#2A2A2A"
    property string textFocusColor: "#2A2A2A"
    property string textPressedColor: "#2A2A2A"
    property string textDisableColor: "#ABABAB"

    property real horizontalAlignment: Text.AlignHCenter
    property real verticalAlignment: Text.AlignVCenter
    property real elide: Text.ElideRight

    property real borderWidth: 1

    property int radius: 5

    property string text
    property bool down: _idMouseArea.pressed
    property bool hovered: false

    Rectangle{
        id: _idBackground
        anchors.fill: parent
        border.width: borderWidth
        border.color: {
            if( headerItem.down )
            {
                borderPressedColor
            }
            else
            {
                if( headerItem.focus )
                {
                    borderFocusColor
                }
                else
                {
                    if( headerItem.hovered )
                        borderHoverColor
                    else
                        borderNormalColor
                }
            }
        }
        color: {
            if( headerItem.down )
            {
                bgPressedColor
            }
            else
            {
                if( headerItem.focus )
                {
                    bgFocusColor
                }
                else
                {
                    if( headerItem.hovered )
                        bgHoverColor
                    else
                        bgNormalColor
                }
            }
        }
        radius: headerItem.radius
    }

    Text {
        id: _idText
        anchors.fill: parent
        text: headerItem.text
        font.bold: true
        opacity: enabled ? 1.0 : 0.3
        color: {
            if( headerItem.down )
            {
                textPressedColor
            }
            else
            {
                if( headerItem.hovered )
                {
                    textHoverColor
                }
                else
                {
                    if( headerItem.focus )
                        textFocusColor
                    else
                        textNormalColor
                }
            }
        }
        horizontalAlignment: headerItem.horizontalAlignment
        verticalAlignment: headerItem.verticalAlignment
    }

    MouseArea{
        id: _idMouseArea
        anchors.fill: parent
        hoverEnabled: true
        onEntered: headerItem.hovered = true
        onExited: headerItem.hovered = false
    }
}
