import QtQuick 2.9
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.4
import BaseComponents 1.0

BaseCombobox {
    id: control

    property string borderNormalColor: "#75929F"
    property string borderHoverColor: "#668695"
    property string borderOpenedColor: "#668695"
    property string borderPressedColor: "#617E8D"
    property string borderDisableColor: "#75929F"

    property string bgNormalColor: "#FFFFFF"
    property string bgHoverColor: "#EAEEF0"
    property string bgOpenedColor: "#EAEEF0"
    property string bgPressedColor: "#617E8D"
    property string bgDisableColor: "#75929F"

    property string textNormalColor: "#2A2A2A"
    property string textHoverColor: "#2A2A2A"
    property string textOpenedColor: "#2A2A2A"
    property string textPressedColor: "#2A2A2A"
    property string textDisableColor: "#ABABAB"

    property string textContentsColor: "#2A2A2A"

    property real horizontalAlignment: Text.AlignLeft
    property real verticalAlignment: Text.AlignVCenter
    property real elide: Text.ElideRight

    property int radius: 5

    font.bold: true
    font.pointSize: 10

    delegate: ItemDelegate {
        width: control.width
        contentItem: Text {
            text: modelData
            color: textContentsColor
            font: control.font
            elide: Text.ElideRight
            verticalAlignment: Text.AlignVCenter
        }
        highlighted: control.highlightedIndex === index
    }

    contentItem: Text {
        text: control.displayText
        font: control.font
        opacity: enabled ? 1.0 : 0.3
        color: {
            if( control.pressed )
            {
                textPressedColor
            }
            else
            {
                if( control.popup.visible )
                {
                    textOpenedColor
                }
                else
                {
                    if( control.hovered )
                        textHoverColor
                    else
                        textNormalColor
                }
            }
        }
        leftPadding: 15
        horizontalAlignment: control.horizontalAlignment
        verticalAlignment: control.verticalAlignment
        elide: control.elide
    }

    background: Rectangle {
        Layout.fillWidth: true
        Layout.fillHeight: true
        border.color: {
            if( control.pressed )
            {
                borderPressedColor
            }
            else
            {
                if( control.popup.visible )
                {
                    borderOpenedColor
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
        border.width: control.visualFocus ? 2 : 1
        radius: control.radius
        color: {
            if( control.pressed )
            {
                bgPressedColor
            }
            else
            {
                if( control.popup.visible )
                {
                    bgOpenedColor
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
    }
}
