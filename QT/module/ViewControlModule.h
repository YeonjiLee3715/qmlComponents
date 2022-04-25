#pragma once
#pragma execution_character_set("utf-8")

#ifndef VIEWCONTROLMODULE_H
#define VIEWCONTROLMODULE_H

#include <thread>
#include <memory>

#include <QBaseModule.h>

#include <cmnDef.h>
#include <ModuleEnum.h>

#include <QQueue>
#include <QReadWriteLock>

#include "handler/WindowEventHandler.h"
#include "handler/ViewEventHandler.h"
#include "handler/ListEventHandler.h"
#include "handler/ButtonEventHandler.h"
#include "handler/ComboBoxEventHandler.h"
#include "handler/DialogEventHandler.h"
#include "handler/TextEditEventHandler.h"

#ifndef Q_MOC_RUN
#ifndef DECLARE_MODULE_REQUEST
#define DECLARE_MODULE_REQUEST( FUNCTION_NAME ) \
    void Req##FUNCTION_NAME( int sender, bool response, QVariantMap mapReq );
#endif // !DECLARE_MODULE_REQUEST
#ifndef DEFINE_MODULE_REQUEST
#define DEFINE_MODULE_REQUEST( CLASS, FUNCTION_NAME ) \
    void CLASS::Req##FUNCTION_NAME( int sender, bool response, QVariantMap mapReq )
#endif // !DEFINE_MODULE_REQUEST
#ifndef REGIST_MODULE_REQUEST
#define REGIST_MODULE_REQUEST( REQ_CODE, FUNCTION_NAME ) \
    insertFunctionToReqCode( static_cast<int>( REQ_CODE ), QString("Req")+#FUNCTION_NAME );
#endif // !REGIST_MODULE_REQUEST

#ifndef DECLARE_MODULE_RESPONSE
#define DECLARE_MODULE_RESPONSE( FUNCTION_NAME ) \
    void Res##FUNCTION_NAME( int sender, QVariantMap mapRes );
#endif // !DECLARE_MODULE_RESPONSE
#ifndef DEFINE_MODULE_RESPONSE
#define DEFINE_MODULE_RESPONSE( CLASS, FUNCTION_NAME ) \
    void CLASS::Res##FUNCTION_NAME( int sender, QVariantMap mapRes )
#endif // !DEFINE_MODULE_RESPONSE
#ifndef REGIST_MODULE_RESPONSE
#define REGIST_MODULE_RESPONSE( RES_CODE, FUNCTION_NAME ) \
    insertFunctionToResCode( static_cast<int>( RES_CODE ), QString("Res")+#FUNCTION_NAME );
#endif // !REGIST_MODULE_RESPONSE
#endif

class ViewControlModule: public QBaseModule
{
    Q_OBJECT

public:
    explicit ViewControlModule( QObject* parent = nullptr );
    virtual ~ViewControlModule();

    void            SetControlEventConnections();
    void            SetControlEventConnection( QObject* pObj, bool bRecursive );

    void            connectObjectEvent( QObject* pObj );

    void            SetControlEventDisconnections();
    void            SetControlEventDisconnection( QObject* pObj, bool bRecursive );

    void            disconnectObjectEvent( QObject* pObj );

    QObject*        GetRootControlObject();
    QObject*        FindChildObject(const QString& objectName, QObject* pParent = nullptr);

    WindowEventHandler*     GetWindowEventHandler();
    ViewEventHandler*       GetViewEventHandler();
    ListEventHandler*       GetListEventHandler();
    ButtonEventHandler*     GetButtonEventHandler();
    ComboBoxEventHandler*   GetComboBoxEventHandler();
    DialogEventHandler*     GetDialogEventHandler();
    TextEditEventHandler*   GetTextEditEventHandler();

private:
    void            SetControlEventConnectionRecursive( QObject* pObj );
    void            SetControlEventDisconnectionRecursive( QObject* pObj );

public:
    virtual void init() override;
    static QString getModuleName();

public slots:
    virtual void doRun() override;
    virtual void stopModule() override;

public slots:
    void            HandleNewControlLoadedEvent( QString objName );
    void            HandleDestroyControlLoadedEvent( QString objName );

private:
    bool                        initQmlEngine();

    void                        clear();

private:
    QQmlApplicationEngine*          m_pEngine;

    WindowEventHandler*             m_pHWindowEvent;
    ViewEventHandler*               m_pHViewEvent;
    ListEventHandler*               m_pHLstEvent;
    ButtonEventHandler*             m_pHBtnCtlEvent;
    ComboBoxEventHandler*           m_pHCbxCtlEvent;
    DialogEventHandler*             m_pHDlgEvent;
    TextEditEventHandler*           m_pHEdtCtlEvent;
};

#endif // ViewControlModule_H
