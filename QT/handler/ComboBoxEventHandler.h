#pragma once
#pragma execution_character_set("utf-8")

#ifndef COMBOBOXEVENTHANDLER_H
#define COMBOBOXEVENTHANDLER_H

#include <QObject>

class ComboBoxEventHandler: public QObject
{
    Q_OBJECT

public:
    explicit            ComboBoxEventHandler( QObject *parent = nullptr);
    virtual             ~ComboBoxEventHandler();

public:
    virtual void        connectObjectEvent( QObject* pObj );
    virtual void        disconnectObjectEvent( QObject* pObj );

signals:

public slots:
    virtual void        HandleControlPressedEvent(bool bPressed);
    virtual void        HandleControlHoveredEvent(bool bHovered);
    virtual void        HandleControlFocusedEvent();
    virtual void        HandleControlFocusOutEvent();

    virtual void        HandleControlEnabledEvent();
    virtual void        HandleControlDisabledEvent();
    virtual void        HandleControlOpenEvent();
    virtual void        HandleControlClosedEvent();

    /* This function only be emitted if the combo box index was changed by the user,
     * ** not when set programmatically.** */
    virtual void        HandleControlSelectedEvent( int idx );

    /* This function is emitted when the Return or Enter key is pressed on an ** editable ** combo box.
     * If the confirmed string is not currently in the model,
     * the currentIndex will be set to -1 and the currentText will be updated accordingly. */
    virtual void        HandleControlAccepted();
};

#endif // COMBOBOXEVENTHANDLER_H
