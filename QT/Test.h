#pragma once
#pragma execution_character_set("utf-8")

#ifndef TEST_H
#define TEST_H

#include <QQmlApplicationEngine>
#include <QQuickView>
#include <QGuiApplication>

#include <QModuleManager.h>

class Test : public QGuiApplication
{
    Q_OBJECT

public:
    explicit Test(int &, char **);
    virtual ~Test();

    bool                initApp();

    bool                initOptions();
    bool                initModules();

    QModuleManager*     GetQModuleManagerInstance();

    QQmlApplicationEngine* GetEngine();

signals:

public:

public slots:
    void                getResponse( int resCode, int sender, QVariantMap resPacket );
    void                ExitApplication( int code );

private:

};

#endif // TEST_H
