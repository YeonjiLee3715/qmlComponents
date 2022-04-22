#pragma once
#pragma execution_character_set("utf-8")

#ifndef VIEWDEFS_H
#define VIEWDEFS_H

#include <QObject>
#include <QMetaType>
#include <QMetaEnum>


#define PROP_B_CONNECT_EVENT                        "bConnectEvent"
#define PROP_IS_EVENT_CONNECTED                     "isEventConnected"

#define PROP_B_CONNECT_CLICKED_EVENT                "bConnectClickedEvent"
#define PROP_B_CONNECT_DOUBLE_CLICKED_EVENT         "bConnectDoubleClickedEvent"
#define PROP_B_CONNECT_PRESS_AND_HOLD_EVENT         "bConnectPressAndHoldEvent"
#define PROP_B_CONNECT_PRESSED_EVENT                "bConnectPressedEvent"
#define PROP_B_CONNECT_RELEASED_EVENT               "bConnectReleasedEvent"
#define PROP_B_CONNECT_CANCELED_EVENT               "bConnectCanceledEvent"
#define PROP_B_CONNECT_TOGGLED_EVENT                "bConnectToggledEvent"
#define PROP_B_CONNECT_HOVERED_EVENT                "bConnectHoveredEvent"
#define PROP_B_CONNECT_FOCUSED_EVENT                "bConnectFocusedEvent"
#define PROP_B_CONNECT_FOCUS_OUT_EVENT              "bConnectFocusOutEvent"
#define PROP_B_CONNECT_ENABLED_EVENT                "bConnectEnabledEvent"
#define PROP_B_CONNECT_DISABLED_EVENT               "bConnectDisabledEvent"
#define PROP_B_CONNECT_OPEN_EVENT                   "bConnectOpenEvent"
#define PROP_B_CONNECT_CLOSED_EVENT                 "bConnectClosedEvent"
#define PROP_B_CONNECT_SELECTED_EVENT               "bConnectSelectedEvent"
#define PROP_B_CONNECT_ACCEPTED_EVENT               "bConnectAcceptedEvent"
#define PROP_B_CONNECT_REJECTED_EVENT               "bConnectRejectedEvent"
#define PROP_B_CONNECT_ENTERED_EVENT                "bConnectEnteredEvent"
#define PROP_B_CONNECT_EXITED_EVENT                 "bConnectExitedEvent"
#define PROP_B_CONNECT_WHEEL_EVENT                  "bConnectWheelEvent"
#define PROP_B_CONNECT_DRAG_EVENT                   "bConnectDragEvent"
#define PROP_B_CONNECT_EDITING_FINISHED_EVENT       "bConnectEditingFinishedEvent"
#define PROP_B_CONNECT_TEXT_EDITED_EVENT            "bConnectTextEditedEvent"
#define PROP_B_CONNECT_SHOW_EVENT                   "bConnectShowEvent"
#define PROP_B_CONNECT_HIDE_EVENT                   "bConnectHideEvent"
#define PROP_B_CONNECT_ACTIVEFOCUS_EVENT            "bConnectActiveFocusEvent"
#define PROP_B_CONNECT_INACTIVEFOCUS_EVENT          "bConnectInactiveFocusEvent"
#define PROP_B_CONNECT_ACTIVE_EVENT                 "bConnectActiveEvent"
#define PROP_B_CONNECT_INACTIVE_EVENT               "bConnectInactiveEvent"

// Qml object names
#define _idRootWindow                   "_idRootWindow"


// End Qml object names

class ViewEnum: public QObject
{
    Q_OBJECT

    Q_ENUMS( eObjectType )

    Q_ENUMS( eWindowType )
    Q_ENUMS( eWindowId )

    Q_ENUMS( eViewType )
    Q_ENUMS( eViewId )

    Q_ENUMS( eDialogType )
    Q_ENUMS( eDialogId )

    Q_ENUMS( eBtnControlType )
    Q_ENUMS( eBtnControlId )

    Q_ENUMS( eEdtControlId )

    Q_ENUMS( eKaraokeConverterMode )

    Q_ENUMS( eWindowClosedCode )

public:
    typedef enum eObjectType
    {
        OBJECT_NONE = 0,
        OBJECT_WINDOW,
        OBJECT_VIEW,
        OBJECT_DIALOG,
        OBJECT_BUTTON_CONTROL,
        OBJECT_COMBOBOX_CONTROL,
        OBJECT_TEXTEDIT_CONTROL,
        OBJECT_LIST_VIEW
    }eObjectType;

    typedef enum eWindowType
    {
        WINDOW_NONE = 0,
        WINDOW_NORMAL
    }eWindowType;

    typedef enum eWindowId
    {
        ID_ROOT_WINDOW = 100
    }eWindowId;

    typedef enum eViewType
    {
        VIEW_NONE = 0,
        VIEW_NORMAL
    }eViewType;

/*
    typedef enum eViewId
    {
        ID_VW_ = 500,
    }eViewId;
*/

    typedef enum eDialogType
    {
        DIALOG_NONE = 0,
        DIALOG_INFORMATION,
        DIALOG_FILE_DIALOG,
        DIALOG_QUESTION_TWO_BUTTONS,
        DIALOG_QUESTION_THREE_BUTTONS
    }eDialogType;

/*
    typedef enum eDialogId
    {
        ID_FD_ = 1000,
    }eDialogId;
*/

    typedef enum eBtnControlType
    {
        CONTROL_NONE = 0,
        CONTROL_BUTTON
    }eControlType;

/*
    typedef enum eBtnControlId
    {
        ID_BTN_ = 10000,
    }eBtnControlId;
*/

/*
    typedef enum eEdtControlId
    {
        ID_EDT_ = 10100,
    }eEdtControlId;
*/

    typedef enum eWindowClosedCode
    {
        WINDOW_CLOSED_CODE_ACCEPTED = 0,
        WINDOW_CLOSED_CODE_REJECTED,
    }eWindowClosedCode;

    ViewEnum( QObject* parent = nullptr ): QObject( parent ) {}

};

Q_DECLARE_METATYPE( ViewEnum::eObjectType )

Q_DECLARE_METATYPE( ViewEnum::eWindowType )
Q_DECLARE_METATYPE( ViewEnum::eWindowId )

Q_DECLARE_METATYPE( ViewEnum::eViewType )
Q_DECLARE_METATYPE( ViewEnum::eViewId )

Q_DECLARE_METATYPE( ViewEnum::eDialogType )
Q_DECLARE_METATYPE( ViewEnum::eDialogId )

Q_DECLARE_METATYPE( ViewEnum::eBtnControlType )
Q_DECLARE_METATYPE( ViewEnum::eBtnControlId )

Q_DECLARE_METATYPE( ViewEnum::eEdtControlId )

Q_DECLARE_METATYPE( ViewEnum::eWindowClosedCode )

#endif // VIEWDEFS_H
