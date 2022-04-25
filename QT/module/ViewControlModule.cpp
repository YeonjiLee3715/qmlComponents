#include "ViewControlModule.h"

#include <QModuleManager.h>
#include <viewDefs.h>

#include <CLogger.h>

namespace nsViewControlModule{
    const char* TAG = "ViewControlModule";
}

using namespace nsViewControlModule;

ViewControlModule::ViewControlModule( QObject *parent )
    : QBaseModule(parent), m_pEngine(nullptr), m_pHWindowEvent(nullptr)
    , m_pHViewEvent(nullptr), m_pHLstEvent(nullptr), m_pHBtnCtlEvent(nullptr)
    , m_pHCbxCtlEvent(nullptr), m_pHDlgEvent(nullptr), m_pHEdtCtlEvent(nullptr)
{

}

ViewControlModule::~ViewControlModule()
{
    SetControlEventDisconnections();

    if( m_pEngine != nullptr )
    {
        m_pEngine->exit( 0 );
        m_pEngine->deleteLater();
        m_pEngine = nullptr;
    }
}

void ViewControlModule::SetControlEventConnections()
{
    QObject* pObjRoot = GetRootControlObject();
    assert( pObjRoot != nullptr );

    LOGD( TAG, "test" );

    QVariant vEventConnected = pObjRoot->property( PROP_IS_EVENT_CONNECTED );
    if( vEventConnected.isNull() || vEventConnected.isValid() == false
            || vEventConnected.toBool() == false )
    {
        connect( pObjRoot, SIGNAL( newControlLoaded(QString) ), this, SLOT( HandleNewControlLoadedEvent(QString) ), Qt::DirectConnection );
        connect( pObjRoot, SIGNAL( destroyControlLoaded(QString) ), this, SLOT( HandleDestroyControlLoadedEvent(QString) ), Qt::DirectConnection );
        pObjRoot->setProperty( PROP_IS_EVENT_CONNECTED, true );
        LOGD( TAG, "test" );
    }

    SetControlEventConnection( pObjRoot, true );
}

void ViewControlModule::SetControlEventConnection(QObject *pObj, bool bRecursive)
{
    if( pObj == nullptr )
    {
        LOGE( TAG, "Object is null" );
        return;
    }

    if( bRecursive )
        SetControlEventConnectionRecursive( pObj );
    else
        connectObjectEvent( pObj );
}

void ViewControlModule::connectObjectEvent(QObject *pObj)
{
    if( pObj == nullptr )
    {
        LOGE( TAG, "Object is null" );
        return;
    }

    QVariant vConnectEvent = pObj->property( PROP_B_CONNECT_EVENT );
    if( vConnectEvent.isNull() || vConnectEvent.isValid() == false
        || vConnectEvent.toBool() == false )
        return;

    QVariant vObjectType = pObj->property( "objectType" );
    if( vObjectType.isNull() || vObjectType.isValid() == false )
    {
        LOGE( TAG, "Object type is null" );
        return;
    }

    switch( vObjectType.toInt() )
    {
    case static_cast<int>( ViewEnum::OBJECT_WINDOW ):
        m_pHWindowEvent->connectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_VIEW ):
        m_pHViewEvent->connectObjectEvent( pObj );
    break;
    case static_cast<int>( ViewEnum::OBJECT_DIALOG ) :
        m_pHDlgEvent->connectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_BUTTON_CONTROL ):
        m_pHBtnCtlEvent->connectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_COMBOBOX_CONTROL ):
        m_pHCbxCtlEvent->connectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_TEXTEDIT_CONTROL ):
        m_pHEdtCtlEvent->connectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_LIST_VIEW ):
        m_pHLstEvent->connectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_NONE ) :
    default:
        LOGE( TAG, "Unknown objectType: %d", vObjectType.toInt() );
    break;
    }
}

void ViewControlModule::SetControlEventDisconnections()
{
    QObject* pObjRoot = GetRootControlObject();
    if( pObjRoot != nullptr )
    {
        QVariant vEventConnected = pObjRoot->property( PROP_IS_EVENT_CONNECTED );
        if( vEventConnected.isNull() == false && vEventConnected.isValid()
                || vEventConnected.toBool() )
        {
            disconnect( pObjRoot, SIGNAL( newControlLoaded(QString) ), this, SLOT( HandleNewControlLoadedEvent(QString) ) );
            disconnect( pObjRoot, SIGNAL( destroyControlLoaded(QString) ), this, SLOT( HandleDestroyControlLoadedEvent(QString) ) );
            pObjRoot->setProperty( PROP_IS_EVENT_CONNECTED, false );
        }

        SetControlEventDisconnection( pObjRoot, true );
    }
}

