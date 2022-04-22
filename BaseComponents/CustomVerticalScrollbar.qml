import QtQuick 2.0;

Item {
    id: scrollbar;
    width: (handleSize + 2 * (backScrollbar.border.width +1));
    visible: (flickable.visibleArea.heightRatio < 1.0);

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

    property string hdNormalColor: "#FFFFFF"
    property string hdHoverColor: "#EAEEF0"
    property string hdFocusColor: "#EAEEF0"
    property string hdPressedColor: "#D3DCE0"
    property string hdDisableColor: "#FFFFFF"

    property string textNormalColor: "#2A2A2A"
    property string textHoverColor: "#2A2A2A"
    property string textFocusColor: "#2A2A2A"
    property string textPressedColor: "#2A2A2A"
    property string textDisableColor: "#ABABAB"

    property int radius: 5
    property Flickable flickable: null
    property int handleSize: 20

    function scrollDown () {
        flickable.contentY = Math.min (flickable.contentY + (flickable.height / 4), flickable.contentHeight - flickable.height);
    }
    function scrollUp () {
        flickable.contentY = Math.max (flickable.contentY - (flickable.height / 4), 0);
    }

   Binding {
        target: handle;
        property: "y";
        value: (flickable.contentY * clicker.drag.maximumY / (flickable.contentHeight - flickable.height));
        when: (!clicker.drag.active);
    }
    Binding {
        target: flickable;
        property: "contentY";
        value: (handle.y * (flickable.contentHeight - flickable.height) / clicker.drag.maximumY);
        when: (clicker.drag.active || clicker.pressed);
    }
    Rectangle {
        id: backScrollbar;
        radius: 2;
        antialiasing: true;
        border.width: 1
        border.color: {
            if( clicker.pressed )
            {
                borderPressedColor
            }
            else
            {
                if( scrollbar.focus )
                {
                    borderFocusColor
                }
                else
                {
                    if( scrollbar.hovered )
                        borderHoverColor
                    else
                        borderNormalColor
                }
            }
        }
        color: {
            if( clicker.pressed && ( clicker.mouseY < handle.y || clicker.mouseY >= handle.y+handle.height ) )
            {
                bgPressedColor
            }
            else
            {
                if( scrollbar.focus )
                {
                    bgFocusColor
                }
                else
                {
                    if( scrollbar.hovered && ( clicker.mouseY < handle.y || clicker.mouseY >= handle.y+handle.height ) )
                        bgHoverColor
                    else
                        bgNormalColor
                }
            }
        }
        anchors { fill: parent; }

        MouseArea {
            anchors.fill: parent;
            onClicked: { }
        }
    }
    Rectangle{
        height: width;
        anchors {
            top: parent.top;
            left: parent.left;
            right: parent.right;
            margins: (backScrollbar.border.width +1);
        }
        color: {
            if( btnUp.pressed )
            {
                bgPressedColor
            }
            else
            {
                if( btnUp.focus )
                {
                    bgFocusColor
                }
                else
                {
                    if( btnUp.hovered )
                        bgHoverColor
                    else
                        bgNormalColor
                }
            }
        }
        radius: scrollbar.radius
        MouseArea {
            id: btnUp;
            property bool hovered: false
            anchors.fill: parent
            hoverEnabled: true
            onClicked: { scrollUp (); }
            onEntered: hovered = true
            onExited: hovered = false

            Text {
                text: "V";
                font.family: "Arial"
                font.bold: true
                opacity: enabled ? 1.0 : 0.3
                color: {
                    if( btnUp.pressed )
                    {
                        textPressedColor
                    }
                    else
                    {
                        if( btnUp.hovered )
                        {
                            textHoverColor
                        }
                        else
                        {
                            if( btnUp.focus )
                                textFocusColor
                            else
                                textNormalColor
                        }
                    }
                }
                rotation: -180;
                anchors.centerIn: parent;
            }
        }
    }
    Rectangle {
        height: width;
        anchors {
            left: parent.left;
            right: parent.right;
            bottom: parent.bottom;
            margins: (backScrollbar.border.width +1);
        }
        color: {
            if( btnDown.pressed )
            {
                bgPressedColor
            }
            else
            {
                if( btnDown.focus )
                {
                    bgFocusColor
                }
                else
                {
                    if( btnDown.hovered )
                        bgHoverColor
                    else
                        bgNormalColor
                }
            }
        }
        radius: scrollbar.radius
        MouseArea {
            id: btnDown;
            property bool hovered: false
            anchors.fill: parent
            hoverEnabled: true
            onClicked: { scrollDown (); }
            onEntered: hovered = true
            onExited: hovered = false

            Text {
                text: "V";
                font.family: "Arial"
                font.bold: true
                opacity: enabled ? 1.0 : 0.3
                color: {
                    if( btnDown.pressed )
                    {
                        textPressedColor
                    }
                    else
                    {
                        if( btnDown.hovered )
                        {
                            textHoverColor
                        }
                        else
                        {
                            if( btnDown.focus )
                                textFocusColor
                            else
                                textNormalColor
                        }
                    }
                }
                anchors.centerIn: parent;
            }
        }
    }

    Item {
        id: groove;
        clip: true;
        anchors {
            fill: parent;
            topMargin: (backScrollbar.border.width +1 + btnUp.height +1);
            leftMargin: (backScrollbar.border.width +1);
            rightMargin: (backScrollbar.border.width +1);
            bottomMargin: (backScrollbar.border.width +1 + btnDown.height +1);
        }

        MouseArea {
            id: clicker;
            property bool hovered: false

            drag {
                target: handle;
                minimumY: 0;
                maximumY: (groove.height - handle.height);
                axis: Drag.YAxis;
            }
            anchors { fill: parent; }
            hoverEnabled: true
            onClicked: { flickable.contentY = (mouse.y / groove.height * (flickable.contentHeight - flickable.height)); }
            onEntered: hovered = true
            onExited: hovered = false
        }
        Item {
            id: handle;
            height: Math.max (20, (flickable.visibleArea.heightRatio * groove.height));
            anchors {
                left: parent.left;
                right: parent.right;
            }

            Rectangle {
                id: backHandle;
                radius: scrollbar.radius
                border.width: 1
                border.color: {
                    if( clicker.pressed )
                    {
                        borderPressedColor
                    }
                    else
                    {
                        if( scrollbar.focus )
                        {
                            borderFocusColor
                        }
                        else
                        {
                            if( clicker.hovered )
                                borderHoverColor
                            else
                                borderNormalColor
                        }
                    }
                }

                color: {
                    if( clicker.pressed && clicker.mouseY >= handle.y && clicker.mouseY < handle.y+handle.height )
                    {
                        hdPressedColor
                    }
                    else
                    {
                        if( scrollbar.focus )
                        {
                            hdFocusColor
                        }
                        else
                        {
                            if( clicker.hovered && clicker.mouseY >= handle.y && clicker.mouseY < handle.y+handle.height )
                                hdHoverColor
                            else
                                hdNormalColor
                        }
                    }
                }
                anchors { fill: parent; }
            }
        }
    }
}
