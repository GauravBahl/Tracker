#!/usr/bin/env python3
# encoding: utf-8
import json
import os
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

#def send_sms(phone_number):
	# send sms to phone number

@app.route('/clickEvent')
def click_event():
	user_id = request.args.get('id')
	print(user_id)
	return redirect("https://www.grubhub.com/restaurant/momo-magic-and-more-4006-w-plano-pkwy-plano/3017433", code=302)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()