#include "ViewEventHandler.h"

#include <QVariant>
#include <QVariantMap>

#include <CLogger.h>

#include "viewDefs.h"

namespace nsViewEventHandler
{
    const char* TAG = "ViewEventHandler";
}

using namespace nsViewEventHandler;

ViewEventHandler::ViewEventHandler(QObject *parent)
    : QObject(parent)
{

}

ViewEventHandler::~ViewEventHandler()
{
    disconnect( this, nullptr, nullptr, nullptr );
}

void ViewEventHandler::connectObjectEvent( QObject * pObj )
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

    QVariant vEventConnected = pObj->property( PROP_IS_EVENT_CONNECTED );
    if( vEventConnected.isNull() == false && vEventConnected.isValid()
            && vEventConnected.toBool() )
        return;

    QVariant vObjectType = pObj->property( "objectType" );
    if( vObjectType.isNull() || vObjectType.isValid() == false )
    {
        LOGE( TAG, "Object type is null" );
        return;
    }

    int nObjectType = vObjectType.toInt();
    if( nObjectType != static_cast<int>( ViewEnum::OBJECT_VIEW ) )
    {
        LOGE( TAG, "This object is not a button control. objectType: %d", nObjectType );
        return;
    }

    QVariant varEventConnectFlag = pObj->property( PROP_B_CONNECT_SHOW_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( viewShowEvent() ), this, SLOT( HandleViewShowEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_HIDE_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( viewHideEvent() ), this, SLOT( HandleViewHideEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_OPEN_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( viewOpenEvent() ), this, SLOT( HandleViewOpenEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_CLOSED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( viewClosedEvent() ), this, SLOT( HandleViewClosedEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_ACTIVEFOCUS_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( viewActiveFocusEvent() ), this, SLOT( HandleViewActiveFocusEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_INACTIVEFOCUS_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( viewInactiveFocusEvent() ), this, SLOT( HandleViewInactiveFocusEvent() ), Qt::QueuedConnection );

    pObj->setProperty( PROP_IS_EVENT_CONNECTED, true );
}

void ViewEventHandler::disconnectObjectEvent( QObject * pObj )
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

    QVariant vEventConnected = pObj->property( PROP_IS_EVENT_CONNECTED );
    if( vEventConnected.isNull() || vEventConnected.isValid() == false
        || vEventConnected.toBool() == false )
        return;

    QVariant vObjectType = pObj->property( "objectType" );
    if( vObjectType.isNull() || vObjectType.isValid() == false )
    {
        LOGE( TAG, "Object type is null" );
        return;
    }

    int nObjectType = vObjectType.toInt();
    if( nObjectType != static_cast<int>( ViewEnum::OBJECT_VIEW ) )
    {
        LOGE( TAG, "This object is not a button control. objectType: %d", nObjectType );
        return;
    }

    QVariant varEventConnectFlag = pObj->property( PROP_B_CONNECT_SHOW_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( viewShowEvent() ), this, SLOT( HandleViewShowEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_HIDE_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( viewHideEvent() ), this, SLOT( HandleViewHideEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_OPEN_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( viewOpenEvent() ), this, SLOT( HandleViewOpenEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_CLOSED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( viewClosedEvent() ), this, SLOT( HandleViewClosedEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_ACTIVEFOCUS_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( viewActiveFocusEvent() ), this, SLOT( HandleViewActiveFocusEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_INACTIVEFOCUS_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( viewInactiveFocusEvent() ), this, SLOT( HandleViewInactiveFocusEvent() ) );

    pObj->setProperty( PROP_IS_EVENT_CONNECTED, false );
}

void ViewEventHandler::HandleViewShowEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}

void ViewEventHandler::HandleViewHideEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}

void ViewEventHandler::HandleViewOpenEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}

void ViewEventHandler::HandleViewClosedEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}

void ViewEventHandler::HandleViewActiveFocusEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}

void ViewEventHandler::HandleViewInactiveFocusEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}
