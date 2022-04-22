import QtQuick 2.0
import QtQuick.Controls 2.4
import BaseComponents 1.0

BaseButton {
    id: control

    property string borderNormalColor: "#75929F"
    property string borderHoverColor: "#668695"
    property string borderFocusColor: "#668695"
    property string borderPressedColor: "#617E8D"
    property string borderDisableColor: "#75929F"

    property string bgNormalColor: "#75929F"
    property string bgHoverColor: "#668695"
    property string bgFocusColor: "#668695"
    property string bgPressedColor: "#617E8D"
    property string bgDisableColor: "#75929F"

    property string textNormalColor: "#ffffff"
    property string textHoverColor: "#ffffff"
    property string textFocusColor: "#ffffff"
    property string textPressedColor: "#ffffff"
    property string textDisableColor: "#435862"

    property string icoNormalColor
    property string icoHoverColor
    property string icoFocusColor
    property string icoPressedColor
    property string icoDisableColor

    property real horizontalAlignment: Text.AlignHCenter
    property real verticalAlignment: Text.AlignVCenter
    property real elide: Text.ElideRight

    font.bold: true
    font.pointSize: 10

    property int radius: 5

    property bool isIcon: false
    property bool isText: true

    background: Rectangle {
        anchors.fill: control
        border.width: 1
        border.color: {
            if( control.enabled )
            {
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
            else
                borderDisableColor
        }
        color: {
            if( control.enabled )
            {
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
            else
                bgDisableColor
        }
        radius: control.radius
    }
    text: ""
    contentItem: Item{
        anchors.fill: parent
        Loader {
            anchors.fill: parent
            sourceComponent: (isText?_idCmpTxt:(isIcon?_idCmpImg:null))
        }
    }
    flat: true

    Component {
        id: _idCmpTxt
        Text {
        anchors.fill: parent
        text: control.text
        font: control.font
        opacity: 1.0
        visible: isText
        color: {
            if( control.enabled )
            {
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
            else
            {
                textDisableColor
            }
        }
        horizontalAlignment: control.horizontalAlignment
        verticalAlignment: control.verticalAlignment
        elide: control.elide
    }
    }

    Component {
        id: _idCmpImg
        Image {
            id: icon
            anchors.fill: parent
            visible: isIcon
            source: {
                if( control.enabled )
                {

                    if( control.down )
                    {
                        if( icoPressedColor !== null && icoPressedColor.length > 0 )
                            icoPressedColor
                        else
                            ''
                    }
                    else
                    {
                        if( control.hovered )
                        {
                            if( icoHoverColor !== null && icoHoverColor.length > 0 )
                                icoHoverColor
                            else
                                ''
                        }
                        else
                        {
                            if( control.focus )
                            {
                                if( icoFocusColor !== null && icoFocusColor.length > 0 )
                                    icoFocusColor
                                else
                                    ''
                            }
                            else
                            {
                                if( icoNormalColor !== null && icoNormalColor.length > 0 )
                                    icoNormalColor
                                else
                                    ''
                            }
                        }
                    }
                }
                else
                {
                    if( icoDisableColor !== null && icoDisableColor.length > 0 )
                        icoDisableColor
                    else
                        ''
                }
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