void ViewControlModule::SetControlEventDisconnection(QObject *pObj, bool bRecursive)
{
    if( pObj == nullptr )
    {
        LOGE( TAG, "Object is null" );
        return;
    }

    if( bRecursive )
        SetControlEventDisconnectionRecursive( pObj );
    else
        disconnectObjectEvent( pObj );
}

void ViewControlModule::disconnectObjectEvent(QObject *pObj)
{
    if( pObj == nullptr )
    {
        LOGE( TAG, "Object is null" );
        return;
    }

    QVariant vConnectEvent = pObj->property( PROP_B_CONNECT_EVENT );
    if( vConnectEvent.isNull() || vConnectEvent.isValid() == false
        || vConnectEvent.toBool() == false )
        return;

    QVariant vObjectType = pObj->property( "objectType" );
    if( vObjectType.isNull() || vObjectType.isValid() == false )
    {
        LOGE( TAG, "Object type is null" );
        return;
    }

    switch( vObjectType.toInt() )
    {
    case static_cast<int>( ViewEnum::OBJECT_WINDOW ):
        m_pHWindowEvent->disconnectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_VIEW ):
        m_pHViewEvent->disconnectObjectEvent( pObj );
    break;
    case static_cast<int>( ViewEnum::OBJECT_DIALOG ) :
        m_pHDlgEvent->disconnectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_BUTTON_CONTROL ):
        m_pHBtnCtlEvent->disconnectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_COMBOBOX_CONTROL ):
        m_pHCbxCtlEvent->disconnectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_TEXTEDIT_CONTROL ):
        m_pHEdtCtlEvent->disconnectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_LIST_VIEW ):
        m_pHLstEvent->disconnectObjectEvent( pObj );
        break;
    case static_cast<int>( ViewEnum::OBJECT_NONE ) :
    default:
        LOGE( TAG, "Unknown objectType: %d", vObjectType.toInt() );
    break;
    }
}

QObject* ViewControlModule::GetRootControlObject()
{
    QObject* pObjRoot = nullptr;

    if( m_pEngine == nullptr || m_pEngine->rootObjects().isEmpty() )
        return nullptr;

    QList<QObject*> lstRootObject = m_pEngine->rootObjects();

    for( QObject* pObj : lstRootObject )
    {
        if( pObj != nullptr )
        {
            if( pObj->objectName().compare( _idRootWindow ) == 0 )
            {
                pObjRoot = pObj;
                break;
            }
        }
    }

    return pObjRoot;
}

QObject* ViewControlModule::FindChildObject(const QString& objectName, QObject* pParent)
{
    if( objectName.isEmpty() )
        return nullptr;

    if( pParent == nullptr )
        pParent = GetRootControlObject();

    if( pParent == nullptr )
        return nullptr;

    if( objectName.compare( pParent->objectName() ) == 0 )
        return pParent;

    return pParent->findChild<QObject*>( objectName );
}

WindowEventHandler* ViewControlModule::GetWindowEventHandler()
{
    return m_pHWindowEvent;
}

ViewEventHandler* ViewControlModule::GetViewEventHandler()
{
    return m_pHViewEvent;
}

ListEventHandler* ViewControlModule::GetListEventHandler()
{
    return m_pHLstEvent;
}

ButtonEventHandler* ViewControlModule::GetButtonEventHandler()
{
    return m_pHBtnCtlEvent;
}

ComboBoxEventHandler* ViewControlModule::GetComboBoxEventHandler()
{
    return m_pHCbxCtlEvent;
}

DialogEventHandler* ViewControlModule::GetDialogEventHandler()
{
    return m_pHDlgEvent;
}

TextEditEventHandler* ViewControlModule::GetTextEditEventHandler()
{
    return m_pHEdtCtlEvent;
}

void ViewControlModule::SetControlEventConnectionRecursive(QObject *pObj)
{
    if( pObj == nullptr )
    {
        LOGE( TAG, "Object is null" );
        return;
    }

    connectObjectEvent( pObj );

    QList<QObject *> lstObjChild = pObj->findChildren<QObject*>( QString(), Qt::FindDirectChildrenOnly );
    if( lstObjChild.isEmpty() )
        return;

    for( QObject* pObjChild : lstObjChild )
    {
        if( pObjChild == nullptr )
            continue;

        SetControlEventConnectionRecursive( pObjChild );
    }
}

