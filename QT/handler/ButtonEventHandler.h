#pragma once
#pragma execution_character_set("utf-8")

#ifndef BUTTONEVENTHANDLER_H
#define BUTTONEVENTHANDLER_H

#include <QObject>

class ButtonEventHandler: public QObject
{
    Q_OBJECT

public:
    explicit ButtonEventHandler( QObject *parent = nullptr);
    virtual ~ButtonEventHandler();

public:
    virtual void        connectObjectEvent( QObject* pObj );
    virtual void        disconnectObjectEvent( QObject* pObj );

signals:
    //void                SigDoSomething(int);

public slots:
    virtual void        HandleControlClickedEvent();
    virtual void        HandleControlDoubleClickedEvent();
    virtual void        HandleControlPressAndHoldEvent();
    virtual void        HandleControlPressedEvent();
    virtual void        HandleControlReleasedEvent();
    virtual void        HandleControlCanceledEvent();
    virtual void        HandleControlToggledEvent();

    virtual void        HandleControlHoveredEvent(bool bHovered);
    virtual void        HandleControlFocusedEvent();
    virtual void        HandleControlFocusOutEvent();
    virtual void        HandleControlEnabledEvent();
    virtual void        HandleControlDisabledEvent();
public:
private:
};

#endif // BUTTONEVENTHANDLER_H
