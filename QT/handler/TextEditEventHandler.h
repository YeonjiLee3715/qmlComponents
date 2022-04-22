#pragma once
#pragma execution_character_set("utf-8")

#ifndef TEXTEDITEVENTHANDLER_H
#define TEXTEDITEVENTHANDLER_H

#include <QObject>

class TextEditEventHandler: public QObject
{
    Q_OBJECT

public:
    explicit            TextEditEventHandler( QObject *parent = nullptr );
    virtual             ~TextEditEventHandler();

public:
    virtual void        connectObjectEvent( QObject* pObj );
    virtual void        disconnectObjectEvent( QObject* pObj );

signals:
    //void                SigSomethingChanged( QString strPath );

public slots:
    void                HandleControlAcceptedEvent();
    void                HandleControlEditingFinishedEvent();
    void                HandleControlTextEditedEvent();
    void                HandleControlFocusedEvent();
    void                HandleControlFocusOutEvent();
    void                HandleControlEnabledEvent();
    void                HandleControlDisabledEvent();

public:
private:
};

#endif // TEXTEDITEVENTHANDLER_H