void ViewControlModule::SetControlEventDisconnectionRecursive(QObject *pObj)
{
    if( pObj == nullptr )
    {
        LOGE( TAG, "Object is null" );
        return;
    }

    disconnectObjectEvent( pObj );

    QList<QObject *> lstObjChild = pObj->findChildren<QObject*>( QString(), Qt::FindDirectChildrenOnly );
    if( lstObjChild.isEmpty() )
        return;

    for( QObject* pObjChild : lstObjChild )
    {
        if( pObjChild == nullptr )
            continue;

        SetControlEventDisconnectionRecursive( pObjChild );
    }
}

void ViewControlModule::init()
{
    if( initQmlEngine() == false )
    {
        LOGE( TAG, "Failed to init QML Engine" );
        return;
    }

    m_pHWindowEvent = new WindowEventHandler();
    m_pHViewEvent = new ViewEventHandler;
    m_pHLstEvent = new ListEventHandler;
    m_pHBtnCtlEvent = new ButtonEventHandler;
    m_pHCbxCtlEvent = new ComboBoxEventHandler;
    m_pHDlgEvent = new DialogEventHandler;
    m_pHEdtCtlEvent = new TextEditEventHandler;

    SetControlEventConnections();

    connect( m_pHEdtCtlEvent, SIGNAL( SigExcelSongInfoFilePathChanged(int, QString) )
             , this, SLOT( OnExcelSongInfoFilePathChanged(int, QString) ), Qt::DirectConnection );
    connect( m_pHEdtCtlEvent, SIGNAL( SigSrcPathChanged(int, QString) )
             , this, SLOT( OnSrcPathChanged(int, QString) ), Qt::DirectConnection );
    connect( m_pHEdtCtlEvent, SIGNAL( SigDstPathChanged(int, QString) )
             , this, SLOT( OnDstPathChanged(int, QString) ), Qt::DirectConnection );

    connect( m_pHBtnCtlEvent, SIGNAL( SigConvert(int) ), this, SLOT( OnConvert(int) ), Qt::DirectConnection );
    connect( m_pHBtnCtlEvent, SIGNAL( SigReload(int) ), this, SLOT( OnReload(int) ), Qt::DirectConnection );

    QBaseModule::init();
}

bool ViewControlModule::initQmlEngine()
{
    m_pEngine = new QQmlApplicationEngine();

    if( m_pEngine->rootContext() != nullptr )
    {
        m_pEngine->addImportPath( QStringLiteral("qrc:/") );
        m_pEngine->addImportPath( QStringLiteral("qrc:///BaseComponents") );
        m_pEngine->addImportPath( QStringLiteral("qrc:///components") );
    }

    qmlRegisterType<ViewEnum>( "ViewEnum", 1, 0, "ViewEnum" );

    const QUrl url(QStringLiteral("qrc:/main.qml"));

    QObject::connect(m_pEngine, &QQmlApplicationEngine::objectCreated
                     , this, [url](QObject *obj, const QUrl &objUrl) {
                            if (!obj && url == objUrl)
                                QCoreApplication::exit(-1);
                        }, Qt::QueuedConnection);

    m_pEngine->load(url);
    if( m_pEngine->rootObjects().isEmpty() )
        return false;

    return true;
}

QString ViewControlModule::getModuleName()
{
    return MDL_NAME( ViewControlModule );
}

void ViewControlModule::doRun()
{

}

void ViewControlModule::stopModule()
{
    QBaseModule::stopModule();

    clear();
}

void ViewControlModule::HandleNewControlLoadedEvent(QString objName)
{
    LOGD( TAG, "test object: %s", objName.toStdString().c_str() );
    QObject* pNewObj = FindChildObject( objName );
    if( pNewObj == nullptr )
    {
        LOGE( TAG, "Failed to get object: %s", objName.toStdString().c_str() );
        return;
    }

    SetControlEventConnection( pNewObj, true );
}

void ViewControlModule::HandleDestroyControlLoadedEvent(QString objName)
{
    LOGD( TAG, "test object: %s", objName.toStdString().c_str() );
    QObject* pNewObj = FindChildObject( objName );
    if( pNewObj == nullptr )
    {
        LOGE( TAG, "Failed to get object: %s", objName.toStdString().c_str() );
        return;
    }

    SetControlEventDisconnection( pNewObj, true );
}

void ViewControlModule::clear()
{

}
