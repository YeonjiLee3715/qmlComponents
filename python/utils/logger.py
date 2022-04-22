#!/usr/bin/env python
# coding: utf8

""" Centralized logging facilities for Spleeter. """

import logging

_FORMAT = '[%(asctime)-15s PID:%(process)d TID:%(thread)d][%(name)s][%(levelname)s] %(module)s::%(funcName)s(%(lineno)d): %(message)s'
_LOG_LEVEL = logging.DEBUG
_LOGGER_NAME = 'TwobeoneSongMgr'

class Logger():
    __instance = None

    @classmethod
    def getInstance(cls):

        if cls.__instance is None:
            formatter = logging.Formatter(_FORMAT)
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            newLogger = logging.getLogger(_LOGGER_NAME)
            newLogger.addHandler(handler)
            newLogger.setLevel(_LOG_LEVEL)
            cls.__instance = newLogger

        return cls.__instance

def getLogger():
    return Logger.getInstance()