# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5.QtGui import QGuiApplication
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from python.src.utils.logger import getLogger

from .module.ViewControlModule.ViewControlModule import ViewControlModule
from .manager import QModuleManager as QMM
from .define.ModuleEnum import QModuleEnum
from python.src.define.viewDefs import *

class Test(QGuiApplication):
    __moduleManager = None

    def __init__(self, argv):
        super().__init__(argv)

    def initApp(self) -> bool:
        viewControlModule = ViewControlModule()

        self.__moduleManager = QMM.QModuleManager()

        viewControlModule.init()
        if viewControlModule.isSet == False:
            getLogger().error('Failed to init ViewControlModule')
            return False

        self.__moduleManager.registDependentModule(viewControlModule, QModuleEnum.eMODULE.ViewControlModule)

        self.__moduleManager.runIndependentModules()

        return True

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
