#pragma once
#pragma execution_character_set("utf-8")

#ifndef WINDOWEVENTHANDLER_H
#define WINDOWEVENTHANDLER_H

#include <QObject>

class WindowEventHandler: public QObject
{
    Q_OBJECT

public:
    explicit            WindowEventHandler( QObject *parent = nullptr );
    virtual             ~WindowEventHandler();

public:
    virtual void        connectObjectEvent( QObject* pObj );
    virtual void        disconnectObjectEvent( QObject* pObj );

signals:

public slots:
    void                HandleWindowShowEvent();
    void                HandleWindowHideEvent();
    void                HandleWindowOpenEvent();
    void                HandleWindowClosedEvent();
    void                HandleWindowActiveEvent();
    void                HandleWindowInactiveEvent();

public:
private:
};

#endif // WINDOWEVENTHANDLER_H
