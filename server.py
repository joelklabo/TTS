#!/usr/bin/env python3

from subprocess import call
from uuid import uuid4

from flask import Flask
from flask import request
from flask import send_from_directory

#!/usr/bin/env python3
from subprocess import call
from uuid import uuid4

from flask import Flask
from flask import request
from flask import send_from_directory

# Import from the 21 Bitcoin Developer Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# Charge a fixed fee of 1000 satoshis per request to the
# /tts endpoint
@app.route('/tts')
@payment.required(1000)
def tts():
  # the text the client sent us
  text = str(request.args.get('text'))

  # a file to store the rendered audio file
  file = str(uuid4()) + '.wav'

  # run the TTS engine
  call(['espeak', '-w', '/tmp/' + file, text])

  # send the rendered audio back to the client
  return send_from_directory(
    '/tmp',
    file,
    as_attachment=True
  )

# Initialize and run the server
if __name__ == '__main__':
  app.run(host='0.0.0.0')
