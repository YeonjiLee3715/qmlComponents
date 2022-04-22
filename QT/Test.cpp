#include "TEST_H.h"

#include <QQmlContext>
#include <QQuickView>
#include <QQuickItem>
#include <QResource>
#include <QDir>

#include <QVariantConverter.h>

#include <CLogger.h>

#include "viewDefs.h"

#include "ModuleEnum.h"
#include "ViewControlModule.h"

namespace nsTest
{
    const char* TAG = "Test";
}

using namespace nsTest;

Test::Test(int &arg, char **argv)
 : QGuiApplication(arg, argv)
{

}

Test::~Test()
{
    GetQModuleManagerInstance()->stopIndependentModules();

    DEREG_DEPENDENT_MODULE( ViewControlModule );
}

bool Test::initApp()
{
    if( initModules() == false )
        return false;

    return true;
}

bool Test::initModules()
{
    ViewControlModule* pViewControlModule = new ViewControlModule();

    pViewControlModule->init();
    if( pViewControlModule->IsSet() == false )
    {
        LOGE( TAG, "Failed to init ViewControlModule" );
        return false;
    }

    REG_DEPENDENT_MODULE( ViewControlModule, pViewControlModule );

    GetQModuleManagerInstance()->runIndependentModules();

    return true;
}

QModuleManager *Test::GetQModuleManagerInstance()
{
    return QModuleManager::GetInstance();
}

void Test::getResponse( int resCode, int sender, QVariantMap resPacket )
{
    switch( resCode )
    {
    case MDL_RES_NONE:
        break;
    default:
        break;
    }
}

void Test::ExitApplication( int code )
{
    exit( code );
}
