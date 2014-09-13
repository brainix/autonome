#-----------------------------------------------------------------------------#
#   app.py                                                                    #
#                                                                             #
#   Copyright (c) 2014, Seventy Four, Inc.                                    #
#   All rights reserved.                                                      #
#-----------------------------------------------------------------------------#



import os

from flask import Flask



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
