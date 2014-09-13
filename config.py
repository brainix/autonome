#-----------------------------------------------------------------------------#
#   config.py                                                                 #
#                                                                             #
#   Copyright (c) 2014, Seventy Four, Inc.                                    #
#   All rights reserved.                                                      #
#-----------------------------------------------------------------------------#

import os

class Config(object):
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    CSRF_ENABLED = False
    SECRET_KEY = os.environ['SECRET_KEY']

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False

class StagingConfig(Config):
    DEBUG = True
    TESTING = False
    DEVELOPMENT = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DEVELOPMENT = True

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    DEVELOPMENT = True
