#!/bin/sh

#-----------------------------------------------------------------------------#
#   web.sh                                                                    #
#                                                                             #
#   Copyright (c) 2014, Seventy Four, Inc.                                    #
#   All rights reserved.                                                      #
#-----------------------------------------------------------------------------#



if [ "$APP_SETTINGS" == "config.DevelopmentConfig" ]; then
    python main.py
else
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn main:app --workers $WEB_CONCURRENCY
fi
