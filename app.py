#!/usr/bin/env python3
# encoding: utf-8

# sudo lsof -i :5000
import json
import os
from flask import Flask, request, jsonify, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/offers')
def click_event():
	user_id = request.args.get('id')
	print(user_id)
	save_to_file(user_id)
	return redirect("https://www.grubhub.com/restaurant/momo-magic-and-more-4006-w-plano-pkwy-plano/3017433", code=302)

def save_to_file(user_id):
	with open("Tracker.txt", "a") as file_object:
		file_object.write('{}\t{}\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user_id))


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()