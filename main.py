#-----------------------------------------------------------------------------#
#   main.py                                                                   #
#                                                                             #
#   Copyright (c) 2014, Seventy Four, Inc.                                    #
#   All rights reserved.                                                      #
#-----------------------------------------------------------------------------#



from app import app
from views import *



if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
