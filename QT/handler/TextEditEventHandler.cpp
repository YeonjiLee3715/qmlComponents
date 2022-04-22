#include "TextEditEventHandler.h"

#include <QDir>

#include <cmnDef.h>

#include <CLogger.h>
#include <assert.h>

#include "viewDefs.h"

namespace nsTextEditEventHandler {
    const char* TAG = "TextEditEventHandler";
}

using namespace nsTextEditEventHandler;

TextEditEventHandler::TextEditEventHandler( QObject *parent)
    : QObject(parent)
{

}

TextEditEventHandler::~TextEditEventHandler()
{
    disconnect( this, nullptr, nullptr, nullptr );
}

void TextEditEventHandler::connectObjectEvent( QObject * pObj )
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
    if( nObjectType != static_cast<int>( ViewEnum::OBJECT_TEXTEDIT_CONTROL ) )
    {
        LOGE( TAG, "This object is not a button control. objectType: %d", nObjectType );
        return;
    }

    QVariant varEventConnectFlag = pObj->property( PROP_B_CONNECT_ACCEPTED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( controlAcceptedEvent() ), this, SLOT( HandleControlAcceptedEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_EDITING_FINISHED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( controlEditingFinishedEvent() ), this, SLOT( HandleControlEditingFinishedEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_TEXT_EDITED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( controlTextEditedEvent() ), this, SLOT( HandleControlTextEditedEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_FOCUSED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( controlFocusedEvent() ), this, SLOT( HandleControlFocusedEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_FOCUS_OUT_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( controlFocusOutEvent() ), this, SLOT( HandleControlFocusOutEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_ENABLED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( controlEnabledEvent() ), this, SLOT( HandleControlEnabledEvent() ), Qt::QueuedConnection );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_DISABLED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        connect( pObj, SIGNAL( controlDisabledEvent() ), this, SLOT( HandleControlDisabledEvent() ), Qt::QueuedConnection );

    pObj->setProperty( PROP_IS_EVENT_CONNECTED, true );
}

void TextEditEventHandler::disconnectObjectEvent( QObject * pObj )
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
    if( nObjectType != static_cast<int>( ViewEnum::OBJECT_WINDOW ) )
    {
        LOGE( TAG, "This object is not a button control. objectType: %d", nObjectType );
        return;
    }

    QVariant varEventConnectFlag = pObj->property( PROP_B_CONNECT_ACCEPTED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( controlAcceptedEvent() ), this, SLOT( HandleControlAcceptedEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_EDITING_FINISHED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( controlEditingFinishedEvent() ), this, SLOT( HandleControlEditingFinishedEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_TEXT_EDITED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( controlTextEditedEvent() ), this, SLOT( HandleControlTextEditedEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_FOCUSED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( controlFocusedEvent() ), this, SLOT( HandleControlFocusedEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_FOCUS_OUT_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( controlFocusOutEvent() ), this, SLOT( HandleControlFocusOutEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_ENABLED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( controlEnabledEvent() ), this, SLOT( HandleControlEnabledEvent() ) );

    varEventConnectFlag = pObj->property( PROP_B_CONNECT_DISABLED_EVENT );
    if( varEventConnectFlag.isNull() == false && varEventConnectFlag.isValid() && varEventConnectFlag.toBool() )
        disconnect( pObj, SIGNAL( controlDisabledEvent() ), this, SLOT( HandleControlDisabledEvent() ) );

    pObj->setProperty( PROP_IS_EVENT_CONNECTED, false );
}

void TextEditEventHandler::HandleControlAcceptedEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}

void TextEditEventHandler::HandleControlEditingFinishedEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );

    QVariant vObjectId = pObj->property( "objectId" );
    if( vObjectId.isNull() || vObjectId.isValid() == false )
    {
        LOGE( TAG, "Object id is null" );
        return;
    }

    QVariant vText = pObj->property( "text" );
    if( vText.isNull() || vText.isValid() == false )
    {
        LOGE( TAG, "text is null" );
        return;
    }

/*
    switch( vObjectId.toInt() )
    {
    case static_cast<int>(ViewEnum::ID_EDT_SOME_TEXT_EDIT):
        emit SigSomethingChanged(vText.toString());
        break;
    default:
        break;
    }
*/
}

void TextEditEventHandler::HandleControlTextEditedEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}

void TextEditEventHandler::HandleControlFocusedEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}

void TextEditEventHandler::HandleControlFocusOutEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}

void TextEditEventHandler::HandleControlEnabledEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}

void TextEditEventHandler::HandleControlDisabledEvent()
{
    QObject* pObj = sender();

    const QString& strObjName = pObj->objectName();

    LOGD( TAG, "strObjName: %s", strObjName.toStdString().c_str() );
}
