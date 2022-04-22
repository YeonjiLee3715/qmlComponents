#pragma once
#pragma execution_character_set("utf-8")

#ifndef DIALOGEVENTHANDLER_H
#define DIALOGEVENTHANDLER_H

#include <QObject>

class DialogEventHandler: public QObject
{
    Q_OBJECT

public:
    explicit            DialogEventHandler( QObject *parent = nullptr );
    virtual             ~DialogEventHandler();

public:
    virtual void        connectObjectEvent( QObject* pObj );
    virtual void        disconnectObjectEvent( QObject* pObj );

signals:

public slots:
    void                HandleDialogShowEvent();
    void                HandleDialogHideEvent();
    void                HandleDialogOpenEvent();
    void                HandleAcceptedEvent();
    void                HandleRejectedEvent();

public:
private:
};

#endif // DIALOGEVENTHANDLER_H
