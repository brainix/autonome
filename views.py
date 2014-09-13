#-----------------------------------------------------------------------------#
#   views.py                                                                  #
#                                                                             #
#   Copyright (c) 2014, Seventy Four, Inc.                                    #
#   All rights reserved.                                                      #
#-----------------------------------------------------------------------------#



import wikipedia

from flask import request
from twilio import twiml

from app import app



@app.route('/sms')
def sms():
    title = request.form.get('Body')
    summary = wikipedia.summary(title, sentences=2, chars=140)
    response = twiml.Response()
    response.message(summary)
    return str(response)
