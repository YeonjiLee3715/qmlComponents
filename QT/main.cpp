#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include "Test.h"

int main(int argc, char *argv[])
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    Test app(argc, argv);

    if( app.initApp() == false )
        return -1;

    return app.exec();
}
