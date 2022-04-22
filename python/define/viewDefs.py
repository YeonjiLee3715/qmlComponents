# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5 import QtCore
from PyQt5.QtCore import Q_ENUMS, QObject

PROP_B_CONNECT_EVENT                        = 'bConnectEvent'
PROP_IS_EVENT_CONNECTED                     = 'isEventConnected'

PROP_B_CONNECT_CLICKED_EVENT                = 'bConnectClickedEvent'
PROP_B_CONNECT_DOUBLE_CLICKED_EVENT         = 'bConnectDoubleClickedEvent'
PROP_B_CONNECT_PRESS_AND_HOLD_EVENT         = 'bConnectPressAndHoldEvent'
PROP_B_CONNECT_PRESSED_EVENT                = 'bConnectPressedEvent'
PROP_B_CONNECT_RELEASED_EVENT               = 'bConnectReleasedEvent'
PROP_B_CONNECT_CANCELED_EVENT               = 'bConnectCanceledEvent'
PROP_B_CONNECT_TOGGLED_EVENT                = 'bConnectToggledEvent'
PROP_B_CONNECT_HOVERED_EVENT                = 'bConnectHoveredEvent'
PROP_B_CONNECT_FOCUSED_EVENT                = 'bConnectFocusedEvent'
PROP_B_CONNECT_FOCUS_OUT_EVENT              = 'bConnectFocusOutEvent'
PROP_B_CONNECT_ENABLED_EVENT                = 'bConnectEnabledEvent'
PROP_B_CONNECT_DISABLED_EVENT               = 'bConnectDisabledEvent'
PROP_B_CONNECT_OPEN_EVENT                   = 'bConnectOpenEvent'
PROP_B_CONNECT_CLOSED_EVENT                 = 'bConnectClosedEvent'
PROP_B_CONNECT_SELECTED_EVENT               = 'bConnectSelectedEvent'
PROP_B_CONNECT_ACCEPTED_EVENT               = 'bConnectAcceptedEvent'
PROP_B_CONNECT_REJECTED_EVENT               = 'bConnectRejectedEvent'
PROP_B_CONNECT_ENTERED_EVENT                = 'bConnectEnteredEvent'
PROP_B_CONNECT_EXITED_EVENT                 = 'bConnectExitedEvent'
PROP_B_CONNECT_WHEEL_EVENT                  = 'bConnectWheelEvent'
PROP_B_CONNECT_DRAG_EVENT                   = 'bConnectDragEvent'
PROP_B_CONNECT_EDITING_FINISHED_EVENT       = 'bConnectEditingFinishedEvent'
PROP_B_CONNECT_TEXT_EDITED_EVENT            = 'bConnectTextEditedEvent'
PROP_B_CONNECT_SHOW_EVENT                   = 'bConnectShowEvent'
PROP_B_CONNECT_HIDE_EVENT                   = 'bConnectHideEvent'
PROP_B_CONNECT_ACTIVEFOCUS_EVENT            = 'bConnectActiveFocusEvent'
PROP_B_CONNECT_INACTIVEFOCUS_EVENT          = 'bConnectInactiveFocusEvent'
PROP_B_CONNECT_ACTIVE_EVENT                 = 'bConnectActiveEvent'
PROP_B_CONNECT_INACTIVE_EVENT               = 'bConnectInactiveEvent'
"""
    Qml object names
"""
ID_idRootWindow                             = '_idRootWindow'

"""
    end Qml object names
"""

class ViewEnum(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    class eObjectType:
        OBJECT_NONE = 0
        OBJECT_WINDOW = 1
        OBJECT_VIEW = 2
        OBJECT_DIALOG = 3
        OBJECT_BUTTON_CONTROL = 4
        OBJECT_COMBOBOX_CONTROL = 5
        OBJECT_TEXTEDIT_CONTROL = 6
        OBJECT_LIST_VIEW = 7

    class eWindowType:
        WINDOW_NONE = 0
        WINDOW_NORMAL = 1

    class eWindowId:
        ROOT_WINDOW = 100

    class eViewType:
        VIEW_NONE = 0
        VIEW_NORMAL = 1

"""
    class eViewId:
        ID_VW_ = 500
"""

    class eDialogType:
        DIALOG_NONE = 0
        DIALOG_INFORMATION = 1
        DIALOG_FILE_DIALOG = 2
        DIALOG_QUESTION_TWO_BUTTONS = 3
        DIALOG_QUESTION_THREE_BUTTONS = 4

"""
    class eDialogId:
        ID_FD_ = 1000
"""

"""
    class eListId:
        ID_LST_ = 0
"""

    class eBtnControlType:
        CONTROL_NONE = 0
        CONTROL_BUTTON = 2

"""
    class eBtnControlId:
        ID_BTN_ = 10000
"""

"""
    class eEdtControlId:
        ID_EDT_ = 10100
"""

    class eWindowClosedCode:
        WINDOW_CLOSED_CODE_ACCEPTED = 0
        WINDOW_CLOSED_CODE_REJECTED = 1

    Q_ENUMS(eObjectType)
    Q_ENUMS(eWindowType)
    Q_ENUMS(eWindowId)
    Q_ENUMS(eViewType)
    Q_ENUMS(eViewId)
    Q_ENUMS(eDialogType)
    Q_ENUMS(eDialogId)
    Q_ENUMS(eListId)
    Q_ENUMS(eBtnControlType)
    Q_ENUMS(eBtnControlId)
    Q_ENUMS(eEdtControlId)
    Q_ENUMS(eWindowClosedCode)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
