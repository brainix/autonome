#-----------------------------------------------------------------------------#
#   views.py                                                                  #
#                                                                             #
#   Copyright (c) 2014, Seventy Four, Inc.                                    #
#   All rights reserved.                                                      #
#-----------------------------------------------------------------------------#



import os

import wikipedia

from flask import request
from twilio.rest import TwilioRestClient

from app import app



@app.route('/sms', methods=['POST'])
def sms():
    to = request.form.get('From')
    title = request.form.get('Body')
    wikipedia.set_lang('simple')
    summary = wikipedia.summary(title, sentences=2, chars=140)

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    from_ = os.environ['TWILIO_NUMBER']
    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(to=to, from_=from_, body=summary)
    return ''
