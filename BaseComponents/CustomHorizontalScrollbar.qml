import QtQuick 2.0;

Item {
    id: scrollbar
    height: (handleSize + 2 * (backScrollbar.border.width +1))
    visible: (flickable.visibleArea.widthRatio < 1.0)

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

    function scrollRight () {
        flickable.contentX = Math.min (flickable.contentX + (flickable.width / 4), flickable.contentWidth - flickable.width);
    }
    function scrollLeft () {
        flickable.contentX = Math.max (flickable.contentX - (flickable.width / 4), 0);
    }

   Binding {
        target: handle;
        property: "x";
        value: (flickable.contentX * clicker.drag.maximumX / (flickable.contentWidth - flickable.width));
        when: (!clicker.drag.active);
    }
    Binding {
        target: flickable;
        property: "contentX";
        value: (handle.x * (flickable.contentWidth - flickable.width) / clicker.drag.maximumX);
        when: (clicker.drag.active || clicker.pressed);
    }
    Rectangle {
        id: backScrollbar;
        radius: scrollbar.radius;
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
            if( clicker.pressed && ( clicker.mouseX < handle.x || clicker.mouseX >= handle.x+handle.width ) )
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
                    if( scrollbar.hovered && ( clicker.mouseX < handle.x || clicker.mouseX >= handle.x+handle.width ) )
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
        width: height;
        anchors {
            top: parent.top;
            left: parent.left;
            bottom: parent.bottom;
            margins: (backScrollbar.border.width +1);
        }
        color: {
            if( btnLeft.pressed )
            {
                bgPressedColor
            }
            else
            {
                if( btnLeft.focus )
                {
                    bgFocusColor
                }
                else
                {
                    if( btnLeft.hovered )
                        bgHoverColor
                    else
                        bgNormalColor
                }
            }
        }
        radius: scrollbar.radius
        MouseArea {
            id: btnLeft;
            property bool hovered: false
            anchors.fill: parent
            hoverEnabled: true
            onClicked: { scrollLeft (); }
            onEntered: hovered = true
            onExited: hovered = false

            Text {
                text: "V"
                font.family: "Arial"
                font.bold: true
                rotation: 90
                opacity: enabled ? 1.0 : 0.3
                color: {
                    if( btnLeft.pressed )
                    {
                        textPressedColor
                    }
                    else
                    {
                        if( btnLeft.hovered )
                        {
                            textHoverColor
                        }
                        else
                        {
                            if( btnLeft.focus )
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
    Rectangle {
        width: height;
        anchors {
            top: parent.top;
            right: parent.right;
            bottom: parent.bottom;
            margins: (backScrollbar.border.width +1);
        }
        color: {
            if( btnRight.pressed )
            {
                bgPressedColor
            }
            else
            {
                if( btnRight.focus )
                {
                    bgFocusColor
                }
                else
                {
                    if( btnRight.hovered )
                        bgHoverColor
                    else
                        bgNormalColor
                }
            }
        }
        radius: scrollbar.radius
        MouseArea {
            id: btnRight;
            property bool hovered: false
            anchors.fill: parent
            hoverEnabled: true
            onClicked: { scrollRight (); }
            onEntered: hovered = true
            onExited: hovered = false

            Text {
                text: "V";
                font.family: "Arial"
                font.bold: true
                rotation: -90
                opacity: enabled ? 1.0 : 0.3
                color: {
                    if( btnRight.pressed )
                    {
                        textPressedColor
                    }
                    else
                    {
                        if( btnRight.hovered )
                        {
                            textHoverColor
                        }
                        else
                        {
                            if( btnRight.focus )
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
            topMargin: (backScrollbar.border.width +1);
            leftMargin: (backScrollbar.border.width +1 + btnLeft.width +1);
            rightMargin: (backScrollbar.border.width +1 + btnRight.width +1);
            bottomMargin: (backScrollbar.border.width +1 );
        }

        MouseArea {
            id: clicker;
            property bool hovered: false

            drag {
                target: handle;
                minimumX: 0;
                maximumX: (groove.width - handle.width);
                axis: Drag.XAxis;
            }
            anchors { fill: parent; }
            hoverEnabled: true
            onClicked: { flickable.contentX = (mouse.x / groove.width * (flickable.contentWidth - flickable.width)); }
            onEntered: hovered = true
            onExited: hovered = false
        }
        Item {
            id: handle;
            width: Math.max (20, (flickable.visibleArea.widthRatio * groove.width));
            anchors {
                top: parent.top;
                bottom: parent.bottom;
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
                    if( clicker.pressed && clicker.mouseX >= handle.x && clicker.mouseX < handle.x+handle.width )
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
                            if( clicker.hovered && clicker.mouseX >= handle.x && clicker.mouseX < handle.x+handle.width )
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
