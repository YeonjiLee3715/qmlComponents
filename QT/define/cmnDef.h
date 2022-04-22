#pragma once
#pragma execution_character_set("utf-8")

#ifndef CMNDEF_H
#define CMNDEF_H

#include "TBO_Generator.h"

#ifndef __QT_DEBUG
#define __QT_DEBUG          ///< 디버그 정보를 콘솔에 표시 하기위해 설정한다.
#endif

#ifndef LOG_LV
#define LOG_LV          0   ///< 로그 표시레벨을 설정한다.(0: Debug~ 4: INFO~ )
#endif

#define mManager (static_cast<TBO_Generator*>(QGuiApplication::instance()))

#define SAFETY_DELETE(x)                            {if(x != NULL){delete x; x=NULL;}}
#define SAFETY_ARRAY_DELETE(x)                      {if(x != NULL){delete[] x; x=NULL;}}
#define IS_CHAR_ARRAY_EMPTY(x)                      ((x == NULL) || strlen(x) == 0)
#define CHAR_COPY_LENGTH(x)                         ((strlen(x) + 1))

#define IS_QVAR_VALID(x)                            (x.isNull() == false && x.isValid())
#define IS_QVAR_INVALID(x)                          (x.isNull() || x.isValid() == false )

#define _USER_ROLE(x)                               (Qt::UserRole + x)

#define _STRINGIFY(x)                               #x
#define _ARG(dataType,x)                            Q_ARG(dataType, x)
#define _RARG(dataType,x)                           Q_RETURN_ARG(dataType, x)
#define _VARG(x)                                    Q_ARG(QVariant, x)
#define _VRARG(x)                                   Q_RETURN_ARG(QVariant, x)
#define _PREFIX(x)                                  QMetaObject::invokeMethod(x

// conectivity: autoconnection
#define INVK_0(pObj, method) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method)); \
    }}
#define INVKR_0(pObj, method, rdataType, rarg) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _RARG(rdataType, rarg)); \
    }}
#define INVK_1(pObj, method, dataType1, arg1) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _ARG(dataType1, arg1)); \
    }}
#define INVKR_1(pObj, method, rdataType, rarg, dataType1, arg1) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _RARG(rdataType, rarg), _ARG(dataType1, arg1)); \
    }}
#define INVK_2(pObj, method, dataType1, arg1, dataType2, arg2) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _ARG(dataType1, arg1), _ARG(dataType2, arg2)); \
    }}
#define INVKR_2(pObj, method, rdataType, rarg, dataType1, arg1, dataType2, arg2) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _RARG(rdataType, rarg), _ARG(dataType1, arg1), _ARG(dataType2, arg2)); \
    }}
#define INVK_3(pObj, method, dataType1, arg1, dataType2, arg2, dataType3, arg3) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _ARG(dataType1, arg1), _ARG(dataType2, arg2), _ARG(dataType3, arg3)); \
    }}
#define INVKR_3(pObj, method, rdataType, rarg, dataType1, arg1, dataType2, arg2, dataType3, arg3) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _RARG(rdataType, rarg), _ARG(dataType1, arg1), _ARG(dataType2, arg2), _ARG(dataType3, arg3)); \
    }}

// conectivity: queuedconnection
#define QINVK_0(pObj, method) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), Qt::QueuedConnection); \
    }}
#define QINVK_1(pObj, method, dataType1, arg1) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), Qt::QueuedConnection, _ARG(dataType1, arg1)); \
    }}
#define QINVK_2(pObj, method, dataType1, arg1, dataType2, arg2) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), Qt::QueuedConnection, _ARG(dataType1, arg1), _ARG(dataType2, arg2)); \
    }}
#define QINVK_3(pObj, method, dataType1, arg1, dataType2, arg2, dataType3, arg3) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), Qt::QueuedConnection, _ARG(dataType1, arg1), _ARG(dataType2, arg2), _ARG(dataType3, arg3)); \
    }}

// macro for qml all of parameters are qvariant. conectivity: autoconnection
#define VINVK_0(pObj, method) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method)); \
    }}
#define VINVKR_0(pObj, method, rarg) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _VRARG(rarg)); \
    }}
#define VINVK_1(pObj, method, arg) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _VARG(arg)); \
    }}
#define VINVKR_1(pObj, method, rarg, arg1) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _VRARG(rarg), _VARG(arg1)); \
    }}
#define VINVK_2(pObj, method, arg1, arg2) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _VARG(arg1), _VARG(arg2)); \
    }}
#define VINVKR_2(pObj, method, rarg, arg1, arg2) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _VRARG(rarg), _VARG(arg1), _VARG(arg2)); \
    }}
#define VINVK_3(pObj, method, arg1, arg2, arg3) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _VARG(arg1), _VARG(arg2), _VARG(arg3)); \
    }}
#define VINVKR_3(pObj, method, rarg, arg1, arg2, arg3) \
    {if(pObj != nullptr)  {\
        _PREFIX(pObj), _STRINGIFY(method), _VRARG(rarg), _VARG(arg1), _VARG(arg2), _VARG(arg3)); \
    }}
#endif // CMNDEF_H
