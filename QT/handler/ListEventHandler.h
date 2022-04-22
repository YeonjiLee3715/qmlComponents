#pragma once
#pragma execution_character_set("utf-8")

#ifndef LISTEVENTHANDLER_H
#define LISTEVENTHANDLER_H

#include <QObject>

class ListEventHandler: public QObject
{
    Q_OBJECT

public:
    explicit            ListEventHandler( QObject *parent = nullptr );
    virtual             ~ListEventHandler();

public:
    virtual void        connectObjectEvent( QObject* pObj );
    virtual void        disconnectObjectEvent( QObject* pObj );

signals:

public slots:
    virtual void        HandleControlClickedEvent( int row, int col );
    virtual void        HandleControlDoubleClickedEvent( int row, int col );
    virtual void        HandleControlEnteredEvent( int row, int col );
    virtual void        HandleControlExitedEvent( int row, int col );
    virtual void        HandleControlPressAndHoldEvent( int row, int col );
    virtual void        HandleControlPressedEvent( int row, int col );
    virtual void        HandleControlReleasedEvent( int row, int col );
    virtual void        HandleControlCanceledEvent( int row, int col );
    virtual void        HandleControlWheelEvent( int row, int col, int x, int y );

    virtual void        HandleControlHoveredEvent( int row, int col );
    virtual void        HandleControlFocusedEvent( int row, int col );
    virtual void        HandleControlFocusOutEvent( int row, int col );

    virtual void        HandleControlOpenEvent( int row, int col );
    virtual void        HandleControlClosedEvent( int row, int col );

    virtual void        HandleControlDragEvent( int row, int col, int x, int y );

    virtual void        HandleControlEnabledEvent( int row, int col );
    virtual void        HandleControlDisabledEvent( int row, int col );

    virtual void        HandleControlSelectedEvent( int row, int col );
};

#endif // LISTEVENTHANDLER_H
