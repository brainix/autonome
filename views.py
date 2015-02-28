#-----------------------------------------------------------------------------#
#   views.py                                                                  #
#                                                                             #
#   Copyright (c) 2014, Seventy Four, Inc.                                    #
#   All rights reserved.                                                      #
#-----------------------------------------------------------------------------#



import os
import random

from flask import request
from twilio.rest import TwilioRestClient

from app import app



@app.route('/sms', methods=['POST'])
def sms():
    to = request.form.get('From')
    command = request.form.get('Body')

    body = 'Text STATUS to get the status of your car, UNSUBSCRIBE to receive no further SMSes, or SUBSCRUBE to re-subscribe to future SMSes.'
    if command == 'STATUS':
        bodies = [
            'Your car is NEXT IN LINE and will be ready for pick up in 2 HOURS.',
            'Your car is GETTING ITS OIL CHANGED and will be ready for pick up in 1 HOUR AND 30 MINUTES.',
            'Your car is GETTING ITS FILTER CHANGED and will be ready for pick up in 1 HOUR.',
            'Your car is GOING THROUGH A 128 POINT INSPECTION and will be ready for pick up in 30 MINUTES.',
            'Your car is BEING DETAILED and will be ready for pick up in 15 MINUTES.',
            'Your car is READY FOR PICK UP NOW.'
        ]
        body = random.choice(body)

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    from_ = os.environ['TWILIO_NUMBER']
    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(to=to, from_=from_, body=body)
    return ''
