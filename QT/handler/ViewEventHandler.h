#pragma once
#pragma execution_character_set("utf-8")

#ifndef VIEWEVENTHANDLER_H
#define VIEWEVENTHANDLER_H

#include <QObject>

class ViewEventHandler: public QObject
{
    Q_OBJECT

public:
    explicit            ViewEventHandler( QObject *parent = nullptr);
    virtual             ~ViewEventHandler();

public:
    virtual void        connectObjectEvent( QObject* pObj );
    virtual void        disconnectObjectEvent( QObject* pObj );

signals:

public slots:
    virtual void        HandleViewShowEvent();
    virtual void        HandleViewHideEvent();
    virtual void        HandleViewOpenEvent();
    virtual void        HandleViewClosedEvent();
    virtual void        HandleViewActiveFocusEvent();
    virtual void        HandleViewInactiveFocusEvent();
};

#endif // VIEWEVENTHANDLER_H
